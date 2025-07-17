from django.shortcuts import render
from .models import Product, Cart, CartItem
from django.http import HttpResponse, JsonResponse
import json


# Create your views here.
def products_menu(request):
    products = Product.objects.all()
    return render(request, 'products/menu.html', {'products': products})

def product_page(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'products/product.html', {'product': product})

def cart(request):
    return render(request, "cart.html")

def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    product = Product.objects.get(id=product_id)

    if request.user.is_autheticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed="False")
        cartitem, created = CartItem.objects_get_or_create(cart=cart, product=product)
        cartitem.quantity += 1
        print(cartitem)
    return JsonResponse("it is working", safe=False)