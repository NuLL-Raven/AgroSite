from django.contrib import admin
from django.utils.html import format_html
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image_preview')  # ✅ Show image preview
    search_fields = ('name',)  # ✅ Allow search by name
    list_filter = ('price',)  # ✅ Add price filtering
    save_as = True  # ✅ Add "Save as New" button
    save_on_top = True  # ✅ Add Save button at the top

    fieldsets = [
        ('Détails du produit', {'fields': ['name', 'description', 'price', 'image']}),  # ✅ Added image upload
    ]

    readonly_fields = ('image_preview',)  # ✅ Prevents accidental editing

    def image_preview(self, obj):
        """Display a small preview of the uploaded image in the admin panel."""
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" style="object-fit: cover;"/>', obj.image.url)
        return "(No image)"

    image_preview.short_description = "Image Preview"


# Register the Product model with the custom admin settings
admin.site.register(Product, ProductAdmin)
