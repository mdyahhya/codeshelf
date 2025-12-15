from rest_framework import serializers
from .models import Language

class LanguageSerializer(serializers.ModelSerializer):
    # This converts Language model to JSON and back
    
    class Meta:
        model = Language
        fields = '__all__'  # Include all fields from the model
        read_only_fields = ['date_added', 'last_updated']  # These are auto-generated
