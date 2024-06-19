from django.db import models
from django.db import models
from ecommerce.models import Product
from django.contrib.auth.models import User
import django.utils.timezone

# Create your models here.


class Cart(models.Model):

    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def subtotal(self):
        return self.quantity*self.product.price

ORDER_STATUS_CHOICES = [
    ('placed', 'Order Placed'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
    ('cancelled', 'Cancelled'),
]

DELIVERY_STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('shipped', 'Shipped'),
    ('out_for_delivery', 'Out for Delivery'),
    ('delivered', 'Delivered'),
]

PAYMENT_STATUS_CHOICES=[('cod','cash on delivery'),
                        ('op','online payment')]

class Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.IntegerField()
    address=models.TextField()
    zip_code = models.CharField(max_length=12)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.user.username


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.ForeignKey(Address,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    no_of_items=models.IntegerField(default='#')
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='placed')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    delivery_status = models.CharField(max_length=20, choices=DELIVERY_STATUS_CHOICES, default='pending')
    ordered_date=models.DateTimeField(auto_now_add=True)
    payment_id=models.CharField(max_length=100,default='#')

    def __str__(self):
        return self.user.username


# Create your models here.
