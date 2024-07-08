from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
    
    # Make title and slug required fields
    title = serializers.CharField(required=True)
    slug = serializers.CharField(required=True)

    def validate(self, data):
        # Additional validation can be added here if needed
        return data