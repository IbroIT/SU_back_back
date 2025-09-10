#!/usr/bin/env python
"""
Скрипт для переноса тегов из старого поля в новые мультиязычные поля
"""

import os
import sys
import django

# Настройка Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from careers.models import Vacancy

def migrate_tags():
    print("Начинаем перенос тегов...")
    
    # Получаем все вакансии с заполненными тегами
    vacancies_with_tags = Vacancy.objects.exclude(tags='').exclude(tags__isnull=True)
    
    print(f"Найдено {vacancies_with_tags.count()} вакансий с тегами")
    
    for vacancy in vacancies_with_tags:
        print(f"\nВакансия: {vacancy.title_ru}")
        print(f"Старые теги: {vacancy.tags}")
        
        # Копируем теги в русское поле (по умолчанию)
        if vacancy.tags and not vacancy.tags_ru:
            vacancy.tags_ru = vacancy.tags
            print(f"Скопировано в tags_ru: {vacancy.tags_ru}")
        
        # Сохраняем изменения
        vacancy.save()
        print("Сохранено")
    
    print("\nПеренос тегов завершен!")

if __name__ == '__main__':
    migrate_tags()
