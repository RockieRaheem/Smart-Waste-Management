from django.shortcuts import render
from rest_framework import generics, permissions
from .models import CollectionRoute
from .serializers import CollectionRouteSerializer

# Create your views here.
class CollectionRouteListCreateView(generics.ListCreateAPIView):
    queryset = CollectionRoute.objects.all()
    serializer_class = CollectionRouteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only allow waste management companies to see their own routes
        if self.request.user.role == 'company':
            return CollectionRoute.objects.filter(company=self.request.user)
        return CollectionRoute.objects.none()

class CollectionRouteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CollectionRoute.objects.all()
    serializer_class = CollectionRouteSerializer
    permission_classes = [permissions.IsAuthenticated]
