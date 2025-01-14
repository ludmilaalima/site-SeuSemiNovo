from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

# Create your models here.

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200) 

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name = 'car_brand')
    
    factory_year = models.IntegerField(
        validators = [
            MinValueValidator(1886),
            MaxValueValidator(datetime.datetime.now().year)
        ]
    )

    model_year = models.IntegerField(
        validators = [
            MinValueValidator(1886),
            MaxValueValidator(datetime.datetime.now().year)
        ]
    )
    plate = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.model



    

