from django.urls import path
from . import views

urlpatterns = [
    path('invoices/',views.invoice_list, name='invoice_list'),
    path('clients/',views.client_list, name='client_list'),
]