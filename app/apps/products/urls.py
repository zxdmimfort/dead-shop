from apps.products import views
from django.urls import path

app_name = "products"
urlpatterns = [
    path("", views.ProductsListView.as_view(), name="index"),
    path(
        "category/<slug:cat_slug>/",
        views.ProductsListView.as_view(),
        name="products_by_category",
    ),
    path(
        "product/<uuid:product_uuid>/",
        views.ProductsDetailView.as_view(),
        name="detail_product",
    ),
]
