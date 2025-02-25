from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, post_delete
from cars.models import Car, CarInventory
from django.db.models import Sum
from deepseek_api import client



def car_inventory_update():
    new_count = Car.objects.count()
    new_price_total = Car.objects.aggregate(cars_price_total=Sum('price')) ['cars_price_total'] or 0
    CarInventory.objects.create(cars_count=new_count, cars_value_total=new_price_total)

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.description:
        generated_description = client.get_car_description(instance.model, instance.brand, instance.factory_year)
        instance.description = generated_description

    