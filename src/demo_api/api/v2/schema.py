from drf_yasg.views import get_schema_view
from rest_framework import permissions
from zds_schema.schema import OpenAPISchemaGenerator

from demo_api.api.zds_helpers import SchemaViewMixin
from demo_api.api.schema import info


DefaultSchemaView = get_schema_view(
    info=info,
    # validators=['flex', 'ssv'],
    generator_class=OpenAPISchemaGenerator,
    public=True,
    permission_classes=(permissions.AllowAny,),

    # We need to point the schema to the v2 urls.
    urlconf='demo_api.api.v2.urls',
)


class SchemaView(SchemaViewMixin, DefaultSchemaView):
    pass
