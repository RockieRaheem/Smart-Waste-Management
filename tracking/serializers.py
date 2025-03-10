from rest_framework import serializers
from .models import GarbageTruck

class GarbageTruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = GarbageTruck
        fields = '__all__'
