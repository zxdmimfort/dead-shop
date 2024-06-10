from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView

from apps.categories.models import Category


class CategoryListView(ListView):
    template_name = "categories/catalog.html"
    context_object_name = "items"
    title = "Catalog"
    model = Category

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        cat_slug = self.kwargs.get("cat_slug", None)
        if cat_slug:
            self.cat = self.model.objects.filter(slug=cat_slug).first()
            if self.cat and self.cat.is_leaf_node():
                return reverse("products:index", args=[self.cat.slug])
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        return self.cat.get_children()
