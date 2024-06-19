from django.shortcuts import render
from django.db.models import Q
from ecommerce.models import Product,Category

def search(request):
    query = ""
    products = None
    if (request.method == "POST"):
        query = request.POST['q']
        if (query):
            products = Product.objects.filter(Q(name__icontains=query) | Q(price__icontains = query) | Q(category__name__icontains=query))
        
    return render(request, 'search.html', {'query': query, 'b': products})

