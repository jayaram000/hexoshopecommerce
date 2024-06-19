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
from ecommerce import views
app_name="ecommerce"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('category/<n>',views.category,name="category"),
    path('Products/',views.products,name="products",),
    path('singleproduct/<int:pk>',views.singleproduct,name="singleprdt"),
    path('register/',views.register,name="register"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('favourite/<int:pk>',views.favourite,name="favo"),
    path('fav_view',views.favor_view,name="fav_view"),
    path('user_profile',views.update_profile,name="userprofile"),
]
