"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include
from .views import home_view, login_view, signup_view, logout_view
from .views import resident_dashboard, company_dashboard, officer_dashboard, driver_dashboard
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('api/', include('users.urls')),
    path('api/', include('waste.urls')),
    path('api/', include('tracking.urls')),
    path('api/', include('routes.urls')),
    path('resident/', resident_dashboard, name='resident_dashboard'),
    path('company/', company_dashboard, name='company_dashboard'),
    path('officer/', officer_dashboard, name='officer_dashboard'),
    path('driver/', driver_dashboard, name='driver_dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)