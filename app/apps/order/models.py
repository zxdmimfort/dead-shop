import uuid

from apps.products.models import Product
from apps.users.models import UserProxy
from django.db import models


class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ("pending", "В ожидании"),
        ("processed", "Обработан"),
        ("shipped", "Отправлен"),
        ("delivered", "Доставлен"),
        ("cancelled", "Отменен"),
        ("received", "Получен"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(UserProxy, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=ORDER_STATUS_CHOICES, default="pending"
    )

    def __str__(self):
        return f"Order {self.id} by {self.user}"

    def get_serialized_data(self):
        return {
            "user": self.user,
            "id": self.id,
            "email": self.email,
            "created_at": self.created_at,
            "status": self.status,
            "items": self.items.all(),
        }


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    price = models.FloatField(null=True)

    def __str__(self):
        return f"{self.amount} x {self.product.name} in order {self.order.id}"
