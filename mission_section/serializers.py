from rest_framework import serializers
from .models import MissionSection, HistoryMilestone, Value, Priority, Achievement


class MissionSectionSerializer(serializers.ModelSerializer):
    """
    Сериализатор для основной секции миссии с поддержкой мультиязычности
    """
    
    # Display fields based on language
    display_title = serializers.SerializerMethodField()
    display_subtitle = serializers.SerializerMethodField()
    display_mission_text = serializers.SerializerMethodField()
    display_vision_title = serializers.SerializerMethodField()
    display_vision_text = serializers.SerializerMethodField()
    display_approach_title = serializers.SerializerMethodField()
    display_approach_text = serializers.SerializerMethodField()
    display_achievements_subtitle = serializers.SerializerMethodField()
    display_impact_title = serializers.SerializerMethodField()
    display_impact_text = serializers.SerializerMethodField()
    display_future_title = serializers.SerializerMethodField()
    display_future_text = serializers.SerializerMethodField()
    
    class Meta:
        model = MissionSection
        fields = [
            'id', 'title', 'subtitle', 'mission_text',
            'title_en', 'subtitle_en', 'mission_text_en',
            'title_ky', 'subtitle_ky', 'mission_text_ky',
            'vision_title', 'vision_text', 'approach_title', 'approach_text',
            'vision_title_en', 'vision_text_en', 'approach_title_en', 'approach_text_en',
            'vision_title_ky', 'vision_text_ky', 'approach_title_ky', 'approach_text_ky',
            'achievements_subtitle', 'impact_title', 'impact_text',
            'achievements_subtitle_en', 'impact_title_en', 'impact_text_en',
            'achievements_subtitle_ky', 'impact_title_ky', 'impact_text_ky',
            'future_title', 'future_text',
            'future_title_en', 'future_text_en',
            'future_title_ky', 'future_text_ky',
            'display_title', 'display_subtitle', 'display_mission_text',
            'display_vision_title', 'display_vision_text',
            'display_approach_title', 'display_approach_text',
            'display_achievements_subtitle', 'display_impact_title', 'display_impact_text',
            'display_future_title', 'display_future_text',
            'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'display_title', 'display_subtitle', 
                           'display_mission_text', 'display_vision_title', 'display_vision_text',
                           'display_approach_title', 'display_approach_text', 'display_achievements_subtitle',
                           'display_impact_title', 'display_impact_text', 'display_future_title', 'display_future_text']

    def _get_language(self, request):
        """Extract language from request"""
        language = 'ru'  # default
        
        if request:
            language = request.GET.get('lang', 'ru')
            # Also check Accept-Language header
            if not request.GET.get('lang'):
                accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
                if 'en' in accept_language:
                    language = 'en'
                elif 'kg' in accept_language or 'ky' in accept_language:
                    language = 'ky'
        
        return language

    def get_display_title(self, obj):
        """Get display title based on request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_title(language)

    def get_display_subtitle(self, obj):
        """Get display subtitle based on request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_subtitle(language)

    def get_display_mission_text(self, obj):
        """Get display mission text based on request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_mission_text(language)

    def get_display_vision_title(self, obj):
        """Get display vision title based on request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_vision_title(language)

    def get_display_vision_text(self, obj):
        """Get display vision text based on request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_vision_text(language)

    def get_display_approach_title(self, obj):
        """Get display approach title based on request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_approach_title(language)

    def get_display_approach_text(self, obj):
        """Get display approach text based on request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_approach_text(language)

    def get_display_achievements_subtitle(self, obj):
        """Get display achievements subtitle based on request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_achievements_subtitle(language)

    def get_display_impact_title(self, obj):
        """Get display impact title based on request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_impact_title(language)

    def get_display_impact_text(self, obj):
        """Get display impact text based on request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_impact_text(language)

    def get_display_future_title(self, obj):
        """Get display future title based on request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_future_title(language)

    def get_display_future_text(self, obj):
        """Get display future text based on request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_future_text(language)


class HistoryMilestoneSerializer(serializers.ModelSerializer):
    """
    Сериализатор для исторических вех с поддержкой мультиязычности
    """
    
    # Display fields based on language
    display_title = serializers.SerializerMethodField()
    display_description = serializers.SerializerMethodField()
    
    class Meta:
        model = HistoryMilestone
        fields = [
            'id', 'title', 'description', 'title_en', 'description_en', 
            'title_ky', 'description_ky', 'year', 'icon_class', 
            'display_title', 'display_description',
            'order', 'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'display_title', 'display_description']

    def _get_language(self, request):
        """Extract language from request"""
        language = 'ru'  # default
        
        if request:
            language = request.GET.get('lang', 'ru')
            # Also check Accept-Language header
            if not request.GET.get('lang'):
                accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
                if 'en' in accept_language:
                    language = 'en'
                elif 'kg' in accept_language or 'ky' in accept_language:
                    language = 'ky'
        
        return language

    def get_display_title(self, obj):
        """Get display title based on request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_title(language)

    def get_display_description(self, obj):
        """Get display description based on request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_description(language)


class ValueSerializer(serializers.ModelSerializer):
    """
    Сериализатор для ценностей с поддержкой мультиязычности
    """
    
    # Display fields based on language
    display_title = serializers.SerializerMethodField()
    display_description = serializers.SerializerMethodField()
    
    class Meta:
        model = Value
        fields = [
            'id', 'type', 'title', 'description', 'title_en', 'description_en',
            'title_ky', 'description_ky', 'display_title', 'display_description',
            'order', 'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'display_title', 'display_description']

    def _get_language(self, request):
        """Extract language from request"""
        language = 'ru'  # default
        
        if request:
            language = request.GET.get('lang', 'ru')
            # Also check Accept-Language header
            if not request.GET.get('lang'):
                accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
                if 'en' in accept_language:
                    language = 'en'
                elif 'kg' in accept_language or 'ky' in accept_language:
                    language = 'ky'
        
        return language

    def get_display_title(self, obj):
        """Get display title based on request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_title(language)

    def get_display_description(self, obj):
        """Get display description based on request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_description(language)


class PrioritySerializer(serializers.ModelSerializer):
    """
    Сериализатор для приоритетов с поддержкой мультиязычности
    """
    
    # Display fields based on language
    display_text = serializers.SerializerMethodField()
    
    class Meta:
        model = Priority
        fields = [
            'id', 'text', 'text_en', 'text_ky', 'display_text',
            'icon_class', 'order', 'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'display_text']

    def _get_language(self, request):
        """Extract language from request"""
        language = 'ru'  # default
        
        if request:
            language = request.GET.get('lang', 'ru')
            # Also check Accept-Language header
            if not request.GET.get('lang'):
                accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
                if 'en' in accept_language:
                    language = 'en'
                elif 'kg' in accept_language or 'ky' in accept_language:
                    language = 'ky'
        
        return language

    def get_display_text(self, obj):
        """Get display text based on request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_text(language)


class AchievementSerializer(serializers.ModelSerializer):
    """
    Сериализатор для достижений с поддержкой мультиязычности
    """
    
    # Display fields based on language
    display_label = serializers.SerializerMethodField()
    
    class Meta:
        model = Achievement
        fields = [
            'id', 'number', 'label', 'label_en', 'label_ky', 'display_label',
            'order', 'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'display_label']

    def _get_language(self, request):
        """Extract language from request"""
        language = 'ru'  # default
        
        if request:
            language = request.GET.get('lang', 'ru')
            # Also check Accept-Language header
            if not request.GET.get('lang'):
                accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
                if 'en' in accept_language:
                    language = 'en'
                elif 'kg' in accept_language or 'ky' in accept_language:
                    language = 'ky'
        
        return language

    def get_display_label(self, obj):
        """Get display label based on request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_label(language)


class MissionCompleteSerializer(serializers.Serializer):
    """
    Комплексный сериализатор для всех данных миссии
    Объединяет все модели в один ответ для фронтенда с поддержкой мультиязычности
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
        # Передаем контекст запроса во все сериализаторы
        context = self.context
        
        # instance должен быть словарем с ключами mission, history, values, priorities, achievements
        return {
            'mission': MissionSectionSerializer(instance.get('mission'), context=context).data if instance.get('mission') else None,
            'history': HistoryMilestoneSerializer(instance.get('history', []), many=True, context=context).data,
            'values': ValueSerializer(instance.get('values', []), many=True, context=context).data,
            'priorities': PrioritySerializer(instance.get('priorities', []), many=True, context=context).data,
            'achievements': AchievementSerializer(instance.get('achievements', []), many=True, context=context).data,
        }