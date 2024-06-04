from django.contrib import admin

from apps.products import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass
