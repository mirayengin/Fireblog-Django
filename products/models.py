from django.db import models
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    amount = models.PositiveIntegerField()
    vote = models.PositiveIntegerField(blank=True, null=True)
    rating = models.PositiveIntegerField(blank=True, null=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    created_date = models.DateField(auto_now_add=True)
    updated_date =models.DateField(auto_now=True)
    image = models.ImageField(upload_to="products", default="avatar.png")

class Favorites(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="favorites", on_delete=models.CASCADE)

class Card(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="card", on_delete=models.CASCADE)