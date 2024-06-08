from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ["name"]
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
