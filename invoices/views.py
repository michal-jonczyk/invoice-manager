from django.shortcuts import render, redirect
from .models import Invoice, Client
from .forms import ClientForm, InvoiceForm


def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoices/invoice_list.html', {'invoices': invoices})


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'invoices/client_list.html', {'clients': clients})


def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'invoices/client_form.html', {'form': form})


def invoice_create(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm()
    return render(request, 'invoices/invoice_form.html', {'form': form})