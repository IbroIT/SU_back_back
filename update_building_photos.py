#!/usr/bin/env python
"""
Скрипт для обновления фотографий зданий
"""
import os
import sys
import django
from django.core.files.base import ContentFile
import base64

# Настройка Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from infrastructure.models import AcademicBuilding, BuildingPhoto

def create_placeholder_image(text="Photo", width=400, height=300):
    """Создает placeholder изображение в формате SVG"""
    svg_content = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
        <rect width="{width}" height="{height}" fill="#f3f4f6"/>
        <text x="{width//2}" y="{height//2}" text-anchor="middle" fill="#6b7280" font-family="Arial" font-size="16">{text}</text>
    </svg>'''
    return svg_content.encode('utf-8')

def update_building_photos():
    """Обновляет фотографии зданий"""
    buildings = AcademicBuilding.objects.all()
    
    for building in buildings:
        # Проверяем, есть ли фотографии у здания
        photos = building.photos.all()
        
        for photo in photos:
            if not photo.photo:
                # Создаем placeholder изображение
                placeholder_content = create_placeholder_image(f"{building.name_ru} - {photo.type}")
                photo.photo.save(
                    f"{building.id}_{photo.type}.svg",
                    ContentFile(placeholder_content),
                    save=True
                )
                print(f"Добавлено placeholder изображение для {building.name_ru} - {photo.type}")

if __name__ == "__main__":
    print("Обновление фотографий зданий...")
    update_building_photos()
    print("Готово!")
