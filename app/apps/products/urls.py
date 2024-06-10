from django.urls import path

from apps.products import views



urlpatterns = [
    path("", views.ProductsListView.as_view(), name="index"),
]
