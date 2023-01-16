from .models import MyUsers, Product, Product, Favorites, Cards
from rest_framework import serializers



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model: Product
        fieids = ["name", "brand", "amount", "vote", "raiting", "seller", "created_date", "updated_date"]


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model: Favorites
        fields = ("product",)

class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model: Cards
        fields = ("product",)

            

class MyUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUsers
        fields = ("username","email", "first_name", "last_name","favorites","card","seller_products")



