#!/usr/bin/env python
"""
Скрипт для очистки всех стоковых изображений из базы данных.
Удаляет image_url, содержащие ссылки на стоковые сервисы.
"""

import os
import sys
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from news.models import News, Event, Announcement

def clean_stock_images():
    """Очищает все стоковые изображения из всех моделей"""
    
    # Список доменов стоковых изображений для удаления
    stock_domains = [
        'unsplash.com',
        'picsum.photos',
        'lorem',
        'placeholder',
        'pexels.com',
        'pixabay.com',
        'freepik.com'
    ]
    
    print("🧹 Начинаем очистку стоковых изображений...")
    
    # Счетчики для отчета
    news_cleaned = 0
    events_cleaned = 0
    announcements_cleaned = 0
    
    # Очистка News
    print("\n📰 Очищаем изображения в News...")
    news_items = News.objects.all()
    for news in news_items:
        cleaned = False
        
        if news.image_url:
            for domain in stock_domains:
                if domain in news.image_url:
                    print(f"   Удаляем стоковое изображение из News #{news.id}: {news.image_url[:80]}...")
                    news.image_url = None
                    cleaned = True
                    break
        
        if cleaned:
            news.save(update_fields=['image_url'])
            news_cleaned += 1
    
    # Очистка Event
    print("\n🎯 Очищаем изображения в Events...")
    events = Event.objects.all()
    for event in events:
        cleaned = False
        
        if event.image_url:
            for domain in stock_domains:
                if domain in event.image_url:
                    print(f"   Удаляем стоковое изображение из Event #{event.id}: {event.image_url[:80]}...")
                    event.image_url = None
                    cleaned = True
                    break
        
        if cleaned:
            event.save(update_fields=['image_url'])
            events_cleaned += 1
    
    # Очистка Announcement
    print("\n📢 Очищаем изображения в Announcements...")
    announcements = Announcement.objects.all()
    for announcement in announcements:
        cleaned = False
        
        if announcement.image_url:
            for domain in stock_domains:
                if domain in announcement.image_url:
                    print(f"   Удаляем стоковое изображение из Announcement #{announcement.id}: {announcement.image_url[:80]}...")
                    announcement.image_url = None
                    cleaned = True
                    break
        
        if cleaned:
            announcement.save(update_fields=['image_url'])
            announcements_cleaned += 1
    
    # Отчет
    print(f"\n✅ Очистка завершена!")
    print(f"📊 Статистика:")
    print(f"   - News очищено: {news_cleaned}")
    print(f"   - Events очищено: {events_cleaned}")
    print(f"   - Announcements очищено: {announcements_cleaned}")
    print(f"   - Всего очищено: {news_cleaned + events_cleaned + announcements_cleaned}")
    
    if news_cleaned + events_cleaned + announcements_cleaned == 0:
        print("🎉 Стоковые изображения не найдены или уже были очищены!")
    else:
        print("🎉 Теперь будут отображаться только изображения, загруженные через админку!")

def verify_cleanup():
    """Проверяет результат очистки"""
    print("\n🔍 Проверяем результат очистки...")
    
    stock_domains = [
        'unsplash.com',
        'picsum.photos',
        'lorem',
        'placeholder'
    ]
    
    # Проверяем News
    news_with_stock = 0
    for news in News.objects.all():
        if news.image_url:
            for domain in stock_domains:
                if domain in news.image_url:
                    news_with_stock += 1
                    break
    
    # Проверяем Events
    events_with_stock = 0
    for event in Event.objects.all():
        if event.image_url:
            for domain in stock_domains:
                if domain in event.image_url:
                    events_with_stock += 1
                    break
    
    # Проверяем Announcements
    announcements_with_stock = 0
    for announcement in Announcement.objects.all():
        if announcement.image_url:
            for domain in stock_domains:
                if domain in announcement.image_url:
                    announcements_with_stock += 1
                    break
    
    total_stock = news_with_stock + events_with_stock + announcements_with_stock
    
    if total_stock == 0:
        print("✅ Проверка пройдена! Стоковые изображения отсутствуют.")
    else:
        print(f"⚠️ Найдено стоковых изображений:")
        print(f"   - News: {news_with_stock}")
        print(f"   - Events: {events_with_stock}")
        print(f"   - Announcements: {announcements_with_stock}")

if __name__ == '__main__':
    try:
        clean_stock_images()
        verify_cleanup()
        
        print("\n💡 Рекомендации:")
        print("   1. Перезапустите Django сервер для применения изменений")
        print("   2. Добавьте изображения через админку для нужных записей")
        print("   3. Проверьте фронтенд - теперь показываются только реальные изображения")
        
    except Exception as e:
        print(f"❌ Ошибка при очистке: {str(e)}")
        sys.exit(1)
