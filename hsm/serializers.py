from rest_framework import serializers
from .models import Faculty, Accreditation


class FacultySerializer(serializers.ModelSerializer):
    position_display = serializers.CharField(source='get_position_display', read_only=True)
    academic_degree_display = serializers.CharField(source='get_academic_degree_display', read_only=True)
    full_name = serializers.CharField(read_only=True)
    
    class Meta:
        model = Faculty
        fields = '__all__'


class AccreditationSerializer(serializers.ModelSerializer):
    accreditation_type_display = serializers.CharField(source='get_accreditation_type_display', read_only=True)
    is_valid = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Accreditation
        fields = '__all__'
