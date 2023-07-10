from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    # Поля модели продукта

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
