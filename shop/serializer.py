from rest_framework import serializers
from .models import *


class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class TagsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProductsSerializers(serializers.ModelSerializer):
    tags = TagsSerializers(read_only=True, many=True)
    cats = CategoriesSerializers(read_only=True, many=True)

    class Meta:
        model = Products
        fields = ['p_id', 'name', 'qnt', 'rate', 'cats', 'tags']


class CustomerSerializers(serializers.ModelSerializer):
    # user = UsersSerializer(read_only=True, many=False)

    class Meta:
        model = Customers
        fields = '__all__'


class OrdersSerializers(serializers.ModelSerializer):
    products = ProductsSerializers(read_only=True, many=True)
    customer = CustomerSerializers(read_only=True, many=False)

    class Meta:
        model = Orders
        fields = ['order_id', 'products', 'order_time', 'customer']
