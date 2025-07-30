from django.shortcuts import render
from .models import Product, Cart, CartItem, Label
from django.http import JsonResponse
import json
from django.contrib import messages
from django.db.models import Q

# Product views are created below.

# products_menu creates the view for the menu sharing variables to html file.
def products_menu(request):
    search_query=request.GET.get('search','')
    labels = Label.objects.all()
    if search_query=='':
        # If search_query wasn't inputted then display all items.
        products = Product.objects.all()
    else:
        # Else display items which contain search_query in label or name.
        products = Product.objects.filter(
            Q(name__icontains = search_query) |
            Q(labelproduct__label__name__icontains = search_query)
            ).distinct()    
    # Shares the variables products, labels and search_query to menu.html.
    return render(request, 'products/menu.html', {'products': products, 
                                                  'labels':labels,
                                                  'search_query':search_query})

# product_page creates the view for a singular products html file auto-gen.
def product_page(request, slug):
    product = Product.objects.get(slug=slug)
    labels = product.labels.all()
    ingredients = product.ingredients.all()
    allergies = []
    for ingredient in ingredients:
        # Getting all allergies in allergy database related to item.
        allergies.extend(ingredient.allergy.all())
    # Set so AnonymousUser can still access page but needs authenticity to buy.
    cartitem = None
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(
            user=request.user, completed=False)
        cartitem = cart.cartitems.filter(product=product).first()
    # Shares the variables displayed below to the product.html.
    return render(request, 'products/product.html', {'product': product, 
                                                     'labels':labels,
                                                     'item':cartitem,
                                                     'ingredients':ingredients,
                                                     'allergies': allergies})

# cart creates the view for the cart.html displaying all items in cart.
def cart(request):
    # This is necessary for AnonymousUser to be able to access the page still.
    cart = None
    cartitems = []
    # This checks if user's authenticated before doing the below to stop errors.
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(
            user=request.user, completed=False)
        cartitems = cart.cartitems.all()
    # This shares the variables cart and cartitems from the models to the html.
    return render(request,"products/cart.html",{"cart":cart,"items":cartitems})

# add_to_cart is a view that doesn't render but uses logic to add items to cart.
def add_to_cart(request):
    # Data collected from JS or models
    data = json.loads(request.body)
    product_id = data["id"]
    quantity = data.get("quantity", 1)
    product = Product.objects.get(id=product_id)
    if request.user.is_authenticated:
        # It makes sure user's authenticated here as they need a cart for below.
        cart, created = Cart.objects.get_or_create(
            user=request.user, completed=False)
        cartitem, created = CartItem.objects.get_or_create(
            cart=cart, product=product)
        cartitem.quantity += quantity
        cartitem.save()
        num_of_items = sum(item.quantity for item in cart.cartitems.all())
        # Here instead of returning render it returns variable and updates db.
        return JsonResponse(num_of_items, safe=False)    
    # If user is not authenticated it prints error message through layout.html.
    return JsonResponse({"error": 
    "You need to <a class='underlined' href='/users/register'>login.</a>"}, 
    status=401)

# remove_from_cart view won't render but uses logic to remove items from cart.
def remove_from_cart(request):
    # Data collected from JS or models
    data = json.loads(request.body)
    product_id = data["id"]
    product = Product.objects.get(id=product_id)
    if request.user.is_authenticated:
        # If user is authenticated it will collect their cart.
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)
        # The if-statement below removes 1 item unless it = 0 where it deletes.
        if cartitem:
            if cartitem.quantity > 1:
                cartitem.quantity -= 1
                cartitem.save()
            else:
                cartitem.delete()
            num_of_items = sum(item.quantity for item in cart.cartitems.all())
        else:
            num_of_items = 0
        # It returns a JsonResponse that updates num_of_items after the logic.
        return JsonResponse(num_of_items, safe=False)
    # Even though AnonymousUser won't have items to remove it's safe to have.
    return JsonResponse({"error": "User not authenticated"}, status=401)
