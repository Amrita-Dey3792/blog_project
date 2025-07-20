from django.urls import path
from .views import *

urlpatterns = [
    # path('', home, name="home"),
    path('', HomeView.as_view(), name="home"),
    
    # path('create-post/', create_post, name="create_post"),
    path('create-post/', CreatePostView.as_view(), name="create_post"),

    path('posts/<int:pk>/details', post_detail, name="post_detail"),
    
    path('posts/<int:pk>/update', update_post, name="update_post"),

    # path('posts/<int:pk>/delete/', delete_post, name="delete_post"),
    path('posts/<int:pk>/delete/', DeletePostView.as_view(), name="delete_post"),
]
