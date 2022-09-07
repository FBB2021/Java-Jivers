from django.urls import path
from .views import index

urlpatterns = [
    path('a/', index, name="index"),
]