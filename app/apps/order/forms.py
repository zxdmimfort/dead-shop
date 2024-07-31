from apps.order.models import Order
from django import forms


class EmailForm(forms.Form):
    email = forms.EmailField()

    class Meta:
        model = Order
        fields = ["email"]
