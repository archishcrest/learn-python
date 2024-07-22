from rest_framework import serializers

class TextSerializer(serializers.ModelSerializer):
    
    # Make title and slug required fields
    prompt = serializers.CharField(required=True)

    def validate(self, data):
        # Additional validation can be added here if needed
        return data