from django.contrib import admin
from . import models

admin.site.register(models.CustomerName)
admin.site.register(models.ProductTemur)

admin.site.register(models.Car)
admin.site.register(models.NummerCar)
