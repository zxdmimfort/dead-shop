from django.core.mail import send_mail

from config.settings import settings


def send_order_status_email(order):
    if settings.DEBUG:
        host = "127.0.0.1:8000"
        schema = "http"
    else:
        host = settings.ALLOWED_HOSTS[0]
        schema = "https"

    subject = f"Статус вашего заказа {order.id} был изменен."
    message = f"Ваш заказ {schema}://{host}/order/my-orders/{order.id}/ сейчас {order.get_status_display()}."
    recipient_list = [order.email]
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
