from django.apps import AppConfig
from django.db.models.signals import post_migrate


class AgrositeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'agrosite'

    def ready(self):
        from .create_superuser import create_superuser

        def create_admin_user(sender, **kwargs):
            create_superuser()

        post_migrate.connect(create_admin_user, sender=self)
