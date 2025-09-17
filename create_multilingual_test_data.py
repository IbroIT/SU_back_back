#!/usr/bin/env python
import os
import sys
import django

# Добавляем путь к проекту
sys.path.append('/Users/adminbaike/medicine/SU_back_back')

# Устанавливаем переменную окружения
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')

# Инициализируем Django
django.setup()

from student_life.models import PartnerOrganization, StudentAppeal

def create_test_data():
    print("Создание тестовых данных с мультиязычностью...")
    
    # Очистка существующих данных
    PartnerOrganization.objects.all().delete()
    StudentAppeal.objects.all().delete()
    
    # Создание партнерских организаций
    organizations = [
        {
            'name_ru': 'Национальная больница',
            'name_kg': 'Улуттук оорукана',
            'name_en': 'National Hospital',
            'description_ru': 'Ведущая государственная клиника города',
            'description_kg': 'Шаардын башкы мамлекеттик клиникасы',
            'description_en': 'Leading state clinic of the city',
            'type': 'government',
            'location': 'Бишкек, ул. Тоголок Молдо, 3',
            'contact_person': 'Иванов И.И.',
            'phone': '+996 312 123456',
            'email': 'info@nathospital.kg',
            'website': 'https://nathospital.kg',
        },
        {
            'name_ru': 'Медицинский центр "Здоровье"',
            'name_kg': '"Ден соолук" медициналык борбору',
            'name_en': 'Health Medical Center',
            'description_ru': 'Современная частная клиника с новейшим оборудованием',
            'description_kg': 'Заманбап жаңы жабдыктар менен жеке клиника',
            'description_en': 'Modern private clinic with latest equipment',
            'type': 'private',
            'location': 'Бишкек, пр. Чуй, 123',
            'contact_person': 'Петрова А.С.',
            'phone': '+996 312 789012',
            'email': 'info@healthcenter.kg',
            'website': 'https://healthcenter.kg',
        },
        {
            'name_ru': 'Кардиологический центр им. Акунбаева',
            'name_kg': 'Акунбаев атындагы кардиологиялык борбор',
            'name_en': 'Akunbaev Cardiology Center',
            'description_ru': 'Специализированный центр кардиологии и кардиохирургии',
            'description_kg': 'Кардиология жана кардиохирургиянын адистештирилген борбору',
            'description_en': 'Specialized center for cardiology and cardiac surgery',
            'type': 'specialized',
            'location': 'Бишкек, ул. Ахунбаева, 92',
            'contact_person': 'Сыдыков К.М.',
            'phone': '+996 312 345678',
            'email': 'info@cardio.kg',
            'website': 'https://cardio.kg',
        }
    ]
    
    for org_data in organizations:
        org = PartnerOrganization.objects.create(**org_data)
        print(f"✅ Создана организация: {org.name_ru}")
    
    # Создание тестового обращения
    appeal = StudentAppeal.objects.create(
        full_name='Тестовый Студент',
        email='student@test.kg',
        phone='+996 700 123456',
        student_id='ST2024001',
        category='academic',
        subject='Тестовое обращение по академическим вопросам',
        message='Это тестовое сообщение для проверки работы системы обращений.',
        status='new'
    )
    print(f"✅ Создано обращение: {appeal.subject}")
    
    print("\n🎉 Тестовые данные успешно созданы!")
    print(f"📊 Организаций: {PartnerOrganization.objects.count()}")
    print(f"📊 Обращений: {StudentAppeal.objects.count()}")

if __name__ == '__main__':
    create_test_data()
