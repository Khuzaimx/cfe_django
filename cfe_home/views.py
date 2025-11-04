from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()

def home(request):
    if request.user.is_authenticated:
        print(request.user.username)
        print("User is authenticated")
    else:
        print("User is not authenticated")
    return render(request, "home.html")
