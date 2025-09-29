from rest_framework import serializers
from .models import Faculty, Accreditation, Leadership


class LeadershipSerializer(serializers.ModelSerializer):
    """Сериализатор для руководства ВШМ"""
    leadership_type_display = serializers.CharField(source='get_leadership_type_display', read_only=True)
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Leadership
        fields = [
            'id', 'name', 'name_kg', 'name_en',
            'position', 'position_kg', 'position_en',
            'degree', 'degree_kg', 'degree_en',
            'experience', 'experience_kg', 'experience_en',
            'bio', 'bio_kg', 'bio_en',
            'achievements', 'achievements_kg', 'achievements_en',
            'department', 'department_kg', 'department_en',
            'specialization', 'specialization_kg', 'specialization_en',
            'staff_count', 'staff_count_kg', 'staff_count_en',
            'email', 'phone', 'image', 'image_url',
            'leadership_type', 'leadership_type_display',
            'is_director', 'order'
        ]
    
    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


class FacultyListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка преподавателей (краткая информация)"""
    position_display = serializers.CharField(source='get_position_display', read_only=True)
    academic_degree_display = serializers.CharField(source='get_academic_degree_display', read_only=True)
    full_name = serializers.CharField(read_only=True)
    photo_url = serializers.SerializerMethodField()
    
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
            'photo', 'photo_url', 'full_name', 'order'
        ]

    def get_photo_url(self, obj):
        if obj.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.photo.url)
            return obj.photo.url
        return None


class FacultySerializer(serializers.ModelSerializer):
    """Полный сериализатор для преподавателей"""
    position_display = serializers.CharField(source='get_position_display', read_only=True)
    academic_degree_display = serializers.CharField(source='get_academic_degree_display', read_only=True)
    full_name = serializers.CharField(read_only=True)
    photo_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Faculty
        fields = '__all__'

    def get_photo_url(self, obj):
        if obj.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.photo.url)
            return obj.photo.url
        return None


class AccreditationSerializer(serializers.ModelSerializer):
    accreditation_type_display = serializers.CharField(source='get_accreditation_type_display', read_only=True)
    is_valid = serializers.BooleanField(read_only=True)
    certificate_image_url = serializers.SerializerMethodField()
    organization_logo_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Accreditation
        fields = '__all__'

    def get_certificate_image_url(self, obj):
        if obj.certificate_image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.certificate_image.url)
            return obj.certificate_image.url
        return None

    def get_organization_logo_url(self, obj):
        if obj.organization_logo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.organization_logo.url)
            return obj.organization_logo.url
        return None
