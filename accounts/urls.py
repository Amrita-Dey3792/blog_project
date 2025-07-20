from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # path("login/", login_view, name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', profile_view, name='profile'),
]
