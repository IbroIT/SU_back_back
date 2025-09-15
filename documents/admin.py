from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Document, DocumentCategory


@admin.register(DocumentCategory)
class DocumentCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'name_ru', 'name_en', 'name_kg']
    list_filter = ['name']
    search_fields = ['name_ru', 'name_en', 'name_kg']
    
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Переводы', {
            'fields': ('name_ru', 'name_en', 'name_kg'),
            'classes': ('wide',)
        }),
    )


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = [
        'title_ru', 'category', 'order', 'file_size', 'is_active', 
        'updated_at', 'download_link', 'file_info'
    ]
    list_filter = ['category', 'is_active', 'created_at', 'updated_at']
    search_fields = ['title_ru', 'title_en', 'title_kg', 'description_ru']
    list_editable = ['is_active', 'order']
    ordering = ['order', '-updated_at']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('category', 'order', 'is_active')
        }),
        ('Название', {
            'fields': ('title_ru', 'title_en', 'title_kg'),
            'classes': ('wide',)
        }),
        ('Описание', {
            'fields': ('description_ru', 'description_en', 'description_kg'),
            'classes': ('wide',)
        }),
        ('Файл', {
            'fields': ('file', 'file_size'),
            'description': 'Размер файла вычисляется автоматически при загрузке'
        }),
        ('Метаданные', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at', 'file_size']
    
    def download_link(self, obj):
        """Ссылка для скачивания документа"""
        if obj.file:
            url = reverse('documents:document-download', args=[obj.pk])
            return format_html(
                '<a href="{}" target="_blank" class="button">Скачать</a>',
                url
            )
        return "Файл не загружен"
    download_link.short_description = "Скачать"
    
    def file_info(self, obj):
        """Информация о файле"""
        if obj.file:
            return format_html(
                '<div style="line-height: 1.4;">'
                '<strong>Файл:</strong> {}<br>'
                '<strong>Размер:</strong> {}<br>'
                '<strong>Тип:</strong> {}'
                '</div>',
                obj.filename,
                obj.file_size or 'Не определен',
                obj.file_extension.upper() if obj.file_extension else 'Неизвестно'
            )
        return "Файл не загружен"
    file_info.short_description = "Информация о файле"
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('category')
    
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }


# Дополнительные настройки админки
admin.site.site_header = "Управление документами Университета Салымбекова"
admin.site.site_title = "Документы"
admin.site.index_title = "Панель управления документами"
