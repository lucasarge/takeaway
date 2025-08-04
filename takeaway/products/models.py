from django.db import models
from django.contrib.auth.models import User
import uuid

# Product models created here.

# Label database with one field and that fields name displayed in admin site.
class Label(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

# Ingredient database with a manytomany connector allergy and name field.
class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    allergy = models.ManyToManyField('Allergy', through='AllergyIngredient')

    def __str__(self):
        return self.name
    
# Allergy database similar to Label database with one field and same return.
class Allergy(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

# Product database that connects all with two manytomany fields and 5 fields.
class Product(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(default='fallback.png', blank=True)
    labels = models.ManyToManyField('Label', through='LabelProduct')
    ingredients = models.ManyToManyField('Ingredient', 
                                         through='IngredientProduct')
    
    def __str__(self):
        return self.name

# AllergyIngredient is a manytomany table connecting Allergy and Ingredient.
class AllergyIngredient(models.Model):
    allergy = models.ForeignKey(Allergy, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient.name

# IngredientProduct is a manytomany table connecting Ingredient and Product.
class IngredientProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

# LabelProduct is a manytomany table connecting Label and Product.
class LabelProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

# Cart database creates cart for each user and stores 
class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    
# Sums for total price using @property allowing for logic added.
    @property
    def total_price(self):
        cartitems = self.cartitems.all()
        total = sum([item.price for item in cartitems])
        return total
    
# Sums for quantity that is used in the context_processors.py.
    @property
    def num_of_items(self):
        cartitems = self.cartitems.all()
        quantity = sum(item.quantity for item in cartitems)
        return quantity

# CartItem is a manytomany table between Cart and Product also storing quantity.
class CartItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='items')
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='cartitems')
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.product.name

# Price calculates the total cost of a specific item and how many are purchased.
    @property
    def price(self):
        quantity_price = self.product.price * self.quantity
        return quantity_price