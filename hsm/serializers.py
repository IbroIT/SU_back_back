from rest_framework import serializers
from .models import HSMInfo, Program, Faculty, Accreditation, LearningGoal


class HSMInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HSMInfo
        fields = '__all__'


class ProgramSerializer(serializers.ModelSerializer):
    program_type_display = serializers.CharField(source='get_program_type_display', read_only=True)
    study_form_display = serializers.CharField(source='get_study_form_display', read_only=True)
    
    class Meta:
        model = Program
        fields = '__all__'


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


class LearningGoalSerializer(serializers.ModelSerializer):
    programs = ProgramSerializer(many=True, read_only=True)
    
    class Meta:
        model = LearningGoal
        fields = '__all__'


class ProgramListSerializer(serializers.ModelSerializer):
    """Краткая информация о программе для списков"""
    program_type_display = serializers.CharField(source='get_program_type_display', read_only=True)
    study_form_display = serializers.CharField(source='get_study_form_display', read_only=True)
    
    class Meta:
        model = Program
        fields = ['id', 'name', 'name_kg', 'name_en', 'program_type', 'program_type_display', 
                 'study_form', 'study_form_display', 'duration_years', 'is_active']


class FacultyListSerializer(serializers.ModelSerializer):
    """Краткая информация о преподавателе для списков"""
    position_display = serializers.CharField(source='get_position_display', read_only=True)
    academic_degree_display = serializers.CharField(source='get_academic_degree_display', read_only=True)
    full_name = serializers.CharField(read_only=True)
    
    class Meta:
        model = Faculty
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'first_name_kg', 
                 'last_name_kg', 'middle_name_kg', 'first_name_en', 'last_name_en', 
                 'middle_name_en', 'full_name', 'position', 'position_display', 
                 'academic_degree', 'academic_degree_display', 'photo', 'email', 
                 'phone', 'office', 'is_active']
