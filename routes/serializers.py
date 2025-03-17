from rest_framework import serializers
from .models import CollectionRoute

class CollectionRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionRoute
        fields = '__all__'
