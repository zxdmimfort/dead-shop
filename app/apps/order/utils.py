from django.core.mail import send_mail
from django.conf import settings

def send_order_status_email(order):
    subject = f'Статус вашего заказа {order.id} был изменен.'
    message = f'Ваш заказ {order.id} сейчас {order.get_status_display()}.'
    recipient_list = [order.user.email]
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)