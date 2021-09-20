from django.urls import path
from . import views


urlpatterns= [
    
    path('', views.Products , name="products") ,

    path('addproduct/',views.addProduct , name="addproduct") ,

]