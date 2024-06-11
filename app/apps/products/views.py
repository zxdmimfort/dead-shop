from django.views.generic import ListView

from apps.products.models import Product


class ProductsListView(ListView):
    template_name = "products/index.html"
    context_object_name = "items"
    title = "Products"
    model = Product
    # allow_empty = False

    def get_queryset(self):
        cat_slug = self.kwargs.get("cat_slug", None)
        if cat_slug:
            return Product.objects.filter(category__slug=cat_slug)
        return Product.objects.all()
