from django.apps import AppConfig


class SignalAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Signal_app'

    def ready(self):
        # this method will be called when the application is ready to perform any inital task
        from . import signal