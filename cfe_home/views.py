from django.shortcuts import render
from django.contrib.auth import get_user_model 
from django.contrib.auth.decorators import  login_required

User = get_user_model()

def home(request):
    if request.user.is_authenticated:
        print(request.user.username)
        print("User is authenticated")
    else:
        print("User is not authenticated")
    return render(request, "home.html")

def pw_protected_view(request):
    is_allowed=False
    if is_allowed:
        return render(request, "protected/view.html")
    return render(request, "protected/entry.html")


@login_required
def user_only_view(request):
    return render(request, "protected/user_only.html", {"username": request.user.username})