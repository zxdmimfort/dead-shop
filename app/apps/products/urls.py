from django.urls import path

from apps.products import views



urlpatterns = [
    path("", views.index, name="index"),
]
