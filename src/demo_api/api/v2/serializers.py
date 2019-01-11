from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from demo_api.datamodel.models import Quote


class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quote
        fields = (
            'url',
            'tekst',
            'bron_naam',
            'bron_link',
            'aangemaakt',
            'laatst_bijgewerkt',
        )
        extra_kwargs = {
            'url': {
                'lookup_field': 'uuid',
                'view_name': 'v2:quote-detail',
                'help_text': _('De volledige resource identifier als URL.')
            }
        }
