#!/usr/bin/env python
"""
Скрипт для создания тестовых данных для документов
"""
import os
import sys
import django
from datetime import datetime

# Setup Django
sys.path.append('/Users/adminbaike/medicine/SU_back_back')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from documents.models import Document, DocumentCategory


def create_test_data():
    """Создание тестовых данных для документов"""
    
    print("Создание категорий документов...")
    
    # Создание категорий
    categories = [
        {
            'name': 'foundational',
            'name_ru': 'Учредительные документы',
            'name_en': 'Founding Documents',
            'name_kg': 'Түзүүчү документтер'
        },
        {
            'name': 'academic',
            'name_ru': 'Учебная деятельность',
            'name_en': 'Academic Activities',
            'name_kg': 'Окуу ишмердүүлүгү'
        },
        {
            'name': 'administrative',
            'name_ru': 'Административная деятельность',
            'name_en': 'Administrative Activities',
            'name_kg': 'Административдик ишмердүүлүк'
        },
        {
            'name': 'research',
            'name_ru': 'Научная деятельность',
            'name_en': 'Research Activities',
            'name_kg': 'Илимий ишмердүүлүк'
        }
    ]
    
    for cat_data in categories:
        category, created = DocumentCategory.objects.get_or_create(
            name=cat_data['name'],
            defaults=cat_data
        )
        if created:
            print(f"Создана категория: {category.name_ru}")
        else:
            print(f"Категория уже существует: {category.name_ru}")
    
    print("\nСоздание документов...")
    
    # Получение категорий
    foundational = DocumentCategory.objects.get(name='foundational')
    academic = DocumentCategory.objects.get(name='academic')
    administrative = DocumentCategory.objects.get(name='administrative')
    research = DocumentCategory.objects.get(name='research')
    
    # Создание документов
    documents = [
        {
            'title_ru': 'Устав Университета Салымбекова',
            'title_en': 'Salymbekov University Charter',
            'title_kg': 'Салымбеков Университетинин уставы',
            'description_ru': 'Основной учредительный документ, определяющий правовой статус, цели, задачи и порядок деятельности университета',
            'description_en': 'The main founding document defining the legal status, goals, objectives and operating procedures of the university',
            'description_kg': 'Университеттин укуктук статусун, максаттарын, милдеттерин жана иш тартибин аныктаган негизги түзүүчү документ',
            'category': foundational,
            'file_size': '2.4 MB',
            'order': 1
        },
        {
            'title_ru': 'Положение об организации учебного процесса',
            'title_en': 'Academic Process Organization Regulations',
            'title_kg': 'Окуу процессин уюштуруу жөнүндө эреже',
            'description_ru': 'Регламентирует порядок организации и проведения учебного процесса в университете',
            'description_en': 'Regulates the organization and conduct of the educational process at the university',
            'description_kg': 'Университетте окуу процессин уюштуруу жана өткөрүү тартибин жөнгө салат',
            'category': academic,
            'file_size': '1.8 MB',
            'order': 2
        },
        {
            'title_ru': 'Правила приема в университет',
            'title_en': 'University Admission Rules',
            'title_kg': 'Университетке кабыл алуу эрежелери',
            'description_ru': 'Определяет порядок приема студентов на образовательные программы университета',
            'description_en': 'Defines the procedure for admitting students to university educational programs',
            'description_kg': 'Студенттерди университеттин билим берүү программаларына кабыл алуу тартибин аныктайт',
            'category': academic,
            'file_size': '1.2 MB',
            'order': 3
        },
        {
            'title_ru': 'Положение о студентах',
            'title_en': 'Student Regulations',
            'title_kg': 'Студенттер жөнүндө эреже',
            'description_ru': 'Регламентирует права, обязанности и порядок обучения студентов',
            'description_en': 'Regulates the rights, duties and procedures for student education',
            'description_kg': 'Студенттердин укуктарын, милдеттерин жана окуу тартибин жөнгө салат',
            'category': academic,
            'file_size': '950 KB',
            'order': 4
        },
        {
            'title_ru': 'Положение о профессорско-преподавательском составе',
            'title_en': 'Faculty and Staff Regulations',
            'title_kg': 'Профессордук-окутуучулук курам жөнүндө эреже',
            'description_ru': 'Определяет требования к ППС, порядок трудоустройства и аттестации',
            'description_en': 'Defines requirements for faculty, employment procedures and certification',
            'description_kg': 'ППСка болгон талаптарды, жумушка орноштуруу жана аттестация тартибин аныктайт',
            'category': administrative,
            'file_size': '1.1 MB',
            'order': 5
        },
        {
            'title_ru': 'Положение о научно-исследовательской деятельности',
            'title_en': 'Research Activity Regulations',
            'title_kg': 'Илимий-изилдөө ишмердүүлүгү жөнүндө эреже',
            'description_ru': 'Регламентирует организацию и проведение научных исследований в университете',
            'description_en': 'Regulates the organization and conduct of research at the university',
            'description_kg': 'Университетте илимий изилдөөлөрдү уюштуруу жана өткөрүүнү жөнгө салат',
            'category': research,
            'file_size': '1.5 MB',
            'order': 6
        },
        {
            'title_ru': 'Положение о системе обеспечения качества образования',
            'title_en': 'Educational Quality Assurance System Regulations',
            'title_kg': 'Билим берүү сапатын камсыз кылуу системасы жөнүндө эреже',
            'description_ru': 'Определяет принципы и механизмы обеспечения качества образовательных услуг',
            'description_en': 'Defines principles and mechanisms for ensuring the quality of educational services',
            'description_kg': 'Билим берүү кызматтарынын сапатын камсыз кылуунун принциптери жана механизмдерин аныктайт',
            'category': academic,
            'file_size': '2.1 MB',
            'order': 7
        },
        {
            'title_ru': 'Положение о библиотеке',
            'title_en': 'Library Regulations',
            'title_kg': 'Китепкана жөнүндө эреже',
            'description_ru': 'Регламентирует деятельность библиотеки и порядок пользования библиотечными ресурсами',
            'description_en': 'Regulates library activities and procedures for using library resources',
            'description_kg': 'Китепкананын ишмердүүлүгүн жана китепкана ресурстарын пайдалануу тартибин жөнгө салат',
            'category': administrative,
            'file_size': '800 KB',
            'order': 8
        }
    ]
    
    for doc_data in documents:
        document, created = Document.objects.get_or_create(
            title_ru=doc_data['title_ru'],
            defaults=doc_data
        )
        if created:
            print(f"Создан документ: {document.title_ru}")
        else:
            print(f"Документ уже существует: {document.title_ru}")
    
    print(f"\nВсего создано:")
    print(f"- Категорий: {DocumentCategory.objects.count()}")
    print(f"- Документов: {Document.objects.count()}")
    print("\nТестовые данные успешно созданы!")


if __name__ == '__main__':
    create_test_data()
