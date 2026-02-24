from django.shortcuts import render
from .models import Invoice, Client

def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, "invoices/invoice_list.html", {"invoices": invoices})


def client_list(request):
    clients = Client.objects.all()
    return render(request, "invoices/client_list.html", {"clients": clients})

