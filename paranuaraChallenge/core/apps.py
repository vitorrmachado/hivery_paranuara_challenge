from django.apps import AppConfig
from django.db.utils import OperationalError
from .db_loader import DBLoader

class CoreConfig(AppConfig):
    name = 'core'
    verbose_name = 'core'

    def ready(self):
        try:
            DBLoader().load()
        except OperationalError:
            pass