from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.http import HttpResponse, Http404, FileResponse
from django.utils.encoding import force_str
import os
import mimetypes
from .models import (
    PartnerOrganization, StudentAppeal, PhotoAlbum, Photo, 
    VideoContent, StudentLifeStatistic, InternshipRequirement, ReportTemplate,
    StudentGuide, GuideRequirement, GuideStep, GuideStepDetail
)
from .serializers import (
    PartnerOrganizationSerializer, StudentAppealSerializer,
    PhotoAlbumSerializer, PhotoSerializer, VideoContentSerializer,
    StudentLifeStatisticSerializer, InternshipRequirementSerializer,
    ReportTemplateSerializer, StudentGuideSerializer
)


class PartnerOrganizationViewSet(viewsets.ModelViewSet):
    queryset = PartnerOrganization.objects.all()
    serializer_class = PartnerOrganizationSerializer
    permission_classes = [AllowAny]

class PhotoAlbumViewSet(viewsets.ModelViewSet):
    """ViewSet для фотоальбомов"""
    queryset = PhotoAlbum.objects.filter(is_active=True)
    serializer_class = PhotoAlbumSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        """Фильтрация по категории если передана"""
        queryset = super().get_queryset()
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category=category)
        return queryset.order_by('-created_at')
    
    @action(detail=True, methods=['get'])
    def photos(self, request, pk=None):
        """Получение фотографий альбома"""
        album = self.get_object()
        photos = album.photos.all().order_by('order')
        serializer = PhotoSerializer(photos, many=True, context={'request': request})
        return Response(serializer.data)

class PhotoViewSet(viewsets.ModelViewSet):
    """ViewSet для фотографий"""
    queryset = Photo.objects.select_related('album').all()
    serializer_class = PhotoSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        """Фильтрация по альбому если передан"""
        queryset = super().get_queryset()
        album_id = self.request.query_params.get('album', None)
        if album_id:
            queryset = queryset.filter(album_id=album_id)
        return queryset.order_by('order')

class VideoContentViewSet(viewsets.ModelViewSet):
    """ViewSet для видеоконтента"""
    queryset = VideoContent.objects.all()
    serializer_class = VideoContentSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        """Фильтрация по категории если передана"""
        queryset = super().get_queryset()
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category=category)
        return queryset.order_by('-created_at')
    
    @action(detail=False, methods=['get'])
    def latest(self, request):
        """Получение последних видео"""
        limit = int(request.query_params.get('limit', 6))
        videos = self.get_queryset()[:limit]
        serializer = self.get_serializer(videos, many=True)
        return Response(serializer.data)

class StudentLifeStatisticViewSet(viewsets.ModelViewSet):
    """ViewSet для статистики студенческой жизни"""
    queryset = StudentLifeStatistic.objects.filter(is_active=True)
    serializer_class = StudentLifeStatisticSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        """Сортировка по порядку"""
        return super().get_queryset().order_by('order')

# =============================================================================
# КОМБИНИРОВАННЫЕ API ENDPOINTS ДЛЯ ФРОНТЕНДА
# =============================================================================

@api_view(['GET'])
def instructions_data(request):
    """
    API endpoint для данных инструкций для студентов.
    Возвращает пошаговые руководства по важным процедурам из базы данных.
    """
    try:
        # Получаем все активные инструкции из базы данных
        guides = StudentGuide.objects.filter(is_active=True).prefetch_related(
            'requirements', 'steps__details'
        ).order_by('order')
        
        # Сериализуем данные
        serializer = StudentGuideSerializer(guides, many=True, context={'request': request})
        
        # Преобразуем данные в формат, ожидаемый фронтендом
        student_guides = []
        for guide_data in serializer.data:
            # Преобразуем требования в простой список строк для каждого языка
            requirements_ru = [req['text_ru'] for req in guide_data.get('requirements', [])]
            requirements_kg = [req['text_kg'] for req in guide_data.get('requirements', [])]
            requirements_en = [req['text_en'] for req in guide_data.get('requirements', [])]
            
            # Преобразуем шаги в нужный формат
            steps = []
            for step_data in guide_data.get('steps', []):
                # Преобразуем детали шага в простой список строк для каждого языка
                details_ru = [detail['text_ru'] for detail in step_data.get('details', [])]
                details_kg = [detail['text_kg'] for detail in step_data.get('details', [])]
                details_en = [detail['text_en'] for detail in step_data.get('details', [])]
                
                step = {
                    "step_number": step_data.get('step_number', 1),
                    "title_ru": step_data.get('title_ru', ''),
                    "title_kg": step_data.get('title_kg', ''),
                    "title_en": step_data.get('title_en', ''),
                    "description_ru": step_data.get('description_ru', ''),
                    "description_kg": step_data.get('description_kg', ''),
                    "description_en": step_data.get('description_en', ''),
                    "timeframe_ru": step_data.get('timeframe_ru', ''),
                    "timeframe_kg": step_data.get('timeframe_kg', ''),
                    "timeframe_en": step_data.get('timeframe_en', ''),
                    "details_ru": details_ru,
                    "details_kg": details_kg,
                    "details_en": details_en
                }
                steps.append(step)
            
            # Формируем данные инструкции в ожидаемом формате
            guide = {
                "id": guide_data['id'],
                "title_ru": guide_data.get('title_ru', ''),
                "title_kg": guide_data.get('title_kg', ''),
                "title_en": guide_data.get('title_en', ''),
                "description_ru": guide_data.get('description_ru', ''),
                "description_kg": guide_data.get('description_kg', ''),
                "description_en": guide_data.get('description_en', ''),
                "icon": guide_data.get('icon', 'DocumentTextIcon'),
                "estimated_time_ru": guide_data.get('estimated_time_ru', ''),
                "estimated_time_kg": guide_data.get('estimated_time_kg', ''),
                "estimated_time_en": guide_data.get('estimated_time_en', ''),
                "max_duration_ru": guide_data.get('max_duration_ru', ''),
                "max_duration_kg": guide_data.get('max_duration_kg', ''),
                "max_duration_en": guide_data.get('max_duration_en', ''),
                "contact_info_ru": guide_data.get('contact_info_ru', ''),
                "contact_info_kg": guide_data.get('contact_info_kg', ''),
                "contact_info_en": guide_data.get('contact_info_en', ''),
                "category": guide_data.get('category', 'academic'),
                "requirements_ru": requirements_ru,
                "requirements_kg": requirements_kg,
                "requirements_en": requirements_en,
                "steps": steps
            }
            student_guides.append(guide)
        
        response_data = {
            "student_guides": student_guides
        }
        
        return Response(response_data, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response(
            {"error": f"Ошибка получения данных инструкций: {str(e)}"}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


class StudentAppealViewSet(viewsets.ModelViewSet):
    queryset = StudentAppeal.objects.all()
    serializer_class = StudentAppealSerializer
    permission_classes = [AllowAny]
