from django.urls import path

from . import views

app_name = "invoicing"

urlpatterns = [

    path("", views.index, name="index"),
    path("<int:invoice_id>/", views.invoice_details, name="invoice_details"),
    path("new_invoice", views.create_invoice, name="create_invoice"),
    path("download/<int:invoice_id>/", views.invoice_download, name="invoice_download"),
]