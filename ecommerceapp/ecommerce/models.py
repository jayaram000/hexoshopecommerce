from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField(default="")
    image=models.ImageField(upload_to="images/category",null=True,blank=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField()
    image=models.ImageField(upload_to="images/product",null=True,blank=True)
    image1=models.ImageField(upload_to="images/product",null=True,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class Favo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
    
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to="images/users", null=True, blank=True)
    

    def __str__(self):
        return self.user.username


