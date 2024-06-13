import uuid
from django.db import models

from apps.categories.models import Category


class Product(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    photo = models.ImageField(upload_to="products", null=True, blank=True)
    category = models.ManyToManyField(Category, related_name="products", blank=True)

    def get_absolute_url(self):
        return f"/products/product/{self.id}/"

    def __str__(self):
        return self.name