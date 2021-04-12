from django import forms

from orderapp.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('user',)