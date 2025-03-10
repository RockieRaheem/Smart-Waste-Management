from rest_framework import generics,permissions
from .models import GarbageRequest, IllegalDumpingReport
from .serializers import GarbageRequestSerializer, IllegalDumpingReportSerializer

class GarbageRequestListCreateView(generics.ListCreateAPIView):
    queryset = GarbageRequest.objects.all()
    serializer_class = GarbageRequestSerializer
    permission_classes = [permissions.IsAuthenticated]  # Protect this endpoint


class IllegalDumpingReportListCreateView(generics.ListCreateAPIView):
    queryset = IllegalDumpingReport.objects.all()
    serializer_class = IllegalDumpingReportSerializer
    permission_classes = [permissions.IsAuthenticated]  # Protect this endpoint



   