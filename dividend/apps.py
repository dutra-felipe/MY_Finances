from django.apps import AppConfig


class DividendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dividend'

    def ready(self):
        import dividend.signals
