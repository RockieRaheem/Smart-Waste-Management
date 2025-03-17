from django.shortcuts import render
from rest_framework import generics, permissions
from .models import GarbageRequest, IllegalDumpingReport
from .serializers import GarbageRequestSerializer, IllegalDumpingReportSerializer

# Create your views here.

class GarbageRequestListCreateView(generics.ListCreateAPIView):
    queryset = GarbageRequest.objects.all()
    serializer_class = GarbageRequestSerializer
    permission_classes = [permissions.IsAuthenticated]  # Protect this endpoint

class IllegalDumpingReportListCreateView(generics.ListCreateAPIView):
    queryset = IllegalDumpingReport.objects.all()
    serializer_class = IllegalDumpingReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == 'officer':  # Only municipal officers can see reports
            return IllegalDumpingReport.objects.all()
        return IllegalDumpingReport.objects.filter(user=self.request.user)
