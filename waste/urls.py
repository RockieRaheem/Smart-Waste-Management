from django.urls import path
from .views import GarbageRequestListCreateView, IllegalDumpingReportListCreateView

urlpatterns = [
    path('garbage-requests/', GarbageRequestListCreateView.as_view(), name='garbage-request-list-create'),
    path('illegal-dumping-reports/', IllegalDumpingReportListCreateView.as_view(), name='illegal-dumping-report-list-create'),
]
