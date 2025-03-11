from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import CustomUser  # Import the user model
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login

def home_view(request):
    return render(request, 'home.html')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html', {'user': request.user})


def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        role = request.POST["role"]

        if password1 != password2:
            return render(request, "signup.html", {"error": "Passwords do not match"})

        user = CustomUser.objects.create(
            username=username,
            email=email,
            password=make_password(password1),  # Hash password
            role=role,
        )
        login(request, user)  # Log in user after signup
        return redirect("dashboard")  # Redirect to dashboard

    return render(request, "signup.html")
