from django.http import Http404
from django.views import View
from django.db import transaction
from django.contrib import messages

from apps.users.models import UserProxy
from config.settings import settings
from .models import Order, OrderItem
from apps.cart.models import Cart, CartItem
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateOrderView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            session = request.session
            session_data = session.get(settings.USER_SESSION_ID)
            if not session_data:
                raise Http404
            session_uuid = session_data["uuid"]
            user = UserProxy.objects.get(session=session_uuid)
        else:
            user, _ = UserProxy.objects.get_or_create(user=request.user)

        cart = Cart.objects.get(client=user)
        if not cart.cartitem_set.exists():
            raise Http404
        return render(request, "order/create_order.html", {"cart": cart})

    def post(self, request):
        if not request.user.is_authenticated:
            session = request.session
            session_data = session.get(settings.USER_SESSION_ID)
            if not session_data:
                raise Http404
            session_uuid = session_data["uuid"]
            user = UserProxy.objects.get(session=session_uuid)
        else:
            user, _ = UserProxy.objects.get_or_create(user=request.user)

        cart = Cart.objects.get(client=user)
        cart_items = CartItem.objects.filter(cart=cart)

        for item in cart_items:
            product = item.product
            if product.stock < item.amount:
                messages.error(
                    request, f"Недостаточно товаров в наличии: {product.name}"
                )
                return redirect("cart:cart_detail")

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
        if self.request.user.is_authenticated:
            user, _ = UserProxy.objects.get_or_create(user=self.request.user)
        else:
            session = self.request.session
            session_data = session.get(settings.USER_SESSION_ID)
            if not session_data:
                raise Http404
            session_uuid = session_data["uuid"]
            user = UserProxy.objects.get(session=session_uuid)

        return Order.objects.filter(user=user)
