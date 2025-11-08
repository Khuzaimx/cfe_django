from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import views
from django.http import HttpResponse
# Create your views here.

@login_required
def profile_view(request, username):
    return HttpResponse(f"This is the profile page for {username}")