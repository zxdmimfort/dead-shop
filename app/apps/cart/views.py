import uuid
from django.db.models.base import Model as Model
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView

from apps.users.models import UserProxy
from config.settings import settings
from apps.products.models import Product

from .models import Cart, CartItem


# Create your views here.
class CartDetailView(DetailView):
    template_name = "cart/cart_detail.html"
    model = Cart

    def get_object(self, queryset=None):
        if not self.request.user.is_authenticated:
            session = self.request.session
            session_data = session.get(settings.USER_SESSION_ID)
            if session_data is None:
                session_data = {"uuid": str(uuid.uuid4())}
                session[settings.USER_SESSION_ID] = session_data
            session_uuid = session_data["uuid"]
            user, _ = UserProxy.objects.get_or_create(session=session_uuid)
        else:
            user, _ = UserProxy.objects.get_or_create(user=self.request.user)
        cart, _ = Cart.objects.get_or_create(client=user)
        return cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart_items"] = CartItem.objects.filter(cart=self.object)
        context["total_price"] = sum(
            item.product.price * item.amount for item in context["cart_items"]
        )
        return context


def add_to_cart(request, product_uuid):
    product = get_object_or_404(Product, id=product_uuid)
    with transaction.atomic():
        if not request.user.is_authenticated:
            session = request.session
            session_data = session.get(settings.USER_SESSION_ID)
            if not session_data:
                session_data = {"uuid": str(uuid.uuid4())}
                session[settings.USER_SESSION_ID] = session_data
            session_uuid = session_data["uuid"]
            user, _ = UserProxy.objects.get_or_create(session=session_uuid)
        else:
            user, _ = UserProxy.objects.get_or_create(user=request.user)
        cart, _ = Cart.objects.get_or_create(client=user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.amount += 1
        else:
            cart_item.amount = 1
        cart_item.save()
    referer_url = request.META.get("HTTP_REFERER")
    if referer_url:
        return redirect(referer_url)
    else:
        return redirect("cart:cart_detail")


def delete_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect("cart:cart_detail")
