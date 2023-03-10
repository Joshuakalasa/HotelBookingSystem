# Generated by Django 4.1.5 on 2023-02-02 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0009_alter_room_room_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="room_type",
            field=models.CharField(
                choices=[
                    (0, "Default"),
                    ("S", "Single"),
                    ("D", "Double"),
                    ("F", "Family"),
                ],
                default=0,
                max_length=1,
            ),
        ),
    ]
