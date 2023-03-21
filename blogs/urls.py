from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    PostSearchView,
)
from django.urls import path

urlpatterns = [
    path('',  PostListView.as_view()  ,name='blog-home'),
    path('search',PostSearchView,name='blog-search'),
    path('user/<str:username>',  UserPostListView.as_view()  ,name='blog-user-posts'),
    path('post/<int:pk>/',  PostDetailView ,name='blog-post-detail'),
    path('post/new/',  PostCreateView.as_view() ,name='blog-post-create'),
    path('post/<int:pk>/update',  PostUpdateView.as_view()  ,name='blog-post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='blog-post-delete'),
    path('about/', views.about,name='blog-about'),
    path('home/',PostListView.as_view() ,name='blog-home_2'),
]
