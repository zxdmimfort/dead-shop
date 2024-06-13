from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.base import Model as Model
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView

from apps.products.models import Product

from .models import Cart, CartItem


# Create your views here.
class CartDetailView(LoginRequiredMixin, DetailView):
    template_name = "cart/cart_detail.html"
    model = Cart

    def get_object(self, queryset=None):
        cart, created = Cart.objects.get_or_create(client=self.request.user)
        return cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart_items"] = CartItem.objects.filter(cart=self.object)
        context["total_price"] = sum(
            item.product.price * item.amount for item in context["cart_items"]
        )
        return context

@login_required
def add_to_cart(request, product_uuid):
    product = get_object_or_404(Product,id=product_uuid)
    cart, created = Cart.objects.get_or_create(client=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.amount += 1
    else:
        cart_item.amount = 1

    cart_item.save()
    print(f"ID корзины: {cart.id}")
    print(f"ID продукта: {product.id}")
    print(f"ID элемента корзины: {cart_item.id}")
    print(f"Количество элемента корзины: {cart_item.amount}")
    referer_url = request.META.get('HTTP_REFERER')
    if referer_url:
        return redirect(referer_url)
    else:
        return redirect("cart:cart_detail")
    

@login_required
def delete_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect("cart:cart_detail")


