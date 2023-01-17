from django.shortcuts import render
from .serializers import ProductSerializer
from .models import Product
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics, status
# Create your views here.

class ProductMVS(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = self.perform_create(serializer)
        data = {
                "message": f"Personal {product.name} saved successfully",
                "product" : serializer.data
            } 
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        product = serializer.save()
        print("user", self.request.user)
        product.seller_id = self.request.user.id
        product.save()
        return product