from django.urls import path

from .views import AddToCartView, CartDetailView, RemoveFromCartView

app_name="cart"

urlpatterns = [
    path("", CartDetailView.as_view(), name="cart_detail"),
    path("add/<int:product_id>/", AddToCartView.as_view(), name="add_to_cart"),
    path("delete/<int:product_id>/", RemoveFromCartView.as_view(), name="delete_from_cart"),
]
