from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from apps.categories.models import Category

@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', )
    search_fields = ('name',)
    list_display_links=('indented_title',)
    ordering = ('name', )