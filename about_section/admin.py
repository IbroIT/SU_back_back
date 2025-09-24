from django.contrib import admin
from django.utils.html import format_html
from .models import Partner, AboutSection


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    """Admin interface for Partner model"""
    
    list_display = [
        'name', 'icon_display', 'color_preview', 'is_active', 
        'order', 'has_logo', 'has_website', 'created_at'
    ]
    list_filter = ['is_active', 'color_theme', 'created_at']
    search_fields = ['name', 'name_en', 'name_ky', 'description']
    ordering = ['order', 'name']
    list_editable = ['is_active', 'order']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'icon', 'logo', 'website', 'is_active', 'order')
        }),
        ('Переводы названия', {
            'fields': ('name_en', 'name_ky'),
            'classes': ('collapse',)
        }),
        ('Описание', {
            'fields': ('description',),
        }),
        ('Переводы описания', {
            'fields': ('description_en', 'description_ky'),
            'classes': ('collapse',)
        }),
        ('Внешний вид', {
            'fields': ('color_theme', 'glow_effect'),
        }),
    )
    
    def icon_display(self, obj):
        """Display icon in admin list"""
        if obj.icon:
            return format_html('<span style="font-size: 20px;">{}</span>', obj.icon)
        return '-'
    icon_display.short_description = 'Иконка'
    
    def color_preview(self, obj):
        """Display color preview in admin list"""
        # Extract colors from Tailwind classes for preview
        color_map = {
            'from-blue-500 to-indigo-600': 'linear-gradient(135deg, #3b82f6, #4f46e5)',
            'from-purple-500 to-pink-600': 'linear-gradient(135deg, #8b5cf6, #db2777)',
            'from-green-500 to-teal-600': 'linear-gradient(135deg, #10b981, #0d9488)',
            'from-amber-500 to-orange-600': 'linear-gradient(135deg, #f59e0b, #ea580c)',
            'from-red-500 to-rose-600': 'linear-gradient(135deg, #ef4444, #e11d48)',
            'from-indigo-500 to-blue-600': 'linear-gradient(135deg, #6366f1, #2563eb)',
            'from-pink-500 to-rose-600': 'linear-gradient(135deg, #ec4899, #e11d48)',
            'from-teal-500 to-emerald-600': 'linear-gradient(135deg, #14b8a6, #059669)',
            'from-cyan-500 to-blue-600': 'linear-gradient(135deg, #06b6d4, #2563eb)',
            'from-yellow-500 to-amber-600': 'linear-gradient(135deg, #eab308, #d97706)',
        }
        
        gradient = color_map.get(obj.color_theme, '#3b82f6')
        return format_html(
            '<div style="width: 30px; height: 20px; background: {}; border-radius: 4px; border: 1px solid #ddd;"></div>',
            gradient
        )
    color_preview.short_description = 'Цвет'
    
    def has_logo(self, obj):
        """Check if partner has logo"""
        return bool(obj.logo)
    has_logo.boolean = True
    has_logo.short_description = 'Есть лого'
    
    def has_website(self, obj):
        """Check if partner has website"""
        return bool(obj.website)
    has_website.boolean = True
    has_website.short_description = 'Есть сайт'
    
    def get_queryset(self, request):
        """Optimize queryset"""
        return super().get_queryset(request).select_related()
    
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)  # Add custom CSS if needed
        }


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    """Admin interface for AboutSection model"""
    
    list_display = [
        'title', 'is_active', 'show_partners', 
        'partners_animation_speed', 'created_at', 'updated_at'
    ]
    list_filter = ['is_active', 'show_partners', 'created_at']
    search_fields = ['title', 'title_en', 'title_ky', 'content']
    list_editable = ['is_active', 'show_partners']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'subtitle', 'is_active')
        }),
        ('Переводы заголовков', {
            'fields': ('title_en', 'title_ky', 'subtitle_en', 'subtitle_ky'),
            'classes': ('collapse',)
        }),
        ('Содержание', {
            'fields': ('content',),
        }),
        ('Переводы содержания', {
            'fields': ('content_en', 'content_ky'),
            'classes': ('collapse',)
        }),
        ('Настройки партнеров', {
            'fields': ('show_partners', 'partners_animation_speed'),
            'description': 'Настройки отображения партнеров в секции'
        }),
    )
    
    def get_queryset(self, request):
        """Optimize queryset"""
        return super().get_queryset(request)
    
    class Media:
        js = ('admin/js/admin_enhancements.js',)  # Add custom JS if needed


# Customize admin site headers
admin.site.site_header = 'Администрирование СалымБеков Университета'
admin.site.site_title = 'СалымБеков Админ'
admin.site.index_title = 'Управление контентом'
