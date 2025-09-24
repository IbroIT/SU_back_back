#!/usr/bin/env python
import os
import sys
import django

# Добавляем путь к Django проекту
sys.path.append('/Users/adminbaike/medicine/SU_back_back')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')

# Инициализируем Django
django.setup()

from news.models import News, Event, Announcement

def check_images():
    """Проверяет изображения во всех событиях и объявлениях"""
    
    print("🔍 Проверка изображений в событиях:")
    events = Event.objects.all()
    for event in events:
        print(f"\n📅 Событие: {event.news.title_ru}")
        print(f"   ID: {event.id}")
        print(f"   Slug: {event.news.slug}")
        print(f"   Event.image: {event.image}")
        print(f"   Event.image_url: {event.image_url}")
        print(f"   News.image: {event.news.image}")
        print(f"   News.image_url: {event.news.image_url}")
        print(f"   image_url_or_default: {event.image_url_or_default}")
        
        # Проверяем доступность файла
        if event.image:
            file_path = event.image.path
            if os.path.exists(file_path):
                print(f"   ✅ Файл существует: {file_path}")
            else:
                print(f"   ❌ Файл не найден: {file_path}")
    
    print("\n" + "="*60)
    print("🔍 Проверка изображений в объявлениях:")
    announcements = Announcement.objects.all()
    for announcement in announcements:
        print(f"\n📢 Объявление: {announcement.news.title_ru}")
        print(f"   ID: {announcement.id}")
        print(f"   Slug: {announcement.news.slug}")
        print(f"   Announcement.image: {announcement.image}")
        print(f"   Announcement.image_url: {announcement.image_url}")
        print(f"   News.image: {announcement.news.image}")
        print(f"   News.image_url: {announcement.news.image_url}")
        print(f"   image_url_or_default: {announcement.image_url_or_default}")
        
        # Проверяем доступность файла
        if announcement.image:
            file_path = announcement.image.path
            if os.path.exists(file_path):
                print(f"   ✅ Файл существует: {file_path}")
            else:
                print(f"   ❌ Файл не найден: {file_path}")

if __name__ == "__main__":
    check_images()
