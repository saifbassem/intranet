import math
from io import BytesIO

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
import pandas
from .models import InvoiceHeader, InvoiceDetail, Item


def index(request):
    """Main Index Page function, Show latest Invoices and handle search"""
    if request.method == 'POST':
        result = request.POST
        invoice_number = result['invoice_number']
        try:
            invoice = InvoiceHeader.objects.get(pk=invoice_number)
        except InvoiceHeader.DoesNotExist:
            messages.error(request, 'Invoice Not Found')
            return redirect('invoicing:index')
        else:

            return redirect("invoicing:invoice_details", invoice_id=invoice.id)

    else:
        latest_invoice_list = InvoiceHeader.objects.filter(closed=0).order_by("-id")[:20]
        context = {"latest_invoice_list": latest_invoice_list}
        return render(request, "invoicing/index.html", context)


def invoice_details(request, invoice_id):
    """Invoice details page"""
    invoice = get_object_or_404(InvoiceHeader, pk=invoice_id)
    quantity = 0
    lines = invoice.invoicedetail_set.all()

    for line in lines:
        quantity += line.quantity

    return render(request, "invoicing/invoice.html", {"invoice": invoice, "quantity": quantity})


def invoice_download(request, invoice_id):
    """Helper function to download the invoice to Excel file"""
    with BytesIO() as b:
        invoice = get_object_or_404(InvoiceHeader, pk=invoice_id)
        lines = invoice.invoicedetail_set.all()
        data = []
        for line in lines:
            data.append([
                line.item.itemlookupcode,
                line.item.description,
                line.item.subdescription,
                line.item.color,
                line.item.size,
                line.quantity,
                line.usd_price,
                line.total_price
            ])
        df = pandas.DataFrame(data,
                              columns=['ItemLookupCode', 'Description', 'Sub Desc.', 'Color', 'Size', 'Quantity',
                                       'USD U.Price', 'USD Total'])

        with pandas.ExcelWriter(b) as writer:
            df.to_excel(writer, sheet_name="Invoice Details", index=False)

        filename = f"Invoice #{invoice.id}.xlsx"
        res = HttpResponse(
            b.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        res['Content-Disposition'] = f'attachment; filename={filename}'
        return res


def truncate(f, n):
    """Helper Function to truncate float to 2 decimal places without rounding"""
    return math.floor(f * 10 ** n) / 10 ** n


def create_invoice(request):
    """Function to show/ create new invoice"""
    if request.method == 'POST':
        result = request.POST.copy()
        # del result['csrfmiddlewaretoken']
        increase = float(result['increase'])
        discount = float(result['discount'])
        usd = float(result['usd'])

        if increase < 0:
            messages.error(request, 'Increase Percent can''t be less than Zero')
            return redirect('invoicing:create_invoice')
        elif discount < 0:
            messages.error(request, 'Discount Percent can''t be less than Zero')
            return redirect('invoicing:create_invoice')
        elif usd < 1:
            messages.error(request, 'USD Rate can''t be less than 1')
            return redirect('invoicing:create_invoice')


        # Create The Invoice Header
        invoice = InvoiceHeader(increase=increase, discount=discount, usd=usd, total=0, closed=0)
        invoice.save()

        # Read the File to get a list of skus
        file = request.FILES['file']
        df = pandas.read_excel(file)
        sku_tuple = tuple(df['sku'].to_list())

        # Get items from sku tuple and save them in invoice lines
        # print(Item.objects.filter(itemlookupcode__in=sku_tuple).query)
        items = Item.objects.filter(itemlookupcode__in=sku_tuple)
        print(items)
        invoice_total = 0
        for item in items:
            item_frame = df.loc[df['sku'] == item.itemlookupcode]

            quantity = float(item_frame['qty'])

            item_price = float(item.price)
            price_increase = truncate(item_price + (item_price * increase / 100), 2)
            calculated_price = truncate(price_increase - (price_increase * discount / 100), 2)
            price_usd = truncate(calculated_price / usd, 2)
            total_price = truncate(price_usd * quantity, 2)

            line = InvoiceDetail(invoice=invoice, item=item, quantity=quantity, unit_price=item_price
                                 , calculated_price=calculated_price, usd_price=price_usd, total_price=total_price)
            line.save()

            invoice_total += total_price

        invoice.total = truncate(invoice_total, 2)
        invoice.save()

        # return redirect("invoicing:index")
        return redirect("invoicing:invoice_details", invoice_id=invoice.id)
    else:
        return render(request, "invoicing/new_invoice.html")
