# Generated by Django 4.1.5 on 2023-02-02 20:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0019_alter_room_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="id",
            field=models.CharField(
                default=uuid.uuid1,
                max_length=40,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
