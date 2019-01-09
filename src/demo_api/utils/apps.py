from django.apps import AppConfig


class UtilsConfig(AppConfig):
    name = 'demo_api.utils'

    def ready(self):
        from . import checks  # noqa
