from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Partner, AboutSection
from .serializers import (
    PartnerSerializer, 
    PartnerListSerializer, 
    AboutSectionSerializer, 
    AboutSectionWithPartnersSerializer
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
