#!/usr/bin/env python
"""
Скрипт для создания тестовых данных аккредитаций HSM с переводами
"""

import os
import sys
import django
from datetime import date

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from hsm.models import Accreditation

def create_accreditations():
    """Создать аккредитации с переводами"""
    print("Создание аккредитаций с переводами...")
    
    accreditations_data = [
        {
            'name': 'Государственная лицензия на образовательную деятельность',
            'name_kg': 'Билим берүү ишмердүүлүгүнө мамлекеттик лицензия',
            'name_en': 'State License for Educational Activities',
            'organization': 'Министерство образования и науки КР',
            'organization_kg': 'КР Билим берүү жана илим министрлиги',
            'organization_en': 'Ministry of Education and Science of KR',
            'accreditation_type': 'national',
            'accreditation_type_kg': 'Улуттук',
            'accreditation_type_en': 'National',
            'description': 'Лицензия на право ведения образовательной деятельности в сфере высшего образования.',
            'description_kg': 'Жогорку билим берүү тармагында билим берүү ишмердүүлүгүн жүргүзүү укугуна лицензия.',
            'description_en': 'License for the right to conduct educational activities in higher education.',
            'issue_date': date(2010, 9, 15),
            'expiry_date': date(2025, 9, 15),
            'certificate_number': 'Л-001-2010',
            'order': 1
        },
        {
            'name': 'Институциональная аккредитация',
            'name_kg': 'Институционалдык аккредитация',
            'name_en': 'Institutional Accreditation',
            'organization': 'Национальное агентство аккредитации и рейтинга',
            'organization_kg': 'Аккредитация жана рейтинг боюнча улуттук агенттик',
            'organization_en': 'National Agency for Accreditation and Rating',
            'accreditation_type': 'institutional',
            'accreditation_type_kg': 'Институционалдык',
            'accreditation_type_en': 'Institutional',
            'description': 'Подтверждение соответствия образовательной деятельности государственным стандартам.',
            'description_kg': 'Билим берүү ишмердүүлүгүнүн мамлекеттик стандарттарга ылайыктуулугун ырастоо.',
            'description_en': 'Confirmation of compliance of educational activities with state standards.',
            'issue_date': date(2020, 6, 10),
            'expiry_date': date(2026, 6, 10),
            'certificate_number': 'ИА-002-2020',
            'order': 2
        },
        {
            'name': 'Международная аккредитация AACSB',
            'name_kg': 'AACSB эл аралык аккредитациясы',
            'name_en': 'AACSB International Accreditation',
            'organization': 'Association to Advance Collegiate Schools of Business',
            'organization_kg': 'Колледждик бизнес мектептерин өркүндөтүү ассоциациясы',
            'organization_en': 'Association to Advance Collegiate Schools of Business',
            'accreditation_type': 'international',
            'accreditation_type_kg': 'Эл аралык',
            'accreditation_type_en': 'International',
            'description': 'Престижная международная аккредитация бизнес-школ.',
            'description_kg': 'Бизнес-мектептердин престиждүү эл аралык аккредитациясы.',
            'description_en': 'Prestigious international accreditation of business schools.',
            'issue_date': date(2022, 3, 1),
            'expiry_date': date(2027, 3, 1),
            'certificate_number': 'AACSB-2022-001',
            'order': 3
        },
        {
            'name': 'Программная аккредитация MBA',
            'name_kg': 'MBA программалык аккредитациясы',
            'name_en': 'MBA Program Accreditation',
            'organization': 'Международная ассоциация MBA',
            'organization_kg': 'MBA эл аралык ассоциациясы',
            'organization_en': 'International MBA Association',
            'accreditation_type': 'programmatic',
            'accreditation_type_kg': 'Программалык',
            'accreditation_type_en': 'Programmatic',
            'description': 'Аккредитация программы MBA международными стандартами.',
            'description_kg': 'MBA программасынын эл аралык стандарттар боюнча аккредитациясы.',
            'description_en': 'Accreditation of the MBA program according to international standards.',
            'issue_date': date(2021, 11, 20),
            'expiry_date': date(2026, 11, 20),
            'certificate_number': 'MBA-2021-003',
            'order': 4
        }
    ]
    
    created_count = 0
    updated_count = 0
    
    for accreditation_data in accreditations_data:
        accreditation, created = Accreditation.objects.update_or_create(
            name=accreditation_data['name'],
            organization=accreditation_data['organization'],
            defaults=accreditation_data
        )
        if created:
            created_count += 1
        else:
            updated_count += 1
    
    print(f"✓ Создано {created_count} новых аккредитаций")
    print(f"✓ Обновлено {updated_count} существующих аккредитаций")
    return Accreditation.objects.all()

def main():
    """Основная функция для создания данных аккредитаций"""
    print("Начинаем создание/обновление данных аккредитаций HSM с переводами...")
    print("=" * 70)
    
    try:
        # Создаем/обновляем аккредитации
        accreditations = create_accreditations()
        
        print("=" * 70)
        print("✅ Данные аккредитаций успешно созданы/обновлены!")
        print(f"📊 Статистика:")
        print(f"   • Всего аккредитаций: {Accreditation.objects.count()}")
        
        # Проверим переводы
        print("\n🔍 Проверка переводов:")
        for acc in Accreditation.objects.all()[:2]:  # Показать первые 2
            print(f"   • {acc.name}:")
            print(f"     - Тип: {acc.accreditation_type} | KG: {acc.accreditation_type_kg} | EN: {acc.accreditation_type_en}")
            print(f"     - Организация KG: {acc.organization_kg}")
            print(f"     - Организация EN: {acc.organization_en}")
        
    except Exception as e:
        print(f"❌ Ошибка при создании данных: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
