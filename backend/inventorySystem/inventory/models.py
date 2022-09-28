from curses import is_term_resized
from enum import unique
from io import BufferedRandom
from pydoc import describe
from tokenize import ContStr
from traceback import print_stack
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
'''
CATEGORY = (
    ('Computer', 'Computer'),
    ('Shoes', 'Shoes'),
    ('Clothes', 'Clothes'),
    ('Food', 'Food'),
)
'''

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
    idItem = models.AutoField(unique=True,primary_key=True)
    name = models.CharField(max_length = 32, null = False, blank = False)
    nameBrand = models.CharField(max_length = 32, null=False, blank=False,default="default")
    quantity = models.IntegerField(null=False, blank=False,default=1)
    nameLocation = models.CharField(max_length=16,null=False, blank=False,default="default")
    # pillow need to be installed to use ImageField
    # python3 -m pip install Pillow
    picture = models.ImageField(null=True, blank=True)
    desciption = models.CharField(primary_key=False,unique=False,max_length=64,blank=True,null=True)
    cost = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
    dateBestBefore = models.DateField(null=True,blank=True)

    weight = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
    length = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
    width  = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)

    categoryStorageCondition = (
    ('Frozen(below -4 degrees)', 'Frozen(below -4 degrees)'),
    ('Normal', 'Normal'),
    ('Refrigeration', 'Refrigeration')
    )   
    conditionStorage = models.CharField(max_length=32, choices=categoryStorageCondition, \
        null=False, blank=False,default="default")


    categoryItem =(
    ('Appliances', 'Appliances'),
    ('Apps & Games', 'Apps & Games'),
    ('Arts, Handicrafts & Sewing', 'Arts, Handicrafts & Sewing'),
    ('Automotive Parts & Accessories', 'Automotive Parts & Accessories'),
    ('Baby', 'Baby'),
    ('Baggage & Travel Equipment', 'Baggage & Travel Equipment'),
    ('Beauty', 'Beauty'),
    ('Beauty & Personal Care', 'Beauty & Personal Care'),
    ('Books', 'Books'),
    ('CDs & Vinyl', 'CDs & Vinyl'),
    ('Cell Phones & Accessories', 'Cell Phones & Accessories'),
    ('Centurion Garden & Outdoor', 'Centurion Garden & Outdoor'),
    ('Clothing, Shoes and Jewelry', 'Clothing, Shoes and Jewelry'),
    ('Collectibles & Fine Art', 'Collectibles & Fine Art'),
    ('Computers & Electronics', 'Computers & Electronics'),
    ('Film Supplies', 'Film Supplies'),
    ('Food', 'Food'),
    ('Handcrafts', 'Handcrafts'),
    ('Health & Baby Care', 'Health & Baby Care'),
    ('Household & Kitchen Appliances', 'Household & Kitchen Appliances'),
    ('Industrial & Scientific Supplies', 'Industrial & Scientific Supplies'),
    ('Musical Instrument', 'Musical Instrument'),
    ('Others', 'Others'),
    ('Pet Supplies', 'Pet Supplies'),
    ('Sports & Outdoor', 'Sports & Outdoor'),
    ('Tools & Home Decoration', 'Tools & Home Decoration'),
    ('Video Games', 'Video Games'),
    ('Toys & Games', 'Toys & Games'),
    )   


    category = models.CharField(max_length=64, choices=categoryItem, null=False, \
        blank=False,default="default")
    
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
