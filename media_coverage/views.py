from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count, Avg, Sum, Case, When, IntegerField
from django.utils import timezone
from datetime import datetime, timedelta
from rest_framework import generics, status, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import (
    MediaCategory, MediaOutlet, MediaArticle, 
    MediaTag, MediaView, MediaStatistics
)
from .serializers import (
    MediaCategorySerializer, MediaOutletSerializer, 
    MediaArticleListSerializer, MediaArticleDetailSerializer,
    MediaArticleCreateUpdateSerializer, MediaTagSerializer,
    MediaStatisticsSerializer, MediaDashboardSerializer,
    MediaSearchSerializer, MediaAnalyticsSerializer
)


class StandardResultsPagination(PageNumberPagination):
    """Стандартная пагинация для медиа-контента"""
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


# КАТЕГОРИИ МЕДИА
class MediaCategoryListView(generics.ListCreateAPIView):
    """Список и создание категорий медиа"""
    queryset = MediaCategory.objects.filter(is_active=True).order_by('name_ru')
    serializer_class = MediaCategorySerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name_ru', 'name_kg', 'name_en']


class MediaCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Детали, обновление и удаление категории медиа"""
    queryset = MediaCategory.objects.all()
    serializer_class = MediaCategorySerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'


# МЕДИА-ИЗДАНИЯ
class MediaOutletListView(generics.ListCreateAPIView):
    """Список и создание медиа-изданий"""
    queryset = MediaOutlet.objects.filter(is_active=True).order_by('name_ru')
    serializer_class = MediaOutletSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name_ru', 'name_kg', 'name_en', 'website']
    filterset_fields = ['default_category']


class MediaOutletDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Детали, обновление и удаление медиа-издания"""
    queryset = MediaOutlet.objects.all()
    serializer_class = MediaOutletSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'


# ТЕГИ МЕДИА
class MediaTagListView(generics.ListCreateAPIView):
    """Список и создание тегов медиа"""
    queryset = MediaTag.objects.filter(is_active=True).order_by('-usage_count', 'name_ru')
    serializer_class = MediaTagSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name_ru', 'name_kg', 'name_en']


class MediaTagDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Детали, обновление и удаление тега медиа"""
    queryset = MediaTag.objects.all()
    serializer_class = MediaTagSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'


# МЕДИА-ПУБЛИКАЦИИ
class MediaArticleListView(generics.ListCreateAPIView):
    """Список и создание медиа-публикаций"""
    queryset = MediaArticle.objects.filter(is_published=True).select_related(
        'category', 'outlet'
    ).prefetch_related('tags').order_by('-publication_date')
    serializer_class = MediaArticleListSerializer
    permission_classes = [AllowAny]
    pagination_class = StandardResultsPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = [
        'title_ru', 'title_kg', 'title_en',
        'description_ru', 'description_kg', 'description_en',
        'content_ru', 'content_kg', 'content_en',
        'keywords', 'journalist_name'
    ]
    filterset_fields = [
        'category', 'outlet', 'sentiment', 'importance_score',
        'is_featured', 'is_verified'
    ]
    ordering_fields = [
        'publication_date', 'importance_score', 'views_count', 'created_at'
    ]
    ordering = ['-publication_date']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MediaArticleCreateUpdateSerializer
        return MediaArticleListSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return [AllowAny()]


class MediaArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Детали, обновление и удаление медиа-публикации"""
    queryset = MediaArticle.objects.select_related('category', 'outlet').prefetch_related('tags')
    serializer_class = MediaArticleDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return MediaArticleCreateUpdateSerializer
        return MediaArticleDetailSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return [AllowAny()]

    def retrieve(self, request, *args, **kwargs):
        """Переопределяем для подсчета просмотров"""
        instance = self.get_object()
        
        # Увеличиваем счетчик просмотров
        if request.META.get('REMOTE_ADDR'):
            MediaView.objects.get_or_create(
                article=instance,
                ip_address=request.META.get('REMOTE_ADDR'),
                defaults={'user_agent': request.META.get('HTTP_USER_AGENT', '')}
            )
            # Обновляем счетчик в статье
            instance.views_count = instance.article_views.count()
            instance.save(update_fields=['views_count'])
        
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


# РЕКОМЕНДУЕМЫЕ ПУБЛИКАЦИИ
class FeaturedMediaArticlesView(generics.ListAPIView):
    """Рекомендуемые медиа-публикации"""
    queryset = MediaArticle.objects.filter(
        is_published=True, 
        is_featured=True
    ).select_related('category', 'outlet').prefetch_related('tags').order_by('-publication_date')
    serializer_class = MediaArticleListSerializer
    permission_classes = [AllowAny]
    pagination_class = StandardResultsPagination


# ПОПУЛЯРНЫЕ ПУБЛИКАЦИИ
class PopularMediaArticlesView(generics.ListAPIView):
    """Популярные медиа-публикации"""
    queryset = MediaArticle.objects.filter(
        is_published=True
    ).select_related('category', 'outlet').prefetch_related('tags').order_by('-views_count', '-publication_date')
    serializer_class = MediaArticleListSerializer
    permission_classes = [AllowAny]
    pagination_class = StandardResultsPagination


# ПОСЛЕДНИЕ ПУБЛИКАЦИИ
class RecentMediaArticlesView(generics.ListAPIView):
    """Последние медиа-публикации"""
    queryset = MediaArticle.objects.filter(
        is_published=True,
        publication_date__gte=timezone.now().date() - timedelta(days=30)
    ).select_related('category', 'outlet').prefetch_related('tags').order_by('-publication_date')
    serializer_class = MediaArticleListSerializer
    permission_classes = [AllowAny]
    pagination_class = StandardResultsPagination


# ПОИСК МЕДИА-МАТЕРИАЛОВ
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def media_search_view(request):
    """Продвинутый поиск медиа-материалов"""
    serializer = MediaSearchSerializer(data=request.data if request.method == 'POST' else request.query_params)
    
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    data = serializer.validated_data
    queryset = MediaArticle.objects.filter(is_published=True)
    
    # Применяем фильтры
    if data.get('query'):
        query = data['query']
        queryset = queryset.filter(
            Q(title_ru__icontains=query) | Q(title_kg__icontains=query) | Q(title_en__icontains=query) |
            Q(description_ru__icontains=query) | Q(description_kg__icontains=query) | Q(description_en__icontains=query) |
            Q(content_ru__icontains=query) | Q(content_kg__icontains=query) | Q(content_en__icontains=query) |
            Q(keywords__icontains=query) | Q(journalist_name__icontains=query)
        )
    
    if data.get('category'):
        queryset = queryset.filter(category_id=data['category'])
    
    if data.get('outlet'):
        queryset = queryset.filter(outlet_id=data['outlet'])
    
    if data.get('sentiment'):
        queryset = queryset.filter(sentiment=data['sentiment'])
    
    if data.get('importance_score_min'):
        queryset = queryset.filter(importance_score__gte=data['importance_score_min'])
    
    if data.get('importance_score_max'):
        queryset = queryset.filter(importance_score__lte=data['importance_score_max'])
    
    if data.get('date_from'):
        queryset = queryset.filter(publication_date__gte=data['date_from'])
    
    if data.get('date_to'):
        queryset = queryset.filter(publication_date__lte=data['date_to'])
    
    if data.get('is_featured') is not None:
        queryset = queryset.filter(is_featured=data['is_featured'])
    
    if data.get('is_verified') is not None:
        queryset = queryset.filter(is_verified=data['is_verified'])
    
    # Применяем сортировку
    ordering = data.get('ordering', '-publication_date')
    queryset = queryset.order_by(ordering)
    
    # Применяем select_related и prefetch_related для оптимизации
    queryset = queryset.select_related('category', 'outlet').prefetch_related('tags')
    
    # Пагинация
    paginator = StandardResultsPagination()
    paginated_queryset = paginator.paginate_queryset(queryset, request)
    
    # Сериализация
    article_serializer = MediaArticleListSerializer(paginated_queryset, many=True)
    
    return paginator.get_paginated_response(article_serializer.data)


# ДАШБОРД МЕДИА-ПОКРЫТИЯ
@api_view(['GET'])
@permission_classes([AllowAny])
def media_dashboard_view(request):
    """Дашборд медиа-покрытия с общей статистикой"""
    
    try:
        # Общая статистика
        total_articles = MediaArticle.objects.filter(is_published=True).count()
        total_views = MediaArticle.objects.filter(is_published=True).aggregate(Sum('views_count'))['views_count__sum'] or 0
        total_outlets = MediaOutlet.objects.filter(is_active=True).count()
        total_categories = MediaCategory.objects.filter(is_active=True).count()
        
        # Статистика по категориям
        articles_by_category = {}
        categories = MediaCategory.objects.filter(is_active=True)
        for category in categories:
            count = MediaArticle.objects.filter(
                is_published=True, 
                category=category
            ).count()
            articles_by_category[category.name_ru] = count
        
        # Статистика по настроениям
        sentiment_stats = {}
        for sentiment in ['positive', 'neutral', 'negative']:
            count = MediaArticle.objects.filter(
                is_published=True,
                sentiment=sentiment
            ).count()
            sentiment_stats[sentiment] = count
        
        # Простые данные без сложных запросов для начала
        dashboard_data = {
            'total_articles': total_articles,
            'total_views': total_views,
            'total_outlets': total_outlets,
            'total_categories': total_categories,
            'articles_by_category': articles_by_category,
            'sentiment_stats': sentiment_stats,
            'top_outlets': [],
            'popular_tags': [],
            'recent_articles': [],
            'featured_articles': [],
        }
        
        return Response(dashboard_data)
    
    except Exception as e:
        return Response({'error': str(e)}, status=500)


# АНАЛИТИКА МЕДИА-ПОКРЫТИЯ
@api_view(['GET'])
@permission_classes([AllowAny])
def media_analytics_view(request):
    """Аналитика медиа-покрытия за период"""
    serializer = MediaAnalyticsSerializer(data=request.query_params)
    
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    data = serializer.validated_data
    period = data.get('period', 'month')
    
    # Определяем период для анализа
    end_date = data.get('end_date', timezone.now().date())
    
    if data.get('start_date'):
        start_date = data['start_date']
    else:
        if period == 'day':
            start_date = end_date - timedelta(days=7)
        elif period == 'week':
            start_date = end_date - timedelta(weeks=4)
        elif period == 'month':
            start_date = end_date - timedelta(days=180)
        elif period == 'quarter':
            start_date = end_date - timedelta(days=365)
        else:  # year
            start_date = end_date - timedelta(days=730)
    
    # Получаем статистику за период
    stats = MediaStatistics.objects.filter(
        date__gte=start_date,
        date__lte=end_date
    ).order_by('date')
    
    # Формируем данные временного ряда
    timeline_data = []
    for stat in stats:
        timeline_data.append({
            'date': stat.date,
            'total_articles': stat.total_articles,
            'total_views': stat.total_views,
            'total_reach': stat.total_reach,
            'positive_articles': stat.positive_articles,
            'neutral_articles': stat.neutral_articles,
            'negative_articles': stat.negative_articles
        })
    
    # Статистика по категориям за период
    category_distribution = MediaArticle.objects.filter(
        publication_date__gte=start_date,
        publication_date__lte=end_date,
        is_published=True
    ).values('category__name_ru').annotate(count=Count('id')).order_by('-count')
    
    category_dict = {item['category__name_ru']: item['count'] for item in category_distribution}
    
    # Тренды тональности
    sentiment_trends = MediaArticle.objects.filter(
        publication_date__gte=start_date,
        publication_date__lte=end_date,
        is_published=True
    ).aggregate(
        positive=Count(Case(When(sentiment='positive', then=1), output_field=IntegerField())),
        neutral=Count(Case(When(sentiment='neutral', then=1), output_field=IntegerField())),
        negative=Count(Case(When(sentiment='negative', then=1), output_field=IntegerField()))
    )
    
    # Производительность изданий
    outlet_performance = MediaOutlet.objects.filter(is_active=True).annotate(
        articles_count=Count('mediaarticle', filter=Q(
            mediaarticle__publication_date__gte=start_date,
            mediaarticle__publication_date__lte=end_date,
            mediaarticle__is_published=True
        )),
        avg_importance=Avg('mediaarticle__importance_score', filter=Q(
            mediaarticle__publication_date__gte=start_date,
            mediaarticle__publication_date__lte=end_date,
            mediaarticle__is_published=True
        )),
        total_views=Sum('mediaarticle__views_count', filter=Q(
            mediaarticle__publication_date__gte=start_date,
            mediaarticle__publication_date__lte=end_date,
            mediaarticle__is_published=True
        ))
    ).filter(articles_count__gt=0).order_by('-articles_count')[:10]
    
    outlet_performance_list = []
    for outlet in outlet_performance:
        outlet_performance_list.append({
            'name': outlet.name_ru,
            'articles_count': outlet.articles_count,
            'avg_importance': round(outlet.avg_importance or 0, 1),
            'total_views': outlet.total_views or 0
        })
    
    # Топ журналистов
    top_journalists = MediaArticle.objects.filter(
        publication_date__gte=start_date,
        publication_date__lte=end_date,
        is_published=True,
        journalist_name__isnull=False
    ).exclude(journalist_name='').values('journalist_name').annotate(
        articles_count=Count('id'),
        avg_importance=Avg('importance_score'),
        total_views=Sum('views_count')
    ).order_by('-articles_count')[:10]
    
    # Облако ключевых слов (топ-50)
    articles_with_keywords = MediaArticle.objects.filter(
        publication_date__gte=start_date,
        publication_date__lte=end_date,
        is_published=True,
        keywords__isnull=False
    ).exclude(keywords='').values_list('keywords', flat=True)
    
    keyword_counts = {}
    for keywords_str in articles_with_keywords:
        keywords = [k.strip() for k in keywords_str.split(',') if k.strip()]
        for keyword in keywords:
            keyword_counts[keyword] = keyword_counts.get(keyword, 0) + 1
    
    keyword_cloud = [
        {'keyword': k, 'count': v} 
        for k, v in sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)[:50]
    ]
    
    analytics_data = {
        'timeline_data': timeline_data,
        'category_distribution': category_dict,
        'sentiment_trends': sentiment_trends,
        'outlet_performance': outlet_performance_list,
        'top_journalists': list(top_journalists),
        'keyword_cloud': keyword_cloud
    }
    
    response_serializer = MediaAnalyticsSerializer(analytics_data)
    return Response(response_serializer.data)


# СТАТИСТИКА
class MediaStatisticsListView(generics.ListAPIView):
    """Список статистики медиа-покрытия"""
    queryset = MediaStatistics.objects.all().order_by('-date')
    serializer_class = MediaStatisticsSerializer
    permission_classes = [AllowAny]
    pagination_class = StandardResultsPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date']
