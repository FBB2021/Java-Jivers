from django.urls import path
from .views import index
from inventory import views
from django.urls import re_path as url
from django.contrib import admin

# upload image
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = 'Java Jivers Database'
admin.site.site_title = 'Java Jivers administration'

urlpatterns = [
    path("", views.index, name="inventory-index"),
    path("manager/", views.manager, name='inventory-manager'),
    path("product/", views.product, name='inventory-product'),
    path("area/", views.area, name='inventory-area'),
    url(r'^inventory$', views.itemApi),
    # ([0-9]+)$ will pass a number here
    url(r'^inventory/([0-9]+)$', views.itemApi),
    # if can use the _id field in mongodb
    url(r'^itemSearch/(?P<name>[\w.@+-]+)$', views.itemSearch),
    # (?P<id>[\w.@+-]+) this will pass a string include the char '.' '@' '+' and '-'
    url(r'^item/savefile', views.SaveFile)
] +static(settings.MEDIA_URL, documnet_root = settings.MEDIA_ROOT)