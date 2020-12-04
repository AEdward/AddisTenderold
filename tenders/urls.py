from django.contrib import admin
from django.urls import path
from . import views
from .views import (PostListView,PostDetailView
,PostCreateView,PostUpdateView,
PostDeleteView,UserPostListView,SearchPostListView,CategoryView)
from django.urls import include

app_name = "tenders"

urlpatterns = [   
    path('',  PostListView.as_view(), name = 'index'),
    path('user/<str:username>',  UserPostListView.as_view(), name = 'user-posts'),
    path('<int:pk>', PostDetailView.as_view(), name = 'detail'),
    path('addnew', PostCreateView.as_view(), name ='addnew'),
    path('<int:pk>/update', PostUpdateView.as_view(), name ='update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name ='delete'),
    path('result', SearchPostListView.as_view(), name ='search'),
    path('<str:cats>', CategoryView, name='category'),
#path('thome', CatView.as_view, name ='thome'),
]