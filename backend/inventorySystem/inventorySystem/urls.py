"""inventorySystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url

from Login import views as viewsLogin
from inventory import views as viewsInventory
# upload image
from django.conf.urls.static import static
from django.conf import settings

# Changes for session based login authentication. Assumed this is our base project head.
from django.shortcuts import render


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("inventory.urls")),
    url(r'^item$', viewsInventory.itemApi),
    url(r'^item/([0-9]+)$', viewsInventory.itemApi),
    url(r'^user$', viewsLogin.userApi),
    url(r'^user/([0-9]+)$', viewsLogin.userApi),
    url(r'^item/savefile', viewsLogin.SaveFile),
    url(r'^user/savefile', viewsLogin.SaveFile),
    path('Login/', include('Login.urls')), #added for login authentication
] +static(settings.MEDIA_URL, documnet_root = settings.MEDIA_ROOT)
