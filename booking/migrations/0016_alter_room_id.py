# Generated by Django 4.1.5 on 2023-02-02 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0015_alter_room_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="id",
            field=models.PositiveIntegerField(
                primary_key=True, serialize=False, unique=True
            ),
        ),
    ]
