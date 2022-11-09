from django.urls import path
from .views import index
from inventory import views
from .views import ItemViewSet
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

admin.site.site_header = 'Java Jivers Database'
admin.site.site_title = 'Java Jivers administration'

urlpatterns = [
    path("", views.index, name="inventory-index"),
    url(r'^item/savefile', views.SaveFile),
] +static(settings.MEDIA_URL, documnet_root = settings.MEDIA_ROOT)+router.urls