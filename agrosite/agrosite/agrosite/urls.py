from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import set_language

from products.views_admin import create_admin_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),  # Includes the products app URLs
    path('set_language/', set_language, name='set_language'),
path("create-admin/", create_admin_view, name="create_admin"),
]

if settings.DEBUG:  # Serve media files only in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)