from django.urls import path
from notifications.views import ShowNotifications, DeleteNotification


app_name = "notifications"

urlpatterns = [
   	path('', ShowNotifications, name='show-notifications'),
   	path('<noti_id>/delete', DeleteNotification, name='delete-notification'),

]