from django.urls import path
from .views import PostListView, PostDetailedView, PostCreateView


urlpatterns = [
    path('', PostListView.as_view(), name="post_list"),
    path('post/<int:pk>/', PostDetailedView.as_view(), name="post_detail"),
    path('post/new/', PostCreateView.as_view(), name="post_new"),
]