from django.contrib import admin
from cars.models import Car, Brand


class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", )


# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "brand", "factory_year", "model_year", 'plate', "price")
    search_fields = ("model", )


admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)

