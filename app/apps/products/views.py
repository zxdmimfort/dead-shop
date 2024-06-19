from django.shortcuts import render
from django.views.generic import DetailView, ListView
from elasticsearch_dsl import Search

from apps.products.models import Product

from .documents import ProductDocument


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


class ProductsDetailView(DetailView):
    model = Product
    template_name = "products/detail.html"
    context_object_name = "item"
    pk_url_kwarg = "product_uuid"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_uuid"] = self.kwargs.get(self.pk_url_kwarg)
        return context


def search(request):
    query = request.GET.get("q", "")
    # s = ProductDocument().search().filter("term", name=query)
    # s = Search(index="product_index").query(
    # "multi_match", query=query, fields=["name", "category"]
    # )
    s = ProductDocument.search().query("match", name=query)
    # response = s.execute()
    # products = [hit for hit in response]
    products = [hit for hit in s]
    return render(
        request, "products\search_results.html", {"products": products, "query": query}
    )
