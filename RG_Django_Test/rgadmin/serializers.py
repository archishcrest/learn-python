from rest_framework import serializers
from .models import Users

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username')
