from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

# Create your models here.
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
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

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.model



    

