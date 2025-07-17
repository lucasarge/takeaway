from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(default='fallback.png', blank=True)
    
    def __str__(self):
        return self.name

class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='item')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='product_cartitem')
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.product.name