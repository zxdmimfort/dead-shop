from django.conf import settings
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl.connections import connections

from .models import Product

connections.create_connection(
    alias="default", hosts=[settings.ELASTICSEARCH_DSL["default"]["hosts"]]
)


@registry.register_document
class ProductDocument(Document):
    class Index:
        name = "product"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Product
        fields = ["name", "price", "stock", "photo"]

    def save(self, **kwargs):
        self.id = str(self.meta.id)
        return super().save(**kwargs)
