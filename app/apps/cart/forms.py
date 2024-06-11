from django import forms


class CartAddProductForm(forms.Form):
    quntity=forms.IntegerField(min_value=1,initial=1)