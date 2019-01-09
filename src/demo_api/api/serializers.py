from rest_framework import serializers

from demo_api.datamodel.models import Quote


class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quote
        fields = (
            'url',
            'tekst',
            'aangemaakt',
        )
        extra_kwargs = {
            'url': {
                'lookup_field': 'uuid',
            }
        }
