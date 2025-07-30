from django.contrib import admin
from .models import Label, LabelProduct
from .models import Product, Cart, CartItem
from .models import Ingredient, IngredientProduct
from .models import Allergy, AllergyIngredient

# Connecting models databases to my admin page.
admin.site.register([Product, Cart, CartItem, 
                     Label, LabelProduct, 
                     Ingredient, IngredientProduct,
                     Allergy, AllergyIngredient])