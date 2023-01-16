from django.db import models
from user.models import MyUser

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    amount = models.PositiveIntegerField()
    vote = models.PositiveIntegerField(blank=True, null=True)
    rating = models.PositiveIntegerField(blank=True, null=True)
    seller = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="products")
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

class Favorites(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, related_name="favorites", on_delete=models.CASCADE)

class Card(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, related_name="card", on_delete=models.CASCADE)