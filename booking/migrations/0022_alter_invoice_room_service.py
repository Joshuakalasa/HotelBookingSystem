# Generated by Django 4.1.5 on 2023-02-02 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0021_service_invoice_date_invoice_mini_bar_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="room_service",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
