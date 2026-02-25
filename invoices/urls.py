from django.urls import path
from . import views

urlpatterns = [
    path('invoices/', views.invoice_list, name='invoice_list'),  # lista faktur
    path('invoices/create/', views.invoice_create, name='invoice_create'),  # nowa faktura
    path('clients/', views.client_list, name='client_list'),  # lista klientów
    path('clients/create/', views.client_create, name='client_create'),  # nowy klient
]