from django.urls import path
from .views import pay, charge, successMsg

app_name = "payment"


urlpatterns = [
    path('', pay, name = "pay"),
    path('charge/', charge, name = "charge"),
    path('success/<str:args>/', successMsg, name = "success"),
]
