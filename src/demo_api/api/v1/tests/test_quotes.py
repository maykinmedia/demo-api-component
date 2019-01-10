from copy import deepcopy

from django.conf import settings
from django.test import override_settings

from rest_framework import status
from rest_framework.test import APITestCase
from zds_schema.tests import reverse

from demo_api.datamodel.models import Quote
from demo_api.datamodel.tests.factories import QuoteFactory


# Force version one to be used.
REST_FRAMEWORK_SETTINGS = deepcopy(settings.REST_FRAMEWORK)
REST_FRAMEWORK_SETTINGS.update({'DEFAULT_VERSION': '1'})


@override_settings(REST_FRAMEWORK=REST_FRAMEWORK_SETTINGS)
class QuoteTests(APITestCase):

    def test_list_and_detail(self):
        url = reverse('quote-list')
        QuoteFactory.create_batch(20)

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data['count'], 20)
        self.assertIn('results', data)

        detail_url = data['results'][3]['url']

        detail = self.client.get(detail_url)

        self.assertEqual(detail.status_code, status.HTTP_200_OK)
        self.assertEqual(detail.json(), data['results'][3])

    def test_create(self):
        url = reverse('quote-list')
        data = {
            'tekst': 'Pluk de dag!'
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = response.json()
        self.assertNotIn('bronNaam', data)

        quote = Quote.objects.get()

        self.assertEqual(quote.bron_naam, '(Onbekend)')
