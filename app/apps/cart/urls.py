from apps.cart import views
from django.urls import path

app_name = "cart"

urlpatterns = [
    path("", views.CartDetailView.as_view(), name="cart_detail"),
    path("add/<uuid:product_uuid>/", views.add_to_cart, name="add_to_cart"),
    path("delete/<int:item_id>/", views.delete_from_cart, name="delete_from_cart"),
]
