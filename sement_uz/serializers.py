from rest_framework import serializers
from .models import Product, Order, User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'image', 'quantity', 'get_image_url']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'phone_number', 'image', 'is_active', 'is_staff', 'is_superuser']

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    user = UserSerializer()

    class Meta:
        model = Order
        fields = ['id', 'user', 'product', 'name', 'phone', 'quantity', 'status']
