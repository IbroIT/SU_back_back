from rest_framework import serializers
from .models import (
    Hospital, HospitalDepartment, Laboratory, LaboratoryEquipment,
    AcademicBuilding, BuildingFacility, BuildingPhoto,
    Dormitory, DormitoryRoom, DormitoryFacility, DormitoryPhoto
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