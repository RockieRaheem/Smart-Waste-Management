from rest_framework import serializers
from .models import GarbageRequest, IllegalDumpingReport

class GarbageRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = GarbageRequest
        fields = '__all__'

class IllegalDumpingReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = IllegalDumpingReport
        fields = '__all__'

