from django.conf import settings
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from elasticsearch import Elasticsearch
from elasticsearch_dsl import MultiSearch, Q, Search

from apps.products.models import Product

client = Elasticsearch(hosts=[settings.ELASTICSEARCH_DSL["default"]["hosts"]])
s = Search(using=client)


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
    query = request.GET.get("q")
    if query:
        q = Q("fuzzy", name={"value": query, "fuzziness": 0})
        products = s.execute(q)
        print(products)
    return render(request, "products/search.html", {"products": products})


"""ms = MultiSearch(index="products")
        name_search = Q(
            "fuzzy",
            name={"value": query, "fuzziness": 2},
            # category={"value": query, "fuzziness": 2},
        )
        category_search = Q("fuzzy", category={"value": query, "fuzziness": 2})
        ms = ms.add(name_search)
        ms = ms.add(category_search)
        products = s.execute()"""
