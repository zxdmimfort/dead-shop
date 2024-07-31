from apps.categories.models import Category
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin, admin.ModelAdmin):
    list_display = ("tree_actions", "indented_title", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)
    list_display_links = ("indented_title",)
