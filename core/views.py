from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.middleware.csrf import rotate_token
from django.views.decorators.csrf import ensure_csrf_cookie
from users.models import CustomUser
from .models import WasteRequest

def redirect_user_to_dashboard(user):
    """Redirects authenticated users to their respective dashboards based on role."""
    if not user.is_authenticated:
        return redirect("login")
    if user.role == "resident":
        return redirect("resident_dashboard")
    elif user.role == "company":
        return redirect("company_dashboard")
    elif user.role == "officer":
        return redirect("officer_dashboard")
    elif user.role == "driver":
        return redirect("driver_dashboard")
    return redirect("home")

@ensure_csrf_cookie
def home_view(request):
    """Renders the home page."""
    return render(request, 'home.html', {'request': request})

@ensure_csrf_cookie
def signup_view(request):
    """Handles user signup with form validation."""
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
    return render(request, "signup.html", {'request': request})

@ensure_csrf_cookie
def login_view(request):
    """Handles user login with CSRF token rotation and session persistence."""
    messages.get_messages(request).used = True
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            rotate_token(request)  # Rotate CSRF token after login
            request.session.save()  # Ensure session is saved
            messages.success(request, "Login successful!")
            return redirect_user_to_dashboard(user)
        messages.error(request, "Invalid username or password.")
        return redirect("login")
    return render(request, "login.html", {'request': request})

def logout_view(request):
    """Handles user logout."""
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("login")

@login_required
@ensure_csrf_cookie
def resident_dashboard(request):
    """Resident dashboard for submitting waste requests."""
    if request.user.role != "resident":
        messages.error(request, "Only residents can access this dashboard.")
        return redirect("login")
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
    return render(request, "resident_dashboard.html", {'request': request})

@login_required
@ensure_csrf_cookie
def company_dashboard(request):
    """Company dashboard for managing waste requests and assigning drivers."""
    if request.user.role != "company":
        messages.error(request, "Only company users can access this dashboard.")
        return redirect("login")
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
                        messages.error(request, "Task is already assigned.")
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
        'request': request,
        'collection_requests': collection_requests,
        'illegal_dumping_reports': illegal_dumping_reports,
        'available_drivers': available_drivers
    })

@login_required
@ensure_csrf_cookie
def officer_dashboard(request):
    """Officer dashboard for managing illegal dumping reports."""
    if request.user.role != "officer":
        messages.error(request, "Only officers can access this dashboard.")
        return redirect("login")
    illegal_dumping_reports = WasteRequest.objects.filter(request_type="illegal_dumping").order_by('-timestamp')
    if request.method == "POST":
        report_id = request.POST.get("report_id")
        action = request.POST.get("action")
        if report_id and action == "delete_report":
            try:
                report = WasteRequest.objects.get(id=report_id)
                report.delete()
                messages.success(request, "Report deleted successfully!")
            except Exception as e:
                messages.error(request, f"Error deleting report: {str(e)}")
        return redirect("officer_dashboard")
    return render(request, 'officer_dashboard.html', {
        'request': request,
        'illegal_dumping_reports': illegal_dumping_reports
    })

@login_required
@ensure_csrf_cookie
def driver_dashboard(request):
    """Driver dashboard for managing assigned tasks."""
    if request.user.role != "driver":
        messages.error(request, "Only drivers can access this dashboard.")
        return redirect("login")
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
                    messages.success(request, "Task rejected successfully!")
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
        'request': request,
        'assigned_tasks': assigned_tasks
    })