from rest_framework import generics
from .models import GarbageRequest, IllegalDumpingReport
from .serializers import GarbageRequestSerializer, IllegalDumpingReportSerializer

class GarbageRequestListCreateView(generics.ListCreateAPIView):
    queryset = GarbageRequest.objects.all()
    serializer_class = GarbageRequestSerializer

class IllegalDumpingReportListCreateView(generics.ListCreateAPIView):
    queryset = IllegalDumpingReport.objects.all()
    serializer_class = IllegalDumpingReportSerializer
