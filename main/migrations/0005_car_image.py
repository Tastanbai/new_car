# Generated by Django 5.0.3 on 2024-03-24 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(null=True, upload_to='car_images'),
        ),
    ]