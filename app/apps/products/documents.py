from django.db import models
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.documents import DocType
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl import Index

from .models import Product

product_index = Index("product_index")


# @product_index.doc_type
@DocType
@registry.register_document
class ProductDocument(Document):
    category = fields.ObjectField(
        properties={
            "name": fields.TextField(),
        }
    )
    # photo = models.ImageField(upload_to="product_photos/")

    class Index:
        name = "products"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Product

        fields = ["name", "price", "stock", "photo"]

    queryset_pagination = 10

    def get_queryset(self):
        return super().get_queryset().select_related("category")
