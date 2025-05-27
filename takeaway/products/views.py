from django.shortcuts import render
from .models import Product

# Create your views here.
def menu_view(request):
    products = Product.objects.all()
    return render(request, 'menu.html', {'products': products})