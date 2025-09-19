#!/usr/bin/env python
"""
Скрипт для создания тестовых данных для практики
"""

import os
import sys
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from student_life.models import PartnerOrganization, OrganizationSpecialization

def create_internship_test_data():
    """Создание тестовых данных для практики"""
    
    print("Создание тестовых данных для практики...")
    
    # Создаем организации-партнеры
    organizations_data = [
        {
            'name_ru': 'Республиканская клиническая больница',
            'name_kg': 'Республикалык клиникалык ооруканасы',
            'name_en': 'Republican Clinical Hospital',
            'description_ru': 'Ведущая медицинская организация с современным оборудованием',
            'description_kg': 'Заманбап жабдуулар менен алдыңкы медициналык уюм',
            'description_en': 'Leading medical organization with modern equipment',
            'type': 'government',
            'location': 'Бишкек',
            'contact_person': 'Иванов Иван Иванович',
            'phone': '+996 312 123-456',
            'email': 'contact@rkb.kg',
            'website': 'https://rkb.kg',
            'specializations': [
                {
                    'name_ru': 'Кардиология',
                    'name_kg': 'Кардиология',
                    'name_en': 'Cardiology'
                },
                {
                    'name_ru': 'Хирургия',
                    'name_kg': 'Хирургия', 
                    'name_en': 'Surgery'
                }
            ]
        },
        {
            'name_ru': 'Медицинский центр "Здоровье"',
            'name_kg': '"Ден соолук" медициналык борбору',
            'name_en': 'Health Medical Center',
            'description_ru': 'Частная клиника с высоким уровнем сервиса',
            'description_kg': 'Жогорку деңгээлдеги кызмат көрсөтүү менен жеке клиника',
            'description_en': 'Private clinic with high level of service',
            'type': 'private',
            'location': 'Бишкек',
            'contact_person': 'Петрова Анна Сергеевна',
            'phone': '+996 312 987-654',
            'email': 'info@health.kg',
            'website': 'https://health.kg',
            'specializations': [
                {
                    'name_ru': 'Терапия',
                    'name_kg': 'Терапия',
                    'name_en': 'Therapy'
                },
                {
                    'name_ru': 'Педиатрия',
                    'name_kg': 'Педиатрия',
                    'name_en': 'Pediatrics'
                }
            ]
        },
        {
            'name_ru': 'Специализированный онкологический центр',
            'name_kg': 'Адистешкен онкологиялык борбор',
            'name_en': 'Specialized Oncology Center',
            'description_ru': 'Центр по лечению онкологических заболеваний',
            'description_kg': 'Онкологиялык оорулуктарды дарылоо борбору',
            'description_en': 'Center for oncological diseases treatment',
            'type': 'specialized',
            'location': 'Бишкек',
            'contact_person': 'Смирнов Петр Александрович',
            'phone': '+996 312 555-123',
            'email': 'oncology@center.kg',
            'website': 'https://onco-center.kg',
            'specializations': [
                {
                    'name_ru': 'Онкология',
                    'name_kg': 'Онкология',
                    'name_en': 'Oncology'
                },
                {
                    'name_ru': 'Радиология',
                    'name_kg': 'Радиология',
                    'name_en': 'Radiology'
                }
            ]
        }
    ]
    
    for org_data in organizations_data:
        specializations_data = org_data.pop('specializations')
        
        # Создаем или получаем организацию
        organization, created = PartnerOrganization.objects.get_or_create(
            name_ru=org_data['name_ru'],
            defaults=org_data
        )
        
        if created:
            print(f"✅ Создана организация: {organization.name_ru}")
        else:
            print(f"ℹ️  Организация уже существует: {organization.name_ru}")
        
        # Создаем специализации
        for spec_data in specializations_data:
            specialization, spec_created = OrganizationSpecialization.objects.get_or_create(
                organization=organization,
                name_ru=spec_data['name_ru'],
                defaults=spec_data
            )
            
            if spec_created:
                print(f"  ✅ Добавлена специализация: {specialization.name_ru}")
            else:
                print(f"  ℹ️  Специализация уже существует: {specialization.name_ru}")
    
    print(f"\n🎉 Создание тестовых данных завершено!")
    print(f"📊 Всего организаций: {PartnerOrganization.objects.count()}")
    print(f"📊 Всего специализаций: {OrganizationSpecialization.objects.count()}")

if __name__ == '__main__':
    create_internship_test_data()
