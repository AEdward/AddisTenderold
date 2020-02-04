from django.contrib import admin
from django.urls import path, include
from .views import room

app_name = 'chat'
urlpatterns = [
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
    path('<str:room_name>/', room, name='room'),

]