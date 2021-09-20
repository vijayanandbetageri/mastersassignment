from django.db import models
import datetime
import uuid

from django.db.models.fields import AutoField

#class Category(models.Model):
#    categoryName = models.CharField(max_length=500)
#    created = models.DateTimeField(auto_now_add=True)

#    def __str__(self):
#        return self.categoryName


class Category(models.Model):
    name = models.CharField(max_length=200, null=True)
    #state = models.BooleanField(default=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    #subcategoryrel = models.ManyToManyField('Subcategory',blank=True)
    def __str__(self):
        return self.name 

class Subcategory(models.Model):
    name = models.CharField(max_length=200,null=True)
    #state = models.BooleanField(default=True)
    categoryrel = models.ManyToManyField(Category)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    subcategory = models.ForeignKey(Subcategory,blank = True, on_delete= models.CASCADE) 
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null=True,blank=True )
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name