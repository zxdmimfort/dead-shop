from django.db import models

from apps.categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    category = models.ManyToManyField(Category, related_name="products", blank=True)

    def get_absolute_url(self):
        return f"/products/{self.id}/"