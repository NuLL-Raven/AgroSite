from django.urls import path
from django.views.i18n import set_language

from . import views
from .views import switch_language

from products.views_admin import create_admin_view

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),  # ✅ `pk` must match the view function
    path('set_language/', set_language, name='set_language'),
    path("create-admin/", create_admin_view, name="create_admin"),
]
