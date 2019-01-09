from django.conf import settings

from drf_yasg import openapi

info = openapi.Info(
    title="Demo API Component",
    default_version=settings.API_VERSION,
    description="Een voorbeeld van een OAS 3.0 API met bijbehorende referentie "
                "implementatie.",
    contact=openapi.Contact(
        email="support@maykinmedia.nl",
        url="https://github.com/maykinmedia/demo-api-component"
    ),
    license=openapi.License(name="EUPL 1.2"),
)
