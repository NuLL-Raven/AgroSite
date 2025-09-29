from django.db.models.signals import post_migrate
from django.apps import apps
from .create_superuser import create_superuser

def create_admin_user(sender, **kwargs):
    create_superuser()

post_migrate.connect(create_admin_user, sender=apps.get_app_config('auth'))
