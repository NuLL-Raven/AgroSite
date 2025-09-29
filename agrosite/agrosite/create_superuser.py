from django.contrib.auth import get_user_model
from django.db.utils import OperationalError

def create_superuser():
    User = get_user_model()
    try:
        if not User.objects.filter(username="AdeloTh").exists():
            User.objects.create_superuser(
                username="AdeloTh",
                email="adeloth0569@gmail.com",
                password="Hiroo210500"
            )
            print("Superuser 'AdeloTh' created ✅")
        else:
            print("Superuser 'AdeloTh' already exists")

    except OperationalError:
        # Database might not be ready during migration
        print("Database not ready, skipping superuser creation")
