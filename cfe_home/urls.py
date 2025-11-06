from django.contrib import admin
from django.urls import include, path 
from auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", auth_views.login_view, name="login"),
    path("protected/", views.pw_protected_view, name="protected"),
    path("user-only/", views.user_only_view, name="user_only"),
]
