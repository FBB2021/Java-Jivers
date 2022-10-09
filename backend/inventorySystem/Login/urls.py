from django.urls import re_path as url
from django.urls import path
from Login import views

# upload image
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^user$', views.userApi),

    # ([0-9]+)$ will pass a number here
    url(r'^user/([0-9]+)$', views.userApi),
    # if can use the _id field in mongodb
    # url(r'^user/(?P<id>[\w.@+-]+)$', views.userApi)
    # (?P<id>[\w.@+-]+) this will pass a string include the char '.' '@' '+' and '-'


    url(r'^user/savefile', views.SaveFile),

    # From https://github.com/duplxey/django-spa-cookie-auth/blob/master/django_react_templates/api/urls.py
    path('login/', views.login_view, name='api-login'),
    path('logout/', views.logout_view, name='api-logout'),
    path('session/', views.session_view, name='api-session'),
    path('whoami/', views.whoami_view, name='api-whoami'),
    # End copied code
] +static(settings.MEDIA_URL, documnet_root = settings.MEDIA_ROOT)