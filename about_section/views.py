from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import (
    Partner, AboutSection, 
    OrganizationStructure, Achievement, UniversityStatistic, UniversityFounder
)
from .serializers import (
    PartnerSerializer, 
    PartnerListSerializer, 
    AboutSectionSerializer, 
    AboutSectionWithPartnersSerializer,
    OrganizationStructureSerializer,
    AchievementSerializer,
    UniversityStatisticSerializer,
    UniversityFounderSerializer,
    UniversityFounderListSerializer
)


class PartnerListView(generics.ListAPIView):
    """
    Get list of active partners
    Supports filtering and ordering
    """
    queryset = Partner.objects.filter(is_active=True)
    serializer_class = PartnerListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_active', 'color_theme']
    search_fields = ['name', 'name_en', 'name_ky', 'description']
    ordering_fields = ['order', 'name', 'created_at']
    ordering = ['order', 'name']


class PartnerDetailView(generics.RetrieveAPIView):
    """
    Get detailed information about a specific partner
    """
    queryset = Partner.objects.filter(is_active=True)
    serializer_class = PartnerSerializer
    lookup_field = 'id'


class AboutSectionListView(generics.ListAPIView):
    """
    Get list of active about sections
    """
    queryset = AboutSection.objects.filter(is_active=True)
    serializer_class = AboutSectionSerializer
    ordering = ['-created_at']


class AboutSectionDetailView(generics.RetrieveAPIView):
    """
    Get detailed information about a specific about section
    """
    queryset = AboutSection.objects.filter(is_active=True)
    serializer_class = AboutSectionSerializer
    lookup_field = 'id'


class AboutSectionWithPartnersView(generics.RetrieveAPIView):
    """
    Get about section with associated partners
    """
    queryset = AboutSection.objects.filter(is_active=True)
    serializer_class = AboutSectionWithPartnersSerializer
    lookup_field = 'id'


@api_view(['GET'])
def partners_for_frontend(request):
    """
    API endpoint optimized for the frontend Partners component
    Returns partners data in the exact format expected by the React component
    """
    try:
        # Get active partners ordered by order field
        partners = Partner.objects.filter(is_active=True).order_by('order', 'name')
        
        # Get language from request
        language = request.GET.get('lang', 'ru')
        if not language:
            accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
            if 'en' in accept_language:
                language = 'en'
            elif 'ky' in accept_language:
                language = 'ky'
        
        # Format data for frontend
        partners_data = []
        for partner in partners:
            # Generate nameKey similar to frontend format
            name_key = partner.name.lower().replace(' ', '_').replace('-', '_')
            
            partner_data = {
                'id': partner.id,
                'nameKey': f'partners.{name_key}',
                'icon': partner.icon,
                'color': partner.color_theme,
                'glow': partner.glow_effect,
                'name': partner.get_display_name(language),
                'description': partner.get_display_description(language),
                'website': partner.website,
                'logo': partner.logo.url if partner.logo else None,
                'email': partner.email,
                'phone': partner.phone,
                'country': partner.get_display_country(language),
                'city': partner.get_display_city(language),
                'address': partner.address,
                'latitude': float(partner.latitude) if partner.latitude else None,
                'longitude': float(partner.longitude) if partner.longitude else None,
                'partner_type': partner.partner_type,
                'established_year': partner.established_year,
                'cooperation_since': partner.cooperation_since,
                'partnership_areas': partner.partnership_areas,
                'order': partner.order
            }
            partners_data.append(partner_data)
        
        return Response({
            'success': True,
            'count': len(partners_data),
            'data': partners_data
        })
        
    except Exception as e:
        return Response({
            'success': False,
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def about_section_with_partners(request):
    """
    Get the main about section with all partners
    Optimized for the frontend Home page
    """
    try:
        # Get the first active about section (assuming there's usually just one main section)
        about_section = AboutSection.objects.filter(is_active=True).first()
        
        if not about_section:
            return Response({
                'success': False,
                'error': 'No active about section found'
            }, status=status.HTTP_404_NOT_FOUND)
        
        # Get language from request
        language = request.GET.get('lang', 'ru')
        if not language:
            accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
            if 'en' in accept_language:
                language = 'en'
            elif 'ky' in accept_language:
                language = 'ky'
        
        # Format about section data
        about_data = {
            'id': about_section.id,
            'title': about_section.get_display_title(language),
            'subtitle': about_section.get_display_subtitle(language),
            'content': about_section.get_display_content(language),
            'show_partners': about_section.show_partners,
            'partners_animation_speed': about_section.partners_animation_speed
        }
        
        # Add partners if enabled
        partners_data = []
        if about_section.show_partners:
            partners = Partner.objects.filter(is_active=True).order_by('order', 'name')
            
            for partner in partners:
                name_key = partner.name.lower().replace(' ', '_').replace('-', '_')
                
                partner_data = {
                    'id': partner.id,
                    'nameKey': f'partners.{name_key}',
                    'icon': partner.icon,
                    'color': partner.color_theme,
                    'glow': partner.glow_effect,
                    'name': partner.get_display_name(language),
                    'description': partner.get_display_description(language),
                    'website': partner.website,
                    'logo': partner.logo.url if partner.logo else None,
                    'order': partner.order
                }
                partners_data.append(partner_data)
        
        return Response({
            'success': True,
            'about_section': about_data,
            'partners': partners_data,
            'partners_count': len(partners_data)
        })
        
    except Exception as e:
        return Response({
            'success': False,
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def partners_stats(request):
    """
    Get statistics about partners
    """
    try:
        total_partners = Partner.objects.count()
        active_partners = Partner.objects.filter(is_active=True).count()
        inactive_partners = total_partners - active_partners
        
        return Response({
            'success': True,
            'stats': {
                'total_partners': total_partners,
                'active_partners': active_partners,
                'inactive_partners': inactive_partners
            }
        })
        
    except Exception as e:
        return Response({
            'success': False,
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Organization Structure Views
class OrganizationStructureListView(generics.ListAPIView):
    """
    Get list of active organizational structures with multilingual support
    """
    queryset = OrganizationStructure.objects.filter(is_active=True, parent__isnull=True)
    serializer_class = OrganizationStructureSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['structure_type', 'is_active']
    ordering_fields = ['structure_type', 'order', 'name_ru']
    ordering = ['structure_type', 'order', 'name_ru']


@api_view(['GET'])
def structure_for_frontend(request):
    """
    API endpoint optimized for the frontend Structure component
    Returns structure data in the exact format expected by the React component
    """
    try:
        # Get language from request
        language = request.GET.get('lang', 'ru')
        if not language:
            accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
            if 'en' in accept_language:
                language = 'en'
            elif 'ky' in accept_language:
                language = 'ky'
        
        # Get structure type filter
        structure_type = request.GET.get('type', None)
        
        # Build queryset
        queryset = OrganizationStructure.objects.filter(is_active=True, parent__isnull=True)
        if structure_type:
            queryset = queryset.filter(structure_type=structure_type)
        
        structures = queryset.order_by('structure_type', 'order')
        
        # Group by structure type
        structure_data = {}
        
        for structure in structures:
            # Get structure type key for grouping
            type_key = structure.structure_type
            
            if type_key not in structure_data:
                # Map structure types to display names
                type_display_mapping = {
                    'leadership': {
                        'ru': 'Руководство',
                        'en': 'Leadership', 
                        'ky': 'Жетекчилик'
                    },
                    'faculties': {
                        'ru': 'Факультеты',
                        'en': 'Faculties',
                        'ky': 'Факультеттер'
                    },
                    'administrative': {
                        'ru': 'Административные подразделения',
                        'en': 'Administrative Departments',
                        'ky': 'Администрациялык бөлүмдөр'
                    },
                    'support': {
                        'ru': 'Вспомогательные подразделения',
                        'en': 'Support Departments',
                        'ky': 'Жардамчы бөлүмдөр'
                    }
                }
                
                title = type_display_mapping.get(type_key, {}).get(language, type_key)
                
                structure_data[type_key] = {
                    'title': title,
                    'icon': structure.icon,
                    'items': []
                }
            
            # Get child departments
            children = structure.children.filter(is_active=True).order_by('order')
            departments = [child.get_display_name(language) for child in children]
            
            item_data = {
                'name': structure.get_display_name(language),
                'head': structure.get_display_head_name(language),
                'phone': structure.phone,
                'email': structure.email,
                'departments': departments
            }
            
            structure_data[type_key]['items'].append(item_data)
        
        return Response({
            'success': True,
            'data': structure_data,
            'language': language
        })
        
    except Exception as e:
        print(f"Error in structure_for_frontend: {str(e)}")
        return Response({
            'success': False,
            'error': str(e),
            'data': {}
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Achievement Views
class AchievementListView(generics.ListAPIView):
    """
    Get list of active achievements with multilingual support
    """
    queryset = Achievement.objects.filter(is_active=True)
    serializer_class = AchievementSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['category', 'featured', 'year', 'is_active']
    ordering_fields = ['year', 'order', 'featured']
    ordering = ['-featured', '-year', 'order']


@api_view(['GET'])
def achievements_for_frontend(request):
    """
    API endpoint optimized for the frontend Achievements component
    Returns achievements data in the exact format expected by the React component
    """
    try:
        # Get active achievements ordered by featured, year, and order
        achievements = Achievement.objects.filter(is_active=True).order_by('-featured', '-year', 'order')
        
        # Get language from request
        language = request.GET.get('lang', 'ru')
        if not language:
            accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
            if 'en' in accept_language:
                language = 'en'
            elif 'ky' in accept_language:
                language = 'ky'
        
        # Get category filter
        category = request.GET.get('category', 'all')
        if category != 'all':
            achievements = achievements.filter(category=category)
        
        # Format data for frontend
        achievements_data = []
        for achievement in achievements:
            achievement_data = {
                'id': achievement.id,
                'title': achievement.get_display_title(language),
                'description': achievement.get_display_description(language),
                'year': str(achievement.year),
                'category': achievement.category,
                'icon': achievement.icon,
                'iconColor': achievement.icon_color,
                'featured': achievement.featured
            }
            
            achievements_data.append(achievement_data)
        
        return Response({
            'success': True,
            'data': achievements_data,
            'count': len(achievements_data),
            'language': language
        })
        
    except Exception as e:
        print(f"Error in achievements_for_frontend: {str(e)}")
        return Response({
            'success': False,
            'error': str(e),
            'data': []
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Statistics Views
class UniversityStatisticListView(generics.ListAPIView):
    """
    Get list of active university statistics with multilingual support
    """
    queryset = UniversityStatistic.objects.filter(is_active=True)
    serializer_class = UniversityStatisticSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['order', 'name_ru']
    ordering = ['order', 'name_ru']


@api_view(['GET'])
def statistics_for_frontend(request):
    """
    API endpoint optimized for the frontend Statistics component
    Returns statistics data in the exact format expected by the React component
    """
    try:
        # Get active statistics ordered by order field
        statistics = UniversityStatistic.objects.filter(is_active=True).order_by('order', 'name_ru')
        
        # Get language from request
        language = request.GET.get('lang', 'ru')
        if not language:
            accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
            if 'en' in accept_language:
                language = 'en'
            elif 'ky' in accept_language:
                language = 'ky'
        
        # Format data for frontend
        statistics_data = []
        for stat in statistics:
            stat_data = {
                'id': stat.id,
                'name': stat.get_display_name(language),
                'value': stat.value,
                'unit': stat.unit,
                'icon': stat.icon
            }
            
            statistics_data.append(stat_data)
        
        return Response({
            'success': True,
            'data': statistics_data,
            'count': len(statistics_data),
            'language': language
        })
        
    except Exception as e:
        print(f"Error in statistics_for_frontend: {str(e)}")
        return Response({
            'success': False,
            'error': str(e),
            'data': []
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UniversityFounderListView(generics.ListAPIView):
    """
    Get list of active university founders
    Supports filtering and ordering
    """
    queryset = UniversityFounder.objects.filter(is_active=True)
    serializer_class = UniversityFounderListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_active']
    search_fields = ['name_ru', 'name_en', 'name_ky', 'position_ru', 'description_ru']
    ordering_fields = ['order', 'name_ru', 'created_at']
    ordering = ['order', 'name_ru']


class UniversityFounderDetailView(generics.RetrieveAPIView):
    """
    Get detailed information about a specific university founder
    """
    queryset = UniversityFounder.objects.filter(is_active=True)
    serializer_class = UniversityFounderSerializer
    lookup_field = 'id'


@api_view(['GET'])
def founders_for_frontend(request):
    """
    API endpoint optimized for the frontend Founders component
    Returns founders data in the exact format expected by the React component
    """
    try:
        # Get active founders ordered by order field
        founders = UniversityFounder.objects.filter(is_active=True).order_by('order', 'name_ru')
        
        # Get language from request
        language = request.GET.get('lang', 'ru')
        if not language:
            accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'ru')
            if 'en' in accept_language:
                language = 'en'
            elif 'ky' in accept_language:
                language = 'ky'
        
        # Format data for frontend
        founders_data = []
        for founder in founders:
            founder_data = {
                'id': founder.id,
                'name': founder.get_name(language),
                'position': founder.get_position(language),
                'years': founder.get_years(language),
                'image': founder.image.url if founder.image else "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=400&h=400&fit=crop&crop=face",
                'description': founder.get_description(language),
                'achievements': founder.get_achievements(language),
                'order': founder.order
            }
            founders_data.append(founder_data)
        
        return Response({
            'success': True,
            'count': len(founders_data),
            'data': founders_data
        })
        
    except Exception as e:
        print(f"Error in founders_for_frontend: {str(e)}")
        return Response({
            'success': False,
            'error': str(e),
            'data': []
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
