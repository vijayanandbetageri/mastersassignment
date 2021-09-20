import products
from products.models import Product
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Category, Product, Subcategory
 

def Products(request):
    products = Product.objects.all()
    context = {'products': products }
    return render(request,"products.html",context)


def addProduct(request):
    form = ProductForm()
    if request.method =='POST':
        form = ProductForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('products')
    context = {'form':form}
    return render(request, "addproduct.html", context)



