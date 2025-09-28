from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils.translation import activate
from .forms import ProductSearchForm
from .models import Product  # Import the Product model

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