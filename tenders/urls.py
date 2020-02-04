from django.contrib import admin
from django.urls import path
from . import views
from .views import (PostListView,PostDetailView,index, 
SearchPostListView,PostCreateView,PostUpdateView,
PostDeleteView,UserPostListView,CategoryPostListView)
from django.urls import include

app_name = "tenders"

urlpatterns = [   
    path('',  PostListView.as_view(), name = 'index'),
    path('category/<str:pk>',  CategoryPostListView.as_view(), name = 'category'),
    path('user/<str:username> ',  UserPostListView.as_view(), name = 'user-posts'),
    #path('<int:pk>',detail, name = 'detail'),
    path('<int:pk>', PostDetailView.as_view(), name = 'detail'),
    path('addnew', PostCreateView.as_view(), name ='addnew'),
    path('<int:pk>/update', PostUpdateView.as_view(), name ='update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name ='delete'),
    path('result', SearchPostListView.as_view(), name ='search'),
]


