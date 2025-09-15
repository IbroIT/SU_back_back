from rest_framework import serializers
from .models import Document, DocumentCategory


class DocumentCategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий документов"""
    
    class Meta:
        model = DocumentCategory
        fields = ['id', 'name', 'name_ru', 'name_en', 'name_kg']


class DocumentListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка документов"""
    
    category_name = serializers.CharField(source='category.name', read_only=True)
    category_display_ru = serializers.CharField(source='category.name_ru', read_only=True)
    category_display_en = serializers.CharField(source='category.name_en', read_only=True)
    category_display_kg = serializers.CharField(source='category.name_kg', read_only=True)
    
    file_url = serializers.SerializerMethodField()
    download_url = serializers.SerializerMethodField()
    filename = serializers.CharField(read_only=True)
    file_extension = serializers.CharField(read_only=True)
    
    class Meta:
        model = Document
        fields = [
            'id', 'title_ru', 'title_en', 'title_kg',
            'description_ru', 'description_en', 'description_kg',
            'category', 'category_name', 
            'category_display_ru', 'category_display_en', 'category_display_kg',
            'file_url', 'download_url', 'filename', 'file_extension',
            'file_size', 'order', 'is_active',
            'created_at', 'updated_at'
        ]
    
    def get_file_url(self, obj):
        """Получение URL файла"""
        if obj.file:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.file.url)
        return None
    
    def get_download_url(self, obj):
        """Получение URL для скачивания"""
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(f'/api/documents/{obj.pk}/download/')
        return f'/api/documents/{obj.pk}/download/'


class DocumentDetailSerializer(DocumentListSerializer):
    """Детальный сериализатор для документа"""
    
    category = DocumentCategorySerializer(read_only=True)
    
    class Meta(DocumentListSerializer.Meta):
        pass


class DocumentCreateUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания и обновления документов"""
    
    class Meta:
        model = Document
        fields = [
            'title_ru', 'title_en', 'title_kg',
            'description_ru', 'description_en', 'description_kg',
            'category', 'file', 'order', 'is_active'
        ]
    
    def validate_file(self, value):
        """Валидация файла"""
        if value:
            # Проверка размера файла (максимум 50MB)
            if value.size > 50 * 1024 * 1024:
                raise serializers.ValidationError(
                    "Размер файла не должен превышать 50MB"
                )
            
            # Проверка типа файла
            allowed_extensions = ['.pdf', '.doc', '.docx', '.txt']
            file_extension = value.name.lower().split('.')[-1]
            if f'.{file_extension}' not in allowed_extensions:
                raise serializers.ValidationError(
                    f"Разрешены только файлы: {', '.join(allowed_extensions)}"
                )
        
        return value
