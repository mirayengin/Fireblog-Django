from django.db import models
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import AbstractUser

from products.models import Favorites, Product,Card

from django.contrib.auth.models import User

# class MyUser(AbstractUser):
#     first_name = models.CharField(max_length=25)
#     last_name = models.CharField(max_length=25)
#     username = models.CharField(max_length=25, unique=True)
#     password = models.CharField(max_length=25)
#     email = models.EmailField(unique=True)
#     role = models.CharField(max_length=10)

ROLE = {
    (1,"Seller"),
    (2,"Customer")
}

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(choices=ROLE, blank=True, null=True)
    favorites = models.ForeignKey(Favorites, on_delete=models.CASCADE, blank=True, null=True)
    cards = models.ForeignKey(Card, on_delete=models.CASCADE, blank=True, null=True)
    sell_products = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    avatar = models.ImageField(upload_to="users", default="avatar.png")
    bio = models.CharField(max_length=100, blank=True, null=True)







