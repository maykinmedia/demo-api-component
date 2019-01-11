from rest_framework import status
from rest_framework.test import APITestCase
from zds_schema.tests import reverse


class SchemaTests(APITestCase):

    def test_schema_version(self):
        url = reverse('v2:schema-json', kwargs={'format': '.json'})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()

        self.assertEqual(data['info']['version'], '2')
        self.assertListEqual(data['definitions']['Quote']['required'], ['tekst', 'bronNaam'])
