from django.contrib import admin
from .models import (
    Hospital, HospitalDepartment, Laboratory, LaboratoryEquipment,
    AcademicBuilding, BuildingFacility, BuildingPhoto,
    Dormitory, DormitoryRoom, DormitoryFacility, DormitoryPhoto,
    ClassroomCategory, Classroom, ClassroomEquipment, ClassroomFeature,
    StartupCategory, Startup, StartupTeamMember, StartupInvestor, StartupAchievement
)


class HospitalDepartmentInline(admin.TabularInline):
    model = HospitalDepartment
    extra = 0
    fields = ['name_ru', 'name_kg', 'name_en', 'description_ru', 'description_kg', 'description_en', 'order']


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'contact_phone', 'is_active', 'order', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name_ru', 'name_kg', 'name_en', 'address_ru', 'address_kg', 'address_en']
    ordering = ['order', 'name_ru']
    inlines = [HospitalDepartmentInline]
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name_ru', 'name_kg', 'name_en', 'photo', 'is_active', 'order')
        }),
        ('Описание', {
            'fields': ('description_ru', 'description_kg', 'description_en')
        }),
        ('Адрес и контакты', {
            'fields': ('address_ru', 'address_kg', 'address_en', 'contact_phone', 'contact_email')
        }),
        ('Практика', {
            'fields': ('practice_opportunities_ru', 'practice_opportunities_kg', 'practice_opportunities_en')
        }),
        ('Координаты', {
            'fields': ('latitude', 'longitude'),
            'classes': ('collapse',)
        }),
    )


class LaboratoryEquipmentInline(admin.TabularInline):
    model = LaboratoryEquipment
    extra = 0
    fields = ['name_ru', 'name_kg', 'name_en', 'description_ru', 'description_kg', 'description_en', 'photo', 'order']


@admin.register(Laboratory)
class LaboratoryAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'type', 'capacity', 'is_active', 'order', 'created_at']
    list_filter = ['type', 'is_active', 'created_at']
    search_fields = ['name_ru', 'name_kg', 'name_en']
    ordering = ['order', 'name_ru']
    inlines = [LaboratoryEquipmentInline]
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name_ru', 'name_kg', 'name_en', 'type', 'photo', 'capacity', 'is_active', 'order')
        }),
        ('Описание', {
            'fields': ('description_ru', 'description_kg', 'description_en')
        }),
        ('График и требования', {
            'fields': ('schedule_ru', 'schedule_kg', 'schedule_en', 'requirements_ru', 'requirements_kg', 'requirements_en')
        }),
    )


class BuildingFacilityInline(admin.TabularInline):
    model = BuildingFacility
    extra = 0
    fields = ['name_ru', 'name_kg', 'name_en', 'count', 'capacity', 'order']


class BuildingPhotoInline(admin.TabularInline):
    model = BuildingPhoto
    extra = 0
    fields = ['photo', 'type', 'title_ru', 'title_kg', 'title_en', 'order']


@admin.register(AcademicBuilding)
class AcademicBuildingAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'floors', 'is_active', 'order', 'created_at']
    list_filter = ['floors', 'is_active', 'created_at']
    search_fields = ['name_ru', 'name_kg', 'name_en', 'address_ru', 'address_kg', 'address_en']
    ordering = ['order', 'name_ru']
    inlines = [BuildingFacilityInline, BuildingPhotoInline]
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name_ru', 'name_kg', 'name_en', 'floors', 'is_active', 'order')
        }),
        ('Описание', {
            'fields': ('description_ru', 'description_kg', 'description_en')
        }),
        ('Адрес', {
            'fields': ('address_ru', 'address_kg', 'address_en')
        }),
        ('Координаты', {
            'fields': ('latitude', 'longitude'),
            'classes': ('collapse',)
        }),
    )


class DormitoryRoomInline(admin.TabularInline):
    model = DormitoryRoom
    extra = 0
    fields = ['type', 'name_ru', 'name_kg', 'name_en', 'price_monthly', 'features_ru', 'features_kg', 'features_en', 'order']


class DormitoryFacilityInline(admin.TabularInline):
    model = DormitoryFacility
    extra = 0
    fields = ['name_ru', 'name_kg', 'name_en', 'order']


class DormitoryPhotoInline(admin.TabularInline):
    model = DormitoryPhoto
    extra = 0
    fields = ['photo', 'type', 'title_ru', 'title_kg', 'title_en', 'order']


@admin.register(Dormitory)
class DormitoryAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'type', 'capacity', 'available', 'is_active', 'order', 'created_at']
    list_filter = ['type', 'is_active', 'created_at']
    search_fields = ['name_ru', 'name_kg', 'name_en', 'address_ru', 'address_kg', 'address_en']
    ordering = ['order', 'name_ru']
    inlines = [DormitoryRoomInline, DormitoryFacilityInline, DormitoryPhotoInline]
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name_ru', 'name_kg', 'name_en', 'type', 'capacity', 'available', 'is_active', 'order')
        }),
        ('Описание', {
            'fields': ('description_ru', 'description_kg', 'description_en')
        }),
        ('Адрес', {
            'fields': ('address_ru', 'address_kg', 'address_en')
        }),
    )


# Register inline models separately for better organization
@admin.register(HospitalDepartment)
class HospitalDepartmentAdmin(admin.ModelAdmin):
    list_display = ['hospital', 'name_ru', 'order']
    list_filter = ['hospital']
    search_fields = ['name_ru', 'name_kg', 'name_en']
    ordering = ['hospital__name_ru', 'order']


@admin.register(LaboratoryEquipment)
class LaboratoryEquipmentAdmin(admin.ModelAdmin):
    list_display = ['laboratory', 'name_ru', 'order']
    list_filter = ['laboratory']
    search_fields = ['name_ru', 'name_kg', 'name_en']
    ordering = ['laboratory__name_ru', 'order']


@admin.register(BuildingFacility)
class BuildingFacilityAdmin(admin.ModelAdmin):
    list_display = ['building', 'name_ru', 'count', 'capacity', 'order']
    list_filter = ['building']
    search_fields = ['name_ru', 'name_kg', 'name_en']
    ordering = ['building__name_ru', 'order']


@admin.register(BuildingPhoto)
class BuildingPhotoAdmin(admin.ModelAdmin):
    list_display = ['building', 'type', 'title_ru', 'order']
    list_filter = ['building', 'type']
    search_fields = ['title_ru', 'title_kg', 'title_en']
    ordering = ['building__name_ru', 'type', 'order']


@admin.register(DormitoryRoom)
class DormitoryRoomAdmin(admin.ModelAdmin):
    list_display = ['dormitory', 'type', 'name_ru', 'price_monthly', 'order']
    list_filter = ['dormitory', 'type']
    search_fields = ['name_ru', 'name_kg', 'name_en']
    ordering = ['dormitory__name_ru', 'order']


@admin.register(DormitoryFacility)
class DormitoryFacilityAdmin(admin.ModelAdmin):
    list_display = ['dormitory', 'name_ru', 'order']
    list_filter = ['dormitory']
    search_fields = ['name_ru', 'name_kg', 'name_en']
    ordering = ['dormitory__name_ru', 'order']


@admin.register(DormitoryPhoto)
class DormitoryPhotoAdmin(admin.ModelAdmin):
    list_display = ['dormitory', 'type', 'title_ru', 'order']
    list_filter = ['dormitory', 'type']
    search_fields = ['title_ru', 'title_kg', 'title_en']
    ordering = ['dormitory__name_ru', 'type', 'order']


# === CLASSROOM ADMIN ===

class ClassroomEquipmentInline(admin.TabularInline):
    model = ClassroomEquipment
    extra = 0
    fields = ['name_ru', 'name_kg', 'name_en', 'order']


class ClassroomFeatureInline(admin.TabularInline):
    model = ClassroomFeature
    extra = 0
    fields = ['name_ru', 'name_kg', 'name_en', 'order']


@admin.register(ClassroomCategory)
class ClassroomCategoryAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'name_kg', 'name_en', 'icon', 'order']
    list_editable = ['order']
    ordering = ['order', 'name_ru']


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'category', 'capacity', 'floor', 'size', 'is_active', 'order']
    list_filter = ['category', 'is_active', 'floor']
    search_fields = ['name_ru', 'name_kg', 'name_en', 'description_ru', 'description_kg', 'description_en']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'name_ru']
    inlines = [ClassroomEquipmentInline, ClassroomFeatureInline]
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('category', 'name_ru', 'name_kg', 'name_en', 'image', 'is_active', 'order')
        }),
        ('Описание', {
            'fields': ('description_ru', 'description_kg', 'description_en')
        }),
        ('Технические характеристики', {
            'fields': ('capacity', 'floor', 'size')
        }),
    )


# === STARTUP ADMIN ===

class StartupTeamMemberInline(admin.TabularInline):
    model = StartupTeamMember
    extra = 0
    fields = ['name_ru', 'name_kg', 'name_en', 'order']


class StartupInvestorInline(admin.TabularInline):
    model = StartupInvestor
    extra = 0
    fields = ['name_ru', 'name_kg', 'name_en', 'order']


class StartupAchievementInline(admin.TabularInline):
    model = StartupAchievement
    extra = 0
    fields = ['achievement_ru', 'achievement_kg', 'achievement_en', 'order']


@admin.register(StartupCategory)
class StartupCategoryAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'name_kg', 'name_en', 'icon', 'order']
    list_editable = ['order']
    ordering = ['order', 'name_ru']


@admin.register(Startup)
class StartupAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'category', 'stage', 'status', 'funding', 'year', 'is_active', 'order']
    list_filter = ['category', 'stage', 'status', 'is_active', 'year']
    search_fields = ['name_ru', 'name_kg', 'name_en', 'description_ru', 'description_kg', 'description_en']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'name_ru']
    inlines = [StartupTeamMemberInline, StartupInvestorInline, StartupAchievementInline]
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('category', 'name_ru', 'name_kg', 'name_en', 'image', 'is_active', 'order')
        }),
        ('Описание', {
            'fields': ('description_ru', 'description_kg', 'description_en')
        }),
        ('Полное описание', {
            'fields': ('full_description_ru', 'full_description_kg', 'full_description_en')
        }),
        ('Статус и финансы', {
            'fields': ('stage', 'status', 'funding', 'year')
        }),
    )

