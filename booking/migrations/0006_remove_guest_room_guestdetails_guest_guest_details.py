# Generated by Django 4.1.5 on 2023-02-02 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0005_reservation_number_of_night_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="guest",
            name="room",
        ),
        migrations.CreateModel(
            name="GuestDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
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
        migrations.AddField(
            model_name="guest",
            name="guest_details",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="booking.guestdetails",
            ),
        ),
    ]