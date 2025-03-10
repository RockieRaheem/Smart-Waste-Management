from rest_framework import generics
from .models import GarbageTruck
from .serializers import GarbageTruckSerializer

class GarbageTruckListView(generics.ListAPIView):
    queryset = GarbageTruck.objects.all()
    serializer_class = GarbageTruckSerializer
