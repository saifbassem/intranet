# Generated by Django 4.2.8 on 2024-06-10 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceDetail',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(db_column='quantity')),
                ('unit_price', models.FloatField(db_column='unit_price')),
                ('calculated_price', models.FloatField(db_column='calculated_price')),
                ('usd_price', models.FloatField(db_column='usd_price')),
                ('total_price', models.FloatField(db_column='total_price')),
            ],
            options={
                'db_table': 'CR_Invoice_Detail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InvoiceHeader',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('increase', models.FloatField(db_column='increase')),
                ('discount', models.FloatField(db_column='discount')),
                ('usd', models.FloatField(db_column='usd')),
                ('total', models.FloatField(db_column='total')),
                ('closed', models.BooleanField(db_column='closed')),
            ],
            options={
                'db_table': 'CR_Invoice_Header',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('itemlookupcode', models.CharField(db_column='itemlookupcode', max_length=35)),
                ('description', models.CharField(db_column='description', max_length=100)),
                ('subdescription', models.CharField(db_column='subdescription3', max_length=100)),
                ('color', models.CharField(db_column='detail1', max_length=100)),
                ('size', models.CharField(db_column='detail2', max_length=100)),
                ('price', models.FloatField(db_column='price')),
            ],
            options={
                'db_table': 'item_invoice',
                'managed': False,
            },
        ),
    ]
