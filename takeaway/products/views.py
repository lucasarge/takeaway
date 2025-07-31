from django.shortcuts import render, redirect
from .models import Product, Cart, CartItem, Label, LabelProduct, Ingredient, IngredientProduct
from django.http import HttpResponse, JsonResponse
import json
from django.contrib import messages
from django.db.models import Q


# Create your views here.
def products_menu(request):
    search_query=request.GET.get('search','')
    labels = Label.objects.all()
    if search_query=='':
        products = Product.objects.all()
    else:
        products = Product.objects.filter(
            Q(name__icontains = search_query) |
            Q(labelproduct__label__name__icontains = search_query)
            ).distinct()
    
    return render(request, 'products/menu.html', {'products': products, 
                                                  'labels':labels,
                                                  'search_query':search_query})

def product_page(request, slug):
    product = Product.objects.get(slug=slug)
    labels = product.labels.all()
    ingredients = product.ingredients.all()
    cartitem = None
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem = cart.cartitems.filter(product=product).first()
    return render(request, 'products/product.html', {'product': product, 
                                                     'labels':labels,
                                                     'item':cartitem,
                                                     'ingredients':ingredients})

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
    quantity = data.get("quantity", 1)
    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cartitem.quantity += quantity
        cartitem.save()
        num_of_items = sum(item.quantity for item in cart.cartitems.all())
        return JsonResponse(num_of_items, safe=False)
    
    messages.error(request, "You need to <a class='underlined' href='/users/register'>login.</a>")
    return JsonResponse({"error": "User not authenticated"}, status=401)

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
    
    messages.error(request, "User is not authenticated.")
    return JsonResponse({"error": "User not authenticated"}, status=401)
