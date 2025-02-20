from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from cars.models import Car, CarInventory
from django.db.models import Sum

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, created, **kwargs):
    new_register_count = Car.objects.count()
    new_register_value_total = Car.objects.aggregate()
    
    '''if created:
        new_register'''