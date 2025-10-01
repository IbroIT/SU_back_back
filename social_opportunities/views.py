from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .models import Event, Club, Project
from .serializers import EventSerializer, ClubSerializer, ProjectSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'status', 'registration', 'popular']
    search_fields = ['title', 'title_en', 'title_ky', 'description', 'description_en', 'description_ky']
    ordering_fields = ['date', 'created_at', 'title']
    ordering = ['date']
    
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """Get events by category"""
        category = request.query_params.get('category', 'events')
        events = self.queryset.filter(category=category)
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def upcoming(self, request):
        """Get upcoming events"""
        events = self.queryset.filter(status='upcoming')
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'status', 'popular']
    search_fields = ['title', 'title_en', 'title_ky', 'description', 'description_en', 'description_ky']
    ordering_fields = ['title', 'created_at', 'members']
    ordering = ['title']
    
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """Get clubs by category"""
        category = request.query_params.get('category', 'clubs')
        clubs = self.queryset.filter(category=category)
        serializer = self.get_serializer(clubs, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def active(self, request):
        """Get active clubs"""
        clubs = self.queryset.filter(status='active')
        serializer = self.get_serializer(clubs, many=True)
        return Response(serializer.data)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'status', 'popular']
    search_fields = ['title', 'title_en', 'title_ky', 'description', 'description_en', 'description_ky']
    ordering_fields = ['title', 'created_at', 'progress']
    ordering = ['-created_at']
    
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """Get projects by category"""
        category = request.query_params.get('category', 'projects')
        projects = self.queryset.filter(category=category)
        serializer = self.get_serializer(projects, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def active(self, request):
        """Get active projects"""
        projects = self.queryset.filter(status='active')
        serializer = self.get_serializer(projects, many=True)
        return Response(serializer.data)
