from django.shortcuts import render,get_object_or_404,redirect
from .models import Cart,Address,Order
from ecommerce.models import Category,Product
from django.contrib.auth.decorators import login_required
from decimal import Decimal            
from django.conf import settings
import razorpay
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
import secrets
import string
from django.http import JsonResponse
import json
from django.contrib import messages
from ecommerce.forms import UserForm,AddressForm
# Create your views here.


@login_required
def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            messages.success(request, 'Address added successfully!')
            return redirect('ecommerce:userprofile')  
    else:
        form = AddressForm()
    return render(request, 'add_address.html', {'form': form})

@login_required
def update_address(request):
    user_address = Address.objects.get(user=request.user)
    if request.method == 'POST':
        form = AddressForm(request.POST,instance=user_address)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('ecommerce:userprofile')
    else:
        form=AddressForm(instance=user_address)
    return render(request, 'update_address.html', {'form': form,})


@login_required
def delete_address(request):
    user_address = Address.objects.get(user=request.user)
    if user_address:
        user_address.delete()
        return redirect('ecommerce:userprofile')

@login_required
def cartview(request):
    try:
        user_address = Address.objects.get(user=request.user)
    except Address.DoesNotExist:
        user_address = None
        messages.error(request, "You need to add an address before placing an order.")
        
    
    u=request.user
    cart=Cart.objects.filter(user=u)
    
    total=0
    for i in cart:
        total+=i.quantity*i.product.price

     
    offer=Decimal('0')
    discount = Decimal('0')
    
    if total >= Decimal('1000'):
        discount = Decimal('0.2') * total  # 20% discount
        offer=total-discount

    return render(request,'cartview.html',{'c':cart,'t':total,'d':discount,'dis':offer,'address':user_address})




@login_required
def addtocart(request,n):

    p=Product.objects.get(name=n)
    u=request.user#current login user
    try:
        cart=Cart.objects.get(user=u,product=p) #it checks if product is already added to cart else except will work
        if(p.stock > 0):
            cart.quantity+=1  # it add one quantity to that particular product
            cart.save()
            p.stock-=1  #after adding quantity and the quantity of that particular product is taken from the stock field so we also need to decrease the stock of that product
            p.save()
    except:
        if(p.stock > 0):
            cart=Cart.objects.create(product=p,user=u,quantity=1) #when we adding first time a product to cart so this will create a cart of that particular product with one quantity
            cart.save()
            p.stock-=1
            p.save()
    return cartview(request)

@login_required
def remove_quantity(request,n):
    p=Product.objects.get(name=n)
    u=request.user
    try:
        cart=Cart.objects.get(user=u,product=p)
        if(cart.quantity>1):
            cart.quantity-=1
            cart.save()
            p.stock+=1
            p.save()

        else:
            cart.delete()
            p.stock += 1
            p.save()
    except:
        pass

    return cartview(request)


@login_required
def delete_item(request,n):
    p=Product.objects.get(name=n)
    u=request.user
    try:
        cart=Cart.objects.get(user=u,product=p)
        cart.delete()
        p.stock+=cart.quantity
        p.save()
    except:
        pass

    return cartview(request)



################### razorpay payment with jquery in below################


@login_required
def order_form(request):

    try:
        user_address = Address.objects.get(user=request.user)
    except Address.DoesNotExist:
        messages.error(request, "You need to add an address before placing an order.")
        return redirect('cart:add_address')
    
    if request.method == "POST":
        payment_method = 'cod'
        cart=Cart.objects.filter(user=request.user)

        total = Decimal('0')
        for i in cart:
            total+=i.quantity*i.product.price

        if total >= Decimal('1000'):
            discount = Decimal('0.2') * total  # 20% discount
            amount=total-discount
        else:
            amount=total
        
        for i in cart:
            address_obj = Order.objects.create(
            user=request.user,
            product=i.product,
            address=user_address,
            payment_status=payment_method,
            no_of_items=i.quantity,
            payment_id='cod'
                )
            
            address_obj.save()

            cart.delete()

    return redirect('cart:orderconfirm')


@login_required
def order_confirm(request):
    return render(request,'order_confirm.html')



@login_required
def razorpaycheck(request):
    cart=Cart.objects.filter(user=request.user)
    user=request.user
    email=user.email
    name = user.get_full_name()
    total = Decimal('0')
    for i in cart:
        total+=i.quantity*i.product.price
    if total >= Decimal('1000'):
        discount = Decimal('0.2') * total  # 20% discount
        amount=total-discount
    else:
        amount=total

    return JsonResponse({
        'total_price':amount,
        'user_name': name,
        'user_email': email,

    })


@login_required
def orders(request):
    user=request.user
    orders=Order.objects.filter(user=user)
    
    return render(request,'orderpage.html',{'orders':orders})