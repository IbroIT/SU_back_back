#!/usr/bin/env python
"""
Скрипт для добавления тегов на кыргызском и английском языках
"""

import os
import sys
import django

# Настройка Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from careers.models import Vacancy

# Словари для перевода тегов
TAGS_TRANSLATIONS = {
    'ru_to_kg': {
        'Библиотека': 'Китепкана',
        'Каталогизация': 'Каталогдоо',
        'Обслуживание': 'Тейлөө',
        'IT': 'IT',
        'Администрирование': 'Администрациялоо',
        'Техподдержка': 'Техникалык колдоо',
        'Международные связи': 'Эл аралык байланыштар',
        'Администрация': 'Администрация',
        'Образование': 'Билим берүү',
        'Преподавание': 'Окутуу',
        'Наука': 'Илим',
        'Биология': 'Биология',
        'Биохимия': 'Биохимия'
    },
    'ru_to_en': {
        'Библиотека': 'Library',
        'Каталогизация': 'Cataloguing',
        'Обслуживание': 'Service',
        'IT': 'IT',
        'Администрирование': 'Administration',
        'Техподдержка': 'Technical Support',
        'Международные связи': 'International Relations',
        'Администрация': 'Administration',
        'Образование': 'Education',
        'Преподавание': 'Teaching',
        'Наука': 'Science',
        'Биология': 'Biology',
        'Биохимия': 'Biochemistry'
    }
}

def translate_tags():
    print("Начинаем добавление переводов тегов...")
    
    # Получаем все вакансии с русскими тегами
    vacancies_with_ru_tags = Vacancy.objects.exclude(tags_ru='').exclude(tags_ru__isnull=True)
    
    print(f"Найдено {vacancies_with_ru_tags.count()} вакансий с русскими тегами")
    
    for vacancy in vacancies_with_ru_tags:
        print(f"\nВакансия: {vacancy.title_ru}")
        print(f"Русские теги: {vacancy.tags_ru}")
        
        # Получаем список русских тегов
        ru_tags = [tag.strip() for tag in vacancy.tags_ru.split(',')]
        
        # Переводим на кыргызский
        kg_tags = []
        for tag in ru_tags:
            translated = TAGS_TRANSLATIONS['ru_to_kg'].get(tag, tag)
            kg_tags.append(translated)
        
        vacancy.tags_kg = ', '.join(kg_tags)
        print(f"Кыргызские теги: {vacancy.tags_kg}")
        
        # Переводим на английский
        en_tags = []
        for tag in ru_tags:
            translated = TAGS_TRANSLATIONS['ru_to_en'].get(tag, tag)
            en_tags.append(translated)
        
        vacancy.tags_en = ', '.join(en_tags)
        print(f"Английские теги: {vacancy.tags_en}")
        
        # Сохраняем изменения
        vacancy.save()
        print("Сохранено")
    
    print("\nДобавление переводов тегов завершено!")

if __name__ == '__main__':
    translate_tags()
