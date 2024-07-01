from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.base import Model as Model
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.views.generic import DetailView

from apps.products.models import Product

from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def add_to_cart(request, product_uuid):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_uuid)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd["quantity"], update_quantity=cd["update"])
    return redirect("cart:cart_detail")


def cart_remove(request, product_uuid):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_uuid)
    cart.remove(product)
    return redirect("cart:cart_detail")


def cart_detail(request):
    cart = Cart(request)
    return render(request, "cart/cart_detail.html", {"cart": cart})
