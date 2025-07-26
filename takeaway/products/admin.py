from django.contrib import admin
from .models import Product, Cart, CartItem, Label, LabelProduct

# Register your models here.
admin.site.register([Product, Cart, CartItem, Label, LabelProduct])