from django.contrib import admin
from django.urls import path
from .views import tenders
# from .views import detail
from django.urls import include

app_name = "tenders"

urlpatterns = [
    path('', tenders, name = 'tenders'),
]