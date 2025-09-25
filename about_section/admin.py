from django.contrib import admin
from django.utils.html import format_html
from .models import Partner, AboutSection, Accreditation, CouncilType, CouncilMember, CouncilDocument


@admin.register(Accreditation)
class AccreditationAdmin(admin.ModelAdmin):
    """Admin interface for Accreditation model"""
    
    list_display = [
        'title', 'logo_display', 'year', 'accreditation_type', 
        'status', 'is_active', 'order', 'color_preview'
    ]
    list_filter = ['accreditation_type', 'status', 'is_active', 'year']
    search_fields = ['title', 'title_en', 'title_ky', 'description']
    ordering = ['order', 'title']
    list_editable = ['is_active', 'order']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'logo', 'year', 'accreditation_type', 'status', 'validity', 'level', 'is_active', 'order')
        }),
        ('Переводы основных полей', {
            'fields': ('title_en', 'title_ky', 'status_en', 'status_ky', 'validity_en', 'validity_ky', 'level_en', 'level_ky'),
            'classes': ('collapse',)
        }),
        ('Описания', {
            'fields': ('description', 'full_description'),
        }),
        ('Переводы описаний', {
            'fields': ('description_en', 'description_ky', 'full_description_en', 'full_description_ky'),
            'classes': ('collapse',)
        }),
        ('Преимущества', {
            'fields': ('benefits', 'benefits_en', 'benefits_ky'),
            'description': 'Введите преимущества в формате JSON списка, например: ["Преимущество 1", "Преимущество 2"]'
        }),
        ('Внешний вид', {
            'fields': ('color', 'icon_color', 'badge_color'),
        }),
    )
    
    def logo_display(self, obj):
        """Display logo emoji in admin list"""
        if obj.logo:
            return format_html('<span style="font-size: 20px;">{}</span>', obj.logo)
        return '-'
    logo_display.short_description = 'Лого'
    
    def color_preview(self, obj):
        """Display color preview in admin list"""
        color_map = {
            'from-blue-500 to-blue-600': 'linear-gradient(135deg, #3b82f6, #2563eb)',
            'from-green-500 to-green-600': 'linear-gradient(135deg, #10b981, #059669)',
            'from-purple-500 to-purple-600': 'linear-gradient(135deg, #8b5cf6, #7c3aed)',
            'from-orange-500 to-orange-600': 'linear-gradient(135deg, #f97316, #ea580c)',
            'from-teal-500 to-teal-600': 'linear-gradient(135deg, #14b8a6, #0d9488)',
            'from-indigo-500 to-indigo-600': 'linear-gradient(135deg, #6366f1, #4f46e5)',
        }
        
        gradient = color_map.get(obj.color, '#3b82f6')
        return format_html(
            '<div style="width: 30px; height: 20px; background: {}; border-radius: 4px; border: 1px solid #ddd;"></div>',
            gradient
        )
    color_preview.short_description = 'Цвет'


@admin.register(CouncilType)
class CouncilTypeAdmin(admin.ModelAdmin):
    """Admin interface for CouncilType model"""
    
    list_display = ['name', 'slug', 'members_count', 'documents_count', 'is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['name', 'name_en', 'name_ky', 'description']
    ordering = ['order', 'name']
    list_editable = ['is_active', 'order']
    prepopulated_fields = {'slug': ('name',)}
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'slug', 'is_active', 'order')
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
    )
    
    def members_count(self, obj):
        """Count of active members"""
        return obj.members.filter(is_active=True).count()
    members_count.short_description = 'Члены'
    
    def documents_count(self, obj):
        """Count of active documents"""
        return obj.documents.filter(is_active=True).count()
    documents_count.short_description = 'Документы'


class CouncilMemberInline(admin.TabularInline):
    """Inline admin for CouncilMember"""
    model = CouncilMember
    extra = 1
    fields = ['name', 'position', 'department', 'email', 'phone', 'is_active', 'order']


class CouncilDocumentInline(admin.TabularInline):
    """Inline admin for CouncilDocument"""
    model = CouncilDocument
    extra = 1
    fields = ['title', 'file', 'date', 'is_active', 'order']


@admin.register(CouncilMember)
class CouncilMemberAdmin(admin.ModelAdmin):
    """Admin interface for CouncilMember model"""
    
    list_display = ['name', 'position', 'council_type', 'department', 'has_photo', 'is_active', 'order']
    list_filter = ['council_type', 'is_active']
    search_fields = ['name', 'position', 'department', 'bio']
    ordering = ['council_type', 'order', 'name']
    list_editable = ['is_active', 'order']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('council_type', 'name', 'photo', 'email', 'phone', 'is_active', 'order')
        }),
        ('Переводы ФИО', {
            'fields': ('name_en', 'name_ky'),
            'classes': ('collapse',)
        }),
        ('Должность и подразделение', {
            'fields': ('position', 'department'),
        }),
        ('Переводы должности и подразделения', {
            'fields': ('position_en', 'position_ky', 'department_en', 'department_ky'),
            'classes': ('collapse',)
        }),
        ('Биография', {
            'fields': ('bio',),
        }),
        ('Переводы биографии', {
            'fields': ('bio_en', 'bio_ky'),
            'classes': ('collapse',)
        }),
    )
    
    def has_photo(self, obj):
        """Check if member has photo"""
        return bool(obj.photo)
    has_photo.boolean = True
    has_photo.short_description = 'Есть фото'


@admin.register(CouncilDocument)
class CouncilDocumentAdmin(admin.ModelAdmin):
    """Admin interface for CouncilDocument model"""
    
    list_display = ['title', 'council_type', 'date', 'size', 'is_active', 'order']
    list_filter = ['council_type', 'is_active', 'date']
    search_fields = ['title', 'title_en', 'title_ky', 'description']
    ordering = ['council_type', 'order', '-date']
    list_editable = ['is_active', 'order']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('council_type', 'title', 'file', 'date', 'size', 'is_active', 'order')
        }),
        ('Переводы названия', {
            'fields': ('title_en', 'title_ky'),
            'classes': ('collapse',)
        }),
        ('Описание', {
            'fields': ('description',),
        }),
        ('Переводы описания', {
            'fields': ('description_en', 'description_ky'),
            'classes': ('collapse',)
        }),
    )


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
                'fields': ('name', 'icon', 'logo', 'website', 'is_active', 'order', 'latitude', 'longitude')
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
