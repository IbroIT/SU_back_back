from rest_framework import serializers
from .models import (
    Partner, AboutSection, Founder, FounderAchievement,
    OrganizationStructure, Achievement, UniversityStatistic
)


class PartnerSerializer(serializers.ModelSerializer):
    """Serializer for Partner model with multilingual support"""
    
    # Computed fields for frontend compatibility
    nameKey = serializers.SerializerMethodField()
    color = serializers.CharField(source='color_theme')
    glow = serializers.CharField(source='glow_effect')
    display_name = serializers.SerializerMethodField()
    display_description = serializers.SerializerMethodField()
    display_country = serializers.SerializerMethodField()
    display_city = serializers.SerializerMethodField()
    
    class Meta:
        model = Partner
        fields = [
            'id', 'name', 'name_en', 'name_ky', 'nameKey', 'display_name',
            'icon', 'logo', 'website', 
            'description', 'description_en', 'description_ky', 'display_description',
            'email', 'phone', 
            'country', 'country_en', 'country_ky', 'display_country',
            'city', 'city_en', 'city_ky', 'display_city',
            'address', 'latitude', 'longitude',
            'partner_type', 'established_year', 'cooperation_since', 'partnership_areas',
            'color_theme', 'color', 'glow_effect', 'glow',
            'is_active', 'order', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'nameKey', 'color', 'glow',
                           'display_name', 'display_description', 'display_country', 'display_city']
    
    def get_nameKey(self, obj):
        """Generate a nameKey for frontend compatibility"""
        # Convert name to a key format similar to the frontend
        name_key = obj.name.lower()
        name_key = name_key.replace(' ', '_')
        name_key = name_key.replace('-', '_')
        return f'partners.{name_key}'
    
    def get_display_name(self, obj):
        """Get display name based on request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_name(language)
    
    def get_display_description(self, obj):
        """Get display description based on request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_description(language)
    
    def get_display_country(self, obj):
        """Get display country based on request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_country(language)
    
    def get_display_city(self, obj):
        """Get display city based on request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_city(language)
    
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
                elif 'ky' in accept_language:
                    language = 'ky'
        
        return language


class PartnerListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for partner list views"""
    
    nameKey = serializers.SerializerMethodField()
    color = serializers.CharField(source='color_theme')
    glow = serializers.CharField(source='glow_effect')
    display_name = serializers.SerializerMethodField()
    display_description = serializers.SerializerMethodField()
    display_country = serializers.SerializerMethodField()
    display_city = serializers.SerializerMethodField()
    
    class Meta:
        model = Partner
        fields = [
            'id', 'nameKey', 'icon', 'logo', 'color', 'glow', 
            'name', 'display_name', 'description', 'display_description',
            'country', 'display_country', 'city', 'display_city',
            'address', 'latitude', 'longitude', 'partner_type',
            'email', 'phone', 'website', 'established_year', 
            'cooperation_since', 'partnership_areas', 'order'
        ]
    
    def get_nameKey(self, obj):
        """Generate a nameKey for frontend compatibility"""
        name_key = obj.name.lower()
        name_key = name_key.replace(' ', '_')
        name_key = name_key.replace('-', '_')
        return f'partners.{name_key}'
    
    def get_display_name(self, obj):
        """Get display name based on request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_name(language)
    
    def get_display_description(self, obj):
        """Get display description based on request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_description(language)
    
    def get_display_country(self, obj):
        """Get display country based on request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_country(language)
    
    def get_display_city(self, obj):
        """Get display city based on request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_city(language)
    
    def _get_language(self, request):
        """Extract language from request"""
        language = 'ru'  # default
        
        if request:
            language = request.GET.get('lang', 'ru')
            if not request.GET.get('lang'):
                accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
                if 'en' in accept_language:
                    language = 'en'
                elif 'ky' in accept_language:
                    language = 'ky'
        
        return language


class AboutSectionSerializer(serializers.ModelSerializer):
    """Serializer for AboutSection model with multilingual support"""
    
    display_title = serializers.SerializerMethodField()
    display_subtitle = serializers.SerializerMethodField()
    display_content = serializers.SerializerMethodField()
    
    class Meta:
        model = AboutSection
        fields = [
            'id', 'title', 'title_en', 'title_ky', 'display_title',
            'subtitle', 'subtitle_en', 'subtitle_ky', 'display_subtitle',
            'content', 'content_en', 'content_ky', 'display_content',
            'is_active', 'show_partners', 'partners_animation_speed',
            'created_at', 'updated_at'
        ]
        read_only_fields = [
            'id', 'created_at', 'updated_at', 
            'display_title', 'display_subtitle', 'display_content'
        ]
    
    def get_display_title(self, obj):
        """Get title in request language"""
        request = self.context.get('request')
        language = 'ru'
        
        if request:
            language = request.GET.get('lang', 'ru')
            if not request.GET.get('lang'):
                accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
                if 'en' in accept_language:
                    language = 'en'
                elif 'ky' in accept_language:
                    language = 'ky'
        
        return obj.get_display_title(language)
    
    def get_display_subtitle(self, obj):
        """Get subtitle in request language"""
        request = self.context.get('request')
        language = 'ru'
        
        if request:
            language = request.GET.get('lang', 'ru')
            if not request.GET.get('lang'):
                accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
                if 'en' in accept_language:
                    language = 'en'
                elif 'ky' in accept_language:
                    language = 'ky'
        
        return obj.get_display_subtitle(language)
    
    def get_display_content(self, obj):
        """Get content in request language"""
        request = self.context.get('request')
        language = 'ru'
        
        if request:
            language = request.GET.get('lang', 'ru')
            if not request.GET.get('lang'):
                accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
                if 'en' in accept_language:
                    language = 'en'
                elif 'ky' in accept_language:
                    language = 'ky'
        
        return obj.get_display_content(language)


class AboutSectionWithPartnersSerializer(AboutSectionSerializer):
    """Extended serializer that includes partners data"""
    
    partners = serializers.SerializerMethodField()
    
    class Meta(AboutSectionSerializer.Meta):
        fields = AboutSectionSerializer.Meta.fields + ['partners']
    
    def get_partners(self, obj):
        """Get active partners ordered by order field"""
        if obj.show_partners:
            partners = Partner.objects.filter(is_active=True).order_by('order', 'name')
            serializer = PartnerListSerializer(
                partners, 
                many=True, 
                context=self.context
            )
            return serializer.data
        return []


class FounderAchievementSerializer(serializers.ModelSerializer):
    """Serializer for FounderAchievement model"""
    
    achievement = serializers.SerializerMethodField()
    
    class Meta:
        model = FounderAchievement
        fields = ['id', 'achievement', 'order', 'achievement_ru', 'achievement_en', 'achievement_ky']
    
    def get_achievement(self, obj):
        """Get achievement in request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_achievement(language)
    
    def _get_language(self, request):
        """Extract language from request"""
        language = 'ru'
        if request:
            language = request.GET.get('lang', 'ru')
            if not request.GET.get('lang'):
                accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
                if 'en' in accept_language:
                    language = 'en'
                elif 'ky' in accept_language:
                    language = 'ky'
        return language


class FounderSerializer(serializers.ModelSerializer):
    """Serializer for Founder model with multilingual support"""
    
    name = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    achievements = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Founder
        fields = [
            'id', 'name', 'name_ru', 'name_en', 'name_ky',
            'position', 'position_ru', 'position_en', 'position_ky',
            'years', 'image', 'image_url',
            'description', 'description_ru', 'description_en', 'description_ky',
            'achievements', 'order', 'is_active'
        ]
        read_only_fields = ['id', 'name', 'position', 'description', 'achievements', 'image_url']
    
    def get_name(self, obj):
        """Get name in request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_name(language)
    
    def get_position(self, obj):
        """Get position in request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_position(language)
    
    def get_description(self, obj):
        """Get description in request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_description(language)
    
    def get_achievements(self, obj):
        """Get achievements in request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        
        # First try to get from related achievement objects
        achievement_objects = obj.achievement_set.all().order_by('order')
        if achievement_objects.exists():
            return [ach.get_display_achievement(language) for ach in achievement_objects]
        
        # Fallback to JSON field
        return obj.get_achievements_for_language(language)
    
    def get_image_url(self, obj):
        """Get full URL for image"""
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None
    
    def _get_language(self, request):
        """Extract language from request"""
        language = 'ru'
        if request:
            language = request.GET.get('lang', 'ru')
            if not request.GET.get('lang'):
                accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
                if 'en' in accept_language:
                    language = 'en'
                elif 'ky' in accept_language:
                    language = 'ky'
        return language


class OrganizationStructureSerializer(serializers.ModelSerializer):
    """Serializer for OrganizationStructure model with multilingual support"""
    
    name = serializers.SerializerMethodField()
    head_name = serializers.SerializerMethodField()
    children = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    
    class Meta:
        model = OrganizationStructure
        fields = [
            'id', 'name', 'name_ru', 'name_en', 'name_ky',
            'head_name', 'head_name_ru', 'head_name_en', 'head_name_ky',
            'structure_type', 'phone', 'email', 'icon', 
            'parent', 'children', 'order', 'is_active', 'title'
        ]
        read_only_fields = ['id', 'name', 'head_name', 'children', 'title']
    
    def get_name(self, obj):
        """Get name in request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_name(language)
    
    def get_head_name(self, obj):
        """Get head name in request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_head_name(language)
    
    def get_title(self, obj):
        """Get title for the structure type"""
        return obj.get_structure_type_display()
    
    def get_children(self, obj):
        """Get child departments"""
        children = obj.children.filter(is_active=True).order_by('order')
        if children.exists():
            serializer = OrganizationStructureSerializer(
                children, 
                many=True, 
                context=self.context
            )
            return serializer.data
        return []
    
    def _get_language(self, request):
        """Extract language from request"""
        language = 'ru'
        if request:
            language = request.GET.get('lang', 'ru')
            if not request.GET.get('lang'):
                accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
                if 'en' in accept_language:
                    language = 'en'
                elif 'ky' in accept_language:
                    language = 'ky'
        return language


class AchievementSerializer(serializers.ModelSerializer):
    """Serializer for Achievement model with multilingual support"""
    
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    
    class Meta:
        model = Achievement
        fields = [
            'id', 'title', 'title_ru', 'title_en', 'title_ky',
            'description', 'description_ru', 'description_en', 'description_ky',
            'year', 'category', 'icon', 'icon_color', 'featured', 
            'order', 'is_active'
        ]
        read_only_fields = ['id', 'title', 'description']
    
    def get_title(self, obj):
        """Get title in request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_title(language)
    
    def get_description(self, obj):
        """Get description in request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_description(language)
    
    def _get_language(self, request):
        """Extract language from request"""
        language = 'ru'
        if request:
            language = request.GET.get('lang', 'ru')
            if not request.GET.get('lang'):
                accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
                if 'en' in accept_language:
                    language = 'en'
                elif 'ky' in accept_language:
                    language = 'ky'
        return language


class UniversityStatisticSerializer(serializers.ModelSerializer):
    """Serializer for UniversityStatistic model with multilingual support"""
    
    name = serializers.SerializerMethodField()
    
    class Meta:
        model = UniversityStatistic
        fields = [
            'id', 'name', 'name_ru', 'name_en', 'name_ky',
            'value', 'unit', 'icon', 'order', 'is_active'
        ]
        read_only_fields = ['id', 'name']
    
    def get_name(self, obj):
        """Get name in request language"""
        request = self.context.get('request')
        language = self._get_language(request)
        return obj.get_display_name(language)
    
    def _get_language(self, request):
        """Extract language from request"""
        language = 'ru'
        if request:
            language = request.GET.get('lang', 'ru')
            if not request.GET.get('lang'):
                accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
                if 'en' in accept_language:
                    language = 'en'
                elif 'ky' in accept_language:
                    language = 'ky'
        return language
