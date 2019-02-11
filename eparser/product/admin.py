from django.contrib import admin
from .models import Phone, Laptop, Order

admin.site.register(Phone)
admin.site.register(Laptop)
admin.site.register(Order)