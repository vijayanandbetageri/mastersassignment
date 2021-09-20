import products
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import ProductSerializer, CategorySerializer, SubcategorySerializer
from products.models import Product , Category, Subcategory

from api import serializers

@api_view(['GET']) 
def getRoutes(request):

    routes = [
            {'GET' : '/api/product'},
            {'GET' : '/api/category'},
            {'GET' : '/api/subcategory'},

    ]

    return Response(routes)

@api_view(['GET'])
def getProduct(request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getCategory(request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getSubcategory(request):
        subcategory = Subcategory.objects.all()
        serializer = SubcategorySerializer(subcategory, many=True)
        return Response(serializer.data)
