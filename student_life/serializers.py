from rest_framework import serializers
from .models import (
    PartnerOrganization, StudentAppeal, OrganizationSpecialization,
    PhotoAlbum, Photo, VideoContent, StudentLifeStatistic
)


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


# =============================================================================
# SERIALIZERS ДЛЯ ФОТОГАЛЕРЕИ И ВИДЕО
# =============================================================================

class PhotoSerializer(serializers.ModelSerializer):
    """Сериализатор для фотографий"""
    tags = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
    album_id = serializers.ReadOnlyField(source='album.id')
    
    class Meta:
        model = Photo
        fields = [
            'id', 'album_id', 'title_ru', 'title_kg', 'title_en', 'title',
            'description_ru', 'description_kg', 'description_en',
            'image', 'url', 'tags_ru', 'tags_kg', 'tags_en', 'tags',
            'photographer', 'order', 'uploaded_at'
        ]
    
    def get_title(self, obj):
        """Возвращает название на текущем языке"""
        request = self.context.get('request')
        if request:
            lang = request.GET.get('lang', 'ru')
            return getattr(obj, f'title_{lang}', obj.title_ru)
        return obj.title_ru
    
    def get_url(self, obj):
        """Возвращает полный URL изображения"""
        # Приоритет: url поле, затем image поле
        if obj.url:
            return obj.url
        elif obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None
    
    def get_tags(self, obj):
        """Возвращает теги в виде списка для текущего языка"""
        request = self.context.get('request')
        if request:
            lang = request.GET.get('lang', 'ru')
            tags_field = getattr(obj, f'tags_{lang}', obj.tags_ru)
        else:
            tags_field = obj.tags_ru
        
        if tags_field:
            return [tag.strip() for tag in tags_field.split(',') if tag.strip()]
        return []


class PhotoAlbumSerializer(serializers.ModelSerializer):
    """Сериализатор для фотоальбомов"""
    photos = PhotoSerializer(many=True, read_only=True)
    photo_count = serializers.ReadOnlyField()
    tags = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    cover = serializers.SerializerMethodField()
    
    class Meta:
        model = PhotoAlbum
        fields = [
            'id', 'title_ru', 'title_kg', 'title_en', 'title',
            'description_ru', 'description_kg', 'description_en',
            'cover_image', 'cover', 'tags_ru', 'tags_kg', 'tags_en', 'tags',
            'event_date', 'photo_count', 'photos', 'order', 'created_at'
        ]
    
    def get_title(self, obj):
        """Возвращает название на текущем языке"""
        request = self.context.get('request')
        if request:
            lang = request.GET.get('lang', 'ru')
            return getattr(obj, f'title_{lang}', obj.title_ru)
        return obj.title_ru
    
    def get_cover(self, obj):
        """Возвращает полный URL обложки"""
        request = self.context.get('request')
        if obj.cover_image and request:
            return request.build_absolute_uri(obj.cover_image.url)
        return obj.cover_image.url if obj.cover_image else None
    
    def get_tags(self, obj):
        """Возвращает теги в виде списка для текущего языка"""
        request = self.context.get('request')
        if request:
            lang = request.GET.get('lang', 'ru')
            tags_field = getattr(obj, f'tags_{lang}', obj.tags_ru)
        else:
            tags_field = obj.tags_ru
        
        if tags_field:
            return [tag.strip() for tag in tags_field.split(',') if tag.strip()]
        return []


class VideoContentSerializer(serializers.ModelSerializer):
    """Сериализатор для видеоконтента"""
    tags = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    thumbnail_url = serializers.SerializerMethodField()
    video_source = serializers.SerializerMethodField()
    
    class Meta:
        model = VideoContent
        fields = [
            'id', 'title_ru', 'title_kg', 'title_en', 'title',
            'description_ru', 'description_kg', 'description_en',
            'video_file', 'video_url', 'video_source', 'thumbnail', 'thumbnail_url',
            'tags_ru', 'tags_kg', 'tags_en', 'tags',
            'type', 'duration', 'event_date', 'views_count',
            'is_featured', 'order', 'created_at'
        ]
    
    def get_title(self, obj):
        """Возвращает название на текущем языке"""
        request = self.context.get('request')
        if request:
            lang = request.GET.get('lang', 'ru')
            return getattr(obj, f'title_{lang}', obj.title_ru)
        return obj.title_ru
    
    def get_thumbnail_url(self, obj):
        """Возвращает полный URL превью"""
        # Приоритет: thumbnail_url поле, затем thumbnail файл
        if obj.thumbnail_url:
            return obj.thumbnail_url
        elif obj.thumbnail:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.thumbnail.url)
            return obj.thumbnail.url
        return None
        return obj.thumbnail.url if obj.thumbnail else None
    
    def get_video_source(self, obj):
        """Возвращает источник видео"""
        request = self.context.get('request')
        if obj.video_file and request:
            return request.build_absolute_uri(obj.video_file.url)
        return obj.video_url
    
    def get_tags(self, obj):
        """Возвращает теги в виде списка для текущего языка"""
        request = self.context.get('request')
        if request:
            lang = request.GET.get('lang', 'ru')
            tags_field = getattr(obj, f'tags_{lang}', obj.tags_ru)
        else:
            tags_field = obj.tags_ru
        
        if tags_field:
            return [tag.strip() for tag in tags_field.split(',') if tag.strip()]
        return []


class StudentLifeStatisticSerializer(serializers.ModelSerializer):
    """Сериализатор для статистики студенческой жизни"""
    label = serializers.SerializerMethodField()
    
    class Meta:
        model = StudentLifeStatistic
        fields = [
            'id', 'label_ru', 'label_kg', 'label_en', 'label',
            'description_ru', 'description_kg', 'description_en',
            'value', 'type', 'icon', 'order', 'last_updated'
        ]
    
    def get_label(self, obj):
        """Возвращает название на текущем языке"""
        request = self.context.get('request')
        if request:
            lang = request.GET.get('lang', 'ru')
            return getattr(obj, f'label_{lang}', obj.label_ru)
        return obj.label_ru


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
