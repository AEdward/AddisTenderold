from django.contrib import admin
from django.urls import path
from .views import home, email
# from .views import detail
from django.urls import include

app_name = "Home"

urlpatterns = [
    path('', home, name = 'index'),
       path('email/', email, name = "email"),
]