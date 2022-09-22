from curses import is_term_resized
from io import BufferedRandom
from pydoc import describe
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
CATEGORY = (
    ('Computer', 'Computer'),
    ('Shoes', 'Shoes'),
    ('Clothes', 'Clothes'),
    ('Food', 'Food'),
)

class Region(models.Model):
    nameRegion = models.CharField(primary_key=True,unique=True,max_length=16,null=False,blank=False)
    description = models.CharField(max_length=64,null=True,blank=True)
    usage = models.DecimalField(max_digits=8, decimal_places=2, null=False,blank=False,default=0)
    # to show name when called.
    def __str__(self) -> str:
        return self.nameRegion

class Location(models.Model):
    nameLocation = models.CharField(primary_key=True,unique=True,max_length=16,blank=False,null=False)
    nameRegion = models.CharField(primary_key=False,unique=False,max_length=16,blank=False,null=False)
    # (*) See data sample of idItem in item collection
    idItem = models.IntegerField(null=False, blank=False,default=-1)
    def __str__(self) -> str:
        return self.nameLocation

class Item(models.Model):
    idItem = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 32, null = False, blank = False)
    nameBrand = models.CharField(max_length = 32, null=False, blank=False,default="default")
    category = models.CharField(max_length=20, choices=CATEGORY, null=False, blank=False,default="default")
    quantity = models.IntegerField(null=False, blank=False,default=1)
    weight = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
    nameLocation = models.CharField(max_length=16,null=False, blank=False,default="default")
    # pillow need to be installed to use ImageField
    # python3 -m pip install Pillow
    picture = models.ImageField(null=True, blank=True)
    
    # to show name when called.
    def __str__(self) -> str:
        return self.name

class Brand(models.Model):
    name = models.CharField(primary_key=True,unique=True,max_length=16,blank=False,null=False)
    desciption = models.CharField(primary_key=False,unique=False,max_length=64,blank=True,null=True)
    # to show name when called.
    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(primary_key=True,unique=True,max_length=16,blank=False,null=False)
    desciption = models.CharField(primary_key=False,unique=False,max_length=64,blank=True,null=True)
    # to show name when called.
    def __str__(self) -> str:
        return self.name
