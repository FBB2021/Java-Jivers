from django.urls import re_path as url
from . import views
from .views import UserCreateViewSet, UserViewSet
from rest_framework.routers import DefaultRouter
# upload image
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register('userviewset',UserViewSet,basename='user')
router.register('user_create',UserCreateViewSet,basename='user')

urlpatterns = [
    url(r'^user/savefile', views.SaveFile)
] +static(settings.MEDIA_URL, documnet_root = settings.MEDIA_ROOT)+router.urls