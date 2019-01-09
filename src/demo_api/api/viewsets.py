from rest_framework import mixins, viewsets

from demo_api.datamodel.models import Quote

from .serializers import QuoteSerializer


class QuoteViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """
    list:
    Bekijk de lijst van quotes.

    read:
    Bekijk een enkele quote.

    create:
    Voeg een quote toe.
    """
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    lookup_field = 'uuid'
