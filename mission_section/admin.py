from django.contrib import admin
from .models import MissionSection, HistoryMilestone, Value, Priority, Achievement

# Временное решение: используем обычный ModelAdmin вместо TranslationAdmin
# чтобы сначала убедиться, что модели отображаются в админке

@admin.register(MissionSection)
class MissionSectionAdmin(admin.ModelAdmin):
    """
    Админ панель для модели MissionSection с поддержкой мультиязычности
    """
    list_display = ['title', 'title_en', 'title_ky', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'title_en', 'title_ky', 'mission_text']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Основная информация (Русский)', {
            'fields': ('title', 'subtitle', 'mission_text', 'is_active')
        }),
        ('Основная информация (English)', {
            'fields': ('title_en', 'subtitle_en', 'mission_text_en'),
            'classes': ('collapse',)
        }),
        ('Основная информация (Кыргызча)', {
            'fields': ('title_ky', 'subtitle_ky', 'mission_text_ky'),
            'classes': ('collapse',)
        }),
        ('Видение и подход (Русский)', {
            'fields': ('vision_title', 'vision_text', 'approach_title', 'approach_text')
        }),
        ('Видение и подход (English)', {
            'fields': ('vision_title_en', 'vision_text_en', 'approach_title_en', 'approach_text_en'),
            'classes': ('collapse',)
        }),
        ('Видение и подход (Кыргызча)', {
            'fields': ('vision_title_ky', 'vision_text_ky', 'approach_title_ky', 'approach_text_ky'),
            'classes': ('collapse',)
        }),
        ('Достижения и перспективы (Русский)', {
            'fields': ('achievements_subtitle', 'impact_title', 'impact_text', 'future_title', 'future_text')
        }),
        ('Достижения и перспективы (English)', {
            'fields': ('achievements_subtitle_en', 'impact_title_en', 'impact_text_en', 'future_title_en', 'future_text_en'),
            'classes': ('collapse',)
        }),
        ('Достижения и перспективы (Кыргызча)', {
            'fields': ('achievements_subtitle_ky', 'impact_title_ky', 'impact_text_ky', 'future_title_ky', 'future_text_ky'),
            'classes': ('collapse',)
        }),
        ('Метаданные', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(HistoryMilestone)
class HistoryMilestoneAdmin(admin.ModelAdmin):
    """
    Админ панель для модели HistoryMilestone с поддержкой мультиязычности
    """
    list_display = ['title', 'title_en', 'title_ky', 'year', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'year']
    search_fields = ['title', 'title_en', 'title_ky', 'description']
    ordering = ['order', 'year']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Основная информация (Русский)', {
            'fields': ('title', 'description', 'year', 'icon_class')
        }),
        ('Основная информация (English)', {
            'fields': ('title_en', 'description_en'),
            'classes': ('collapse',)
        }),
        ('Основная информация (Кыргызча)', {
            'fields': ('title_ky', 'description_ky'),
            'classes': ('collapse',)
        }),
        ('Настройки отображения', {
            'fields': ('order', 'is_active')
        }),
        ('Метаданные', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    """
    Админ панель для модели Value с поддержкой мультиязычности
    """
    list_display = ['title', 'title_en', 'title_ky', 'type', 'order', 'is_active', 'created_at']
    list_filter = ['type', 'is_active']
    search_fields = ['title', 'title_en', 'title_ky', 'description']
    ordering = ['order']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Основная информация (Русский)', {
            'fields': ('type', 'title', 'description')
        }),
        ('Основная информация (English)', {
            'fields': ('title_en', 'description_en'),
            'classes': ('collapse',)
        }),
        ('Основная информация (Кыргызча)', {
            'fields': ('title_ky', 'description_ky'),
            'classes': ('collapse',)
        }),
        ('Настройки отображения', {
            'fields': ('order', 'is_active')
        }),
        ('Метаданные', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    """
    Админ панель для модели Priority с поддержкой мультиязычности
    """
    list_display = ['short_text', 'short_text_en', 'short_text_ky', 'icon_class', 'order', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['text', 'text_en', 'text_ky']
    ordering = ['order']
    readonly_fields = ['created_at', 'updated_at']
    
    def short_text(self, obj):
        """Короткое отображение текста в списке (русский)"""
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    short_text.short_description = 'Текст (RU)'
    
    def short_text_en(self, obj):
        """Короткое отображение текста в списке (английский)"""
        if obj.text_en:
            return obj.text_en[:50] + '...' if len(obj.text_en) > 50 else obj.text_en
        return '-'
    short_text_en.short_description = 'Текст (EN)'
    
    def short_text_ky(self, obj):
        """Короткое отображение текста в списке (кыргызский)"""
        if obj.text_ky:
            return obj.text_ky[:50] + '...' if len(obj.text_ky) > 50 else obj.text_ky
        return '-'
    short_text_ky.short_description = 'Текст (KY)'
    
    fieldsets = (
        ('Основная информация (Русский)', {
            'fields': ('text', 'icon_class')
        }),
        ('Основная информация (English)', {
            'fields': ('text_en',),
            'classes': ('collapse',)
        }),
        ('Основная информация (Кыргызча)', {
            'fields': ('text_ky',),
            'classes': ('collapse',)
        }),
        ('Настройки отображения', {
            'fields': ('order', 'is_active')
        }),
        ('Метаданные', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    """
    Админ панель для модели Achievement с поддержкой мультиязычности
    """
    list_display = ['number', 'label', 'label_en', 'label_ky', 'order', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['number', 'label', 'label_en', 'label_ky']
    ordering = ['order']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('number',)
        }),
        ('Подписи (Русский)', {
            'fields': ('label',)
        }),
        ('Подписи (English)', {
            'fields': ('label_en',),
            'classes': ('collapse',)
        }),
        ('Подписи (Кыргызча)', {
            'fields': ('label_ky',),
            'classes': ('collapse',)
        }),
        ('Настройки отображения', {
            'fields': ('order', 'is_active')
        }),
        ('Метаданные', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
