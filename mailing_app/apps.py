from django.apps import AppConfig


class MailingAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mailing_app"

    def ready(self):
        from .services import start_scheduler

        start_scheduler()
