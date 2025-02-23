from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from cars.models import Car, CarInventory
from django.db.models import Sum

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, created, **kwargs):
    new_register_count = Car.objects.count()
    new_register_value_total = Car.objects.aggregate(cars_value_total=Sum('price')) ['cars_value_total'] or 0

    if created:
        CarInventory.objects.create(cars_count=new_register_count, cars_value_total=new_register_value_total)

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, created, **kwargs):
    count_after_delete = Car.objects.count()
    sum_after_delete = Car.objects.aggregate(cars_value_total=Sum('price')) ['cars_value_total'] or 0
