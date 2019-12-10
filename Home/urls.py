from django.contrib import admin
from django.urls import path
from .views import home
# from .views import detail
from django.urls import include
app_name = "Home"

urlpatterns = [
    path('', home, name = 'index'),
]