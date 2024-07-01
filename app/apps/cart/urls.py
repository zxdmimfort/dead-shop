from django.urls import path

from apps.cart import views

app_name = "cart"

urlpatterns = [
    path("", views.cart_detail, name="cart_detail"),
    path("add/<uuid:product_uuid>/", views.add_to_cart, name="add_to_cart"),
    path("remove/<uuid:product_uuid>/", views.cart_remove, name="cart_remove"),
]
