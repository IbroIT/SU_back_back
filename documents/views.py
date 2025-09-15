from django.shortcuts import render
from django.http import Http404, HttpResponse, FileResponse
from django.utils.encoding import smart_str
from rest_framework import generics, status, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
import os

from .models import Document, DocumentCategory
from .serializers import (
    DocumentListSerializer, 
    DocumentDetailSerializer, 
    DocumentCreateUpdateSerializer,
    DocumentCategorySerializer
)


class DocumentCategoryListView(generics.ListAPIView):
    """Список категорий документов"""
    
    queryset = DocumentCategory.objects.all()
    serializer_class = DocumentCategorySerializer
    permission_classes = [AllowAny]


class DocumentListView(generics.ListAPIView):
    """Список документов с фильтрацией и поиском"""
    
    serializer_class = DocumentListSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'category__name', 'is_active']
    search_fields = ['title_ru', 'title_en', 'title_kg', 'description_ru', 'description_en', 'description_kg']
    ordering_fields = ['order', 'created_at', 'updated_at', 'title_ru']
    ordering = ['order', '-updated_at']
    
    def get_queryset(self):
        queryset = Document.objects.filter(is_active=True).select_related('category')
        
        # Фильтрация по категории
        category = self.request.query_params.get('category', None)
        if category and category != 'all':
            queryset = queryset.filter(category__name=category)
        
        # Поиск по тексту
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(
                Q(title_ru__icontains=search) |
                Q(title_en__icontains=search) |
                Q(title_kg__icontains=search) |
                Q(description_ru__icontains=search) |
                Q(description_en__icontains=search) |
                Q(description_kg__icontains=search)
            )
        
        return queryset


class DocumentDetailView(generics.RetrieveAPIView):
    """Детальная информация о документе"""
    
    queryset = Document.objects.filter(is_active=True)
    serializer_class = DocumentDetailSerializer
    permission_classes = [AllowAny]


class DocumentCreateView(generics.CreateAPIView):
    """Создание нового документа (для админки)"""
    
    queryset = Document.objects.all()
    serializer_class = DocumentCreateUpdateSerializer
    # permission_classes = [IsAdminUser]  # Раскомментировать для продакшена


class DocumentUpdateView(generics.UpdateAPIView):
    """Обновление документа (для админки)"""
    
    queryset = Document.objects.all()
    serializer_class = DocumentCreateUpdateSerializer
    # permission_classes = [IsAdminUser]  # Раскомментировать для продакшена


class DocumentDeleteView(generics.DestroyAPIView):
    """Удаление документа (для админки)"""
    
    queryset = Document.objects.all()
    # permission_classes = [IsAdminUser]  # Раскомментировать для продакшена


@api_view(['GET'])
@permission_classes([AllowAny])
def download_document(request, pk):
    """Скачивание документа"""
    
    try:
        document = Document.objects.get(pk=pk, is_active=True)
    except Document.DoesNotExist:
        raise Http404("Документ не найден")
    
    if not document.file:
        return Response(
            {'error': 'Файл не найден'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    
    # Проверка существования файла
    if not os.path.exists(document.file.path):
        return Response(
            {'error': 'Файл не найден на сервере'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    
    try:
        # Получение имени файла для скачивания
        filename = document.filename
        if not filename:
            filename = f"document_{document.pk}{document.file_extension}"
        
        # Возврат файла для скачивания
        response = FileResponse(
            open(document.file.path, 'rb'),
            as_attachment=True,
            filename=smart_str(filename)
        )
        
        # Добавление заголовков
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Length'] = os.path.getsize(document.file.path)
        
        return response
        
    except Exception as e:
        return Response(
            {'error': f'Ошибка при скачивании файла: {str(e)}'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
@permission_classes([AllowAny])
def document_stats(request):
    """Статистика документов"""
    
    stats = {
        'total_documents': Document.objects.filter(is_active=True).count(),
        'by_category': {}
    }
    
    categories = DocumentCategory.objects.all()
    for category in categories:
        stats['by_category'][category.name] = {
            'count': Document.objects.filter(
                category=category, 
                is_active=True
            ).count(),
            'name_ru': category.name_ru,
            'name_en': category.name_en,
            'name_kg': category.name_kg
        }
    
    return Response(stats)
