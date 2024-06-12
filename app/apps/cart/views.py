from typing import Any

from apps.products.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, View

from .forms import CartAddProductForm
from .models import Cart, CartItem


# Create your views here.
class CartDetailView(LoginRequiredMixin,DetailView):
    template_name="cart/cart_detail.html"
    model=Cart

    def get_object(self, queryset=None):
        cart, created = Cart.objects.get_or_create(client=self.request.user)
        return cart
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_items'] = CartItem.objects.filter(cart=self.object)
        context['total_price'] = sum(item.product.price * item.amount for item in context['cart_items'])
        return context

def add_to_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    cart,created=Cart.objects.get_or_create(client=request.user)
    print(cart)
    cart_item,created=CartItem.objects.get_or_create(cart=cart,product=product)
    cart_item.amount+=1
    cart_item.save()
    return redirect("cart:cart_detail")

def delete_from_cart(request,item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect("cart:cart_detail")
    


"""class CartAddView(LoginRequiredMixin,View):
    def get(self, request, pk):
        return redirect('cart:cart_detail')
    
    def post(self,request,product_id):
        product=get_object_or_404(Product,id=product_id)
        cart,created=CartItem.objects.get_or_create(client=request.user)
        cart_item,created= CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.amount+=1
        cart.product.save()
        return redirect("cart:cart_detail")
       
class CartRemoveView(LoginRequiredMixin,View):
    def post(self, request,cart_item):
        cart_item=get_object_or_404(CartItem,id=cart_item)
        cart_item.delete()
        return redirect("cart:detail")
"""

    