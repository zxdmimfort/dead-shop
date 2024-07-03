from django.http import Http404
from django.views import View
from django.db import transaction
from django.contrib import messages

from apps.users.models import UserProxy
from .models import Order, OrderItem
from apps.cart.models import Cart, CartItem
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateOrderView(View):
    def get(self, request):
        user, user_created, anon = UserProxy.objects.get_or_create(request=request)
        cart, cart_created = Cart.objects.get_or_create(client=user)

        # Здесь нужно отобразить страницу типа сначала нужно добавить товары в корзину
        if user_created or cart_created or not cart.cartitem_set.exists():
            raise Http404

        # Здесь нужно отрендерить страницу с вводом мыла для аноним. юзеров
        if anon:
            return render(request, "order/create_order.html", {"cart": cart})
        return render(request, "order/create_order.html", {"cart": cart})

    def post(self, request):
        user, _, anon = UserProxy.objects.get_or_create(request=request)
        cart, _ = Cart.objects.get_or_create(client=user)
        cart_items = CartItem.objects.filter(cart=cart)

        # TODO Не отображается ошибка
        for item in cart_items:
            product = item.product
            if product.stock < item.amount:
                messages.error(
                    request, f"Недостаточно товаров в наличии: {product.name}"
                )
                return redirect("cart:cart_detail")

        # TODO Вот этот участок тоже в менеджер нужно вынести
        with transaction.atomic():
            order = Order.objects.create(user=user)
            cart_items = CartItem.objects.filter(cart=cart)
            for item in cart_items:
                item.product.stock -= item.amount
                item.product.save()
                OrderItem.objects.create(
                    order=order, product=item.product, amount=item.amount
                )
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
        user, _, _ = UserProxy.objects.get_or_create(request=self.request)
        return Order.objects.filter(user=user)
