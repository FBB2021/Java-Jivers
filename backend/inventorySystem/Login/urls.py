from django.urls import re_path as url
from . import views
from .views import UserViewSet
from rest_framework.routers import DefaultRouter
# upload image
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register(
    'userviewset',UserViewSet,basename='user'
)

urlpatterns = [
    url(r'^user$', views.userApi),

    # ([0-9]+)$ will pass a number here
    url(r'^user/([0-9]+)$', views.userApi),
    # if can use the _id field in mongodb
    # (?P<id>[\w.@+-]+) this will pass a string include the char '.' '@' '+' and '-'

    # for saving uploaded files
    url(r'^user/savefile', views.SaveFile)
] +static(settings.MEDIA_URL, documnet_root = settings.MEDIA_ROOT)+router.urls