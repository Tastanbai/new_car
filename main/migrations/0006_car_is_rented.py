# Generated by Django 5.0.3 on 2024-03-24 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='is_rented',
            field=models.BooleanField(default=False),
        ),
    ]
