# Generated by Django 4.1.5 on 2023-02-02 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0008_reservation_details"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="room_type",
            field=models.CharField(
                choices=[(0, "Default"), (1, "Single"), (2, "Double"), (3, "Family")],
                default=0,
                max_length=2,
            ),
        ),
    ]
