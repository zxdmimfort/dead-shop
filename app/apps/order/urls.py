from django.urls import path
from apps.order import views

app_name = "order"

urlpatterns = [
    path('create/', views.CreateOrderView.as_view(), name='create_order'),
    path('confirmation/<uuid:order_id>/', views.OrderConfirmationView.as_view(), name='order_confirmation'),
    path('my-orders/', views.UserOrdersView.as_view(), name='user_orders'),
]