from django.contrib import admin
from .models import Cart,Address,Order
# Register your models here.

admin.site.register(Cart)
admin.site.register(Address)
admin.site.register(Order)