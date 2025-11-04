from django.contrib import admin
from django.urls import include, path 
from auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", auth_views.login_view, name="login"),
]
