from django.shortcuts import render
from .models import Product
from django.http import HttpResponse


# Create your views here.
def products_menu(request):
    products = Product.objects.all()
    return render(request, 'products/menu.html', {'products': products})

def product_page(request, slug):
    product = Product.objects.get(slug=slug)
    all = Product.objects.all()
    return render(request, 'products/product.html', {'product': product, 'all': all})