from rest_framework import generics, permissions
from .models import GarbageTruck
from .serializers import GarbageTruckSerializer

class GarbageTruckListView(generics.ListAPIView):
    queryset = GarbageTruck.objects.all()
    serializer_class = GarbageTruckSerializer
    permission_classes = [permissions.IsAuthenticated]  # Protect this endpoint
