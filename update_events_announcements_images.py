#!/usr/bin/env python
"""
Скрипт для добавления стоковых изображений к событиям и объявлениям
"""
import os
import sys
import django

# Настройка Django
sys.path.append('/Users/adminbaike/medicine/SU_back_back')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from news.models import Event, Announcement

# Стоковые изображения для событий по категориям
EVENT_STOCK_IMAGES = {
    'conference': [
        'https://images.unsplash.com/photo-1505751172876-fa1923c5c528?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1591115765373-5207764f72e7?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=600&h=400&fit=crop',
    ],
    'open-day': [
        'https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=600&h=400&fit=crop',
    ],
    'competition': [
        'https://images.unsplash.com/photo-1552664730-d307ca884978?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1579952363873-27d3bfad9c0d?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=600&h=400&fit=crop',
    ],
    'ceremony': [
        'https://images.unsplash.com/photo-1523580494863-6f3031224c94?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1517457373958-b7bdd4587205?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1511578314322-379afb476865?w=600&h=400&fit=crop',
    ],
    'workshop': [
        'https://images.unsplash.com/photo-1517180102446-f3ece451e9d8?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1572726729207-a78d6feb18d7?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1531482615713-2afd69097998?w=600&h=400&fit=crop',
    ],
    'seminar': [
        'https://images.unsplash.com/photo-1556761175-4b46a572b786?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1559136555-9303baea8ebd?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=600&h=400&fit=crop',
    ],
    'lecture': [
        'https://images.unsplash.com/photo-1524178232363-1fb2b075b655?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1557426272-fc759fdf7a8d?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=600&h=400&fit=crop',
    ],
}

# Стоковые изображения для объявлений по типам
ANNOUNCEMENT_STOCK_IMAGES = {
    'academic': [
        'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1513475382585-d06e58bcb0e0?w=600&h=400&fit=crop',
    ],
    'scholarship': [
        'https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1532012197267-da84d127e765?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=600&h=400&fit=crop',
    ],
    'schedule': [
        'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1495364141860-b0d03eccd065?w=600&h=400&fit=crop',
    ],
    'competition': [
        'https://images.unsplash.com/photo-1552664730-d307ca884978?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1579952363873-27d3bfad9c0d?w=600&h=400&fit=crop',
    ],
    'health': [
        'https://images.unsplash.com/photo-1559757175-0eb30cd8c063?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1530026405186-ed1f139313f8?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=600&h=400&fit=crop',
    ],
    'technical': [
        'https://images.unsplash.com/photo-1518709268805-4e9042af2176?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&h=400&fit=crop',
    ],
    'administrative': [
        'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1573166364524-d9b113de5c1c?w=600&h=400&fit=crop',
        'https://images.unsplash.com/photo-1521791136064-7986c2920216?w=600&h=400&fit=crop',
    ],
}

def update_events():
    """Обновляем изображения для событий"""
    print("Обновление изображений для событий...")
    
    events = Event.objects.all()
    updated_count = 0
    
    for event in events:
        if not event.image and not event.image_url:
            category = event.event_category
            images = EVENT_STOCK_IMAGES.get(category, EVENT_STOCK_IMAGES['conference'])
            
            # Выбираем изображение по ID события для равномерного распределения
            image_index = event.id % len(images)
            event.image_url = images[image_index]
            event.save()
            
            print(f"✅ Обновлено событие: {event.news.title_ru} - {event.image_url}")
            updated_count += 1
        else:
            print(f"⏭️  Пропущено событие (уже есть изображение): {event.news.title_ru}")
    
    print(f"Обновлено событий: {updated_count}")

def update_announcements():
    """Обновляем изображения для объявлений"""
    print("\nОбновление изображений для объявлений...")
    
    announcements = Announcement.objects.all()
    updated_count = 0
    
    for announcement in announcements:
        if not announcement.image and not announcement.image_url:
            ann_type = announcement.announcement_type
            images = ANNOUNCEMENT_STOCK_IMAGES.get(ann_type, ANNOUNCEMENT_STOCK_IMAGES['academic'])
            
            # Выбираем изображение по ID объявления для равномерного распределения
            image_index = announcement.id % len(images)
            announcement.image_url = images[image_index]
            announcement.save()
            
            print(f"✅ Обновлено объявление: {announcement.news.title_ru} - {announcement.image_url}")
            updated_count += 1
        else:
            print(f"⏭️  Пропущено объявление (уже есть изображение): {announcement.news.title_ru}")
    
    print(f"Обновлено объявлений: {updated_count}")

def main():
    print("🖼️  Добавление стоковых изображений к событиям и объявлениям")
    print("=" * 60)
    
    update_events()
    update_announcements()
    
    print("\n✅ Обновление завершено!")

if __name__ == "__main__":
    main()
