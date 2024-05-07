from django.apps import AppConfig


class VendorConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "vendor"

    def ready(self):
        from vendor import signals
