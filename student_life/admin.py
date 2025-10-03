from django.contrib import admin
from .models import (
    PartnerOrganization, OrganizationSpecialization,
    InternshipRequirement, InternshipRequirementItem, ReportTemplate,
    PartnerUniversity, UniversityProgram,
    ExchangeOpportunity, ExchangeBenefit, MobilityRequirement,
    InternalRule, InternalRuleItem,
    AcademicRegulation, AcademicRegulationSection, AcademicRegulationRule,
    DownloadableDocument,
    StudentGuide, GuideRequirement, GuideStep, GuideStepDetail,
    StudentAppeal, PhotoAlbum, Photo, VideoContent, StudentLifeStatistic,
    EResourceCategory, EResource, EResourceFeature
)


# =============================================================================
# ADMIN ДЛЯ ПРАКТИКИ
# =============================================================================

class OrganizationSpecializationInline(admin.TabularInline):
    model = OrganizationSpecialization
    extra = 1
    fields = ['name_ru', 'name_kg', 'name_en']


@admin.register(PartnerOrganization)
class PartnerOrganizationAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'type', 'location', 'contact_person', 'has_logo', 'is_active']
    list_filter = ['type', 'is_active', 'location']
    search_fields = ['name_ru', 'name_kg', 'name_en', 'contact_person', 'location']
    inlines = [OrganizationSpecializationInline]
    ordering = ['name_ru']
    
    def has_logo(self, obj):
        return bool(obj.logo)
    has_logo.boolean = True
    has_logo.short_description = 'Логотип'
    
    fieldsets = (
        ('Основная информация', {
            'fields': ['type', 'location', 'contact_person', 'phone', 'email', 'website', 'logo', 'is_active']
        }),
        ('Русский', {
            'fields': ['name_ru', 'description_ru'],
            'classes': ['collapse']
        }),
        ('Кыргызский', {
            'fields': ['name_kg', 'description_kg'],
            'classes': ['collapse']
        }),
        ('Английский', {
            'fields': ['name_en', 'description_en'],
            'classes': ['collapse']
        }),
    )


class InternshipRequirementItemInline(admin.TabularInline):
    model = InternshipRequirementItem
    extra = 1
    fields = ['text_ru', 'order']


@admin.register(InternshipRequirement)
class InternshipRequirementAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'category', 'order', 'is_active']
    list_filter = ['category', 'is_active']
    inlines = [InternshipRequirementItemInline]
    ordering = ['category', 'order']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ['category', 'order', 'is_active']
        }),
        ('Русский', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызский', {
            'fields': ['title_kg', 'description_kg'],
            'classes': ['collapse']
        }),
        ('Английский', {
            'fields': ['title_en', 'description_en'],
            'classes': ['collapse']
        }),
    )


@admin.register(ReportTemplate)
class ReportTemplateAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['name_ru', 'name_kg', 'name_en']
    ordering = ['name_ru']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ['file', 'is_active']
        }),
        ('Русский', {
            'fields': ['name_ru', 'description_ru'],
        }),
        ('Кыргызский', {
            'fields': ['name_kg', 'description_kg'],
            'classes': ['collapse']
        }),
        ('Английский', {
            'fields': ['name_en', 'description_en'],
            'classes': ['collapse']
        }),
    )


# =============================================================================
# ADMIN ДЛЯ АКАДЕМИЧЕСКОЙ МОБИЛЬНОСТИ
# =============================================================================

class UniversityProgramInline(admin.TabularInline):
    model = UniversityProgram
    extra = 1
    fields = ['name_ru', 'duration', 'language']


@admin.register(PartnerUniversity)
class PartnerUniversityAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'country', 'city', 'is_active']
    list_filter = ['country', 'is_active']
    search_fields = ['name_ru', 'name_kg', 'name_en', 'country', 'city']
    inlines = [UniversityProgramInline]
    ordering = ['name_ru']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ['country', 'city', 'website', 'logo', 'is_active']
        }),
        ('Русский', {
            'fields': ['name_ru', 'description_ru'],
        }),
        ('Кыргызский', {
            'fields': ['name_kg', 'description_kg'],
            'classes': ['collapse']
        }),
        ('Английский', {
            'fields': ['name_en', 'description_en'],
            'classes': ['collapse']
        }),
    )


class ExchangeBenefitInline(admin.TabularInline):
    model = ExchangeBenefit
    extra = 1
    fields = ['text_ru', 'order']


@admin.register(ExchangeOpportunity)
class ExchangeOpportunityAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'type', 'is_active']
    list_filter = ['type', 'is_active']
    inlines = [ExchangeBenefitInline]
    
    fieldsets = (
        ('Основная информация', {
            'fields': ['type', 'is_active']
        }),
        ('Русский', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызский', {
            'fields': ['title_kg', 'description_kg'],
            'classes': ['collapse']
        }),
        ('Английский', {
            'fields': ['title_en', 'description_en'],
            'classes': ['collapse']
        }),
    )


@admin.register(MobilityRequirement)
class MobilityRequirementAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'category', 'order', 'is_active']
    list_filter = ['category', 'is_active']
    ordering = ['category', 'order']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ['category', 'order', 'is_active']
        }),
        ('Русский', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызский', {
            'fields': ['title_kg', 'description_kg'],
            'classes': ['collapse']
        }),
        ('Английский', {
            'fields': ['title_en', 'description_en'],
            'classes': ['collapse']
        }),
    )


# =============================================================================
# ADMIN ДЛЯ РЕГЛАМЕНТОВ И ПРАВИЛ
# =============================================================================

class InternalRuleItemInline(admin.TabularInline):
    model = InternalRuleItem
    extra = 1
    fields = ['text_ru', 'order']


@admin.register(InternalRule)
class InternalRuleAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'order', 'is_active']
    list_filter = ['is_active']
    inlines = [InternalRuleItemInline]
    ordering = ['order']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ['order', 'is_active']
        }),
        ('Русский', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызский', {
            'fields': ['title_kg', 'description_kg'],
            'classes': ['collapse']
        }),
        ('Английский', {
            'fields': ['title_en', 'description_en'],
            'classes': ['collapse']
        }),
    )


class AcademicRegulationRuleInline(admin.TabularInline):
    model = AcademicRegulationRule
    extra = 1
    fields = ['number', 'text_ru', 'order']


class AcademicRegulationSectionInline(admin.StackedInline):
    model = AcademicRegulationSection
    extra = 1
    fields = ['number', 'title_ru', 'order']


@admin.register(AcademicRegulation)
class AcademicRegulationAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'version', 'effective_date', 'is_active']
    list_filter = ['is_active', 'effective_date']
    inlines = [AcademicRegulationSectionInline]
    ordering = ['-effective_date']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ['version', 'effective_date', 'is_active']
        }),
        ('Русский', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызский', {
            'fields': ['title_kg', 'description_kg'],
            'classes': ['collapse']
        }),
        ('Английский', {
            'fields': ['title_en', 'description_en'],
            'classes': ['collapse']
        }),
    )


@admin.register(AcademicRegulationSection)
class AcademicRegulationSectionAdmin(admin.ModelAdmin):
    list_display = ['regulation', 'number', 'title_ru', 'order']
    list_filter = ['regulation']
    inlines = [AcademicRegulationRuleInline]
    ordering = ['regulation', 'order']


@admin.register(DownloadableDocument)
class DownloadableDocumentAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'file_size', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['title_ru', 'title_kg', 'title_en']
    ordering = ['title_ru']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ['file', 'file_size', 'is_active']
        }),
        ('Русский', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызский', {
            'fields': ['title_kg', 'description_kg'],
            'classes': ['collapse']
        }),
        ('Английский', {
            'fields': ['title_en', 'description_en'],
            'classes': ['collapse']
        }),
    )


# =============================================================================
# ADMIN ДЛЯ ИНСТРУКЦИЙ
# =============================================================================

class GuideRequirementInline(admin.TabularInline):
    model = GuideRequirement
    extra = 1
    fields = ['text_ru', 'order']


class GuideStepDetailInline(admin.TabularInline):
    model = GuideStepDetail
    extra = 1
    fields = ['text_ru', 'order']


class GuideStepInline(admin.StackedInline):
    model = GuideStep
    extra = 1
    fields = ['title_ru', 'order']


@admin.register(StudentGuide)
class StudentGuideAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title_ru', 'title_kg', 'title_en']
    inlines = [GuideRequirementInline, GuideStepInline]
    ordering = ['order']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ['order', 'is_active']
        }),
        ('Русский', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызский', {
            'fields': ['title_kg', 'description_kg'],
            'classes': ['collapse']
        }),
        ('Английский', {
            'fields': ['title_en', 'description_en'],
            'classes': ['collapse']
        }),
    )


@admin.register(GuideStep)
class GuideStepAdmin(admin.ModelAdmin):
    list_display = ['guide', 'order', 'title_ru']
    list_filter = ['guide']
    inlines = [GuideStepDetailInline]
    ordering = ['guide', 'order']


# =============================================================================
# ADMIN ДЛЯ ОБРАЩЕНИЙ
# =============================================================================

@admin.register(StudentAppeal)
class StudentAppealAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'category', 'subject', 'status', 'created_at']
    list_filter = ['category', 'status', 'created_at']
    search_fields = ['full_name', 'email', 'subject']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']

    fieldsets = (
        ('Информация о студенте', {
            'fields': ('full_name', 'email', 'phone', 'student_id')
        }),
        ('Обращение', {
            'fields': ('category', 'subject', 'message', 'attachment')
        }),
        ('Обработка', {
            'fields': ('status', 'response', 'processed_by')
        }),
        ('Системная информация', {
            'fields': ('created_at', 'updated_at'),
            'classes': ['collapse']
        }),
    )


# =============================================================================
# ADMIN ДЛЯ ФОТОГАЛЕРЕИ И ВИДЕО
# =============================================================================

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 0
    fields = ['title_ru', 'image', 'tags_ru', 'order', 'is_active']
    readonly_fields = ['uploaded_at']


@admin.register(PhotoAlbum)
class PhotoAlbumAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'event_date', 'photo_count', 'is_active', 'order']
    list_filter = ['is_active', 'event_date']
    search_fields = ['title_ru', 'title_kg', 'title_en', 'tags_ru']
    inlines = [PhotoInline]
    ordering = ['-event_date', 'order']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ['cover_image', 'event_date', 'order', 'is_active']
        }),
        ('Русский', {
            'fields': ['title_ru', 'description_ru', 'tags_ru'],
        }),
        ('Кыргызский', {
            'fields': ['title_kg', 'description_kg', 'tags_kg'],
            'classes': ['collapse']
        }),
        ('Английский', {
            'fields': ['title_en', 'description_en', 'tags_en'],
            'classes': ['collapse']
        }),
    )


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'album', 'photographer', 'order', 'is_active', 'uploaded_at']
    list_filter = ['album', 'is_active', 'uploaded_at']
    search_fields = ['title_ru', 'title_kg', 'title_en', 'tags_ru', 'photographer']
    ordering = ['album', 'order', '-uploaded_at']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ['album', 'image', 'photographer', 'order', 'is_active']
        }),
        ('Русский', {
            'fields': ['title_ru', 'description_ru', 'tags_ru'],
        }),
        ('Кыргызский', {
            'fields': ['title_kg', 'description_kg', 'tags_kg'],
            'classes': ['collapse']
        }),
        ('Английский', {
            'fields': ['title_en', 'description_en', 'tags_en'],
            'classes': ['collapse']
        }),
    )


@admin.register(VideoContent)
class VideoContentAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'type', 'duration', 'views_count', 'is_featured', 'is_active', 'created_at']
    list_filter = ['type', 'is_active', 'is_featured', 'event_date']
    search_fields = ['title_ru', 'title_kg', 'title_en', 'tags_ru']
    ordering = ['-created_at', 'order']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ['type', 'video_file', 'video_url', 'thumbnail', 'duration', 'event_date', 'is_featured', 'is_active', 'order']
        }),
        ('Статистика', {
            'fields': ['views_count'],
            'classes': ['collapse']
        }),
        ('Русский', {
            'fields': ['title_ru', 'description_ru', 'tags_ru'],
        }),
        ('Кыргызский', {
            'fields': ['title_kg', 'description_kg', 'tags_kg'],
            'classes': ['collapse']
        }),
        ('Английский', {
            'fields': ['title_en', 'description_en', 'tags_en'],
            'classes': ['collapse']
        }),
    )


@admin.register(StudentLifeStatistic)
class StudentLifeStatisticAdmin(admin.ModelAdmin):
    list_display = ['label_ru', 'type', 'value', 'order', 'is_active', 'last_updated']
    list_filter = ['type', 'is_active']
    search_fields = ['label_ru', 'label_kg', 'label_en']
    ordering = ['order', 'type']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ['type', 'value', 'icon', 'order', 'is_active']
        }),
        ('Русский', {
            'fields': ['label_ru', 'description_ru'],
        }),
        ('Кыргызский', {
            'fields': ['label_kg', 'description_kg'],
            'classes': ['collapse']
        }),
        ('Английский', {
            'fields': ['label_en', 'description_en'],
            'classes': ['collapse']
        }),
    )


# =============================================================================
# ADMIN ДЛЯ ЭЛЕКТРОННЫХ РЕСУРСОВ
# =============================================================================

@admin.register(EResourceCategory)
class EResourceCategoryAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'icon', 'color', 'count', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name_ru', 'name_kg', 'name_en']
    ordering = ['order', 'name_ru']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ['icon', 'color', 'order', 'is_active']
        }),
        ('Русский', {
            'fields': ['name_ru'],
        }),
        ('Кыргызский', {
            'fields': ['name_kg'],
            'classes': ['collapse']
        }),
        ('Английский', {
            'fields': ['name_en'],
            'classes': ['collapse']
        }),
    )
    
    def count(self, obj):
        return obj.count
    count.short_description = 'Количество ресурсов'


class EResourceFeatureInline(admin.TabularInline):
    model = EResourceFeature
    extra = 1
    fields = ['text_ru', 'text_kg', 'text_en', 'order']


@admin.register(EResource)
class EResourceAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'category', 'status', 'users_count', 'is_popular', 'is_active', 'order']
    list_filter = ['category', 'status', 'is_popular', 'is_active']
    search_fields = ['title_ru', 'title_kg', 'title_en', 'description_ru']
    ordering = ['order', 'title_ru']
    inlines = [EResourceFeatureInline]
    
    fieldsets = (
        ('Основная информация', {
            'fields': ['category', 'icon', 'color', 'url', 'users_count', 'status', 'is_popular', 'is_active', 'order']
        }),
        ('Русский', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызский', {
            'fields': ['title_kg', 'description_kg'],
            'classes': ['collapse']
        }),
        ('Английский', {
            'fields': ['title_en', 'description_en'],
            'classes': ['collapse']
        }),
    )
