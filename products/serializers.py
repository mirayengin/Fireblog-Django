from .models import Product, Product, Favorites, Cards
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
