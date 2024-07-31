from apps.order import views
from django.urls import path

app_name = "order"

urlpatterns = [
    path("create/", views.CreateOrderView.as_view(), name="create_order"),
    path(
        "my-orders/<uuid:order_id>/",
        views.OrderDetailView.as_view(),
        name="order_detail",
    ),
    path("my-orders/", views.UserOrdersView.as_view(), name="user_orders"),
]
