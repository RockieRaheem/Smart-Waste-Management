from django.urls import path
from .views import GarbageTruckListView

urlpatterns = [
    path('garbage-trucks/', GarbageTruckListView.as_view(), name='garbage-truck-list'),
]
