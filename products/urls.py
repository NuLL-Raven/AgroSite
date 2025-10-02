from django.urls import path
from django.views.i18n import set_language

from . import views
from .views import switch_language

from .views import create_admin_view

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),  # ✅ `pk` must match the view function
    path('set_language/', set_language, name='set_language'),
    path("create-admin/", create_admin_view, name="create_admin"),
]

from django.conf.urls import handler404, handler500
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)

handler404 = custom_404
handler500 = custom_500