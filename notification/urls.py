from django.conf.urls import include
from .views import notification
from django.urls import path

app_name = "notification"

urlpatterns = [
    
    path('show/', show_notification, name = 'show_notification'),
    path('delete/', delete_notification, name = 'delete_notification'),
]