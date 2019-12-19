from django.contrib import admin
from django.urls import path
from .views import contact
# from .views import detail
from django.urls import include

app_name = "contact"

urlpatterns = [
    path('', contact, name = 'contact'),
]