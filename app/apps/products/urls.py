from django.urls import path

from apps.products import views


app_name = "products"

urlpatterns = [
    path("", views.ProductsListView.as_view(), name="index"),
    path("category/<slug:cat_slug>/", views.ProductsListView.as_view(), name="products_by_category"),
]
