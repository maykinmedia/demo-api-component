from django.utils.translation import ugettext_lazy as _

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
                'help_text': _('De volledige resource identifier als URL.')
            }
        }

    def create(self, validated_data):
        # Forward compatibility with version 2.
        validated_data.update({
            'bron_naam': '(Onbekend)'
        })
        return super().create(validated_data)
