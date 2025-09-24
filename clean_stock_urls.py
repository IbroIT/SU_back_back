#!/usr/bin/env python
import os
import sys
import django

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from news.models import News, Event, Announcement

def clean_stock_image_urls():
    """Удаляет записи со стоковыми URL-адресами изображений"""
    
    # Паттерны для определения стоковых изображений
    stock_patterns = [
        'unsplash.com',
        'picsum.photos',
        'placeholder',
        'example.com',
        'stock-photo',
        'shutterstock',
        'getty',
        'pexels.com',
        'dummyimage.com',
        'placehold.it',
        'via.placeholder.com',
        'placeimg.com',
        'lorempixel.com'
    ]
    
    print("🔍 Поиск и очистка стоковых URL изображений...")
    
    # Очистка в таблице News
    news_cleaned = 0
    for news in News.objects.all():
        if news.image:
            image_str = str(news.image)
            if any(pattern in image_str for pattern in stock_patterns):
                print(f"  ❌ Удаление стокового изображения из новости: {news.title_ru}")
                news.image = None
                news.save()
                news_cleaned += 1
    
    print(f"\n✅ Очистка завершена:")
    print(f"  - Новости: {news_cleaned} стоковых изображений удалено")

def show_all_news_with_images():
    """Показывает все новости с изображениями"""
    
    print("\n📊 Все новости с изображениями:")
    
    news_with_images = News.objects.filter(image__isnull=False).exclude(image='')
    print(f"\n📰 Новости с изображениями ({news_with_images.count()}):")
    for news in news_with_images:
        print(f"  - {news.title_ru} | Изображение: {news.image}")
    
    # Показываем события
    events = Event.objects.all()
    print(f"\n📅 События ({events.count()}):")
    for event in events:
        if event.news and event.news.image:
            print(f"  - {event.news.title_ru} | ✅ Есть изображение: {event.news.image}")
        else:
            print(f"  - {event.news.title_ru if event.news else 'Без названия'} | ❌ Нет изображения")
    
    # Показываем объявления
    announcements = Announcement.objects.all()
    print(f"\n📢 Объявления ({announcements.count()}):")
    for announcement in announcements:
        if announcement.news and announcement.news.image:
            print(f"  - {announcement.news.title_ru} | ✅ Есть изображение: {announcement.news.image}")
        else:
            print(f"  - {announcement.news.title_ru if announcement.news else 'Без названия'} | ❌ Нет изображения")

if __name__ == '__main__':
    print("🚀 Начало очистки стоковых URL изображений...")
    
    # Показываем текущее состояние
    show_all_news_with_images()
    
    # Очищаем стоковые URL
    clean_stock_image_urls()
    
    # Показываем результат
    print("\n" + "="*50)
    print("ПОСЛЕ ОЧИСТКИ:")
    show_all_news_with_images()
    
    print("\n🎉 Очистка завершена! Остались только реальные изображения, загруженные через админку.")
