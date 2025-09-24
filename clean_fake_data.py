#!/usr/bin/env python
import os
import sys
import django

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from news.models import Event, Announcement

def clean_stock_images():
    """Удаляет все стоковые изображения из базы данных"""
    
    # Паттерны для определения стоковых изображений
    stock_patterns = [
        'unsplash.com',
        'picsum.photos',
        'placeholder',
        'example.com',
        'stock-photo',
        'shutterstock',
        'getty',
        'pexels.com'
    ]
    
    print("🔍 Поиск и удаление стоковых изображений...")
    
    # Очистка событий (Events)
    events_cleaned = 0
    for event in Event.objects.all():
        if event.image and any(pattern in str(event.image) for pattern in stock_patterns):
            print(f"  ❌ Удаление стокового изображения из события: {event.title}")
            event.image = None
            event.save()
            events_cleaned += 1
    
    # Очистка объявлений (Announcements)  
    announcements_cleaned = 0
    for announcement in Announcement.objects.all():
        if announcement.image and any(pattern in str(announcement.image) for pattern in stock_patterns):
            print(f"  ❌ Удаление стокового изображения из объявления: {announcement.title}")
            announcement.image = None
            announcement.save()
            announcements_cleaned += 1
    
    print(f"\n✅ Очистка завершена:")
    print(f"  - События: {events_cleaned} стоковых изображений удалено")
    print(f"  - Объявления: {announcements_cleaned} стоковых изображений удалено")

def clean_fake_data():
    """Удаляет все автоматически созданные записи с фейковыми данными"""
    
    print("\n🔍 Поиск автоматически созданных записей...")
    
    # Паттерны для определения автоматически созданных данных
    fake_patterns = [
        'Lorem ipsum',
        'Sed ut perspiciatis',
        'At vero eos',
        'But I must explain',
        'On the other hand',
        'Temporibus autem',
        'Et harum quidem',
        'Nam libero tempore'
    ]
    
    # Удаление фейковых событий
    events_deleted = 0
    for event in Event.objects.all():
        # Проверяем содержимое связанной новости
        if event.news and any(pattern in str(event.news.content_ru or '') for pattern in fake_patterns):
            print(f"  🗑️ Удаление фейкового события: {event.news.title_ru}")
            event.delete()
            events_deleted += 1
    
    # Удаление фейковых объявлений
    announcements_deleted = 0
    for announcement in Announcement.objects.all():
        # Проверяем содержимое связанной новости
        if announcement.news and any(pattern in str(announcement.news.content_ru or '') for pattern in fake_patterns):
            print(f"  🗑️ Удаление фейкового объявления: {announcement.news.title_ru}")
            announcement.delete()
            announcements_deleted += 1
    
    print(f"\n✅ Очистка фейковых данных завершена:")
    print(f"  - События: {events_deleted} записей удалено")
    print(f"  - Объявления: {announcements_deleted} записей удалено")

def show_remaining_data():
    """Показывает оставшиеся данные в базе"""
    
    print("\n📊 Оставшиеся данные в базе:")
    
    events = Event.objects.all()
    print(f"\n📅 События ({events.count()}):")
    for event in events:
        image_status = "✅ Есть изображение" if event.news and event.news.image else "❌ Нет изображения"
        title = event.news.title_ru if event.news else "Без названия"
        print(f"  - {title} | {image_status}")
    
    announcements = Announcement.objects.all()
    print(f"\n📢 Объявления ({announcements.count()}):")
    for announcement in announcements:
        image_status = "✅ Есть изображение" if announcement.news and announcement.news.image else "❌ Нет изображения"
        title = announcement.news.title_ru if announcement.news else "Без названия"
        print(f"  - {title} | {image_status}")

if __name__ == '__main__':
    print("🚀 Начало очистки базы данных от фейковых данных...")
    
    # Очищаем стоковые изображения
    clean_stock_images()
    
    # Очищаем автоматически созданные записи
    clean_fake_data()
    
    # Показываем что осталось
    show_remaining_data()
    
    print("\n🎉 Очистка завершена! Теперь в базе данных только реальные данные, добавленные через админку.")
