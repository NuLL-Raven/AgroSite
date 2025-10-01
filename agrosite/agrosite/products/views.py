from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils.translation import activate
from .forms import ProductSearchForm
from .models import Product  # Import the Product model
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.conf import settings
from .forms import AdminCreationForm

# Homepage with Contact Section
def home(request):
    products = Product.objects.all()[:5]
    return render(request, 'products/home.html', {'products': products})

# Product Listing Page
def product_list(request):
    products = Product.objects.all()
    form = ProductSearchForm(request.GET)

    if form.is_valid():
        search = form.cleaned_data.get('search')
        if search:
            products = products.filter(name__icontains=search)

    return render(request, 'products/product_list.html', {'products': products, 'form': form})

# Product Detail Page
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})  # ✅ Use the correct path

def switch_language(request, lang_code):
    activate(lang_code)
    request.session['django_language'] = lang_code
    return redirect(request.META.get('HTTP_REFERER', '/'))

def create_admin_view(request):
    User = get_user_model()

    # Optional: prevent if already exists
    if User.objects.filter(is_superuser=True).exists():
        messages.error(request, "An admin already exists.")
        return redirect("/admin/")

    if request.method == "POST":
        form = AdminCreationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["secret_key"] == settings.ADMIN_CREATION_KEY:
                User.objects.create_superuser(
                    username=form.cleaned_data["username"],
                    email=form.cleaned_data["email"],
                    password=form.cleaned_data["password"]
                )
                messages.success(request, "Superuser created successfully! You can now log in.")
                return redirect("/admin/")
            else:
                messages.error(request, "Invalid secret key.")
    else:
        form = AdminCreationForm()

    return render(request, "create_admin.html", {"form": form})