from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import  Faculty, Accreditation
from .serializers import (
    FacultySerializer, 
    FacultyListSerializer,
    AccreditationSerializer, 
)



class FacultyViewSet(viewsets.ReadOnlyModelViewSet):
    """API для профессорско-преподавательского состава ВШМ"""
    queryset = Faculty.objects.filter(is_active=True)
    serializer_class = FacultySerializer
    
    def get_serializer_class(self):
        if self.action == 'list':
            return FacultySerializer
        return FacultySerializer
    
    def get_queryset(self):
        queryset = Faculty.objects.filter(is_active=True)
        position = self.request.query_params.get('position', None)
        search = self.request.query_params.get('search', None)
        
        if position:
            queryset = queryset.filter(position=position)
        
        if search:
            queryset = queryset.filter(
                Q(first_name__icontains=search) |
                Q(last_name__icontains=search) |
                Q(middle_name__icontains=search) |
                Q(first_name_kg__icontains=search) |
                Q(last_name_kg__icontains=search) |
                Q(first_name_en__icontains=search) |
                Q(last_name_en__icontains=search) |
                Q(specialization__icontains=search) |
                Q(specialization_kg__icontains=search) |
                Q(specialization_en__icontains=search)
            )
            
        return queryset
    
    @action(detail=False, methods=['get'])
    def by_position(self, request):
        """Получить преподавателей по должностям"""
        positions = Faculty.POSITIONS
        result = {}
        
        # Переводы для названий должностей
        position_translations = {
            'professor': {
                'ru': 'Профессор',
                'kg': 'Профессор', 
                'en': 'Professor'
            },
            'associate_professor': {
                'ru': 'Доцент',
                'kg': 'Доцент',
                'en': 'Associate Professor'
            },
            'senior_lecturer': {
                'ru': 'Старший преподаватель',
                'kg': 'Улук окутуучу',
                'en': 'Senior Lecturer'
            },
            'lecturer': {
                'ru': 'Преподаватель',
                'kg': 'Окутуучу',
                'en': 'Lecturer'
            },
            'assistant': {
                'ru': 'Ассистент',
                'kg': 'Ассистент',
                'en': 'Assistant'
            },
            'head_of_department': {
                'ru': 'Заведующий кафедрой',
                'kg': 'Кафедра башчысы',
                'en': 'Head of Department'
            },
            'dean': {
                'ru': 'Декан',
                'kg': 'Декан',
                'en': 'Dean'
            },
            'vice_dean': {
                'ru': 'Заместитель декана',
                'kg': 'Декандын орун басары',
                'en': 'Vice Dean'
            }
        }
        
        for position_code, position_name in positions:
            faculty = Faculty.objects.filter(
                is_active=True, 
                position=position_code
            ).order_by('order', 'last_name')
            
<<<<<<< HEAD
            serializer = FacultySerializer(faculty, many=True)
            result[position_code] = {
                'name': position_name,
                'faculty': serializer.data
            }
=======
            if faculty.exists():  # Только если есть преподаватели с такой должностью
                serializer = FacultySerializer(faculty, many=True)
                result[position_code] = {
                    'name': position_name,  # Русское название (по умолчанию)
                    'name_kg': position_translations.get(position_code, {}).get('kg', position_name),
                    'name_en': position_translations.get(position_code, {}).get('en', position_name),
                    'faculty': serializer.data
                }
>>>>>>> c00094fbb5af6df0856986206af95759d5ce7948
        
        return Response(result)


class AccreditationViewSet(viewsets.ReadOnlyModelViewSet):
    """API для аккредитаций ВШМ"""
    queryset = Accreditation.objects.filter(is_active=True)
    serializer_class = AccreditationSerializer
    
    def get_queryset(self):
        queryset = Accreditation.objects.filter(is_active=True)
        accreditation_type = self.request.query_params.get('type', None)
        valid_only = self.request.query_params.get('valid_only', None)
        
        if accreditation_type:
            queryset = queryset.filter(accreditation_type=accreditation_type)
        
        if valid_only == 'true':
            from django.utils import timezone
            queryset = queryset.filter(
                Q(expiry_date__isnull=True) |
                Q(expiry_date__gte=timezone.now().date())
            )
            
        return queryset
    
    @action(detail=False, methods=['get'])
    def by_type(self, request):
        """Получить аккредитации по типам"""
        types = Accreditation.ACCREDITATION_TYPES
        result = {}
        
        # Переводы для типов аккредитации
        type_translations = {
            'national': {
                'ru': 'Национальная',
                'kg': 'Улуттук',
                'en': 'National'
            },
            'international': {
                'ru': 'Международная',
                'kg': 'Эл аралык',
                'en': 'International'
            },
            'institutional': {
                'ru': 'Институциональная',
                'kg': 'Институционалдык',
                'en': 'Institutional'
            },
            'programmatic': {
                'ru': 'Программная',
                'kg': 'Программалык',
                'en': 'Programmatic'
            }
        }
        
        for type_code, type_name in types:
            accreditations = Accreditation.objects.filter(
                is_active=True,
                accreditation_type=type_code
            ).order_by('order', '-issue_date')
            
            if accreditations.exists():  # Только если есть аккредитации такого типа
                serializer = AccreditationSerializer(accreditations, many=True)
                result[type_code] = {
                    'name': type_name,  # Русское название (по умолчанию)
                    'name_kg': type_translations.get(type_code, {}).get('kg', type_name),
                    'name_en': type_translations.get(type_code, {}).get('en', type_name),
                    'accreditations': serializer.data
                }
        
        return Response(result)


