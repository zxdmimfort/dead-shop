from django.views.generic import ListView

from apps.products.models import Product


class ProductsListView(ListView):
    template_name = "products/index.html"
    context_object_name = "items"
    title = "Products"
    model = Product
