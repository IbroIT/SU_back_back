#!/usr/bin/env python
"""
Скрипт для миграции данных из старой модели Founder в новую модель UniversityFounder
"""
import os
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from about_section.models import Founder, UniversityFounder

def migrate_founders():
    """Мигрирует данные основателей из старой модели в новую"""
    
    print("🔄 Начинаю миграцию данных основателей...")
    
    # Получаем все активные записи из старой модели
    old_founders = Founder.objects.filter(is_active=True).order_by('order')
    
    print(f"📊 Найдено {old_founders.count()} основателей в старой модели")
    
    migrated_count = 0
    
    for old_founder in old_founders:
        try:
            # Проверяем, не существует ли уже такая запись
            existing = UniversityFounder.objects.filter(
                name_ru=old_founder.name_ru
            ).first()
            
            if existing:
                print(f"⚠️  Основатель '{old_founder.name_ru}' уже существует в новой модели")
                continue
            
            # Создаем новую запись
            new_founder = UniversityFounder.objects.create(
                # Основная информация
                name_ru=old_founder.name_ru,
                name_en=old_founder.name_en or '',
                name_ky=old_founder.name_ky or '',
                
                # Должность
                position_ru=old_founder.position_ru or '',
                position_en=old_founder.position_en or '',
                position_ky=old_founder.position_ky or '',
                
                # Годы службы (если есть такое поле)
                years_ru=getattr(old_founder, 'years', '') or '',
                years_en='',
                years_ky='',
                
                # Изображение
                image=old_founder.image,
                
                # Описание
                description_ru=old_founder.description_ru or '',
                description_en=old_founder.description_en or '',
                description_ky=old_founder.description_ky or '',
                
                # Достижения
                achievements_ru=old_founder.achievements if hasattr(old_founder, 'achievements') else [],
                achievements_en=[],
                achievements_ky=[],
                
                # Порядок и статус
                order=old_founder.order,
                is_active=old_founder.is_active,
            )
            
            print(f"✅ Мигрирован: {new_founder.name_ru}")
            migrated_count += 1
            
        except Exception as e:
            print(f"❌ Ошибка при миграции '{old_founder.name_ru}': {e}")
    
    print(f"\n🎉 Миграция завершена! Мигрировано: {migrated_count} основателей")
    
    # Проверяем результат
    total_new = UniversityFounder.objects.count()
    print(f"📈 Всего в новой модели: {total_new} основателей")

if __name__ == "__main__":
    migrate_founders()