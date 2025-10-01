from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MissionSectionViewSet, HistoryMilestoneViewSet, 
    ValueViewSet, PriorityViewSet, AchievementViewSet,
    MissionCompleteViewSet
)

# Создаем роутер для DRF ViewSets
router = DefaultRouter()

# Регистрируем ViewSets с роутером
router.register(r'mission-sections', MissionSectionViewSet, basename='mission-section')
router.register(r'history', HistoryMilestoneViewSet, basename='history-milestone')
router.register(r'values', ValueViewSet, basename='value')
router.register(r'priorities', PriorityViewSet, basename='priority')
router.register(r'achievements', AchievementViewSet, basename='achievement')
router.register(r'complete', MissionCompleteViewSet, basename='mission-complete')

app_name = 'mission_section'

urlpatterns = [
    # API endpoints через роутер
    path('api/', include(router.urls)),
    
    # Дополнительные специальные endpoints можно добавить здесь
    # path('api/mission/summary/', views.mission_summary, name='mission-summary'),
]