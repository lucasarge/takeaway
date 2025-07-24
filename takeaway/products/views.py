from django.shortcuts import render, redirect
from .models import Product, Cart, CartItem
from django.http import HttpResponse, JsonResponse
import json
from django.contrib import messages


# Create your views here.
def products_menu(request):
    products = Product.objects.all()
    return render(request, 'products/menu.html', {'products': products})

def product_page(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'products/product.html', {'product': product})

def cart(request):

    cart = None
    cartitems = []

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitems = cart.cartitems.all()

    return render(request, "products/cart.html", {"cart":cart, "items":cartitems})


def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cartitem.quantity += 1
        cartitem.save()

        num_of_items = sum(item.quantity for item in cart.cartitems.all())
    return JsonResponse(num_of_items, safe=False)

def remove_from_cart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)
        
        if cartitem:
            if cartitem.quantity > 1:
                cartitem.quantity -= 1
                cartitem.save()
            else:
                cartitem.delete()
            num_of_items = sum(item.quantity for item in cart.cartitems.all())
        else:
            num_of_items = 0
    return JsonResponse(num_of_items, safe=False)