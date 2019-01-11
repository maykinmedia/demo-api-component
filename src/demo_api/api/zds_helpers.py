"""
Largely copied from `zds_schema.schema` module.

The SchemaView is converted to a mixin so the SchemaView can be altered.
"""

import os
from urllib.parse import urlsplit

from django.conf import settings
from drf_yasg.codecs import yaml_sane_load
from rest_framework.response import Response
from zds_schema.schema import SPEC_RENDERERS


# TODO: Move this mixin to zds_schema
class SchemaViewMixin:

    @property
    def _is_openapi_v3(self) -> bool:
        version = self.request.GET.get('v', '')
        return version.startswith('3')

    def get_renderers(self):
        if not self._is_openapi_v3:
            return super().get_renderers()
        return [renderer() for renderer in SPEC_RENDERERS]

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)

        if not self._is_openapi_v3:
            return response

        # serve the staticically included V3 schema
        SCHEMA_PATH = os.path.join(settings.BASE_DIR, 'src', 'openapi.yaml')
        with open(SCHEMA_PATH, 'r') as infile:
            schema = yaml_sane_load(infile)

        # fix the servers
        for server in schema['servers']:
            split_url = urlsplit(server['url'])
            if split_url.netloc:
                continue

            prefix = settings.FORCE_SCRIPT_NAME or ''
            if prefix.endswith('/'):
                prefix = prefix[:-1]
            server_path = f"{prefix}{server['url']}"
            server['url'] = request.build_absolute_uri(server_path)

        return Response(
            data=schema,
            headers={'X-OAS-Version': schema['openapi']}
        )
