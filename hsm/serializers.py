from rest_framework import serializers
from .models import Faculty, Accreditation


class FacultyListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка преподавателей (краткая информация)"""
    position_display = serializers.CharField(source='get_position_display', read_only=True)
    academic_degree_display = serializers.CharField(source='get_academic_degree_display', read_only=True)
    full_name = serializers.CharField(read_only=True)
    
    class Meta:
        model = Faculty
        fields = [
            'id', 'first_name', 'last_name', 'middle_name',
            'first_name_kg', 'last_name_kg', 'middle_name_kg',
            'first_name_en', 'last_name_en', 'middle_name_en',
            'position', 'position_display', 'position_custom',
            'position_kg', 'position_en',
            'academic_degree', 'academic_degree_display', 
            'academic_degree_kg', 'academic_degree_en',
            'academic_title', 'academic_title_kg', 'academic_title_en',
            'photo', 'full_name', 'order'
        ]


class FacultySerializer(serializers.ModelSerializer):
    """Полный сериализатор для преподавателей"""
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
