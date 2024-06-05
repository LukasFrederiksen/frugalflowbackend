from django.apps import AppConfig
from project.apps import unique_product


class UniqueProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project.apps.unique_product'
