from django.contrib import admin
from .models import Item, Location, Region, Brand, Category
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','nameBrand','quantity','nameLocation','weight')
    list_filter = ('nameBrand','quantity','category')

# Register your models here.
admin.site.register(Item, ProductAdmin)
admin.site.register(Region)
admin.site.register(Location)
admin.site.register(Brand)
admin.site.register(Category)
#admin.site.unregister(Group)
