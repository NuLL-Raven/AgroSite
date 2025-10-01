# products/views_admin.py
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.conf import settings

def create_admin_view(request):
    if request.method == "POST":
        key = request.POST.get("key")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # ✅ Verify key
        if key != settings.ADMIN_CREATION_KEY:
            messages.error(request, "Clé invalide. Accès refusé ❌")
            return redirect("create_admin")

        User = get_user_model()
        if User.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur existe déjà ⚠️")
            return redirect("create_admin")

        # ✅ Create superuser
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )
        messages.success(request, f"Compte admin {username} créé avec succès ✅")
        return redirect("admin:login")

    return render(request, "create_admin.html")
