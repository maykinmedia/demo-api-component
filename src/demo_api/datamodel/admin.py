from django.contrib import admin

from .models import Quote


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('tekst', 'aangemaakt', )
    search_fields = ('tekst', )
    ordering = ('tekst', )
    readonly_fields = ('uuid', )
