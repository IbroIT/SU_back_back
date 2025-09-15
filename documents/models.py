from django.db import models
from django.utils.translation import gettext_lazy as _
import os


class DocumentCategory(models.Model):
    """Категории документов"""
    
    CATEGORY_CHOICES = [
        ('foundational', _('Учредительные документы')),
        ('academic', _('Учебная деятельность')),
        ('administrative', _('Административная деятельность')),
        ('research', _('Научная деятельность')),
    ]
    
    name = models.CharField(
        max_length=50, 
        choices=CATEGORY_CHOICES, 
        unique=True,
        verbose_name=_('Категория')
    )
    name_ru = models.CharField(max_length=100, verbose_name=_('Название (RU)'))
    name_en = models.CharField(max_length=100, verbose_name=_('Название (EN)'))
    name_kg = models.CharField(max_length=100, verbose_name=_('Название (KG)'))
    
    class Meta:
        verbose_name = _('Категория документа')
        verbose_name_plural = _('Категории документов')
        
    def __str__(self):
        return self.name_ru


class Document(models.Model):
    """Модель для нормативно-правовых документов"""
    
    # Основные поля
    title_ru = models.CharField(max_length=255, verbose_name=_('Название (RU)'))
    title_en = models.CharField(max_length=255, verbose_name=_('Название (EN)'))
    title_kg = models.CharField(max_length=255, verbose_name=_('Название (KG)'))
    
    description_ru = models.TextField(verbose_name=_('Описание (RU)'))
    description_en = models.TextField(verbose_name=_('Описание (EN)'))
    description_kg = models.TextField(verbose_name=_('Описание (KG)'))
    
    # Категория документа
    category = models.ForeignKey(
        DocumentCategory, 
        on_delete=models.CASCADE,
        related_name='documents',
        verbose_name=_('Категория')
    )
    
    # Файл документа
    file = models.FileField(
        upload_to='documents/%Y/%m/',
        verbose_name=_('Файл документа')
    )
    
    # Метаданные
    file_size = models.CharField(
        max_length=20, 
        blank=True,
        verbose_name=_('Размер файла')
    )
    
    # Порядок отображения
    order = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Порядок отображения')
    )
    
    # Статус публикации
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Активен')
    )
    
    # Временные метки
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Дата создания')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Дата обновления')
    )
    
    class Meta:
        verbose_name = _('Документ')
        verbose_name_plural = _('Документы')
        ordering = ['order', '-updated_at']
        
    def __str__(self):
        return self.title_ru
    
    def save(self, *args, **kwargs):
        """Автоматическое вычисление размера файла при сохранении"""
        if self.file and not self.file_size:
            self.file_size = self.format_file_size(self.file.size)
        super().save(*args, **kwargs)
    
    @staticmethod
    def format_file_size(size_bytes):
        """Форматирование размера файла в читаемый вид"""
        if size_bytes == 0:
            return "0 B"
        
        size_names = ["B", "KB", "MB", "GB"]
        import math
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return f"{s} {size_names[i]}"
    
    @property
    def filename(self):
        """Получение имени файла"""
        return os.path.basename(self.file.name) if self.file else ""
    
    @property
    def file_extension(self):
        """Получение расширения файла"""
        if self.file:
            return os.path.splitext(self.file.name)[1].lower()
        return ""
    
    def get_absolute_url(self):
        """URL для скачивания документа"""
        return f"/api/documents/{self.pk}/download/"
