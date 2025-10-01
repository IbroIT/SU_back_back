from rest_framework import serializers
from .models import (
    Hospital, HospitalDepartment, Laboratory, LaboratoryEquipment,
    AcademicBuilding, BuildingFacility, BuildingPhoto,
    Dormitory, DormitoryRoom, DormitoryFacility, DormitoryPhoto,
    ClassroomCategory, Classroom, ClassroomEquipment, ClassroomFeature,
    StartupCategory, Startup, StartupTeamMember, StartupInvestor, StartupAchievement
)


class HospitalDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalDepartment
        fields = ['id', 'name_ru', 'name_kg', 'name_en', 'description_ru', 'description_kg', 'description_en', 'order']


class HospitalSerializer(serializers.ModelSerializer):
    departments = HospitalDepartmentSerializer(many=True, read_only=True)
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Hospital
        fields = [
            'id', 'name_ru', 'name_kg', 'name_en',
            'description_ru', 'description_kg', 'description_en',
            'address_ru', 'address_kg', 'address_en',
            'practice_opportunities_ru', 'practice_opportunities_kg', 'practice_opportunities_en',
            'contact_phone', 'contact_email', 'photo_url',
            'latitude', 'longitude', 'is_active', 'order',
            'departments', 'created_at', 'updated_at'
        ]

    def get_photo_url(self, obj):
        if obj.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.photo.url)
            return obj.photo.url
        return None


class LaboratoryEquipmentSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = LaboratoryEquipment
        fields = [
            'id', 'name_ru', 'name_kg', 'name_en',
            'description_ru', 'description_kg', 'description_en',
            'photo_url', 'order'
        ]

    def get_photo_url(self, obj):
        if obj.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.photo.url)
            return obj.photo.url
        return None


class LaboratorySerializer(serializers.ModelSerializer):
    equipment = LaboratoryEquipmentSerializer(many=True, read_only=True)
    photo_url = serializers.SerializerMethodField()
    type_display = serializers.CharField(source='get_type_display', read_only=True)

    class Meta:
        model = Laboratory
        fields = [
            'id', 'name_ru', 'name_kg', 'name_en', 'type', 'type_display',
            'description_ru', 'description_kg', 'description_en',
            'schedule_ru', 'schedule_kg', 'schedule_en',
            'requirements_ru', 'requirements_kg', 'requirements_en',
            'capacity', 'photo_url', 'is_active', 'order',
            'equipment', 'created_at', 'updated_at'
        ]

    def get_photo_url(self, obj):
        if obj.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.photo.url)
            return obj.photo.url
        return None


class BuildingFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingFacility
        fields = ['id', 'name_ru', 'name_kg', 'name_en', 'count', 'capacity_ru', 'capacity_kg', 'capacity_en', 'capacity', 'order']


class BuildingPhotoSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()  # Изменено с photo_url на url для фронтенда
    photo_url = serializers.SerializerMethodField()  # Оставляем для обратной совместимости
    type_display = serializers.CharField(source='get_type_display', read_only=True)

    class Meta:
        model = BuildingPhoto
        fields = [
            'id', 'url', 'photo_url', 'type', 'type_display',
            'title_ru', 'title_kg', 'title_en', 'order'
        ]

    def get_url(self, obj):
        if obj.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.photo.url)
            return obj.photo.url
        return None

    def get_photo_url(self, obj):
        if obj.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.photo.url)
            return obj.photo.url
        return None


class AcademicBuildingSerializer(serializers.ModelSerializer):
    facilities = BuildingFacilitySerializer(many=True, read_only=True)
    photos = BuildingPhotoSerializer(many=True, read_only=True)
    photo_url = serializers.SerializerMethodField()  # Главное фото для совместимости с фронтендом
    facade_photo = serializers.SerializerMethodField()  # Фото фасада

    class Meta:
        model = AcademicBuilding
        fields = [
            'id', 'name_ru', 'name_kg', 'name_en',
            'description_ru', 'description_kg', 'description_en',
            'address_ru', 'address_kg', 'address_en',
            'floors', 'latitude', 'longitude',
            'is_active', 'order', 'facilities', 'photos',
            'photo_url', 'facade_photo',
            'created_at', 'updated_at'
        ]

    def get_photo_url(self, obj):
        # Сначала ищем фасад, потом первое доступное фото
        facade_photo = obj.photos.filter(type='facade').first()
        if facade_photo and facade_photo.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(facade_photo.photo.url)
            return facade_photo.photo.url
        
        # Если нет фасада, берем первое фото
        first_photo = obj.photos.first()
        if first_photo and first_photo.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(first_photo.photo.url)
            return first_photo.photo.url
        return None

    def get_facade_photo(self, obj):
        facade_photo = obj.photos.filter(type='facade').first()
        if facade_photo and facade_photo.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(facade_photo.photo.url)
            return facade_photo.photo.url
        return None


class DormitoryRoomSerializer(serializers.ModelSerializer):
    type_display = serializers.CharField(source='get_type_display', read_only=True)

    class Meta:
        model = DormitoryRoom
        fields = [
            'id', 'type', 'type_display',
            'name_ru', 'name_kg', 'name_en',
            'price_monthly', 'features_ru', 'features_kg', 'features_en',
            'order'
        ]


class DormitoryFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DormitoryFacility
        fields = ['id', 'name_ru', 'name_kg', 'name_en', 'order']


class DormitoryPhotoSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()  # Изменено с photo_url на url для фронтенда
    photo_url = serializers.SerializerMethodField()  # Оставляем для обратной совместимости
    type_display = serializers.CharField(source='get_type_display', read_only=True)

    class Meta:
        model = DormitoryPhoto
        fields = [
            'id', 'url', 'photo_url', 'type', 'type_display',
            'title_ru', 'title_kg', 'title_en', 'order'
        ]

    def get_url(self, obj):
        if obj.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.photo.url)
            return obj.photo.url
        return None

    def get_photo_url(self, obj):
        if obj.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.photo.url)
            return obj.photo.url
        return None


class DormitorySerializer(serializers.ModelSerializer):
    rooms = DormitoryRoomSerializer(many=True, read_only=True)
    facilities = DormitoryFacilitySerializer(many=True, read_only=True)
    photos = DormitoryPhotoSerializer(many=True, read_only=True)
    type_display = serializers.CharField(source='get_type_display', read_only=True)
    main_photo = serializers.SerializerMethodField()  # Главное фото для совместимости
    exterior_photo = serializers.SerializerMethodField()  # Фото внешнего вида

    class Meta:
        model = Dormitory
        fields = [
            'id', 'name_ru', 'name_kg', 'name_en',
            'type', 'type_display',
            'description_ru', 'description_kg', 'description_en',
            'address_ru', 'address_kg', 'address_en',
            'capacity', 'available', 'is_active', 'order',
            'rooms', 'facilities', 'photos', 'main_photo', 'exterior_photo',
            'created_at', 'updated_at'
        ]

    def get_main_photo(self, obj):
        # Сначала ищем exterior, потом первое доступное фото
        exterior_photo = obj.photos.filter(type='exterior').first()
        if exterior_photo and exterior_photo.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(exterior_photo.photo.url)
            return exterior_photo.photo.url
        
        # Если нет exterior, берем первое фото
        first_photo = obj.photos.first()
        if first_photo and first_photo.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(first_photo.photo.url)
            return first_photo.photo.url
        return None

    def get_exterior_photo(self, obj):
        exterior_photo = obj.photos.filter(type='exterior').first()
        if exterior_photo and exterior_photo.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(exterior_photo.photo.url)
            return exterior_photo.photo.url
        return None


# Simplified serializers for list views
class HospitalListSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Hospital
        fields = [
            'id', 'name_ru', 'name_kg', 'name_en',
            'description_ru', 'description_kg', 'description_en',
            'address_ru', 'address_kg', 'address_en',
            'contact_phone', 'photo_url', 'is_active'
        ]

    def get_photo_url(self, obj):
        if obj.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.photo.url)
            return obj.photo.url
        return None


class LaboratoryListSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    type_display = serializers.CharField(source='get_type_display', read_only=True)

    class Meta:
        model = Laboratory
        fields = [
            'id', 'name_ru', 'name_kg', 'name_en', 'type', 'type_display',
            'description_ru', 'description_kg', 'description_en',
            'capacity', 'photo_url', 'is_active'
        ]

    def get_photo_url(self, obj):
        if obj.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.photo.url)
            return obj.photo.url
        return None


class AcademicBuildingListSerializer(serializers.ModelSerializer):
    facade_photo = serializers.SerializerMethodField()

    class Meta:
        model = AcademicBuilding
        fields = [
            'id', 'name_ru', 'name_kg', 'name_en',
            'description_ru', 'description_kg', 'description_en',
            'address_ru', 'address_kg', 'address_en',
            'floors', 'facade_photo', 'is_active'
        ]

    def get_facade_photo(self, obj):
        facade_photo = obj.photos.filter(type='facade').first()
        if facade_photo and facade_photo.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(facade_photo.photo.url)
            return facade_photo.photo.url
        return None


class DormitoryListSerializer(serializers.ModelSerializer):
    exterior_photo = serializers.SerializerMethodField()
    type_display = serializers.CharField(source='get_type_display', read_only=True)

    class Meta:
        model = Dormitory
        fields = [
            'id', 'name_ru', 'name_kg', 'name_en',
            'type', 'type_display',
            'description_ru', 'description_kg', 'description_en',
            'address_ru', 'address_kg', 'address_en',
            'capacity', 'available', 'exterior_photo', 'is_active'
        ]

    def get_exterior_photo(self, obj):
        exterior_photo = obj.photos.filter(type='exterior').first()
        if exterior_photo and exterior_photo.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(exterior_photo.photo.url)
            return exterior_photo.photo.url
        return None
# === CLASSROOM SERIALIZERS ===

class ClassroomEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassroomEquipment
        fields = ['id', 'name_ru', 'name_kg', 'name_en', 'order']


class ClassroomFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassroomFeature
        fields = ['id', 'name_ru', 'name_kg', 'name_en', 'order']


class ClassroomCategorySerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()
    
    class Meta:
        model = ClassroomCategory
        fields = ['id', 'name_ru', 'name_kg', 'name_en', 'icon', 'count', 'order']
    
    def get_count(self, obj):
        return obj.classrooms.filter(is_active=True).count()


class ClassroomSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    equipment = ClassroomEquipmentSerializer(many=True, read_only=True)
    features = ClassroomFeatureSerializer(many=True, read_only=True)
    
    class Meta:
        model = Classroom
        fields = [
            'id', 'category_name',
            'name_ru', 'name_kg', 'name_en',
            'description_ru', 'description_kg', 'description_en',
            'capacity', 'floor', 'size', 'image',
            'equipment', 'features', 'order', 'is_active'
        ]
    
    def get_category_name(self, obj):
        return {
            'ru': obj.category.name_ru,
            'kg': obj.category.name_kg,
            'en': obj.category.name_en
        }


class ClassroomLanguageAwareSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()
    equipment = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()
    
    class Meta:
        model = Classroom
        fields = [
            'id', 'name', 'description', 'category_name',
            'capacity', 'floor', 'size', 'image', 
            'equipment', 'features', 'order'
        ]
    
    def get_language(self):
        request = self.context.get('request')
        if request:
            lang = request.GET.get('lang')
            if lang in ['ru', 'kg', 'en']:
                return lang
            accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', '')
            if 'kg' in accept_language:
                return 'kg'
            elif 'en' in accept_language:
                return 'en'
        return 'ru'
    
    def get_name(self, obj):
        lang = self.get_language()
        return getattr(obj, f'name_{lang}', obj.name_ru)
    
    def get_description(self, obj):
        lang = self.get_language()
        return getattr(obj, f'description_{lang}', obj.description_ru)
        
    def get_category_name(self, obj):
        lang = self.get_language()
        return getattr(obj.category, f'name_{lang}', obj.category.name_ru)
    
    def get_equipment(self, obj):
        lang = self.get_language()
        return [getattr(eq, f'name_{lang}', eq.name_ru) for eq in obj.equipment.all()]
    
    def get_features(self, obj):
        lang = self.get_language()
        return [getattr(feat, f'name_{lang}', feat.name_ru) for feat in obj.features.all()]


# === STARTUP SERIALIZERS ===

class StartupTeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartupTeamMember
        fields = ['id', 'name_ru', 'name_kg', 'name_en', 'order']


class StartupInvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartupInvestor
        fields = ['id', 'name_ru', 'name_kg', 'name_en', 'order']


class StartupAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartupAchievement
        fields = ['id', 'achievement_ru', 'achievement_kg', 'achievement_en', 'order']


class StartupCategorySerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()
    
    class Meta:
        model = StartupCategory
        fields = ['id', 'name_ru', 'name_kg', 'name_en', 'icon', 'count', 'order']
    
    def get_count(self, obj):
        return obj.startups.filter(is_active=True).count()


class StartupSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    team_members = StartupTeamMemberSerializer(many=True, read_only=True)
    investors = StartupInvestorSerializer(many=True, read_only=True)
    achievements = StartupAchievementSerializer(many=True, read_only=True)
    stage_display = serializers.CharField(source='get_stage_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Startup
        fields = [
            'id', 'category_name',
            'name_ru', 'name_kg', 'name_en',
            'description_ru', 'description_kg', 'description_en',
            'full_description_ru', 'full_description_kg', 'full_description_en',
            'stage', 'stage_display', 'status', 'status_display',
            'funding', 'year', 'image',
            'team_members', 'investors', 'achievements',
            'order', 'is_active'
        ]
    
    def get_category_name(self, obj):
        return {
            'ru': obj.category.name_ru,
            'kg': obj.category.name_kg,
            'en': obj.category.name_en
        }


class StartupLanguageAwareSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    full_description = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()
    investors = serializers.SerializerMethodField()
    achievements = serializers.SerializerMethodField()
    stage_display = serializers.SerializerMethodField()
    status_display = serializers.SerializerMethodField()
    
    class Meta:
        model = Startup
        fields = [
            'id', 'name', 'description', 'full_description', 'category', 'category_name',
            'stage', 'stage_display', 'status', 'status_display',
            'funding', 'year', 'image', 
            'team', 'investors', 'achievements', 'order'
        ]
    
    def get_language(self):
        request = self.context.get('request')
        if request:
            lang = request.GET.get('lang')
            if lang in ['ru', 'kg', 'en']:
                return lang
            accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', '')
            if 'kg' in accept_language:
                return 'kg'
            elif 'en' in accept_language:
                return 'en'
        return 'ru'
    
    def get_name(self, obj):
        lang = self.get_language()
        return getattr(obj, f'name_{lang}', obj.name_ru)
    
    def get_description(self, obj):
        lang = self.get_language()
        return getattr(obj, f'description_{lang}', obj.description_ru)
    
    def get_full_description(self, obj):
        lang = self.get_language()
        return getattr(obj, f'full_description_{lang}', obj.full_description_ru)
        
    def get_category_name(self, obj):
        lang = self.get_language()
        return getattr(obj.category, f'name_{lang}', obj.category.name_ru)
    
    def get_team(self, obj):
        lang = self.get_language()
        return [getattr(member, f'name_{lang}', member.name_ru) for member in obj.team_members.all()]
    
    def get_investors(self, obj):
        lang = self.get_language()
        return [getattr(inv, f'name_{lang}', inv.name_ru) for inv in obj.investors.all()]
    
    def get_achievements(self, obj):
        lang = self.get_language()
        return [getattr(ach, f'achievement_{lang}', ach.achievement_ru) for ach in obj.achievements.all()]

    def get_stage_display(self, obj):
        """Get localized stage display"""
        stage_translations = {
            'seed': {
                'ru': 'Посевная стадия',
                'kg': 'Себүү баскычы',
                'en': 'Seed Stage'
            },
            'series_a': {
                'ru': 'Серия A',
                'kg': 'A сериясы',
                'en': 'Series A'
            },
            'growth': {
                'ru': 'Рост',
                'kg': 'Өсүү',
                'en': 'Growth'
            },
            'research': {
                'ru': 'Исследования',
                'kg': 'Изилдөөлөр',
                'en': 'Research'
            },
            'prototype': {
                'ru': 'Прототип',
                'kg': 'Прототип',
                'en': 'Prototype'
            },
            'scaling': {
                'ru': 'Масштабирование',
                'kg': 'Масштабдоо',
                'en': 'Scaling'
            },
        }
        
        lang = self.get_language()
        return stage_translations.get(obj.stage, {}).get(lang, obj.get_stage_display())

    def get_status_display(self, obj):
        """Get localized status display"""
        status_translations = {
            'active': {
                'ru': 'Активный',
                'kg': 'Активдүү',
                'en': 'Active'
            },
            'development': {
                'ru': 'В разработке',
                'kg': 'Иштеп жатат',
                'en': 'In Development'
            },
            'scaling': {
                'ru': 'Масштабирование',
                'kg': 'Масштабдоо',
                'en': 'Scaling'
            },
            'research': {
                'ru': 'Исследования',
                'kg': 'Изилдөөлөр',
                'en': 'Research'
            },
            'prototype': {
                'ru': 'Прототип',
                'kg': 'Прототип',
                'en': 'Prototype'
            },
        }
        
        lang = self.get_language()
        return status_translations.get(obj.status, {}).get(lang, obj.get_status_display())

