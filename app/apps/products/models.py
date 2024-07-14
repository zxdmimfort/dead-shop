import uuid
from django.db import models

from apps.categories.models import Category

def user_directory_path(instance, filename):
    return f"products/{instance.id}.jpg"


class Product(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    name = models.CharField(max_length=300)
    price = models.FloatField()
    stock = models.IntegerField()
    photo = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products", null=True
    )

    def get_absolute_url(self):
        return f"/products/product/{self.id}/"

    def __str__(self):
        return self.name
