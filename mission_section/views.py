from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.utils.translation import get_language

from .models import MissionSection, HistoryMilestone, Value, Priority, Achievement
from .serializers import (
    MissionSectionSerializer, HistoryMilestoneSerializer, 
    ValueSerializer, PrioritySerializer, AchievementSerializer,
    MissionCompleteSerializer
)


class MissionSectionViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления секциями миссии
    """
    queryset = MissionSection.objects.filter(is_active=True)
    serializer_class = MissionSectionSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['is_active']
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']


class HistoryMilestoneViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления историческими вехами
    """
    queryset = HistoryMilestone.objects.filter(is_active=True)
    serializer_class = HistoryMilestoneSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['is_active', 'year']
    ordering_fields = ['order', 'year', 'created_at']
    ordering = ['order', 'year']


class ValueViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления ценностями
    """
    queryset = Value.objects.filter(is_active=True)
    serializer_class = ValueSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['is_active', 'type']
    ordering_fields = ['order', 'type', 'created_at']
    ordering = ['order']


class PriorityViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления приоритетами
    """
    queryset = Priority.objects.filter(is_active=True)
    serializer_class = PrioritySerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['is_active']
    ordering_fields = ['order', 'created_at']
    ordering = ['order']


class AchievementViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления достижениями
    """
    queryset = Achievement.objects.filter(is_active=True)
    serializer_class = AchievementSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['is_active']
    ordering_fields = ['order', 'created_at']
    ordering = ['order']


class MissionCompleteViewSet(viewsets.ViewSet):
    """
    Специальный ViewSet для получения всех данных миссии одним запросом
    Идеально подходит для фронтенда
    """
    
    @action(detail=False, methods=['get'])
    def complete_data(self, request):
        """
        Возвращает все данные миссии в одном ответе
        GET /api/mission/complete_data/
        """
        try:
            # Получаем основную секцию миссии (берем первую активную)
            mission = MissionSection.objects.filter(is_active=True).first()
            
            # Получаем все связанные данные
            history = HistoryMilestone.objects.filter(is_active=True).order_by('order', 'year')
            values = Value.objects.filter(is_active=True).order_by('order')
            priorities = Priority.objects.filter(is_active=True).order_by('order')
            achievements = Achievement.objects.filter(is_active=True).order_by('order')
            
            # Формируем данные для сериализатора
            data = {
                'mission': mission,
                'history': history,
                'values': values,
                'priorities': priorities,
                'achievements': achievements,
            }
            
            # Сериализуем данные
            serializer = MissionCompleteSerializer(data)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {'error': f'Ошибка при получении данных: {str(e)}'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def list(self, request):
        """
        Альтернативный endpoint для получения всех данных
        GET /api/mission/
        """
        return self.complete_data(request)
