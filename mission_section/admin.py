from django.contrib import admin
from .models import MissionSection, HistoryMilestone, Value, Priority, Achievement

# Временное решение: используем обычный ModelAdmin вместо TranslationAdmin
# чтобы сначала убедиться, что модели отображаются в админке

@admin.register(MissionSection)
class MissionSectionAdmin(admin.ModelAdmin):
    """
    Админ панель для модели MissionSection
    """
    list_display = ['title', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'mission_text']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'subtitle', 'mission_text', 'is_active')
        }),
        ('Видение и подход', {
            'fields': ('vision_title', 'vision_text', 'approach_title', 'approach_text')
        }),
        ('Достижения и перспективы', {
            'fields': ('achievements_subtitle', 'impact_title', 'impact_text', 'future_title', 'future_text')
        }),
        ('Метаданные', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(HistoryMilestone)
class HistoryMilestoneAdmin(admin.ModelAdmin):
    """
    Админ панель для модели HistoryMilestone
    """
    list_display = ['title', 'year', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'year']
    search_fields = ['title', 'description']
    ordering = ['order', 'year']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description', 'year', 'icon_class')
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
    Админ панель для модели Value
    """
    list_display = ['title', 'type', 'order', 'is_active', 'created_at']
    list_filter = ['type', 'is_active']
    search_fields = ['title', 'description']
    ordering = ['order']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('type', 'title', 'description')
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
    Админ панель для модели Priority
    """
    list_display = ['short_text', 'icon_class', 'order', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['text']
    ordering = ['order']
    readonly_fields = ['created_at', 'updated_at']
    
    def short_text(self, obj):
        """Короткое отображение текста в списке"""
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    short_text.short_description = 'Текст приоритета'
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('text', 'icon_class')
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
    Админ панель для модели Achievement
    """
    list_display = ['number', 'label', 'order', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['number', 'label']
    ordering = ['order']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('number', 'label')
        }),
        ('Настройки отображения', {
            'fields': ('order', 'is_active')
        }),
        ('Метаданные', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
