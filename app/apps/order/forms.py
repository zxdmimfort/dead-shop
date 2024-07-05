from django import forms

from apps.order.models import Order


class EmailForm(forms.Form):
    email = forms.EmailField()

    class Meta:
        model = Order
        fields = ["email"]
