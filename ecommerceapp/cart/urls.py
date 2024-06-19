"""
URL configuration for ecommerceapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from cart import views
app_name="cart"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_address/', views.add_address, name='add_address'),
    path('update_address/', views.update_address, name='update_address'),
    path('delete_address/', views.delete_address, name='delete_address'),
    path('cart/',views.cartview,name="cartview"),
    path('addcart/<n>',views.addtocart,name="addtocart"),
    path('remove_quantity/<n>',views.remove_quantity,name="removequantity"),
    path('delete_item/<n>',views.delete_item,name="delete"),
    path('orderform/',views.order_form,name="orderform"),
    path('order_confirm/',views.order_confirm,name="orderconfirm"),
    path('view_orders/',views.orders,name="orders"),
   
    
    

    


    
]

