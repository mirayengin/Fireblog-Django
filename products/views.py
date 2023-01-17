from django.shortcuts import render
from .serializers import ProductSerializer, FavoritesSerializer, CardSerializer
from .models import Product, Favorites, Card


from rest_framework import viewsets
# Create your views here.

class ProductMVS(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class FavoritesMVS(viewsets.ModelViewSet):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer
