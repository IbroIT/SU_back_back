from rest_framework import serializers
from django.utils import timezone
from .models import (
    MediaCategory, MediaOutlet, MediaArticle, 
    MediaTag, MediaArticleTag, MediaStatistics
)


class MediaCategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий медиа"""
    
    class Meta:
        model = MediaCategory
        fields = [
            'id', 'name', 'slug', 'icon',
            'name_ru', 'name_kg', 'name_en',
            'description_ru', 'description_kg', 'description_en',
            'is_active', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class MediaCategoryBasicSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для категорий (для использования в других сериализаторах)"""
    
    class Meta:
        model = MediaCategory
        fields = ['id', 'name_ru', 'name_kg', 'name_en', 'slug', 'icon']


class MediaOutletSerializer(serializers.ModelSerializer):
    """Сериализатор для медиа-изданий"""
    default_category = MediaCategoryBasicSerializer(read_only=True)
    logo_url_or_default = serializers.ReadOnlyField()
    
    class Meta:
        model = MediaOutlet
        fields = [
            'id', 'name', 'slug',
            'name_ru', 'name_kg', 'name_en',
            'description_ru', 'description_kg', 'description_en',
            'website', 'email', 'phone',
            'logo', 'logo_url', 'logo_url_or_default',
            'default_category', 'total_articles',
            'is_active', 'created_at'
        ]
        read_only_fields = ['id', 'total_articles', 'created_at']


class MediaOutletBasicSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для изданий (для использования в других сериализаторах)"""
    logo_url_or_default = serializers.ReadOnlyField()
    
    class Meta:
        model = MediaOutlet
        fields = ['id', 'name_ru', 'name_kg', 'name_en', 'slug', 'logo_url_or_default']


class MediaTagSerializer(serializers.ModelSerializer):
    """Сериализатор для тегов медиа"""
    
    class Meta:
        model = MediaTag
        fields = [
            'id', 'name_ru', 'name_kg', 'name_en', 'slug',
            'color', 'usage_count', 'is_active', 'created_at'
        ]
        read_only_fields = ['id', 'usage_count', 'created_at']


class MediaTagBasicSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для тегов"""
    
    class Meta:
        model = MediaTag
        fields = ['id', 'name_ru', 'name_kg', 'name_en', 'slug', 'color']


class MediaArticleListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка медиа-публикаций"""
    category = MediaCategoryBasicSerializer(read_only=True)
    outlet = MediaOutletBasicSerializer(read_only=True)
    tags = serializers.SerializerMethodField()
    image_url_or_default = serializers.ReadOnlyField()
    
    class Meta:
        model = MediaArticle
        fields = [
            'id', 'title_ru', 'title_kg', 'title_en', 'slug',
            'description_ru', 'description_kg', 'description_en',
            'category', 'outlet', 'tags',
            'image', 'image_url', 'image_url_or_default',
            'original_url', 'official_site_url', 'publication_date',
            'importance_score', 'sentiment', 'views_count',
            'is_published', 'is_featured', 'is_verified',
            'created_at'
        ]
        read_only_fields = ['id', 'views_count', 'created_at']
    
    def get_tags(self, obj):
        """Получаем теги через промежуточную модель"""
        tag_relationships = obj.tags.all()
        tags_data = []
        for tag_rel in tag_relationships:
            tags_data.append({
                'id': tag_rel.tag.id,
                'name_ru': tag_rel.tag.name_ru,
                'name_kg': tag_rel.tag.name_kg,
                'name_en': tag_rel.tag.name_en,
                'slug': tag_rel.tag.slug,
                'color': tag_rel.tag.color
            })
        return tags_data


class MediaArticleDetailSerializer(serializers.ModelSerializer):
    """Детальный сериализатор для медиа-публикаций"""
    category = MediaCategoryBasicSerializer(read_only=True)
    outlet = MediaOutletBasicSerializer(read_only=True)
    tags = serializers.SerializerMethodField()
    image_url_or_default = serializers.ReadOnlyField()
    
    class Meta:
        model = MediaArticle
        fields = [
            'id', 'title_ru', 'title_kg', 'title_en', 'slug',
            'description_ru', 'description_kg', 'description_en',
            'content_ru', 'content_kg', 'content_en',
            'category', 'outlet', 'tags',
            'image', 'image_url', 'image_url_or_default',
            'original_url', 'official_site_url', 'archive_url',
            'author_ru', 'author_kg', 'author_en',
            'journalist_name', 'journalist_email',
            'publication_date', 'importance_score', 'sentiment',
            'views_count', 'reach_estimate', 'keywords',
            'is_published', 'is_featured', 'is_verified',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'views_count', 'created_at', 'updated_at']
    
    def get_tags(self, obj):
        """Получаем теги через промежуточную модель"""
        tag_relationships = obj.tags.all()
        tags_data = []
        for tag_rel in tag_relationships:
            tags_data.append({
                'id': tag_rel.tag.id,
                'name_ru': tag_rel.tag.name_ru,
                'name_kg': tag_rel.tag.name_kg,
                'name_en': tag_rel.tag.name_en,
                'slug': tag_rel.tag.slug,
                'color': tag_rel.tag.color
            })
        return tags_data


class MediaArticleCreateUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания и обновления медиа-публикаций"""
    tag_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False,
        help_text="Список ID тегов"
    )
    
    class Meta:
        model = MediaArticle
        fields = [
            'title_ru', 'title_kg', 'title_en', 'slug',
            'description_ru', 'description_kg', 'description_en',
            'content_ru', 'content_kg', 'content_en',
            'category', 'outlet',
            'image', 'image_url',
            'original_url', 'archive_url',
            'author_ru', 'author_kg', 'author_en',
            'journalist_name', 'journalist_email',
            'publication_date', 'importance_score', 'sentiment',
            'reach_estimate', 'keywords',
            'is_published', 'is_featured', 'is_verified',
            'tag_ids'
        ]
    
    def validate_importance_score(self, value):
        """Валидация оценки важности"""
        if value < 1 or value > 10:
            raise serializers.ValidationError("Оценка важности должна быть от 1 до 10.")
        return value
    
    def validate_publication_date(self, value):
        """Валидация даты публикации"""
        if value > timezone.now().date():
            raise serializers.ValidationError("Дата публикации не может быть в будущем.")
        return value
    
    def create(self, validated_data):
        """Создание медиа-публикации с тегами"""
        tag_ids = validated_data.pop('tag_ids', [])
        article = MediaArticle.objects.create(**validated_data)
        
        # Добавляем теги
        if tag_ids:
            tags = MediaTag.objects.filter(id__in=tag_ids, is_active=True)
            for tag in tags:
                MediaArticleTag.objects.create(article=article, tag=tag)
        
        return article
    
    def update(self, instance, validated_data):
        """Обновление медиа-публикации с тегами"""
        tag_ids = validated_data.pop('tag_ids', None)
        
        # Обновляем основные поля
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        
        # Обновляем теги, если они переданы
        if tag_ids is not None:
            # Удаляем существующие связи
            MediaArticleTag.objects.filter(article=instance).delete()
            
            # Добавляем новые теги
            tags = MediaTag.objects.filter(id__in=tag_ids, is_active=True)
            for tag in tags:
                MediaArticleTag.objects.create(article=instance, tag=tag)
        
        return instance


class MediaStatisticsSerializer(serializers.ModelSerializer):
    """Сериализатор для статистики медиа"""
    
    class Meta:
        model = MediaStatistics
        fields = [
            'id', 'date',
            'tv_articles', 'newspaper_articles', 'online_articles',
            'radio_articles', 'magazine_articles', 'total_articles',
            'total_views', 'total_reach',
            'positive_articles', 'neutral_articles', 'negative_articles',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class MediaDashboardSerializer(serializers.Serializer):
    """Сериализатор для дашборда медиа-покрытия"""
    
    # Общая статистика
    total_articles = serializers.IntegerField()
    total_views = serializers.IntegerField()
    total_outlets = serializers.IntegerField()
    total_categories = serializers.IntegerField()
    
    # Статистика по категориям
    articles_by_category = serializers.DictField()
    
    # Статистика по тональности
    sentiment_stats = serializers.DictField()
    
    # Топ медиа-изданий
    top_outlets = serializers.ListField()
    
    # Популярные теги
    popular_tags = serializers.ListField()
    
    # Последние статьи
    recent_articles = MediaArticleListSerializer(many=True)
    
    # Рекомендуемые статьи
    featured_articles = MediaArticleListSerializer(many=True)


class MediaSearchSerializer(serializers.Serializer):
    """Сериализатор для поиска медиа-материалов"""
    
    # Параметры поиска
    query = serializers.CharField(required=False, help_text="Поисковый запрос")
    category = serializers.IntegerField(required=False, help_text="ID категории")
    outlet = serializers.IntegerField(required=False, help_text="ID издания")
    sentiment = serializers.ChoiceField(
        choices=['positive', 'neutral', 'negative'],
        required=False,
        help_text="Тональность"
    )
    importance_score_min = serializers.IntegerField(
        required=False, min_value=1, max_value=10,
        help_text="Минимальная оценка важности"
    )
    importance_score_max = serializers.IntegerField(
        required=False, min_value=1, max_value=10,
        help_text="Максимальная оценка важности"
    )
    date_from = serializers.DateField(required=False, help_text="Дата публикации от")
    date_to = serializers.DateField(required=False, help_text="Дата публикации до")
    is_featured = serializers.BooleanField(required=False, help_text="Только рекомендуемые")
    is_verified = serializers.BooleanField(required=False, help_text="Только проверенные")
    
    # Параметры сортировки
    ordering = serializers.ChoiceField(
        choices=[
            'publication_date', '-publication_date',
            'importance_score', '-importance_score',
            'views_count', '-views_count',
            'created_at', '-created_at'
        ],
        required=False,
        default='-publication_date',
        help_text="Поле для сортировки"
    )
    
    # Параметры пагинации
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    page_size = serializers.IntegerField(required=False, min_value=1, max_value=100, default=20)
    
    def validate(self, data):
        """Валидация параметров поиска"""
        # Проверяем корректность диапазона важности
        min_score = data.get('importance_score_min')
        max_score = data.get('importance_score_max')
        
        if min_score and max_score and min_score > max_score:
            raise serializers.ValidationError({
                'importance_score_min': 'Минимальная оценка не может быть больше максимальной.'
            })
        
        # Проверяем корректность диапазона дат
        date_from = data.get('date_from')
        date_to = data.get('date_to')
        
        if date_from and date_to and date_from > date_to:
            raise serializers.ValidationError({
                'date_from': 'Дата "от" не может быть больше даты "до".'
            })
        
        return data


class MediaAnalyticsSerializer(serializers.Serializer):
    """Сериализатор для аналитики медиа-покрытия"""
    
    period = serializers.ChoiceField(
        choices=['day', 'week', 'month', 'quarter', 'year'],
        required=False,
        default='month',
        help_text="Период для аналитики"
    )
    
    start_date = serializers.DateField(required=False, help_text="Начальная дата")
    end_date = serializers.DateField(required=False, help_text="Конечная дата")
    
    # Результаты аналитики
    timeline_data = serializers.ListField(read_only=True)
    category_distribution = serializers.DictField(read_only=True)
    sentiment_trends = serializers.DictField(read_only=True)
    outlet_performance = serializers.ListField(read_only=True)
    top_journalists = serializers.ListField(read_only=True)
    keyword_cloud = serializers.ListField(read_only=True)
