from django.apps import AppConfig

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

class ClientsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clients_app'
    verbose_name = 'клиенты'


