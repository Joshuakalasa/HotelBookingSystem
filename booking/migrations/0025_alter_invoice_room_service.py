# Generated by Django 4.1.5 on 2023-02-02 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0024_invoice_customer_invoice_guest_invoice_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="room_service",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
