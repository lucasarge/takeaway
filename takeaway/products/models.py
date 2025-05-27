from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField()
    
    def __str__(self):
        return self.name

