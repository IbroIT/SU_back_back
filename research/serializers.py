from rest_framework import serializers
from .models import (
    ResearchArea, ResearchCenter, Grant, Conference, Publication, GrantApplication,
    ResearchManagementPosition, ScientificCouncil, Commission,
    ScientificJournal, JournalIssue, JournalArticle
)


class ResearchAreaSerializer(serializers.ModelSerializer):
    """Сериализатор для областей исследований"""
    
    class Meta:
        model = ResearchArea
        fields = [
            'id', 'title_ru', 'title_en', 'title_kg',
            'description_ru', 'description_en', 'description_kg',
            'icon', 'color', 'projects_count', 'publications_count',
            'researchers_count', 'is_active'
        ]


class ResearchCenterSerializer(serializers.ModelSerializer):
    """Сериализатор для исследовательских центров"""
    
    class Meta:
        model = ResearchCenter
        fields = [
            'id', 'name_ru', 'name_en', 'name_kg',
            'description_ru', 'description_en', 'description_kg',
            'director_ru', 'director_en', 'director_kg', 
            'staff_count', 'established_year',
            'equipment_ru', 'equipment_en', 'equipment_kg',
            'image', 'website', 'email', 'phone', 'is_active'
        ]


class GrantListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка грантов (краткая информация)"""
    is_deadline_soon = serializers.ReadOnlyField()
    
    class Meta:
        model = Grant
        fields = [
            'id', 'title_ru', 'title_en', 'title_kg',
            'organization_ru', 'organization_en', 'organization_kg', 
            'amount', 'deadline', 'category', 'status',
            'duration_ru', 'duration_en', 'duration_kg',
            'is_deadline_soon'
        ]


class GrantDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для детальной информации о гранте"""
    is_deadline_soon = serializers.ReadOnlyField()
    
    class Meta:
        model = Grant
        fields = [
            'id', 'title_ru', 'title_en', 'title_kg',
            'organization_ru', 'organization_en', 'organization_kg', 
            'amount', 'deadline', 'category', 'status',
            'duration_ru', 'duration_en', 'duration_kg',
            'requirements_ru', 'requirements_en', 'requirements_kg',
            'description_ru', 'description_en', 'description_kg',
            'contact', 'website', 'is_deadline_soon', 'created_at'
        ]


class ConferenceSerializer(serializers.ModelSerializer):
    """Сериализатор для конференций"""
    is_upcoming = serializers.ReadOnlyField()
    
    class Meta:
        model = Conference
        fields = [
            'id', 'title_ru', 'title_en', 'title_kg',
            'start_date', 'end_date', 'deadline',
            'location_ru', 'location_en', 'location_kg',
            'description_ru', 'description_en', 'description_kg',
            'topics_ru', 'topics_en', 'topics_kg',
            'speakers_ru', 'speakers_en', 'speakers_kg',
            'speakers_count', 'participants_limit', 'image',
            'website', 'status', 'is_upcoming'
        ]


class PublicationListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка публикаций (краткая информация)"""
    research_area_name = serializers.CharField(source='research_area.title_ru', read_only=True)
    research_center_name = serializers.CharField(source='research_center.name_ru', read_only=True)
    
    class Meta:
        model = Publication
        fields = [
            'id', 'title_ru', 'title_en', 'title_kg',
            'authors_ru', 'authors_en', 'authors_kg', 
            'journal', 'publication_date', 'publication_type',
            'impact_factor', 'citations_count', 'doi', 'url',
            'research_area_name', 'research_center_name', 'is_featured'
        ]


class PublicationDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для детальной информации о публикации"""
    research_area = ResearchAreaSerializer(read_only=True)
    research_center = ResearchCenterSerializer(read_only=True)
    
    class Meta:
        model = Publication
        fields = [
            'id', 'title_ru', 'title_en', 'title_kg',
            'authors_ru', 'authors_en', 'authors_kg', 
            'journal', 'publication_date', 'publication_type',
            'impact_factor', 'citations_count', 'doi', 'url',
            'abstract_ru', 'abstract_en', 'abstract_kg',
            'keywords_ru', 'keywords_en', 'keywords_kg',
            'research_area', 'research_center', 'file',
            'is_featured', 'created_at'
        ]


class GrantApplicationCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания заявки на грант"""
    
    class Meta:
        model = GrantApplication
        fields = [
            'grant', 'project_title', 'principal_investigator',
            'email', 'phone', 'department', 'team_members',
            'project_description', 'budget', 'timeline',
            'expected_results', 'files'
        ]
        
    def validate_budget(self, value):
        if value <= 0:
            raise serializers.ValidationError("Бюджет должен быть больше 0")
        return value
        
    def validate_timeline(self, value):
        if value <= 0 or value > 60:
            raise serializers.ValidationError("Срок реализации должен быть от 1 до 60 месяцев")
        return value


class GrantApplicationSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра заявок на грант"""
    grant_title = serializers.CharField(source='grant.title_ru', read_only=True)
    
    class Meta:
        model = GrantApplication
        fields = [
            'id', 'grant', 'grant_title', 'project_title',
            'principal_investigator', 'email', 'phone', 'department',
            'team_members', 'project_description', 'budget', 'timeline',
            'expected_results', 'files', 'status', 'admin_notes',
            'submitted_at', 'reviewed_at'
        ]
        read_only_fields = ['status', 'admin_notes', 'reviewed_at']


# Статистические сериализаторы
class ResearchStatsSerializer(serializers.Serializer):
    """Сериализатор для статистики исследований"""
    total_areas = serializers.IntegerField()
    total_centers = serializers.IntegerField()
    total_grants = serializers.IntegerField()
    active_grants = serializers.IntegerField()
    total_publications = serializers.IntegerField()
    total_conferences = serializers.IntegerField()
    upcoming_conferences = serializers.IntegerField()
    pending_applications = serializers.IntegerField()


class GrantStatsSerializer(serializers.Serializer):
    """Сериализатор для статистики грантов по категориям"""
    category = serializers.CharField()
    count = serializers.IntegerField()
    total_amount = serializers.CharField()


class PublicationStatsSerializer(serializers.Serializer):
    """Сериализатор для статистики публикаций по типам"""
    publication_type = serializers.CharField()
    count = serializers.IntegerField()
    avg_impact_factor = serializers.DecimalField(max_digits=5, decimal_places=2)


# Сериализаторы для научного управления
class ResearchManagementPositionSerializer(serializers.ModelSerializer):
    """Сериализатор для должностей в научном управлении"""
    children = serializers.SerializerMethodField()
    
    class Meta:
        model = ResearchManagementPosition
        fields = [
            'id', 'title_ru', 'title_en', 'title_kg',
            'full_name_ru', 'full_name_en', 'full_name_kg',
            'position_type', 'bio_ru', 'bio_en', 'bio_kg',
            'education_ru', 'education_en', 'education_kg',
            'scientific_interests_ru', 'scientific_interests_en', 'scientific_interests_kg',
            'contact_email', 'contact_phone', 'office_location',
            'photo', 'order', 'parent', 'children'
        ]
    
    def get_children(self, obj):
        children = obj.get_children()
        return ResearchManagementPositionSerializer(children, many=True, context=self.context).data


class ScientificCouncilSerializer(serializers.ModelSerializer):
    """Сериализатор для научных советов"""
    
    class Meta:
        model = ScientificCouncil
        fields = [
            'id', 'name_ru', 'name_en', 'name_kg',
            'description_ru', 'description_en', 'description_kg',
            'chairman_ru', 'chairman_en', 'chairman_kg',
            'secretary_ru', 'secretary_en', 'secretary_kg',
            'members_ru', 'members_en', 'members_kg',
            'responsibilities_ru', 'responsibilities_en', 'responsibilities_kg',
            'meeting_schedule_ru', 'meeting_schedule_en', 'meeting_schedule_kg',
            'contact_email', 'contact_phone'
        ]


class CommissionSerializer(serializers.ModelSerializer):
    """Сериализатор для комиссий"""
    
    class Meta:
        model = Commission
        fields = [
            'id', 'name_ru', 'name_en', 'name_kg', 'commission_type',
            'description_ru', 'description_en', 'description_kg',
            'chairman_ru', 'chairman_en', 'chairman_kg',
            'members_ru', 'members_en', 'members_kg',
            'functions_ru', 'functions_en', 'functions_kg',
            'contact_email', 'contact_phone'
        ]


# Сериализаторы для научных журналов
class JournalArticleSerializer(serializers.ModelSerializer):
    """Сериализатор для статей журнала"""
    
    class Meta:
        model = JournalArticle
        fields = [
            'id', 'title_ru', 'title_en', 'title_kg',
            'authors_ru', 'authors_en', 'authors_kg',
            'abstract_ru', 'abstract_en', 'abstract_kg',
            'keywords_ru', 'keywords_en', 'keywords_kg',
            'pages_start', 'pages_end', 'doi', 'pdf_file',
            'received_date', 'accepted_date', 'published_date',
            'citations_count', 'order', 'is_open_access'
        ]


class JournalIssueListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка выпусков журнала"""
    journal_title = serializers.CharField(source='journal.title_ru', read_only=True)
    
    class Meta:
        model = JournalIssue
        fields = [
            'id', 'volume', 'number', 'year', 'publication_date',
            'title_ru', 'title_en', 'title_kg',
            'cover_image', 'pdf_file', 'doi',
            'pages_count', 'articles_count', 'is_published',
            'journal_title'
        ]


class JournalIssueDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для детальной информации о выпуске журнала"""
    journal = serializers.StringRelatedField(read_only=True)
    articles = JournalArticleSerializer(many=True, read_only=True)
    
    class Meta:
        model = JournalIssue
        fields = [
            'id', 'journal', 'volume', 'number', 'year', 'publication_date',
            'title_ru', 'title_en', 'title_kg',
            'description_ru', 'description_en', 'description_kg',
            'cover_image', 'pdf_file', 'doi',
            'pages_count', 'articles_count', 'is_published',
            'articles', 'created_at'
        ]


class ScientificJournalListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка научных журналов"""
    latest_issue = serializers.SerializerMethodField()
    issues_count = serializers.SerializerMethodField()
    
    class Meta:
        model = ScientificJournal
        fields = [
            'id', 'title_ru', 'title_en', 'title_kg',
            'description_ru', 'description_en', 'description_kg',
            'issn', 'eissn', 'editor_in_chief_ru', 'editor_in_chief_en', 'editor_in_chief_kg',
            'publication_frequency_ru', 'publication_frequency_en', 'publication_frequency_kg',
            'cover_image', 'website', 'established_year', 'impact_factor',
            'is_open_access', 'is_peer_reviewed',
            'latest_issue', 'issues_count'
        ]
    
    def get_latest_issue(self, obj):
        latest = obj.issues.filter(is_published=True, is_active=True).order_by('-year', '-volume', '-number').first()
        if latest:
            return JournalIssueListSerializer(latest).data
        return None
    
    def get_issues_count(self, obj):
        return obj.issues.filter(is_published=True, is_active=True).count()


class ScientificJournalDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для детальной информации о научном журнале"""
    recent_issues = serializers.SerializerMethodField()
    issues_by_year = serializers.SerializerMethodField()
    
    class Meta:
        model = ScientificJournal
        fields = [
            'id', 'title_ru', 'title_en', 'title_kg',
            'description_ru', 'description_en', 'description_kg',
            'issn', 'eissn', 'editor_in_chief_ru', 'editor_in_chief_en', 'editor_in_chief_kg',
            'editorial_board_ru', 'editorial_board_en', 'editorial_board_kg',
            'publication_frequency_ru', 'publication_frequency_en', 'publication_frequency_kg',
            'scope_ru', 'scope_en', 'scope_kg',
            'submission_guidelines_ru', 'submission_guidelines_en', 'submission_guidelines_kg',
            'cover_image', 'website', 'contact_email', 'established_year', 'impact_factor',
            'is_open_access', 'is_peer_reviewed',
            'recent_issues', 'issues_by_year', 'created_at'
        ]
    
    def get_recent_issues(self, obj):
        recent = obj.issues.filter(is_published=True, is_active=True).order_by('-year', '-volume', '-number')[:5]
        return JournalIssueListSerializer(recent, many=True).data
    
    def get_issues_by_year(self, obj):
        """Группировка выпусков по годам для архива"""
        issues = obj.issues.filter(is_published=True, is_active=True).order_by('-year', '-volume', '-number')
        
        years_data = {}
        for issue in issues:
            year = issue.year
            if year not in years_data:
                years_data[year] = []
            years_data[year].append(JournalIssueListSerializer(issue).data)
        
        # Преобразуем в список для удобства фронтенда
        return [{'year': year, 'issues': issues} for year, issues in sorted(years_data.items(), reverse=True)]
