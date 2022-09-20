from django.urls import path
from .views import index
from inventory import views
from django.urls import re_path as url

# upload image
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('a/', index, name="index"),
]

urlpatterns = [
    url(r'^inventory$', views.itemApi),

    # ([0-9]+)$ will pass a number here
    url(r'^inventory/([0-9]+)$', views.itemApi),
    # if can use the _id field in mongodb
    # url(r'^user/(?P<id>[\w.@+-]+)$', views.userApi)
    # (?P<id>[\w.@+-]+) this will pass a string include the char '.' '@' '+' and '-'
    url(r'^item/savefile', views.SaveFile)
] +static(settings.MEDIA_URL, documnet_root = settings.MEDIA_ROOT)