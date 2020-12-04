from django.contrib import admin
from django.urls import path
from . import views
from .views import (show_notification,delete_notification) 


'''
urlpatterns = patterns('notification.views',
 url(r'^show/(?p<notification_id>\d+)/s, 'show_notification'),
 url(r'^delete/(?p<notification_id>\d+)/s, 'delete_notification'),
)
'''


app_name = "notification"

urlpatterns = [   
    path('show',  show_notification, name = 'show'),
    path('delete',  delete_notification, name = 'delete'),
    
] 