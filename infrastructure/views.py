from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.db.models import Q, Sum

from .models import (
    Hospital, Laboratory, AcademicBuilding, Dormitory
)
from .serializers import (
    HospitalSerializer, HospitalListSerializer,
    LaboratorySerializer, LaboratoryListSerializer,
    AcademicBuildingSerializer, AcademicBuildingListSerializer,
    DormitorySerializer, DormitoryListSerializer
)


class HospitalListCreateView(generics.ListCreateAPIView):
    """
    List all hospitals or create a new hospital
    """
    queryset = Hospital.objects.filter(is_active=True).prefetch_related('departments')
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name_ru', 'name_kg', 'name_en', 'address_ru', 'address_kg', 'address_en']
    ordering_fields = ['order', 'name_ru', 'created_at']
    ordering = ['order', 'name_ru']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return HospitalListSerializer
        return HospitalSerializer


class HospitalDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a hospital instance
    """
    queryset = Hospital.objects.filter(is_active=True).prefetch_related('departments')
    serializer_class = HospitalSerializer


class LaboratoryListCreateView(generics.ListCreateAPIView):
    """
    List all laboratories or create a new laboratory
    """
    queryset = Laboratory.objects.filter(is_active=True).prefetch_related('equipment')
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['type']
    search_fields = ['name_ru', 'name_kg', 'name_en', 'description_ru', 'description_kg', 'description_en']
    ordering_fields = ['order', 'name_ru', 'type', 'capacity', 'created_at']
    ordering = ['order', 'name_ru']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return LaboratoryListSerializer
        return LaboratorySerializer


class LaboratoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a laboratory instance
    """
    queryset = Laboratory.objects.filter(is_active=True).prefetch_related('equipment')
    serializer_class = LaboratorySerializer


class AcademicBuildingListCreateView(generics.ListCreateAPIView):
    """
    List all academic buildings or create a new building
    """
    queryset = AcademicBuilding.objects.filter(is_active=True).prefetch_related('facilities', 'photos')
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name_ru', 'name_kg', 'name_en', 'address_ru', 'address_kg', 'address_en']
    ordering_fields = ['order', 'name_ru', 'floors', 'created_at']
    ordering = ['order', 'name_ru']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AcademicBuildingListSerializer
        return AcademicBuildingSerializer


class AcademicBuildingDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an academic building instance
    """
    queryset = AcademicBuilding.objects.filter(is_active=True).prefetch_related('facilities', 'photos')
    serializer_class = AcademicBuildingSerializer


class DormitoryListCreateView(generics.ListCreateAPIView):
    """
    List all dormitories or create a new dormitory
    """
    queryset = Dormitory.objects.filter(is_active=True).prefetch_related('rooms', 'facilities', 'photos')
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['type']
    search_fields = ['name_ru', 'name_kg', 'name_en', 'address_ru', 'address_kg', 'address_en']
    ordering_fields = ['order', 'name_ru', 'type', 'capacity', 'available', 'created_at']
    ordering = ['order', 'name_ru']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DormitoryListSerializer
        return DormitorySerializer


class DormitoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a dormitory instance
    """
    queryset = Dormitory.objects.filter(is_active=True).prefetch_related('rooms', 'facilities', 'photos')
    serializer_class = DormitorySerializer


@api_view(['GET'])
def infrastructure_overview(request):
    """
    Get overview statistics for all infrastructure
    """
    hospitals_count = Hospital.objects.filter(is_active=True).count()
    laboratories_count = Laboratory.objects.filter(is_active=True).count()
    buildings_count = AcademicBuilding.objects.filter(is_active=True).count()
    dormitories_count = Dormitory.objects.filter(is_active=True).count()
    total_dormitory_capacity = Dormitory.objects.filter(is_active=True).aggregate(
        total=Sum('capacity')
    )['total'] or 0
    total_available_places = Dormitory.objects.filter(is_active=True).aggregate(
        total=Sum('available')
    )['total'] or 0

    data = {
        'hospitals': hospitals_count,
        'laboratories': laboratories_count,
        'academic_buildings': buildings_count,
        'dormitories': dormitories_count,
        'total_dormitory_capacity': total_dormitory_capacity,
        'available_dormitory_places': total_available_places,
        'laboratory_types': Laboratory.objects.filter(is_active=True).values_list('type', flat=True).distinct(),
        'dormitory_types': Dormitory.objects.filter(is_active=True).values_list('type', flat=True).distinct(),
    }

    return Response(data)


@api_view(['GET'])
def search_infrastructure(request):
    """
    Global search across all infrastructure
    """
    query = request.GET.get('q', '')
    if not query:
        return Response({'error': 'Query parameter "q" is required'}, status=status.HTTP_400_BAD_REQUEST)

    # Search hospitals
    hospitals = Hospital.objects.filter(
        Q(name_ru__icontains=query) | Q(name_kg__icontains=query) | Q(name_en__icontains=query) |
        Q(description_ru__icontains=query) | Q(description_kg__icontains=query) | Q(description_en__icontains=query) |
        Q(address_ru__icontains=query) | Q(address_kg__icontains=query) | Q(address_en__icontains=query),
        is_active=True
    )

    # Search laboratories
    laboratories = Laboratory.objects.filter(
        Q(name_ru__icontains=query) | Q(name_kg__icontains=query) | Q(name_en__icontains=query) |
        Q(description_ru__icontains=query) | Q(description_kg__icontains=query) | Q(description_en__icontains=query),
        is_active=True
    )

    # Search buildings
    buildings = AcademicBuilding.objects.filter(
        Q(name_ru__icontains=query) | Q(name_kg__icontains=query) | Q(name_en__icontains=query) |
        Q(description_ru__icontains=query) | Q(description_kg__icontains=query) | Q(description_en__icontains=query) |
        Q(address_ru__icontains=query) | Q(address_kg__icontains=query) | Q(address_en__icontains=query),
        is_active=True
    )

    # Search dormitories
    dormitories = Dormitory.objects.filter(
        Q(name_ru__icontains=query) | Q(name_kg__icontains=query) | Q(name_en__icontains=query) |
        Q(description_ru__icontains=query) | Q(description_kg__icontains=query) | Q(description_en__icontains=query) |
        Q(address_ru__icontains=query) | Q(address_kg__icontains=query) | Q(address_en__icontains=query),
        is_active=True
    )

    data = {
        'hospitals': HospitalListSerializer(hospitals, many=True, context={'request': request}).data,
        'laboratories': LaboratoryListSerializer(laboratories, many=True, context={'request': request}).data,
        'academic_buildings': AcademicBuildingListSerializer(buildings, many=True, context={'request': request}).data,
        'dormitories': DormitoryListSerializer(dormitories, many=True, context={'request': request}).data,
    }

    return Response(data)
