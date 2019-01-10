import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Quote(models.Model):
    uuid = models.UUIDField(
        unique=True, default=uuid.uuid4,
        help_text="Unieke resource identifier (UUID4)"
    )
    tekst = models.CharField(
        _("quote"), max_length=200,
        help_text=_("De tekst van de quote.")
    )
    bron_naam = models.CharField(
        _("bron naam"), max_length=200,
        help_text=_("Naam van de bron.")
    )
    bron_link = models.URLField(
        _("bron link"), blank=True,
        help_text=_("Link naar de oorspronkelijke bron.")
    )
    aangemaakt = models.DateTimeField(
        _("aangemaakt"), auto_now_add=True,
        help_text=_("Datum en tijd van wanneer het object is aangemaakt.")
    )

    class Meta:
        verbose_name = _("quote")
        verbose_name_plural = _("quotes")
        ordering = ("tekst", )

    def __str__(self):
        return self.tekst
