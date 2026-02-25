from django import forms
from .models import Client, Invoice


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'address']


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['client','number','status','amount','due_date','notes']