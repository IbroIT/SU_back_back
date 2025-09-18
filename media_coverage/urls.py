from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'media_coverage'

urlpatterns = [
    # КАТЕГОРИИ МЕДИА
    path('categories/', views.MediaCategoryListView.as_view(), name='category-list'),
    path('categories/<slug:slug>/', views.MediaCategoryDetailView.as_view(), name='category-detail'),
    
    # МЕДИА-ИЗДАНИЯ
    path('outlets/', views.MediaOutletListView.as_view(), name='outlet-list'),
    path('outlets/<slug:slug>/', views.MediaOutletDetailView.as_view(), name='outlet-detail'),
    
    # ТЕГИ МЕДИА
    path('tags/', views.MediaTagListView.as_view(), name='tag-list'),
    path('tags/<slug:slug>/', views.MediaTagDetailView.as_view(), name='tag-detail'),
    
    # МЕДИА-ПУБЛИКАЦИИ
    path('articles/', views.MediaArticleListView.as_view(), name='article-list'),
    path('articles/<slug:slug>/', views.MediaArticleDetailView.as_view(), name='article-detail'),
    
    # СПЕЦИАЛЬНЫЕ КОЛЛЕКЦИИ ПУБЛИКАЦИЙ
    path('articles/featured/', views.FeaturedMediaArticlesView.as_view(), name='featured-articles'),
    path('articles/popular/', views.PopularMediaArticlesView.as_view(), name='popular-articles'),
    path('articles/recent/', views.RecentMediaArticlesView.as_view(), name='recent-articles'),
    
    # ПОИСК И АНАЛИТИКА
    path('search/', views.media_search_view, name='search'),
    path('dashboard/', views.media_dashboard_view, name='dashboard'),
    path('analytics/', views.media_analytics_view, name='analytics'),
    
    # СТАТИСТИКА
    path('statistics/', views.MediaStatisticsListView.as_view(), name='statistics-list'),
]
