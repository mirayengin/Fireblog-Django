from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    seller = serializers.StringRelatedField()
    seller_id = serializers.IntegerField()
    class Meta:
        model = Product
        fields = ['name', 'brand', 'amount', 'vote', 'rating',"seller_id", 'seller', 'created_date', 'updated_date']

# class FavoritesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Favorites
#         fields = ['product']

# class CardSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Card
#         fields = ['product']