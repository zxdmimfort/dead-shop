from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from apps.cart.models import Cart, CartItem
from .models import Order, OrderItem

class CreateOrderView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart.objects.get(client=request.user)
        return render(request, 'order/create_order.html', {'cart': cart})

    def post(self, request):
        cart = Cart.objects.get(client=request.user)
        order = Order.objects.create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, amount=item.amount)
        cart_items.delete()
        return redirect('order_detail', order_id=order.id)

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'order/order_detail.html'
    context_object_name = 'order'
    pk_url_kwarg = 'order_id'

class UserOrdersView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order/user_orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)