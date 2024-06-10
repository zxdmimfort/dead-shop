import uuid
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse


class Category(MPTTModel, models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    photo = models.ImageField(upload_to="categories", null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("categories:category_list", args=[self.slug])

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
