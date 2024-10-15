from django.db import models


class InvoiceHeader(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    increase = models.FloatField(db_column='increase')
    discount = models.FloatField(db_column='discount')
    usd = models.FloatField(db_column='usd')
    total = models.FloatField(db_column='total')
    closed = models.BooleanField(db_column='closed')

    class Meta:
        db_table = "CR_Invoice_Header"
        managed = False


class Item(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    itemlookupcode = models.CharField( max_length=35, db_column='itemlookupcode')
    description = models.CharField(max_length=100, db_column='description')
    subdescription = models.CharField(max_length=100, db_column='subdescription3')
    color = models.CharField(max_length=100, db_column='detail1')
    size = models.CharField(max_length=100, db_column='detail2')
    price = models.FloatField(db_column='price')


    def __str__(self):
        return f"{self.id}"

    class Meta:
        db_table = "item_invoice"
        managed = False


class InvoiceDetail(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    invoice = models.ForeignKey(InvoiceHeader, on_delete=models.DO_NOTHING, db_column='invoice_id')
    item = models.ForeignKey(Item,on_delete=models.DO_NOTHING, db_column='item_id')
    quantity = models.IntegerField(db_column='quantity')
    unit_price = models.FloatField(db_column='unit_price')
    calculated_price = models.FloatField(db_column='calculated_price')
    usd_price = models.FloatField(db_column='usd_price')
    total_price = models.FloatField(db_column='total_price')

    class Meta:
        db_table = "CR_Invoice_Detail"
        managed = False
