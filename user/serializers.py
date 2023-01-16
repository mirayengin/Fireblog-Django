from .models import MyUser
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer

# class MyUserSerializer(serializers.ModelSerializer):
#     seller_product_count = serializers.SerializerMethodField()
#     class Meta:
#         model = MyUser
#         fields = ("username","email", "first_name", "last_name","favorites","card","seller_products")

    
#     def get_seller_product_count(self, obj):
#         return obj.products.count()


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    # email = serializers.EmailField(required=True, validators=[UniqueValidator])
    class Meta:
        model = MyUser
        fields = ("username","email", "first_name", "last_name", "role", "password", "password2")

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError(
                {"password2": "Passwords must match"}
            )
        return data
    
    # def create(self, validated_data):
    #     validated_data.pop("password2")
    #     user = super().create(**validated_data)
    #     return user
    
    def create(self, validated_data):
        password = validated_data["password"]
        password2 = validated_data.pop("password2")
        user = MyUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
            model = MyUser
            fields = ("id", "username", "email")


class CustomTokenSerializer(TokenSerializer):
     user = UserTokenSerializer(read_only=True)

     class Meta(TokenSerializer):
          fields = ("key","user")












