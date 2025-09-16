from rest_framework import serializers
from .models import PartnerOrganization, StudentAppeal


class PartnerOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerOrganization
        fields = [
            'id', 'name_ru', 'name_kg', 'name_en',
            'description_ru', 'description_kg', 'description_en',
            'type', 'location', 'contact_person', 'phone', 'email', 
            'website', 'is_active'
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
