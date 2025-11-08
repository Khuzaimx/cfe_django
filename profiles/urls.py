
from django.urls import include, path
from .import views
urlpatterns = [
    path("<str:username>/", views.profile_view, name="profile"),
]
