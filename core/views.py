from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from users.models import CustomUser
from .models import WasteRequest
from django.middleware.csrf import rotate_token


def login_view(request):
    messages.get_messages(request).used = True
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            rotate_token(request)  # Regenerate CSRF token after login
            messages.success(request, "Login successful!")
            return redirect_user_to_dashboard(user)
        messages.error(request, "Invalid username or password.")
        return redirect("login")
    return render(request, "login.html")

# Function to Redirect Users to Their Dashboard Based on Role (Only on Initial Login)
def redirect_user_to_dashboard(user):
    if not user.is_authenticated:
        return redirect("login")
    print(f"Redirecting user: {user.username}, Role: {user.role}")  # Debug log
    if user.role == "resident":
        return redirect("resident_dashboard")
    elif user.role == "company":
        return redirect("company_dashboard")
    elif user.role == "officer":
        return redirect("officer_dashboard")
    elif user.role == "driver":
        return redirect("driver_dashboard")
    return redirect("home")  # Fallback

# Home Page View
def home_view(request):
    return render(request, 'home.html')

# Signup View
def signup_view(request):
    messages.get_messages(request).used = True
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        phone_number = request.POST["phone_number"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        role = request.POST["role"]

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("signup")
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return redirect("signup")
        if CustomUser.objects.filter(phone_number=phone_number).exists():
            messages.error(request, "Phone number already in use.")
            return redirect("signup")
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")
        
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            phone_number=phone_number,
            password=password1,
            role=role,
        )
        messages.success(request, "Account created successfully! You can now log in.")
        return redirect("login")
    return render(request, "signup.html")

# Login View
def login_view(request):
    messages.get_messages(request).used = True
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect_user_to_dashboard(user)
        messages.error(request, "Invalid username or password.")
        return redirect("login")
    return render(request, "login.html")

# Logout View
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("login")

@login_required
def resident_dashboard(request):
    # Only redirect if user is not a resident AND this is not a POST request or refresh
    if request.user.role != "resident" and request.method == "GET":
        messages.error(request, "Only residents can access this dashboard.")
        return redirect_user_to_dashboard(request.user)
    if request.method == "POST":
        try:
            waste_request = WasteRequest(
                resident=request.user,
                request_type=request.POST.get("request_type"),
                location=request.POST.get("location"),
                image=request.FILES.get("image"),
                status="pending"
            )
            waste_request.save()
            messages.success(request, "Request submitted successfully!")
        except Exception as e:
            messages.error(request, f"Error submitting request: {str(e)}")
        return redirect("resident_dashboard")
    return render(request, "resident_dashboard.html")

@login_required
def company_dashboard(request):
    messages.get_messages(request).used = True
    if request.user.role != "company" and request.method == "GET":
        messages.error(request, "Only company users can access this dashboard.")
        return redirect_user_to_dashboard(request.user)
    collection_requests = WasteRequest.objects.filter(request_type="collection").order_by('-timestamp')
    illegal_dumping_reports = WasteRequest.objects.filter(request_type="illegal_dumping").order_by('-timestamp')
    available_drivers = CustomUser.objects.filter(role="driver")
    if request.method == "POST":
        request_id = request.POST.get("request_id")
        driver_id = request.POST.get("driver_id")
        action = request.POST.get("action")
        if request_id:
            try:
                waste_request = WasteRequest.objects.get(id=request_id)
                if action == "assign" and driver_id:
                    if waste_request.status in ["pending", "rejected"]:
                        driver = CustomUser.objects.get(id=driver_id)
                        waste_request.assigned_driver = driver
                        waste_request.status = "assigned"
                        waste_request.assigned_by = request.user
                        waste_request.rejected_by = None
                        waste_request.save()
                        messages.success(request, "Task assigned successfully!")
                    else:
                        messages.error(request, "Task is already assigned to a driver.")
                elif action == "mark_completed":
                    waste_request.status = "completed"
                    waste_request.save()
                    messages.success(request, "Task marked as completed!")
                elif action == "remove_task":
                    if waste_request.status == "completed":
                        waste_request.delete()
                        messages.success(request, "Task removed successfully!")
                    else:
                        messages.error(request, "Only completed tasks can be removed.")
            except Exception as e:
                messages.error(request, f"Error processing action: {str(e)}")
        return redirect("company_dashboard")
    return render(request, 'company_dashboard.html', {
        'collection_requests': collection_requests,
        'illegal_dumping_reports': illegal_dumping_reports,
        'available_drivers': available_drivers
    })

@login_required
def officer_dashboard(request):
    messages.get_messages(request).used = True
    if request.user.role != "officer" and request.method == "GET":
        messages.error(request, "Only officers can access this dashboard.")
        return redirect_user_to_dashboard(request.user)
    illegal_dumping_reports = WasteRequest.objects.filter(request_type="illegal_dumping").order_by('-timestamp')
    if request.method == "POST":
        report_id = request.POST.get("report_id")
        action = request.POST.get("action")
        if report_id and action == "delete_report":
            try:
                report = WasteRequest.objects.get(id=report_id)
                report.delete()
                messages.success(request, "Illegal dumping report deleted successfully!")
            except Exception as e:
                messages.error(request, f"Error deleting report: {str(e)}")
        return redirect("officer_dashboard")
    return render(request, 'officer_dashboard.html', {
        'illegal_dumping_reports': illegal_dumping_reports
    })

@login_required
def driver_dashboard(request):
    messages.get_messages(request).used = True
    if request.user.role != "driver" and request.method == "GET":
        messages.error(request, "Only drivers can access this dashboard.")
        return redirect_user_to_dashboard(request.user)
    assigned_tasks = WasteRequest.objects.filter(assigned_driver=request.user).order_by('-timestamp')
    if request.method == "POST":
        task_id = request.POST.get("task_id")
        action = request.POST.get("action")
        if task_id:
            try:
                task = WasteRequest.objects.get(id=task_id)
                if action == "accept":
                    task.status = "accepted"
                    task.save()
                    messages.success(request, "Task accepted successfully!")
                elif action == "reject":
                    task.status = "rejected"
                    task.rejected_by = request.user
                    task.assigned_driver = None
                    task.save()
                    messages.success(request, "Task rejected. It can now be reassigned.")
                elif action == "complete":
                    task.status = "completed"
                    task.save()
                    messages.success(request, "Task marked as completed!")
                elif action == "remove_task":
                    if task.status == "rejected":
                        task.delete()
                        messages.success(request, "Rejected task removed successfully!")
                    else:
                        messages.error(request, "Only rejected tasks can be removed.")
            except Exception as e:
                messages.error(request, f"Error processing task: {str(e)}")
        return redirect("driver_dashboard")
    return render(request, 'driver_dashboard.html', {
        'assigned_tasks': assigned_tasks
    })