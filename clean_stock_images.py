#!/usr/bin/env python
"""
Скрипт для удаления всех стоковых изображений из базы данных
"""
import os
import sys
import django

# Настройка Django
sys.path.append('/Users/adminbaike/medicine/SU_back_back')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from news.models import News, Event, Announcement

def clean_stock_images():
    """Очищаем все стоковые изображения из базы данных"""
    print("🧹 Очистка стоковых изображений из базы данных...")
    print("=" * 60)
    
    # Домены стоковых изображений
    stock_domains = ['unsplash.com', 'picsum.photos', 'lorem', 'placeholder']
    
    # Очистка изображений в новостях
    news_updated = 0
    for news in News.objects.all():
        updated = False
        
        if news.image_url and any(domain in news.image_url for domain in stock_domains):
            print(f"🗑️  Удаляем стоковое изображение из новости: {news.title_ru}")
            news.image_url = None
            updated = True
        
        if updated:
            news.save()
            news_updated += 1
    
    # Очистка изображений в событиях
    events_updated = 0
    for event in Event.objects.all():
        updated = False
        
        if event.image_url and any(domain in event.image_url for domain in stock_domains):
            print(f"🗑️  Удаляем стоковое изображение из события: {event.news.title_ru}")
            event.image_url = None
            updated = True
        
        if updated:
            event.save()
            events_updated += 1
    
    # Очистка изображений в объявлениях
    announcements_updated = 0
    for announcement in Announcement.objects.all():
        updated = False
        
        if announcement.image_url and any(domain in announcement.image_url for domain in stock_domains):
            print(f"🗑️  Удаляем стоковое изображение из объявления: {announcement.news.title_ru}")
            announcement.image_url = None
            updated = True
        
        if updated:
            announcement.save()
            announcements_updated += 1
    
    print("\n✅ Очистка завершена!")
    print(f"Обновлено новостей: {news_updated}")
    print(f"Обновлено событий: {events_updated}")
    print(f"Обновлено объявлений: {announcements_updated}")
    print(f"Всего обновлено: {news_updated + events_updated + announcements_updated}")

def main():
    print("🧹 Удаление стоковых изображений")
    print("=" * 60)
    print("Этот скрипт удалит все стоковые изображения из Unsplash")
    print("и других внешних источников из базы данных.")
    print("Останутся только изображения, загруженные через админку.")
    print()
    
    confirm = input("Продолжить? (y/N): ")
    if confirm.lower() in ['y', 'yes', 'да']:
        clean_stock_images()
    else:
        print("Операция отменена.")

if __name__ == "__main__":
    main()
