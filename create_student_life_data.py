#!/usr/bin/env python
"""
Скрипт для создания тестовых данных для студенческой жизни
"""
import os
import sys
import django
from datetime import date

# Setup Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from student_life.models import *


def create_partner_organizations():
    """Создание организаций-партнеров"""
    orgs_data = [
        {
            'name': 'Национальный госпиталь при Министерстве здравоохранения КР',
            'type': 'government',
            'location': 'г. Бишкек',
            'contact_person': 'Иванов И.И.',
            'phone': '+996 312 123-456',
            'email': 'internships@nathos.kg',
            'specializations': ['Кардиология', 'Неврология', 'Хирургия', 'Терапия']
        },
        {
            'name': 'Медицинский центр "Адо"',
            'type': 'private',
            'location': 'г. Бишкек',
            'contact_person': 'Петрова А.С.',
            'phone': '+996 312 987-654',
            'email': 'practice@ado.kg',
            'specializations': ['Педиатрия', 'Гинекология', 'Офтальмология']
        },
        {
            'name': 'Областная больница г. Ош',
            'type': 'government',
            'location': 'г. Ош',
            'contact_person': 'Сыдыков М.Т.',
            'phone': '+996 3222 5-67-89',
            'email': 'practice@oshhos.kg',
            'specializations': ['Общая хирургия', 'Внутренние болезни', 'Акушерство']
        },
        {
            'name': 'Республиканский центр кардиологии',
            'type': 'specialized',
            'location': 'г. Бишкек',
            'contact_person': 'Жумабеков К.А.',
            'phone': '+996 312 456-789',
            'email': 'students@cardio.kg',
            'specializations': ['Кардиология', 'Кардиохирургия', 'Интервенционная кардиология']
        }
    ]

    for org_data in orgs_data:
        specializations = org_data.pop('specializations')
        org, created = PartnerOrganization.objects.get_or_create(
            name=org_data['name'],
            defaults=org_data
        )
        if created:
            for spec in specializations:
                OrganizationSpecialization.objects.create(
                    organization=org,
                    name=spec
                )
            print(f"Создана организация: {org.name}")


def create_internship_requirements():
    """Создание требований к практике"""
    requirements_data = [
        {
            'title': 'Академические требования',
            'category': 'academic',
            'items': [
                'Успешное прохождение теоретических курсов',
                'Средний балл не ниже 3.0',
                'Отсутствие академических задолженностей',
                'Прохождение медицинского осмотра'
            ]
        },
        {
            'title': 'Документы для практики',
            'category': 'documents',
            'items': [
                'Направление от университета',
                'Медицинская справка',
                'Справка о прививках',
                'Студенческий билет',
                'Паспорт или удостоверение личности'
            ]
        },
        {
            'title': 'Продолжительность практики',
            'category': 'duration',
            'items': [
                'Учебная практика: 2-4 недели',
                'Производственная практика: 4-6 недель',
                'Преддипломная практика: 8-12 недель',
                'Клиническая практика: по специальности'
            ]
        }
    ]

    for req_data in requirements_data:
        items = req_data.pop('items')
        req, created = InternshipRequirement.objects.get_or_create(
            title=req_data['title'],
            defaults=req_data
        )
        if created:
            for i, item in enumerate(items):
                InternshipRequirementItem.objects.create(
                    requirement=req,
                    text=item,
                    order=i
                )
            print(f"Создано требование: {req.title}")


def create_partner_universities():
    """Создание университетов-партнеров"""
    universities_data = [
        {
            'name': 'Московский государственный медицинский университет им. И.М. Сеченова',
            'country': 'Россия',
            'city': 'Москва',
            'duration': '1-2 семестра',
            'language': 'Русский',
            'gpa_requirement': '3.5',
            'language_cert': 'Не требуется',
            'contact_email': 'international@sechenov.ru',
            'programs': ['Лечебное дело', 'Стоматология', 'Педиатрия']
        },
        {
            'name': 'Казахский Национальный медицинский университет им. С.Д. Асфендиярова',
            'country': 'Казахстан',
            'city': 'Алматы',
            'duration': '1 семестр',
            'language': 'Русский, Казахский',
            'gpa_requirement': '3.0',
            'language_cert': 'Не требуется',
            'contact_email': 'mobility@kaznmu.kz',
            'programs': ['Общая медицина', 'Фармация', 'Общественное здравоохранение']
        },
        {
            'name': 'Medizinische Universität Wien',
            'country': 'Австрия',
            'city': 'Вена',
            'duration': '1 семестр',
            'language': 'English, German',
            'gpa_requirement': '4.0',
            'language_cert': 'IELTS 6.5+ или немецкий B2',
            'contact_email': 'international@meduniwien.ac.at',
            'programs': ['Medicine', 'Dentistry']
        }
    ]

    for uni_data in universities_data:
        programs = uni_data.pop('programs')
        uni, created = PartnerUniversity.objects.get_or_create(
            name=uni_data['name'],
            defaults=uni_data
        )
        if created:
            for program in programs:
                UniversityProgram.objects.create(
                    university=uni,
                    name=program
                )
            print(f"Создан университет: {uni.name}")


def create_student_guides():
    """Создание инструкций для студентов"""
    guides_data = [
        {
            'id_slug': 'academic-leave',
            'title': 'Как оформить академический отпуск',
            'guide_type': 'academic-leave',
            'description': 'Пошаговая инструкция по оформлению академического отпуска',
            'max_duration': 'До 2 лет',
            'contact': 'Деканат, каб. 105, тел. +996 312 123-456',
            'requirements': [
                'Отсутствие академических задолженностей',
                'Уважительная причина для отпуска',
                'Полный пакет документов'
            ],
            'steps': [
                {
                    'step_number': 1,
                    'title': 'Подготовка документов',
                    'description': 'Соберите необходимые документы для подачи заявления',
                    'timeframe': '3-5 дней',
                    'details': [
                        'Заявление на имя ректора (образец в деканате)',
                        'Справка из медицинского учреждения (при болезни)',
                        'Документы, подтверждающие семейные обстоятельства',
                        'Студенческий билет',
                        'Зачетная книжка'
                    ]
                },
                {
                    'step_number': 2,
                    'title': 'Подача документов в деканат',
                    'description': 'Сдайте полный пакет документов в деканат факультета',
                    'timeframe': '1 день',
                    'details': [
                        'Проверка комплектности документов',
                        'Заполнение дополнительных форм',
                        'Получение расписки о приеме документов',
                        'Уведомление о сроках рассмотрения'
                    ]
                }
            ]
        }
    ]

    for guide_data in guides_data:
        requirements = guide_data.pop('requirements')
        steps = guide_data.pop('steps')
        
        guide, created = StudentGuide.objects.get_or_create(
            id_slug=guide_data['id_slug'],
            defaults=guide_data
        )
        
        if created:
            # Создаем требования
            for i, req in enumerate(requirements):
                GuideRequirement.objects.create(
                    guide=guide,
                    text=req,
                    order=i
                )
            
            # Создаем шаги
            for step_data in steps:
                details = step_data.pop('details')
                step = GuideStep.objects.create(
                    guide=guide,
                    **step_data,
                    order=step_data['step_number']
                )
                
                # Создаем детали шага
                for j, detail in enumerate(details):
                    GuideStepDetail.objects.create(
                        step=step,
                        text=detail,
                        order=j
                    )
            
            print(f"Создана инструкция: {guide.title}")


def create_downloadable_documents():
    """Создание документов для скачивания"""
    documents_data = [
        {
            'title': 'Устав университета',
            'description': 'Основной документ, регламентирующий деятельность университета',
            'type': 'charter',
            'file_size': '2.1 MB',
            'format': 'PDF',
            'last_updated': date(2024, 1, 15)
        },
        {
            'title': 'Правила внутреннего распорядка',
            'description': 'Подробные правила поведения студентов и сотрудников',
            'type': 'regulation',
            'file_size': '856 KB',
            'format': 'PDF',
            'last_updated': date(2023, 9, 1)
        },
        {
            'title': 'Кодекс чести студента',
            'description': 'Этические принципы и нормы поведения студентов',
            'type': 'code',
            'file_size': '198 KB',
            'format': 'PDF',
            'last_updated': date(2023, 8, 20)
        }
    ]

    for doc_data in documents_data:
        doc, created = DownloadableDocument.objects.get_or_create(
            title=doc_data['title'],
            defaults=doc_data
        )
        if created:
            print(f"Создан документ: {doc.title}")


def main():
    """Основная функция"""
    print("Создание тестовых данных для студенческой жизни...")
    
    create_partner_organizations()
    create_internship_requirements()
    create_partner_universities()
    create_student_guides()
    create_downloadable_documents()
    
    print("\nТестовые данные успешно созданы!")
    print("\nДоступные API endpoints:")
    print("- /api/student-life/api/data/internships_data/")
    print("- /api/student-life/api/data/academic_mobility_data/")
    print("- /api/student-life/api/data/regulations_data/")
    print("- /api/student-life/api/student-guides/")
    print("- /api/student-life/api/student-appeals/")


if __name__ == '__main__':
    main()
