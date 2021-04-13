from django.urls import path
from .views import PostListAPIView, PostDetailAPIView, PostInfoAPIView, \
        PostInfoCreateAPIView

urlpatterns = [
    path('', PostListAPIView.as_view(), name='blog-list'),
    path('info/<slug:slug>', PostInfoAPIView.as_view(), name='blog-post-info'),
    path('create/', PostInfoCreateAPIView.as_view(), name='blog-post-create'),
    path('details/<slug:slug>', PostDetailAPIView.as_view(), name='blog-post-detail')
]