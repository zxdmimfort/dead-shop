from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from .utils import send_order_status_email

@receiver(post_save, sender=Order)
def send_order_status_update(sender, instance, **kwargs):
    if not kwargs.get('created', False):
        send_order_status_email(instance)