import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "agrosite.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = "AdeloTh"
email = "adeloth0569@gmail.com"
password = "Hiroo210500"   # 👉 change to a strong password

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(">>> Superuser created")
else:
    print(">>> Superuser already exists")
