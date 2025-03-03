# Generated by Django 5.1.3 on 2025-01-14 21:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_car_photo_car_plate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='factory_year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1886), django.core.validators.MaxValueValidator(2025)]),
        ),
        migrations.AlterField(
            model_name='car',
            name='model_year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1886), django.core.validators.MaxValueValidator(2025)]),
        ),
    ]
