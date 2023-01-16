from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import MyUser
from .serializers import RegisterUserSerializer
# Create your views here.

class RegisterUserView(CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = RegisterUserSerializer

    