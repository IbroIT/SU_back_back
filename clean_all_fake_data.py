#!/usr/bin/env python3
"""
Скрипт для полной очистки всех фейковых данных
"""

import os
import sys
import django

# Добавляем корневую папку проекта в путь Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Настраиваем Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from news.models import News, Event, Announcement


def clean_fake_data():
    """Удаляет все фейковые данные из базы"""
    
    print("🗑️  Начинаем удаление всех фейковых данных...")
    
    # Подсчитываем количество записей перед удалением
    initial_news_count = News.objects.count()
    initial_events_count = Event.objects.count()
    initial_announcements_count = Announcement.objects.count()
    
    print(f"📊 Текущее состояние базы данных:")
    print(f"   - Новости: {initial_news_count}")
    print(f"   - События: {initial_events_count}")
    print(f"   - Объявления: {initial_announcements_count}")
    
    # Удаляем все записи с фейковыми данными (содержащие "lorem", "ipsum", "test", "demo", "example")
    fake_keywords = ['lorem', 'ipsum', 'test', 'demo', 'example', 'фейк', 'тест', 'демо']
    
    deleted_news = 0
    deleted_events = 0
    deleted_announcements = 0
    
    # Удаляем новости с фейковыми заголовками или содержимым
    for keyword in fake_keywords:
        news_to_delete = News.objects.filter(
            models.Q(title_ru__icontains=keyword) |
            models.Q(title_kg__icontains=keyword) |
            models.Q(title_en__icontains=keyword) |
            models.Q(content_ru__icontains=keyword) |
            models.Q(content_kg__icontains=keyword) |
            models.Q(content_en__icontains=keyword) |
            models.Q(summary_ru__icontains=keyword) |
            models.Q(summary_kg__icontains=keyword) |
            models.Q(summary_en__icontains=keyword)
        )
        count = news_to_delete.count()
        if count > 0:
            news_to_delete.delete()
            deleted_news += count
            print(f"   ✅ Удалено {count} новостей с ключевым словом '{keyword}'")
    
    # Удаляем остальные записи, которые могли остаться после удаления новостей
    events_to_delete = Event.objects.filter(news__isnull=True)
    count = events_to_delete.count()
    if count > 0:
        events_to_delete.delete()
        deleted_events += count
        print(f"   ✅ Удалено {count} осиротевших событий")
    
    announcements_to_delete = Announcement.objects.filter(news__isnull=True)
    count = announcements_to_delete.count()
    if count > 0:
        announcements_to_delete.delete()
        deleted_announcements += count
        print(f"   ✅ Удалено {count} осиротевших объявлений")
    
    # Финальная статистика
    final_news_count = News.objects.count()
    final_events_count = Event.objects.count()
    final_announcements_count = Announcement.objects.count()
    
    print(f"\n📈 Результаты очистки:")
    print(f"   - Новости: {initial_news_count} → {final_news_count} (-{deleted_news})")
    print(f"   - События: {initial_events_count} → {final_events_count} (-{deleted_events})")
    print(f"   - Объявления: {initial_announcements_count} → {final_announcements_count} (-{deleted_announcements})")
    
    print(f"\n✅ Очистка завершена! Теперь в базе данных только реальные данные, добавленные через админку.")
    
    return {
        'deleted_news': deleted_news,
        'deleted_events': deleted_events,
        'deleted_announcements': deleted_announcements,
        'final_counts': {
            'news': final_news_count,
            'events': final_events_count,
            'announcements': final_announcements_count
        }
    }


if __name__ == '__main__':
    try:
        from django.db import models
        results = clean_fake_data()
        
        if results['deleted_news'] == 0 and results['deleted_events'] == 0 and results['deleted_announcements'] == 0:
            print("ℹ️  Фейковых данных для удаления не найдено.")
        else:
            print(f"🎉 Успешно очищено {results['deleted_news'] + results['deleted_events'] + results['deleted_announcements']} записей!")
            
    except Exception as e:
        print(f"❌ Ошибка при очистке данных: {e}")
        import traceback
        traceback.print_exc()
