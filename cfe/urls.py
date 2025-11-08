

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("cfe_home.urls")),
    path("", include("auth.urls")),
    path('accounts/', include('allauth.urls')),
    path("", include("profiles.urls")),
]
