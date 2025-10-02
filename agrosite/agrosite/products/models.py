from cloudinary_storage.storage import MediaCloudinaryStorage
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(
        upload_to='product_images/',
        storage=MediaCloudinaryStorage()  # <- explicitly use Cloudinary
    )

    def __str__(self):
        return self.name
