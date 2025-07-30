from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Label(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Allergy(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(default='fallback.png', blank=True)
    labels = models.ManyToManyField('Label', through='LabelProduct')
    ingredients = models.ManyToManyField('Ingredient', through='IngredientProduct')
    
    def __str__(self):
        return self.name

class AllergyIngredient(models.Model):
    allergy = models.ForeignKey(Allergy, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

class IngredientProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

class LabelProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    
    @property
    def total_price(self):
        cartitems = self.cartitems.all()
        total = sum([item.price for item in cartitems])
        return total
    
    @property
    def num_of_items(self):
        cartitems = self.cartitems.all()
        quantity = sum(item.quantity for item in cartitems)
        return quantity
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitems')
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.product.name
    
    @property
    def price(self):
        quantity_price = self.product.price * self.quantity
        return quantity_price