from django.contrib import admin
from .models import HSMInfo, Program, Faculty, Accreditation, LearningGoal


@admin.register(HSMInfo)
class HSMInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'title_kg', 'title_en']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'title_kg', 'title_en', 'is_active')
        }),
        ('Описание', {
            'fields': ('description', 'description_kg', 'description_en')
        }),
        ('История', {
            'fields': ('history', 'history_kg', 'history_en')
        }),
        ('Основные направления', {
            'fields': ('main_directions', 'main_directions_kg', 'main_directions_en')
        }),
        ('Метаданные', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'program_type', 'study_form', 'duration_years', 'is_active', 'order']
    list_filter = ['program_type', 'study_form', 'is_active', 'duration_years']
    search_fields = ['name', 'name_kg', 'name_en', 'description']
    list_editable = ['order', 'is_active']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'name_kg', 'name_en', 'program_type', 'study_form')
        }),
        ('Длительность обучения', {
            'fields': ('duration_years', 'duration_semesters')
        }),
        ('Описание программы', {
            'fields': ('description', 'description_kg', 'description_en')
        }),
        ('Компетенции', {
            'fields': ('competencies', 'competencies_kg', 'competencies_en')
        }),
        ('Карьерные перспективы', {
            'fields': ('career_prospects', 'career_prospects_kg', 'career_prospects_en')
        }),
        ('Настройки', {
            'fields': ('is_active', 'order')
        }),
        ('Метаданные', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'position', 'academic_degree', 'email', 'is_active', 'order']
    list_filter = ['position', 'academic_degree', 'is_active']
    search_fields = ['first_name', 'last_name', 'middle_name', 'first_name_kg', 'last_name_kg',
                    'first_name_en', 'last_name_en', 'email', 'specialization']
    list_editable = ['order', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'full_name']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('first_name', 'last_name', 'middle_name', 'photo')
        }),
        ('Перевод на кыргызский', {
            'fields': ('first_name_kg', 'last_name_kg', 'middle_name_kg'),
            'classes': ('collapse',)
        }),
        ('Перевод на английский', {
            'fields': ('first_name_en', 'last_name_en', 'middle_name_en'),
            'classes': ('collapse',)
        }),
        ('Должность и степень', {
            'fields': ('position', 'position_custom', 'academic_degree', 'academic_title')
        }),
        ('Контакты', {
            'fields': ('email', 'phone', 'office')
        }),
        ('Биография', {
            'fields': ('bio', 'bio_kg', 'bio_en'),
            'classes': ('collapse',)
        }),
        ('Специализация', {
            'fields': ('specialization', 'specialization_kg', 'specialization_en'),
            'classes': ('collapse',)
        }),
        ('Образование', {
            'fields': ('education', 'education_kg', 'education_en'),
            'classes': ('collapse',)
        }),
        ('Опыт работы', {
            'fields': ('experience', 'experience_kg', 'experience_en'),
            'classes': ('collapse',)
        }),
        ('Публикации', {
            'fields': ('publications', 'publications_kg', 'publications_en'),
            'classes': ('collapse',)
        }),
        ('Настройки', {
            'fields': ('is_active', 'order')
        }),
        ('Метаданные', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )


@admin.register(Accreditation)
class AccreditationAdmin(admin.ModelAdmin):
    list_display = ['name', 'organization', 'accreditation_type', 'issue_date', 'expiry_date', 'is_valid', 'is_active']
    list_filter = ['accreditation_type', 'is_active', 'issue_date', 'expiry_date']
    search_fields = ['name', 'name_kg', 'name_en', 'organization', 'certificate_number']
    list_editable = ['is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_valid']
    date_hierarchy = 'issue_date'
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'name_kg', 'name_en', 'accreditation_type')
        }),
        ('Организация', {
            'fields': ('organization', 'organization_kg', 'organization_en', 'organization_logo')
        }),
        ('Описание', {
            'fields': ('description', 'description_kg', 'description_en'),
            'classes': ('collapse',)
        }),
        ('Сертификат', {
            'fields': ('certificate_image', 'certificate_number', 'issue_date', 'expiry_date')
        }),
        ('Настройки', {
            'fields': ('is_active', 'order')
        }),
        ('Метаданные', {
            'fields': ('created_at', 'updated_at', 'is_valid'),
            'classes': ('collapse',)
        })
    )


@admin.register(LearningGoal)
class LearningGoalAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'order', 'created_at']
    list_filter = ['is_active', 'programs', 'created_at']
    search_fields = ['title', 'title_kg', 'title_en', 'description']
    list_editable = ['order', 'is_active']
    readonly_fields = ['created_at', 'updated_at']
    filter_horizontal = ['programs']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'title_kg', 'title_en')
        }),
        ('Описание', {
            'fields': ('description', 'description_kg', 'description_en')
        }),
        ('Компетенции', {
            'fields': ('competencies', 'competencies_kg', 'competencies_en')
        }),
        ('Карьерные перспективы', {
            'fields': ('career_prospects', 'career_prospects_kg', 'career_prospects_en')
        }),
        ('Связанные программы', {
            'fields': ('programs',)
        }),
        ('Настройки', {
            'fields': ('is_active', 'order')
        }),
        ('Метаданные', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
