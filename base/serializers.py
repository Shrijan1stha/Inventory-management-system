from rest_framework import serializers
from .models import User, Product, ProductCategory, Department, Suppliers, Purchase
from django.contrib.auth.models import Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id','name']



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password', 'groups']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' # sabai fileds ko lagi
        # fields = ['id', 'name', 'name of individual fields in a model'] chaiyeko fields ko lagi

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'