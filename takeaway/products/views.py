from django.shortcuts import render
from .models import Product
from django.http import HttpResponse, JsonResponse
import json
# , Cart, CartItem

# Create your views here.

def products_cart(request):
    return render(request, 'products/cart.html')

def products_menu(request):
    products = Product.objects.all()
    return render(request, 'products/menu.html', {'products': products})

def product_page(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'products/product.html', {'product': product})

# def cart(request):

#     cart = None
#     cartitems = []

#     if request.user.is_authenticated:
#         cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
#         cartitems = cart.cartitems.all()

#     context = {"cart":cart,"items":cartitems}
#     return render(request, "cart.html", context)

# def add_to_cart(request):
#     data = json.loads(request.body)
#     product_id = data["id"]
#     product = Product.objects.get(id=product_id)

    # if request.user.is_autheticated:
    #     cart, created = Cart.objects.get_or_create(user=request.user, completed="False")
    #     cartitem, created = CartItem.objects_get_or_create(cart=cart, product=product)
    #     cartitem.quantity += 1
    #     print(cartitem)
    # return JsonResponse("it is working", safe=False)