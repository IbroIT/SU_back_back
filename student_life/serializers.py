from rest_framework import serializers
from .models import PartnerOrganization, StudentAppeal, OrganizationSpecialization


class OrganizationSpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationSpecialization
        fields = ['id', 'name_ru', 'name_kg', 'name_en']


class PartnerOrganizationSerializer(serializers.ModelSerializer):
    specializations = OrganizationSpecializationSerializer(many=True, read_only=True)
    
    class Meta:
        model = PartnerOrganization
        fields = [
            'id', 'name_ru', 'name_kg', 'name_en',
            'description_ru', 'description_kg', 'description_en',
            'type', 'location', 'contact_person', 'phone', 'email', 
            'website', 'is_active', 'specializations'
        ]


class StudentAppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAppeal
        fields = [
            'id', 'full_name', 'email', 'phone', 'student_id',
            'category', 'subject', 'message', 'attachment',
            'status', 'response', 'created_at', 'updated_at', 'processed_by'
        ]
        read_only_fields = ['status', 'response', 'processed_by', 'created_at', 'updated_at']
