from django.db import models

from apps.products.models import Product
from apps.users.models import Client


# Create your models here.
class Cart(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return self.product.name
