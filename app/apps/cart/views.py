from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, UpdateView
from products.models import Product

from .forms import CartAddProductForm
from .models import Cart, CartItem


# Create your views here.
class CartDetailView(LoginRequiredMixin,DetailView):
    template_name="cart_detail.html"


    def get_context_data(self, **kwargs: Any):
        context=super().get_context_data(**kwargs)
        cart=get_object_or_404(Cart,client=self.request.user)
        cart_items=CartItem.objects.filter(cart=cart)
        total_price=sum(product.price * product.amount for product in cart_items)
        context["cart"]=cart
        context["cart_items"]=cart_items
        context["total_price"]=total_price
        return context

class CartAddView(LoginRequiredMixin,UpdateView):
    def post(self,request,product_id):
        product=get_object_or_404(Product,id=product_id)
        cart,created=CartItem.objects.get_or_create(client=request.user)
        cart_item,created= CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.amount+=1
        cart.product.save()
        return redirect("cart:cart_detail")
       
class CartRemoveView(LoginRequiredMixin,UpdateView):
    def post(self, request,cart_item):
        cart_item=get_object_or_404(CartItem,id=cart_item)
        cart_item.delete()
        return redirect("cart:detail")


    