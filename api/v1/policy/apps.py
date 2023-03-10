from django.apps import AppConfig


class PolicyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api.v1.policy"

    def ready(self):
        from api.v1.policy import signals
