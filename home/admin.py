from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Menu)
admin.site.register(Food)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Contact)
admin.site.register(Coupon)