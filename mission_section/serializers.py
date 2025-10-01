from rest_framework import serializers
from .models import MissionSection, HistoryMilestone, Value, Priority, Achievement


class MissionSectionSerializer(serializers.ModelSerializer):
    """
    Сериализатор для основной секции миссии
    """
    
    class Meta:
        model = MissionSection
        fields = [
            'id', 'title', 'subtitle', 'mission_text',
            'vision_title', 'vision_text', 'approach_title', 'approach_text',
            'achievements_subtitle', 'impact_title', 'impact_text',
            'future_title', 'future_text', 'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class HistoryMilestoneSerializer(serializers.ModelSerializer):
    """
    Сериализатор для исторических вех
    """
    
    class Meta:
        model = HistoryMilestone
        fields = [
            'id', 'title', 'description', 'year', 'icon_class', 
            'order', 'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class ValueSerializer(serializers.ModelSerializer):
    """
    Сериализатор для ценностей
    """
    
    class Meta:
        model = Value
        fields = [
            'id', 'type', 'title', 'description', 'order',
            'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class PrioritySerializer(serializers.ModelSerializer):
    """
    Сериализатор для приоритетов
    """
    
    class Meta:
        model = Priority
        fields = [
            'id', 'text', 'icon_class', 'order',
            'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class AchievementSerializer(serializers.ModelSerializer):
    """
    Сериализатор для достижений
    """
    
    class Meta:
        model = Achievement
        fields = [
            'id', 'number', 'label', 'order',
            'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class MissionCompleteSerializer(serializers.Serializer):
    """
    Комплексный сериализатор для всех данных миссии
    Объединяет все модели в один ответ для фронтенда
    """
    
    mission = MissionSectionSerializer(read_only=True)
    history = HistoryMilestoneSerializer(many=True, read_only=True)
    values = ValueSerializer(many=True, read_only=True)
    priorities = PrioritySerializer(many=True, read_only=True)
    achievements = AchievementSerializer(many=True, read_only=True)
    
    def to_representation(self, instance):
        """
        Переопределяем метод для формирования правильной структуры данных
        """
        # instance должен быть словарем с ключами mission, history, values, priorities, achievements
        return {
            'mission': MissionSectionSerializer(instance.get('mission')).data if instance.get('mission') else None,
            'history': HistoryMilestoneSerializer(instance.get('history', []), many=True).data,
            'values': ValueSerializer(instance.get('values', []), many=True).data,
            'priorities': PrioritySerializer(instance.get('priorities', []), many=True).data,
            'achievements': AchievementSerializer(instance.get('achievements', []), many=True).data,
        }