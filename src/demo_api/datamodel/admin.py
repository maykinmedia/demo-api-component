from django.contrib import admin

from .models import Quote


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('tekst', 'bron_naam', 'aangemaakt', 'laatst_bijgewerkt', )
    search_fields = ('tekst', 'bron_naam', )
    ordering = ('tekst', )
    readonly_fields = ('uuid', )
