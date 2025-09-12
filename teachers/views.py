from django.shortcuts import render
from rest_framework import viewsets
from .models import Teacher, Management
from .serializers import TeacherSerializer, ManagementSerializer

# Create your views here.

class TeacherViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class ManagementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Management.objects.filter(parent__isnull=True)
    serializer_class = ManagementSerializer
