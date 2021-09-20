from django.urls import path
from . import views

urlpatterns = [

        path('',views.getRoutes),
        path('product/',views.getProduct),
        path('category/',views.getCategory),
        path('subcategory/',views.getSubcategory),

        
        ]