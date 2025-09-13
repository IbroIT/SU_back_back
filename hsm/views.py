from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import HSMInfo, Program, Faculty, Accreditation, LearningGoal
from .serializers import (
    HSMInfoSerializer, ProgramSerializer, FacultySerializer, 
    AccreditationSerializer, LearningGoalSerializer,
    ProgramListSerializer, FacultyListSerializer
)


class HSMInfoViewSet(viewsets.ReadOnlyModelViewSet):
    """API для получения информации о ВШМ"""
    queryset = HSMInfo.objects.filter(is_active=True)
    serializer_class = HSMInfoSerializer
    
    def get_queryset(self):
        return HSMInfo.objects.filter(is_active=True)


class ProgramViewSet(viewsets.ReadOnlyModelViewSet):
    """API для программ обучения ВШМ"""
    queryset = Program.objects.filter(is_active=True)
    serializer_class = ProgramSerializer
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ProgramListSerializer
        return ProgramSerializer
    
    def get_queryset(self):
        queryset = Program.objects.filter(is_active=True)
        program_type = self.request.query_params.get('type', None)
        
        if program_type:
            queryset = queryset.filter(program_type=program_type)
            
        return queryset
    
    @action(detail=False, methods=['get'])
    def bachelor(self, request):
        """Получить программы бакалавриата"""
        programs = Program.objects.filter(is_active=True, program_type='bachelor')
        serializer = self.get_serializer(programs, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def master(self, request):
        """Получить программы магистратуры"""
        programs = Program.objects.filter(is_active=True, program_type='master')
        serializer = self.get_serializer(programs, many=True)
        return Response(serializer.data)


class FacultyViewSet(viewsets.ReadOnlyModelViewSet):
    """API для профессорско-преподавательского состава ВШМ"""
    queryset = Faculty.objects.filter(is_active=True)
    serializer_class = FacultySerializer
    
    def get_serializer_class(self):
        if self.action == 'list':
            return FacultyListSerializer
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
        
        for position_code, position_name in positions:
            faculty = Faculty.objects.filter(
                is_active=True, 
                position=position_code
            ).order_by('order', 'last_name')
            
            serializer = FacultyListSerializer(faculty, many=True)
            result[position_code] = {
                'name': position_name,
                'faculty': serializer.data
            }
        
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
        
        for type_code, type_name in types:
            accreditations = Accreditation.objects.filter(
                is_active=True,
                accreditation_type=type_code
            ).order_by('order', '-issue_date')
            
            serializer = AccreditationSerializer(accreditations, many=True)
            result[type_code] = {
                'name': type_name,
                'accreditations': serializer.data
            }
        
        return Response(result)


class LearningGoalViewSet(viewsets.ReadOnlyModelViewSet):
    """API для целей и результатов обучения ВШМ"""
    queryset = LearningGoal.objects.filter(is_active=True)
    serializer_class = LearningGoalSerializer
    
    def get_queryset(self):
        queryset = LearningGoal.objects.filter(is_active=True)
        program_id = self.request.query_params.get('program', None)
        
        if program_id:
            queryset = queryset.filter(programs__id=program_id)
            
        return queryset
