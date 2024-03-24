# Generated by Django 5.0.3 on 2024-03-20 12:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fuel_type', models.CharField(max_length=50)),
                ('volume', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent', models.CharField(max_length=100)),
                ('date_out', models.DateField()),
                ('time_out', models.TimeField()),
                ('date_in', models.DateField()),
                ('time_in', models.TimeField()),
                ('fuel', models.DecimalField(decimal_places=2, max_digits=5)),
                ('mileage', models.PositiveIntegerField()),
                ('payment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('notes', models.TextField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.car')),
            ],
        ),
    ]
