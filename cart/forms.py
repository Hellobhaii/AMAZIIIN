from django import forms
from.models import Order

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'email', 'address')

class PaymentForm(forms.Form):
    payment_method = forms.ChoiceField(choices=[('cash', 'Cash'), ('credit', 'Credit Card')])
    card_number = forms.CharField(required=False)
    expiration_date = forms.CharField(required=False)
    cvv = forms.CharField(required=False)