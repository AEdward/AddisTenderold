from django.contrib import admin
from django.urls import path
from . import views
from .views import tender, posts, PostListView, tenders, PostDetailView
from django.urls import include

app_name = "tenders"

urlpatterns = [
    path(' ', PostListView.as_view(), name = 'ten'),
    path('<int:tenders_id>/ ', PostDetailView.as_view(), name = 'detail'),
]


