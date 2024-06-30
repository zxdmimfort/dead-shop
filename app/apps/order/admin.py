from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created_at", "status")
    list_filter = ("status", "created_at", "user")
    search_fields = ("user__username", "user__email")
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
