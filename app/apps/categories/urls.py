from django.urls import path

from apps.categories import views


app_name = "categories"

urlpatterns = [
    path("<slug:cat_slug>/", views.CategoryListView.as_view(), name="category_list"),
    path("", views.CategoryListView.as_view(), name="category_list_root"),
]
