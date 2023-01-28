from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    
    path('post/', views.PostCreateView.as_view(), name="post"),
    path('postdone/', views.PostdoneView.as_view(), name="postdone"),
    path('post-list/', views.PostListView.as_view(), name="post-list"),
    path('post-detail/<int:pk>/', views.PostDetailView.as_view(), name="post-detail"),

    
]