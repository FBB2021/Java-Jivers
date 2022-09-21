from django.contrib import admin
from .models import Item
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','nameBrand','quantity','nameLocation','weight')
    list_filter = ('nameBrand','quantity','category')

# Register your models here.
admin.site.register(Item, ProductAdmin)
#admin.site.unregister(Group)
