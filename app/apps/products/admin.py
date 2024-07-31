from apps.products import models
from django.contrib import admin


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass
