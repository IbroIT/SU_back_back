from django.contrib import admin
from .models import (
    ResearchArea, ResearchCenter, Grant, Conference, Publication, GrantApplication,
    ResearchManagementPosition, ScientificCouncil, Commission,
    ScientificJournal, JournalIssue, JournalArticle
)


@admin.register(ResearchArea)
class ResearchAreaAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'projects_count', 'publications_count', 'researchers_count', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title_ru', 'title_en', 'title_kg']
    list_editable = ['projects_count', 'publications_count', 'researchers_count', 'is_active']
    ordering = ['title_ru']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title_ru', 'title_en', 'title_kg', 'icon', 'color')
        }),
        ('Описание', {
            'fields': ('description_ru', 'description_en', 'description_kg')
        }),
        ('Статистика', {
            'fields': ('projects_count', 'publications_count', 'researchers_count')
        }),
        ('Настройки', {
            'fields': ('is_active',)
        }),
    )


@admin.register(ResearchCenter)
class ResearchCenterAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'director_ru', 'staff_count', 'established_year', 'is_active']
    list_filter = ['is_active', 'established_year']
    search_fields = ['name_ru', 'name_en', 'name_kg', 'director_ru', 'director_en', 'director_kg']
    list_editable = ['staff_count', 'is_active']
    ordering = ['name_ru']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name_ru', 'name_en', 'name_kg', 'director_ru', 'director_en', 'director_kg', 'established_year', 'staff_count')
        }),
        ('Описание', {
            'fields': ('description_ru', 'description_en', 'description_kg')
        }),
        ('Оборудование', {
            'fields': ('equipment_ru', 'equipment_en', 'equipment_kg')
        }),
        ('Контакты', {
            'fields': ('website', 'email', 'phone')
        }),
        ('Медиа', {
            'fields': ('image',)
        }),
        ('Настройки', {
            'fields': ('is_active',)
        }),
    )


@admin.register(Grant)
class GrantAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'organization_ru', 'amount', 'deadline', 'category', 'status']
    list_filter = ['category', 'status', 'is_active', 'created_at']
    search_fields = ['title_ru', 'title_en', 'title_kg', 'organization_ru', 'organization_en', 'organization_kg']
    list_editable = ['status']
    date_hierarchy = 'deadline'
    ordering = ['-created_at']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title_ru', 'title_en', 'title_kg', 'organization_ru', 'organization_en', 'organization_kg', 'amount')
        }),
        ('Сроки', {
            'fields': ('deadline', 'duration_ru', 'duration_en', 'duration_kg')
        }),
        ('Категория и статус', {
            'fields': ('category', 'status')
        }),
        ('Требования', {
            'fields': ('requirements_ru', 'requirements_en', 'requirements_kg')
        }),
        ('Описание', {
            'fields': ('description_ru', 'description_en', 'description_kg')
        }),
        ('Контакты', {
            'fields': ('contact', 'website', 'application_url')
        }),
        ('Настройки', {
            'fields': ('is_active',)
        }),
    )
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related()


@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'start_date', 'end_date', 'location_ru', 'status', 'speakers_count']
    list_filter = ['status', 'start_date', 'is_active']
    search_fields = ['title_ru', 'title_en', 'title_kg', 'location_ru']
    list_editable = ['status', 'speakers_count']
    date_hierarchy = 'start_date'
    ordering = ['start_date']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title_ru', 'title_en', 'title_kg', 'status')
        }),
        ('Даты', {
            'fields': ('start_date', 'end_date', 'deadline')
        }),
        ('Место проведения', {
            'fields': ('location_ru', 'location_en', 'location_kg')
        }),
        ('Описание', {
            'fields': ('description_ru', 'description_en', 'description_kg')
        }),
        ('Темы', {
            'fields': ('topics_ru', 'topics_en', 'topics_kg')
        }),
        ('Спикеры', {
            'fields': ('speakers_ru', 'speakers_en', 'speakers_kg', 'speakers_count')
        }),
        ('Дополнительно', {
            'fields': ('participants_limit', 'website', 'image')
        }),
        ('Настройки', {
            'fields': ('is_active',)
        }),
    )


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'authors_ru', 'journal', 'publication_date', 'publication_type', 'impact_factor', 'citations_count', 'is_featured']
    list_filter = ['publication_type', 'publication_date', 'is_featured', 'is_active', 'research_area']
    search_fields = ['title_ru', 'title_en', 'title_kg', 'authors_ru', 'authors_en', 'authors_kg', 'journal']
    list_editable = ['is_featured', 'citations_count']
    date_hierarchy = 'publication_date'
    ordering = ['-publication_date']
    raw_id_fields = ['research_area', 'research_center']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title_ru', 'title_en', 'title_kg', 'authors_ru', 'authors_en', 'authors_kg', 'publication_type')
        }),
        ('Публикация', {
            'fields': ('journal', 'publication_date', 'doi', 'url')
        }),
        ('Метрики', {
            'fields': ('impact_factor', 'citations_count')
        }),
        ('Аннотация', {
            'fields': ('abstract_ru', 'abstract_en', 'abstract_kg')
        }),
        ('Ключевые слова', {
            'fields': ('keywords_ru', 'keywords_en', 'keywords_kg')
        }),
        ('Связи', {
            'fields': ('research_area', 'research_center')
        }),
        ('Файлы', {
            'fields': ('file',)
        }),
        ('Настройки', {
            'fields': ('is_featured', 'is_active')
        }),
    )


@admin.register(GrantApplication)
class GrantApplicationAdmin(admin.ModelAdmin):
    list_display = ['project_title', 'principal_investigator', 'grant', 'status', 'budget', 'submitted_at']
    list_filter = ['status', 'submitted_at', 'grant__category']
    search_fields = ['project_title', 'principal_investigator', 'email', 'department']
    list_editable = ['status']
    date_hierarchy = 'submitted_at'
    ordering = ['-submitted_at']
    raw_id_fields = ['grant']
    readonly_fields = ['submitted_at']
    
    fieldsets = (
        ('Заявка', {
            'fields': ('grant', 'project_title', 'status')
        }),
        ('Контактная информация', {
            'fields': ('principal_investigator', 'email', 'phone', 'department')
        }),
        ('Команда', {
            'fields': ('team_members',)
        }),
        ('Проект', {
            'fields': ('project_description', 'budget', 'timeline', 'expected_results')
        }),
        ('Файлы', {
            'fields': ('files',)
        }),
        ('Администрирование', {
            'fields': ('admin_notes', 'submitted_at', 'reviewed_at')
        }),
    )
    
    actions = ['approve_applications', 'reject_applications']
    
    def approve_applications(self, request, queryset):
        updated = queryset.update(status='approved')
        self.message_user(request, f'{updated} заявок одобрено.')
    approve_applications.short_description = "Одобрить выбранные заявки"
    
    def reject_applications(self, request, queryset):
        updated = queryset.update(status='rejected')
        self.message_user(request, f'{updated} заявок отклонено.')
    reject_applications.short_description = "Отклонить выбранные заявки"


# Админ для научного управления
@admin.register(ResearchManagementPosition)
class ResearchManagementPositionAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'full_name_ru', 'position_type', 'order', 'parent', 'is_active']
    list_filter = ['position_type', 'is_active', 'created_at']
    search_fields = ['title_ru', 'title_en', 'title_kg', 'full_name_ru', 'full_name_en', 'full_name_kg']
    list_editable = ['order', 'is_active']
    ordering = ['position_type', 'order', 'title_ru']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title_ru', 'title_en', 'title_kg', 'position_type', 'order', 'parent')
        }),
        ('Персональные данные', {
            'fields': ('full_name_ru', 'full_name_en', 'full_name_kg', 'photo')
        }),
        ('Биография', {
            'fields': ('bio_ru', 'bio_en', 'bio_kg')
        }),
        ('Образование', {
            'fields': ('education_ru', 'education_en', 'education_kg')
        }),
        ('Научные интересы', {
            'fields': ('scientific_interests_ru', 'scientific_interests_en', 'scientific_interests_kg')
        }),
        ('Контакты', {
            'fields': ('contact_email', 'contact_phone', 'office_location')
        }),
        ('Настройки', {
            'fields': ('is_active',)
        }),
    )


@admin.register(ScientificCouncil)
class ScientificCouncilAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'chairman_ru', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name_ru', 'name_en', 'name_kg', 'chairman_ru', 'chairman_en', 'chairman_kg']
    list_editable = ['is_active']
    ordering = ['name_ru']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name_ru', 'name_en', 'name_kg')
        }),
        ('Описание', {
            'fields': ('description_ru', 'description_en', 'description_kg')
        }),
        ('Руководство', {
            'fields': ('chairman_ru', 'chairman_en', 'chairman_kg', 'secretary_ru', 'secretary_en', 'secretary_kg')
        }),
        ('Члены совета', {
            'fields': ('members_ru', 'members_en', 'members_kg')
        }),
        ('Функции и обязанности', {
            'fields': ('responsibilities_ru', 'responsibilities_en', 'responsibilities_kg')
        }),
        ('График работы', {
            'fields': ('meeting_schedule_ru', 'meeting_schedule_en', 'meeting_schedule_kg')
        }),
        ('Контакты', {
            'fields': ('contact_email', 'contact_phone')
        }),
        ('Настройки', {
            'fields': ('is_active',)
        }),
    )


@admin.register(Commission)
class CommissionAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'commission_type', 'chairman_ru', 'is_active', 'created_at']
    list_filter = ['commission_type', 'is_active', 'created_at']
    search_fields = ['name_ru', 'name_en', 'name_kg', 'chairman_ru', 'chairman_en', 'chairman_kg']
    list_editable = ['is_active']
    ordering = ['commission_type', 'name_ru']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name_ru', 'name_en', 'name_kg', 'commission_type')
        }),
        ('Описание', {
            'fields': ('description_ru', 'description_en', 'description_kg')
        }),
        ('Руководство', {
            'fields': ('chairman_ru', 'chairman_en', 'chairman_kg')
        }),
        ('Члены комиссии', {
            'fields': ('members_ru', 'members_en', 'members_kg')
        }),
        ('Функции', {
            'fields': ('functions_ru', 'functions_en', 'functions_kg')
        }),
        ('Контакты', {
            'fields': ('contact_email', 'contact_phone')
        }),
        ('Настройки', {
            'fields': ('is_active',)
        }),
    )


# Админ для научных журналов
@admin.register(ScientificJournal)
class ScientificJournalAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'established_year', 'impact_factor', 'is_open_access', 'is_peer_reviewed', 'is_active']
    list_filter = ['is_open_access', 'is_peer_reviewed', 'is_active', 'established_year']
    search_fields = ['title_ru', 'title_en', 'title_kg', 'issn', 'eissn']
    list_editable = ['impact_factor', 'is_open_access', 'is_peer_reviewed', 'is_active']
    ordering = ['title_ru']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title_ru', 'title_en', 'title_kg', 'established_year')
        }),
        ('Идентификаторы', {
            'fields': ('issn', 'eissn')
        }),
        ('Описание', {
            'fields': ('description_ru', 'description_en', 'description_kg')
        }),
        ('Редакция', {
            'fields': ('editor_in_chief_ru', 'editor_in_chief_en', 'editor_in_chief_kg')
        }),
        ('Редакционная коллегия', {
            'fields': ('editorial_board_ru', 'editorial_board_en', 'editorial_board_kg')
        }),
        ('Публикация', {
            'fields': ('publication_frequency_ru', 'publication_frequency_en', 'publication_frequency_kg')
        }),
        ('Тематика', {
            'fields': ('scope_ru', 'scope_en', 'scope_kg')
        }),
        ('Требования к публикации', {
            'fields': ('submission_guidelines_ru', 'submission_guidelines_en', 'submission_guidelines_kg')
        }),
        ('Медиа', {
            'fields': ('cover_image',)
        }),
        ('Контакты', {
            'fields': ('website', 'contact_email')
        }),
        ('Метрики', {
            'fields': ('impact_factor',)
        }),
        ('Настройки', {
            'fields': ('is_open_access', 'is_peer_reviewed', 'is_active')
        }),
    )


class JournalArticleInline(admin.TabularInline):
    model = JournalArticle
    extra = 0
    fields = ['title_ru', 'authors_ru', 'pages_start', 'pages_end', 'order', 'is_active']
    readonly_fields = ['created_at']


@admin.register(JournalIssue)
class JournalIssueAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'publication_date', 'articles_count', 'pages_count', 'is_published', 'is_active']
    list_filter = ['journal', 'year', 'is_published', 'is_active', 'publication_date']
    search_fields = ['title_ru', 'title_en', 'title_kg', 'description_ru', 'description_en', 'description_kg']
    list_editable = ['is_published', 'is_active']
    ordering = ['-year', '-volume', '-number']
    raw_id_fields = ['journal']
    inlines = [JournalArticleInline]
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('journal', 'volume', 'number', 'year', 'publication_date')
        }),
        ('Название', {
            'fields': ('title_ru', 'title_en', 'title_kg')
        }),
        ('Описание', {
            'fields': ('description_ru', 'description_en', 'description_kg')
        }),
        ('Медиа', {
            'fields': ('cover_image', 'pdf_file')
        }),
        ('Метаданные', {
            'fields': ('doi', 'pages_count', 'articles_count')
        }),
        ('Настройки', {
            'fields': ('is_published', 'is_active')
        }),
    )


@admin.register(JournalArticle)
class JournalArticleAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'issue', 'authors_ru', 'pages_start', 'pages_end', 'citations_count', 'is_active']
    list_filter = ['issue__journal', 'issue__year', 'is_open_access', 'is_active', 'published_date']
    search_fields = ['title_ru', 'title_en', 'title_kg', 'authors_ru', 'authors_en', 'authors_kg', 'abstract_ru', 'abstract_en', 'abstract_kg']
    list_editable = ['citations_count', 'is_active']
    ordering = ['-issue__year', '-issue__volume', '-issue__number', 'order']
    raw_id_fields = ['issue']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('issue', 'title_ru', 'title_en', 'title_kg', 'order')
        }),
        ('Авторы', {
            'fields': ('authors_ru', 'authors_en', 'authors_kg')
        }),
        ('Аннотация', {
            'fields': ('abstract_ru', 'abstract_en', 'abstract_kg')
        }),
        ('Ключевые слова', {
            'fields': ('keywords_ru', 'keywords_en', 'keywords_kg')
        }),
        ('Страницы', {
            'fields': ('pages_start', 'pages_end')
        }),
        ('Идентификаторы', {
            'fields': ('doi',)
        }),
        ('Файлы', {
            'fields': ('pdf_file',)
        }),
        ('Даты', {
            'fields': ('received_date', 'accepted_date', 'published_date')
        }),
        ('Метрики', {
            'fields': ('citations_count',)
        }),
        ('Настройки', {
            'fields': ('is_open_access', 'is_active')
        }),
    )
