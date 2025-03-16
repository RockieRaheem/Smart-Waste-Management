"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from .views import home_view, login_view, dashboard_view
from .views import signup_view, login_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('api/', include('users.urls')),
    path('api/', include('waste.urls')),
    path('api/', include('tracking.urls')),
    path('api/', include('routes.urls')),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('resident/', resident_dashboard, name='resident_dashboard'),
    path('company/', company_dashboard, name='company_dashboard'),
    path('officer/', officer_dashboard, name='officer_dashboard'),
    path('driver/', driver_dashboard, name='driver_dashboard'),
]





