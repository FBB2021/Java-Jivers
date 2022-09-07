from io import BufferedRandom
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
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