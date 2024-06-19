from django.shortcuts import render,redirect,get_object_or_404
from ecommerce.models import Product,Category,Favo,UserProfile
from cart.models import Address
from ecommerce.forms import UserForm,AddressForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def home(request):
    # Get the Category objects for Men, Women, and Kids
    men_category = Category.objects.get(name='Men')
    women_category = Category.objects.get(name='Women')
    kids_category = Category.objects.get(name='Kids')

    # Filter products for Men, Women, and Kids categories
    men_products = Product.objects.filter(category=men_category)
    women_products = Product.objects.filter(category=women_category)
    kids_products = Product.objects.filter(category=kids_category)

    context = {
        'men': men_products,
        'women': women_products,
        'kids': kids_products,
    }
    return render(request, 'home.html', context)


def category(request,n):

    cat=Category.objects.get(name=n)
    prdt=Product.objects.filter(category=cat)

    context={'cat':cat,'prdt':prdt
             }
    return render(request,'cat_based_products.html',context)



def products(request):
    prdts=Product.objects.all()
    context={'prdts':prdts
             }
    return render(request,'products.html',context)


def singleproduct(request,pk):
    prdt = get_object_or_404(Product, pk=pk)
    f = None
    if request.user.is_authenticated:
        f = Favo.objects.filter(user=request.user, item=prdt)
    return render(request,'single-product.html',{'prdt':prdt,'f':f})


def register(request):
        
    if (request.method=="POST"):

        un = request.POST['uname']
        p = request.POST['pass']
        cpass = request.POST['cpass']
        fn = request.POST['fname']
        ln = request.POST['lname']
        email = request.POST['email']

        userExists=User.objects.filter(username=un)
        emailExists=User.objects.filter(email=email)

        if cpass==p:
            if userExists:
                return render(request, 'register.html', {'failed': 'Username already exists!!'})
            else:
                if emailExists:
                    return render(request, 'register.html', {'failed': 'User with email already exists!!'})
                else:
                    u=User.objects.create_user(username=un, password=p,email=email,first_name=fn,last_name=ln)
                    u.save()
                    return render(request, 'register.html', {'success': 'User Created Successfully!!'})
        else:
            return render(request, 'register.html', {'failed': 'password not matching!!'})

    return render(request,'register.html')
    

def user_login(request):
    
    if (request.method == 'POST'):
        username = request.POST['uname']
        password = request.POST['pass']

        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('ecommerce:home')
        else:
            # msg="invalid credentials"
            return render(request, 'login.html', {'failed': "invalid credentials,Try again!!"})

    return render(request,'login.html')


def user_logout(request):
    logout(request)
    return redirect('ecommerce:login')


@login_required
def favourite(request,pk):

    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return render(request, 'error_page.html', {'error_message': 'Item not found'})

    u = request.user
    existing_favorite = Favo.objects.filter(user=u, item=product).exists()

    if existing_favorite:
        Favo.objects.filter(user=u, item=product).delete()
        # messages = 'Product removed from favorites.'
        messages.success(request, 'Product removed from favorites.')
        
    else:
        Favo.objects.create(user=u, item=product).save()
        # messages = 'Product added to favorites.'
        messages.success(request, 'Product added to favorites.')
    
    return redirect('ecommerce:singleprdt',pk=pk)

@login_required
def favor_view(request):
    f=Favo.objects.filter(user=request.user)
    return render(request, 'favo.html',{'f':f})
    

    
@login_required
def update_profile(request):

    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    try:
        user_address = Address.objects.get(user=request.user)
    except Address.DoesNotExist:
        user_address = None
        messages.warning(request, 'You need to add an address.')
    
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('ecommerce:userprofile')
     
    else:
        form = UserForm(instance=user_profile)
    return render(request, 'userprofile.html', {'form': form, 'user_profile': user_profile,'address':user_address})
