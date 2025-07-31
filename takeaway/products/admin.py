from django.contrib import admin
from .models import Label, LabelProduct
from .models import Product, Cart, CartItem
from .models import Ingredient, IngredientProduct
from .models import Allergy, AllergyIngredient

# Register your models here.
admin.site.register([Product, Cart, CartItem, 
                     Label, LabelProduct, 
                     Ingredient, IngredientProduct,
                     Allergy, AllergyIngredient])