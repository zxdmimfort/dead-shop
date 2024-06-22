from django.views import View
from django.db import transaction
from django.contrib import messages
from .models import Order, OrderItem
from apps.cart.models import Cart, CartItem
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateOrderView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart.objects.get(client=request.user)
        return render(request, "order/create_order.html", {"cart": cart})

    def post(self, request):
        cart = Cart.objects.get(client=request.user)
        cart_items = CartItem.objects.filter(cart=cart)

        for item in cart_items:
            product = item.product
            if product.stock < item.amount:
                messages.error(request, f'Недостаточно товаров в наличии: {product.name}')
                return redirect('cart:cart_detail')

        with transaction.atomic():
            order = Order.objects.create(user=request.user)
            cart_items = CartItem.objects.filter(cart=cart)
            for item in cart_items:
                item.product.stock -= item.amount
                item.product.save()
                OrderItem.objects.create(order=order, product=item.product, amount=item.amount)
            cart_items.delete()
        return redirect("order:order_detail", order_id=order.id)


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "order/order_detail.html"
    context_object_name = "order"
    pk_url_kwarg = "order_id"


class UserOrdersView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "order/user_orders.html"
    context_object_name = "orders"

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
