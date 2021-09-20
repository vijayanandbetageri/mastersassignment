from rest_framework import serializers
from products.models import Product , Category, Subcategory



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        category = CategorySerializer(many = False)
        model = Subcategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    subcategory = SubcategorySerializer(many = False)
    category = CategorySerializer(many = False)
    class Meta:
        model = Product
        fields = '__all__'