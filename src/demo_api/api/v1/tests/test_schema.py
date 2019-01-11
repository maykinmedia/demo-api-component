from copy import deepcopy

from django.conf import settings
from django.test import override_settings

from rest_framework import status
from rest_framework.test import APITestCase
from zds_schema.tests import reverse

# Force version 1 to be used.
REST_FRAMEWORK_SETTINGS = deepcopy(settings.REST_FRAMEWORK)
REST_FRAMEWORK_SETTINGS.update({'DEFAULT_VERSION': '1'})


@override_settings(REST_FRAMEWORK=REST_FRAMEWORK_SETTINGS)
class SchemaTests(APITestCase):

    def test_schema_version(self):
        url = reverse('schema-json', kwargs={'format': '.json'})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()

        self.assertEqual(data['info']['version'], '1')
        self.assertListEqual(data['definitions']['Quote']['required'], ['tekst'])
