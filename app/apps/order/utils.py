from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.urls import reverse

from config.settings import settings


def send_order_status_email(order):
    if settings.DEBUG:
        host = "127.0.0.1:8000"
        schema = "http"
    else:
        host = settings.ALLOWED_HOSTS[0]
        schema = "https"

    link = reverse("order:order_detail", args=[order.id])
    template = get_template("order/email_notification.html")
    context = {"order": order.get_serialized_data(), "link": f"{schema}://{host}{link}"}
    message = template.render(context)
    mail = EmailMessage(
        subject=f"Статус вашего заказа {order.id} был изменен.",
        body=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[order.email],
    )
    mail.content_subtype = "html"
    return mail.send()
