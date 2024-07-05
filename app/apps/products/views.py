from django.shortcuts import render
from django.views.generic import DetailView, ListView
from elasticsearch_dsl.query import MultiMatch

from apps.products.models import Product

from .documents import ProductDocument


class ProductsListView(ListView):
    template_name = "products/index.html"
    context_object_name = "items"
    title = "Products"
    model = Product
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("q")
        print(query)
        if query:
            q = MultiMatch(query=query, fields=["name"], fuzziness="AUTO")
            s = ProductDocument.search().query(q).to_queryset()
            return s

        else:
            cat_slug = self.kwargs.get("cat_slug", None)
            if cat_slug:
                return Product.objects.filter(category__slug=cat_slug)
            return Product.objects.all()


class ProductsDetailView(DetailView):
    model = Product
    template_name = "products/detail.html"
    context_object_name = "item"
    pk_url_kwarg = "product_uuid"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_uuid"] = self.kwargs.get(self.pk_url_kwarg)
        return context
