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

def clear_external_image_urls():
    """Очищает внешние URL изображений, чтобы показать загруженные файлы"""
    
    print("🔄 Очистка внешних URL изображений...")
    
    # Очищаем image_url у событий, где есть загруженные изображения
    events_updated = 0
    for event in Event.objects.all():
        has_uploaded_image = event.image or event.news.image
        if has_uploaded_image and event.image_url:
            event.image_url = None
            event.save()
            events_updated += 1
            print(f"✅ Очищен image_url для события: {event.news.title_ru}")
    
    # Очищаем image_url у объявлений, где есть загруженные изображения  
    announcements_updated = 0
    for announcement in Announcement.objects.all():
        has_uploaded_image = announcement.image or announcement.news.image
        if has_uploaded_image and announcement.image_url:
            announcement.image_url = None
            announcement.save()
            announcements_updated += 1
            print(f"✅ Очищен image_url для объявления: {announcement.news.title_ru}")
    
    # Очищаем image_url у новостей, где есть загруженные файлы
    news_updated = 0
    for news in News.objects.all():
        if news.image and news.image_url:
            news.image_url = None
            news.save()
            news_updated += 1
            print(f"✅ Очищен image_url для новости: {news.title_ru}")
    
    print(f"\n📊 Результат:")
    print(f"   События обновлены: {events_updated}")
    print(f"   Объявления обновлены: {announcements_updated}")
    print(f"   Новости обновлены: {news_updated}")

if __name__ == "__main__":
    clear_external_image_urls()
