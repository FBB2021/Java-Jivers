from curses import is_term_resized
from io import BufferedRandom
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
'''
class Inventory(models.Model):
    item_id = models.IntegerField(null=False, blank=False,default=-1)
    name = models.CharField(max_length = 100, null = False, blank = False)
    price = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    brand = models.CharField(max_length = 100, null=False, blank=False,default="default")
    category = models.CharField(max_length=100,null=False, blank=False,default="default")
    location = models.CharField(max_length=100,null=False, blank=False,default="default")
    weight = models.DecimalField(max_digits=19, decimal_places=2,null=False, blank=False,default= -1)



    def __str__(self) -> str:
        return self.name
'''
CATEGORY = (
    ('Computer', 'Computer'),
    ('Shoes', 'Shoes'),
    ('Clothes', 'Clothes'),
    ('Food', 'Food'),
)

class Item(models.Model):
    idItem = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 32, null = False, blank = False)
    nameBrand = models.CharField(max_length = 32, null=False, blank=False,default="default")
    category = models.CharField(max_length=20, choices=CATEGORY, null=False, blank=False,default="default")
    quantity = models.IntegerField(null=False, blank=False)
    weight = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
    nameLocation = models.CharField(max_length=16,null=False, blank=False,default="default")
    # pillow need to be installed to use ImageField
    # python3 -m pip install Pillow
    picture = models.ImageField(null=True, blank=True)
    
    # to show name of the Item when called.
    def __str__(self) -> str:
        return self.name