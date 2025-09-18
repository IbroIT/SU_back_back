from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from .models import (
    MediaCategory, MediaOutlet, MediaArticle, 
    MediaTag, MediaArticleTag, MediaView, MediaStatistics
)


@admin.register(MediaCategory)
class MediaCategoryAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'name', 'slug', 'icon', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name_ru', 'name_kg', 'name_en']
    prepopulated_fields = {'slug': ('name_ru',)}
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'slug', 'icon')
        }),
        ('Многоязычные названия', {
            'fields': (('name_ru', 'name_kg', 'name_en'),)
        }),
        ('Описания', {
            'fields': (
                'description_ru',
                'description_kg', 
                'description_en'
            ),
            'classes': ['collapse']
        }),
        ('Настройки', {
            'fields': ('is_active',)
        }),
        ('Метаданные', {
            'fields': ('created_at', 'updated_at'),
            'classes': ['collapse']
        }),
    )


@admin.register(MediaOutlet)
class MediaOutletAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'default_category', 'total_articles', 'website', 'is_active', 'logo_preview']
    list_filter = ['default_category', 'is_active', 'created_at']
    search_fields = ['name_ru', 'name_kg', 'name_en', 'website']
    prepopulated_fields = {'slug': ('name_ru',)}
    readonly_fields = ['created_at', 'updated_at', 'total_articles', 'logo_preview']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'slug', 'default_category')
        }),
        ('Многоязычные названия', {
            'fields': (('name_ru', 'name_kg', 'name_en'),)
        }),
        ('Описания', {
            'fields': (
                'description_ru',
                'description_kg', 
                'description_en'
            ),
            'classes': ['collapse']
        }),
        ('Контактная информация', {
            'fields': ('website', 'email', 'phone')
        }),
        ('Логотип', {
            'fields': ('logo', 'logo_url', 'logo_preview')
        }),
        ('Настройки', {
            'fields': ('is_active',)
        }),
        ('Статистика', {
            'fields': ('total_articles',),
            'classes': ['collapse']
        }),
        ('Метаданные', {
            'fields': ('created_at', 'updated_at'),
            'classes': ['collapse']
        }),
    )
    
    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 5px;" />', obj.logo.url)
        elif obj.logo_url:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 5px;" />', obj.logo_url)
        return "Нет логотипа"
    logo_preview.short_description = 'Превью логотипа'


@admin.register(MediaTag)
class MediaTagAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'slug', 'color_preview', 'usage_count', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name_ru', 'name_kg', 'name_en']
    prepopulated_fields = {'slug': ('name_ru',)}
    readonly_fields = ['created_at', 'usage_count']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('slug', 'color')
        }),
        ('Многоязычные названия', {
            'fields': (('name_ru', 'name_kg', 'name_en'),)
        }),
        ('Настройки', {
            'fields': ('is_active',)
        }),
        ('Статистика', {
            'fields': ('usage_count',),
            'classes': ['collapse']
        }),
        ('Метаданные', {
            'fields': ('created_at',),
            'classes': ['collapse']
        }),
    )
    
    def color_preview(self, obj):
        return format_html(
            '<div style="width: 30px; height: 20px; background-color: {}; border: 1px solid #ccc; border-radius: 3px;"></div>',
            obj.color
        )
    color_preview.short_description = 'Цвет'


class MediaArticleTagInline(admin.TabularInline):
    model = MediaArticleTag
    extra = 1
    autocomplete_fields = ['tag']


@admin.register(MediaArticle)
class MediaArticleAdmin(admin.ModelAdmin):
    list_display = [
        'title_ru', 'outlet', 'category', 'publication_date', 'importance_score',
        'sentiment', 'is_published', 'is_featured', 'is_verified', 'views_count', 'image_preview'
    ]
    list_filter = [
        'category', 'outlet', 'sentiment', 'importance_score',
        'is_published', 'is_featured', 'is_verified',
        'publication_date', 'created_at'
    ]
    search_fields = [
        'title_ru', 'title_kg', 'title_en', 
        'description_ru', 'description_kg', 'description_en',
        'content_ru', 'content_kg', 'content_en',
        'journalist_name', 'keywords'
    ]
    prepopulated_fields = {'slug': ('title_ru',)}
    readonly_fields = ['created_at', 'updated_at', 'views_count', 'image_preview']
    date_hierarchy = 'publication_date'
    autocomplete_fields = ['outlet', 'category']
    
    fieldsets = (
        ('Основная информация', {
            'fields': (
                ('title_ru', 'title_kg', 'title_en'),
                'slug',
                ('description_ru', 'description_kg', 'description_en')
            )
        }),
        ('Полное содержание (опционально)', {
            'fields': (
                'content_ru',
                'content_kg',
                'content_en'
            ),
            'classes': ['collapse']
        }),
        ('Классификация', {
            'fields': (
                ('category', 'outlet'),
                ('sentiment', 'importance_score'),
                'keywords'
            )
        }),
        ('Изображения', {
            'fields': ('image', 'image_url', 'image_preview')
        }),
        ('Ссылки', {
            'fields': ('original_url', 'official_site_url', 'archive_url')
        }),
        ('Автор и журналист', {
            'fields': (
                ('author_ru', 'author_kg', 'author_en'),
                ('journalist_name', 'journalist_email')
            ),
            'classes': ['collapse']
        }),
        ('Даты и публикация', {
            'fields': (
                'publication_date',
                ('is_published', 'is_featured', 'is_verified')
            )
        }),
        ('Дополнительные метрики', {
            'fields': ('reach_estimate',),
            'classes': ['collapse']
        }),
        ('Метаинформация', {
            'fields': ('created_at', 'updated_at', 'views_count'),
            'classes': ['collapse']
        }),
    )
    
    inlines = [MediaArticleTagInline]
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="60" style="border-radius: 5px;" />', obj.image.url)
        elif obj.image_url:
            return format_html('<img src="{}" width="100" height="60" style="border-radius: 5px;" />', obj.image_url)
        return "Нет изображения"
    image_preview.short_description = 'Превью'
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('category', 'outlet')
    
    actions = [
        'make_published', 'make_unpublished', 'make_featured', 'make_verified',
        'mark_positive', 'mark_neutral', 'mark_negative'
    ]
    
    def make_published(self, request, queryset):
        queryset.update(is_published=True)
    make_published.short_description = "Опубликовать выбранные статьи"
    
    def make_unpublished(self, request, queryset):
        queryset.update(is_published=False)
    make_unpublished.short_description = "Снять с публикации"
    
    def make_featured(self, request, queryset):
        queryset.update(is_featured=True)
    make_featured.short_description = "Сделать рекомендуемыми"
    
    def make_verified(self, request, queryset):
        queryset.update(is_verified=True)
    make_verified.short_description = "Пометить как проверенные"
    
    def mark_positive(self, request, queryset):
        queryset.update(sentiment='positive')
    mark_positive.short_description = "Пометить как позитивные"
    
    def mark_neutral(self, request, queryset):
        queryset.update(sentiment='neutral')
    mark_neutral.short_description = "Пометить как нейтральные"
    
    def mark_negative(self, request, queryset):
        queryset.update(sentiment='negative')
    mark_negative.short_description = "Пометить как негативные"


@admin.register(MediaView)
class MediaViewAdmin(admin.ModelAdmin):
    list_display = ['article', 'ip_address', 'viewed_at']
    list_filter = ['viewed_at', 'article__category']
    search_fields = ['article__title_ru', 'ip_address']
    readonly_fields = ['article', 'ip_address', 'user_agent', 'viewed_at']
    date_hierarchy = 'viewed_at'
    
    def has_add_permission(self, request):
        return False  # Запрещаем ручное добавление просмотров
    
    def has_change_permission(self, request, obj=None):
        return False  # Запрещаем редактирование просмотров


@admin.register(MediaStatistics)
class MediaStatisticsAdmin(admin.ModelAdmin):
    list_display = [
        'date', 'total_articles', 'tv_articles', 'newspaper_articles', 
        'online_articles', 'radio_articles', 'total_views', 'total_reach'
    ]
    list_filter = ['date']
    readonly_fields = [
        'date', 'tv_articles', 'newspaper_articles', 'online_articles', 
        'radio_articles', 'magazine_articles', 'total_articles', 'total_views',
        'total_reach', 'positive_articles', 'neutral_articles', 'negative_articles',
        'created_at', 'updated_at'
    ]
    date_hierarchy = 'date'
    
    fieldsets = (
        ('Дата', {
            'fields': ('date',)
        }),
        ('Статистика по категориям', {
            'fields': (
                ('tv_articles', 'newspaper_articles'),
                ('online_articles', 'radio_articles', 'magazine_articles'),
                'total_articles'
            )
        }),
        ('Общие показатели', {
            'fields': ('total_views', 'total_reach')
        }),
        ('Анализ тональности', {
            'fields': (
                ('positive_articles', 'neutral_articles', 'negative_articles'),
            ),
            'classes': ['collapse']
        }),
        ('Метаданные', {
            'fields': ('created_at', 'updated_at'),
            'classes': ['collapse']
        }),
    )
    
    def has_add_permission(self, request):
        return False  # Статистика создается автоматически
    
    def has_delete_permission(self, request, obj=None):
        return False  # Защищаем от случайного удаления


# Настройки админ-панели для медиа-покрытия
admin.site.site_header = "Салымбековский Университет - Управление медиа-покрытием"
admin.site.site_title = "Медиа СУ"
admin.site.index_title = "Панель управления медиа-материалами"
