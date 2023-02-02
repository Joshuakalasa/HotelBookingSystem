# Generated by Django 4.1.5 on 2023-02-02 20:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0017_alter_room_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.CreateModel(
            name="Invoice",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid3,
                        max_length=40,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="booking.room",
                    ),
                ),
            ],
        ),
    ]