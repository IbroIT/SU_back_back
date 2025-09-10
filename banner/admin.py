from django.contrib import admin
from .models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'is_active', 'order', 'created_at']
    list_editable = ['is_active', 'order']
    list_filter = ['is_active', 'created_at']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['order', '-created_at']
    
    fieldsets = (
        ('Основное', {
            'fields': ['photo', 'is_active', 'order']
        }),
        ('Служебная информация', {
            'fields': ['created_at', 'updated_at'],
            'classes': ['collapse']
        }),
    )
