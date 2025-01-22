from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from cars.models import Brand, Car
import datetime

'''class CarForm(forms.Form):
    model = forms.CharField(max_length=100)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField(
        validators=[
            MinValueValidator(1886),  # Primeiro carro foi fabricado em 1886
            MaxValueValidator(datetime.datetime.now().year)
        ],
    )
    model_year = forms.IntegerField(  
        validators=[
            MinValueValidator(1886),
            MaxValueValidator(datetime.datetime.now().year)
        ],
    )
    plate = forms.CharField(max_length=10)
    price = forms.FloatField()
    photo = forms.ImageField()



    def save(self):
        new_car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            price = self.cleaned_data['price'],
            photo = self.cleaned_data['photo'],
        )

        new_car.save()
        return Car'''


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 8000:
            self.add_error('price', "Valor mínimo do carro é de R$8.000")




