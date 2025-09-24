#!/usr/bin/env python
import os
import sys
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from news.models import News

def make_featured():
    """Делаем некоторые новости рекомендуемыми"""
    try:
        # Получаем первые две новости и делаем их рекомендуемыми
        news_items = News.objects.filter(is_published=True)[:2]
        
        for news in news_items:
            news.is_featured = True
            news.save()
            print(f"✅ Новость '{news.title_ru}' теперь рекомендуемая")
            
        print(f"\n🎉 Успешно обновлено {len(news_items)} новостей")
        
        # Проверяем результат
        featured_count = News.objects.filter(is_featured=True).count()
        print(f"📊 Всего рекомендуемых новостей: {featured_count}")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    make_featured()
