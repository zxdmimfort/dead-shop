from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import Product


@registry.register_document
class ProductDocument(Document):
    category = fields.ObjectField(
        properties={"name": fields.TextField(), "slug": fields.TextField()}
    )

    class Index:
        name = "products"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Product
        fields = [
            "name",
        ]
        related_models = ["Category"]
