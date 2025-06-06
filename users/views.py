from django.shortcuts import render
from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import UserSerializer

# Create your views here.

class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users can access
