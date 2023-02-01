# Generated by Django 4.1.5 on 2023-02-01 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0004_room_remove_reservation_room_number_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="number_of_night",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="reservation",
            name="number_of_people",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="room",
            name="room_name",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
