from django.urls import path
from .views import index
from inventory import views
from .views import ItemViewSet,brandViewSet
from rest_framework.routers import DefaultRouter
from django.urls import re_path as url
from django.contrib import admin

# upload image
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register(
    'itemviewset',ItemViewSet,basename='item'
)
router.register(
    'brandviewset',brandViewSet,basename='item'
)

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
    # url(r'^user/(?P<id>[\w.@+-]+)$', views.userApi)
    # (?P<id>[\w.@+-]+) this will pass a string include the char '.' '@' '+' and '-'
    url(r'^item/savefile', views.SaveFile),
    url(r'^itemSearch/(?P<name>[\w.@+-]+)$', views.itemSearch)
] +static(settings.MEDIA_URL, documnet_root = settings.MEDIA_ROOT)+router.urls