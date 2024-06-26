from rest_framework import serializers
from .models import ProfileCategory

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileCategory
        fields = ('id')