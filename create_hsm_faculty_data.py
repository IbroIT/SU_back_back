#!/usr/bin/env python
"""
Скрипт для создания тестовых данных преподавателей HSM с переводами
"""

import os
import sys
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from hsm.models import Faculty

def create_faculty():
    """Создать профессорско-преподавательский состав с переводами"""
    print("Создание ППС с переводами...")
    
    faculty_data = [
        {
            'first_name': 'Азамат',
            'last_name': 'Салымбеков',
            'middle_name': 'Рустамович',
            'first_name_kg': 'Азамат',
            'last_name_kg': 'Салымбеков',
            'middle_name_kg': 'Рустамович',
            'first_name_en': 'Azamat',
            'last_name_en': 'Salymbekov',
            'position': 'dean',
            'position_kg': 'Декан',
            'position_en': 'Dean',
            'academic_degree': 'doctor',
            'academic_degree_kg': 'Илимдин доктору',
            'academic_degree_en': 'Doctor of Sciences',
            'academic_title': 'Профессор',
            'academic_title_kg': 'Профессор',
            'academic_title_en': 'Professor',
            'email': 'a.salymbekov@salymbekov.edu.kg',
            'phone': '+996 312 123456',
            'office': 'Корпус А, 301',
            'bio': 'Доктор экономических наук, профессор. Основатель и ректор Салымбекова Университета.',
            'bio_kg': 'Экономика илимдеринин доктору, профессор. Салымбеков Университетинин негиздөөчүсү жана ректору.',
            'bio_en': 'Doctor of Economics, Professor. Founder and Rector of Salymbekov University.',
            'specialization': 'Стратегический менеджмент, предпринимательство',
            'specialization_kg': 'Стратегиялык менеджмент, ишкердик',
            'specialization_en': 'Strategic management, entrepreneurship',
            'order': 1
        },
        {
            'first_name': 'Гульнара',
            'last_name': 'Иманова',
            'middle_name': 'Асановна',
            'first_name_kg': 'Гүлнара',
            'last_name_kg': 'Иманова',
            'middle_name_kg': 'Асан кызы',
            'first_name_en': 'Gulnara',
            'last_name_en': 'Imanova',
            'position': 'professor',
            'position_kg': 'Профессор',
            'position_en': 'Professor',
            'academic_degree': 'doctor',
            'academic_degree_kg': 'Илимдин доктору',
            'academic_degree_en': 'Doctor of Sciences',
            'academic_title': 'Профессор',
            'academic_title_kg': 'Профессор',
            'academic_title_en': 'Professor',
            'email': 'g.imanova@salymbekov.edu.kg',
            'phone': '+996 312 123457',
            'office': 'Корпус А, 302',
            'bio': 'Доктор экономических наук, эксперт в области финансового менеджмента.',
            'bio_kg': 'Экономика илимдеринин доктору, каржылык менеджмент тармагындагы эксперт.',
            'bio_en': 'Doctor of Economics, expert in financial management.',
            'specialization': 'Финансовый менеджмент, корпоративные финансы',
            'specialization_kg': 'Каржылык менеджмент, корпоративдик каржы',
            'specialization_en': 'Financial management, corporate finance',
            'order': 2
        },
        {
            'first_name': 'Бакыт',
            'last_name': 'Жумабеков',
            'middle_name': 'Эркинович',
            'first_name_kg': 'Бакыт',
            'last_name_kg': 'Жумабеков',
            'middle_name_kg': 'Эркин уулу',
            'first_name_en': 'Bakyt',
            'last_name_en': 'Zhumabekov',
            'position': 'associate_professor',
            'position_kg': 'Доцент',
            'position_en': 'Associate Professor',
            'academic_degree': 'candidate',
            'academic_degree_kg': 'Илимдин кандидаты',
            'academic_degree_en': 'Candidate of Sciences',
            'academic_title': 'Доцент',
            'academic_title_kg': 'Доцент',
            'academic_title_en': 'Associate Professor',
            'email': 'b.zhumabekov@salymbekov.edu.kg',
            'phone': '+996 312 123458',
            'office': 'Корпус А, 303',
            'bio': 'Кандидат экономических наук, специалист по маркетингу и управлению персоналом.',
            'bio_kg': 'Экономика илимдеринин кандидаты, маркетинг жана кадрларды башкаруу боюнча адис.',
            'bio_en': 'Candidate of Economic Sciences, specialist in marketing and human resource management.',
            'specialization': 'Маркетинг, управление персоналом',
            'specialization_kg': 'Маркетинг, кадрларды башкаруу',
            'specialization_en': 'Marketing, human resource management',
            'order': 3
        },
        {
            'first_name': 'Айжан',
            'last_name': 'Токтогулова',
            'middle_name': 'Мирлановна',
            'first_name_kg': 'Айжан',
            'last_name_kg': 'Токтогулова',
            'middle_name_kg': 'Мирлан кызы',
            'first_name_en': 'Aizhan',
            'last_name_en': 'Toktogulova',
            'position': 'senior_lecturer',
            'position_kg': 'Улук окутуучу',
            'position_en': 'Senior Lecturer',
            'academic_degree': 'master',
            'academic_degree_kg': 'Магистр',
            'academic_degree_en': 'Master',
            'email': 'a.toktogulova@salymbekov.edu.kg',
            'phone': '+996 312 123459',
            'office': 'Корпус А, 304',
            'bio': 'Магистр делового администрирования, практикующий консультант.',
            'bio_kg': 'Ишкердик администрациялоонун магистри, практикалык консультант.',
            'bio_en': 'Master of Business Administration, practicing consultant.',
            'specialization': 'Проектный менеджмент, бизнес-консалтинг',
            'specialization_kg': 'Долбоорлук менеджмент, бизнес-консалтинг',
            'specialization_en': 'Project management, business consulting',
            'order': 4
        },
        {
            'first_name': 'Нурбек',
            'last_name': 'Осмонов',
            'middle_name': 'Талантович',
            'first_name_kg': 'Нурбек',
            'last_name_kg': 'Осмонов',
            'middle_name_kg': 'Талант уулу',
            'first_name_en': 'Nurbek',
            'last_name_en': 'Osmonov',
            'position': 'lecturer',
            'position_kg': 'Окутуучу',
            'position_en': 'Lecturer',
            'academic_degree': 'master',
            'academic_degree_kg': 'Магистр',
            'academic_degree_en': 'Master',
            'email': 'n.osmonov@salymbekov.edu.kg',
            'phone': '+996 312 123460',
            'office': 'Корпус А, 305',
            'bio': 'Магистр экономических наук, специалист по цифровой экономике.',
            'bio_kg': 'Экономика илимдеринин магистри, санариптик экономика боюнча адис.',
            'bio_en': 'Master of Economics, specialist in digital economy.',
            'specialization': 'Цифровая экономика, инновации',
            'specialization_kg': 'Санариптик экономика, инновациялар',
            'specialization_en': 'Digital economy, innovations',
            'order': 5
        },
        {
            'first_name': 'Анара',
            'last_name': 'Турсунова',
            'middle_name': 'Бакытовна',
            'first_name_kg': 'Анара',
            'last_name_kg': 'Турсунова',
            'middle_name_kg': 'Бакыт кызы',
            'first_name_en': 'Anara',
            'last_name_en': 'Tursunova',
            'position': 'assistant',
            'position_kg': 'Ассистент',
            'position_en': 'Assistant',
            'academic_degree': 'bachelor',
            'academic_degree_kg': 'Бакалавр',
            'academic_degree_en': 'Bachelor',
            'email': 'a.tursunova@salymbekov.edu.kg',
            'phone': '+996 312 123461',
            'office': 'Корпус А, 306',
            'bio': 'Бакалавр экономических наук, молодой специалист.',
            'bio_kg': 'Экономика илимдеринин бакалавры, жаш адис.',
            'bio_en': 'Bachelor of Economics, young specialist.',
            'specialization': 'Общий менеджмент',
            'specialization_kg': 'Жалпы менеджмент',
            'specialization_en': 'General management',
            'order': 6
        }
    ]
    
    created_count = 0
    updated_count = 0
    
    for faculty_member_data in faculty_data:
        faculty_member, created = Faculty.objects.update_or_create(
            first_name=faculty_member_data['first_name'],
            last_name=faculty_member_data['last_name'],
            middle_name=faculty_member_data['middle_name'],
            defaults=faculty_member_data
        )
        if created:
            created_count += 1
        else:
            updated_count += 1
    
    print(f"✓ Создано {created_count} новых преподавателей")
    print(f"✓ Обновлено {updated_count} существующих преподавателей")
    return Faculty.objects.all()

def main():
    """Основная функция для создания данных преподавателей"""
    print("Начинаем создание/обновление данных преподавателей HSM с переводами...")
    print("=" * 60)
    
    try:
        # Создаем/обновляем ППС
        faculty = create_faculty()
        
        print("=" * 60)
        print("✅ Данные преподавателей успешно созданы/обновлены!")
        print(f"📊 Статистика:")
        print(f"   • Всего преподавателей: {Faculty.objects.count()}")
        
        # Проверим переводы
        print("\n🔍 Проверка переводов:")
        for f in Faculty.objects.all()[:2]:  # Показать первых 2
            print(f"   • {f.full_name}:")
            print(f"     - Должность: {f.position} | KG: {f.position_kg} | EN: {f.position_en}")
            print(f"     - Степень: {f.academic_degree} | KG: {f.academic_degree_kg} | EN: {f.academic_degree_en}")
        
    except Exception as e:
        print(f"❌ Ошибка при создании данных: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
