#!/usr/bin/env python3
"""
Скрипт для создания тестовых данных для моделей student_life (академическая мобильность)
"""

import os
import sys
import django

# Настройка Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from student_life.models import (
    MobilityRequirement, PartnerUniversity, UniversityProgram, 
    ExchangeOpportunity, ExchangeBenefit, PartnerOrganization,
    OrganizationSpecialization, InternshipRequirement, InternshipRequirementItem,
    ReportTemplate, InternalRule, InternalRuleItem, AcademicRegulation,
    AcademicRegulationSection, AcademicRegulationRule, DownloadableDocument,
    StudentGuide, GuideRequirement, GuideStep, GuideStepDetail,
    StudentAppeal
)

def create_mobility_requirements():
    """Создание требований для академической мобильности"""
    print("Создание требований для академической мобильности...")
    
    # Академические требования
    academic_req = MobilityRequirement.objects.create(
        title_ru="Академические требования",
        title_kg="Академиялык талаптар",
        title_en="Academic Requirements",
        description_ru="Основные академические требования для участия в программах мобильности",
        description_kg="Мобилдүүлүк программаларына катышуу үчүн негизги академиялык талаптар",
        description_en="Basic academic requirements for participation in mobility programs",
        category="academic",
        order=1
    )
    
    # Языковые требования
    language_req = MobilityRequirement.objects.create(
        title_ru="Языковые требования",
        title_kg="Тил талаптары",
        title_en="Language Requirements",
        description_ru="Требования к знанию языков для обучения за рубежом",
        description_kg="Чет өлкөдө окуу үчүн тил билүү талаптары",
        description_en="Language proficiency requirements for studying abroad",
        category="language",
        order=2
    )
    
    # Документы
    documents_req = MobilityRequirement.objects.create(
        title_ru="Необходимые документы",
        title_kg="Керектүү документтер",
        title_en="Required Documents",
        description_ru="Полный список документов для подачи заявки",
        description_kg="Арыз берүү үчүн документтердин толук тизмеси",
        description_en="Complete list of documents for application",
        category="documents",
        order=3
    )
    
    print(f"✅ Создано {MobilityRequirement.objects.count()} требований мобильности")

def create_partner_universities():
    """Создание университетов-партнеров"""
    print("Создание университетов-партнеров...")
    
    universities = [
        {
            'name_ru': 'Гарвардский университет',
            'name_kg': 'Гарвард университети',
            'name_en': 'Harvard University',
            'description_ru': 'Престижный американский университет с богатой историей',
            'description_kg': 'Бай тарыхы бар престиждүү америкалык университет',
            'description_en': 'Prestigious American university with rich history',
            'country': 'США',
            'city': 'Кембридж',
            'website': 'https://www.harvard.edu'
        },
        {
            'name_ru': 'Московский государственный университет',
            'name_kg': 'Москва мамлекеттик университети',
            'name_en': 'Moscow State University',
            'description_ru': 'Ведущий российский университет',
            'description_kg': 'Россиянын алдыңкы университети',
            'description_en': 'Leading Russian university',
            'country': 'Россия',
            'city': 'Москва',
            'website': 'https://www.msu.ru'
        },
        {
            'name_ru': 'Берлинский университет Гумбольдта',
            'name_kg': 'Гумбольдттун Берлин университети',
            'name_en': 'Humboldt University of Berlin',
            'description_ru': 'Известный немецкий университет',
            'description_kg': 'Белгилүү немис университети',
            'description_en': 'Famous German university',
            'country': 'Германия',
            'city': 'Берлин',
            'website': 'https://www.hu-berlin.de'
        }
    ]
    
    for uni_data in universities:
        university = PartnerUniversity.objects.create(**uni_data)
        
        # Создаем программы для каждого университета
        programs = [
            {
                'name_ru': 'Медицинский обмен',
                'name_kg': 'Медициналык алмашуу',
                'name_en': 'Medical Exchange',
                'description_ru': 'Программа обмена для студентов медицинских специальностей',
                'description_kg': 'Медициналык адистиктердин студенттери үчүн алмашуу программасы',
                'description_en': 'Exchange program for medical students',
                'duration': '1 семестр',
                'language': 'Английский'
            },
            {
                'name_ru': 'Исследовательская стажировка',
                'name_kg': 'Изилдөө стажировкасы',
                'name_en': 'Research Internship',
                'description_ru': 'Исследовательская программа для аспирантов',
                'description_kg': 'Аспиранттар үчүн изилдөө программасы',
                'description_en': 'Research program for graduate students',
                'duration': '6 месяцев',
                'language': 'Английский/Местный'
            }
        ]
        
        for prog_data in programs:
            UniversityProgram.objects.create(university=university, **prog_data)
    
    print(f"✅ Создано {PartnerUniversity.objects.count()} университетов-партнеров")
    print(f"✅ Создано {UniversityProgram.objects.count()} программ обмена")

def create_exchange_opportunities():
    """Создание возможностей обмена"""
    print("Создание возможностей обмена...")
    
    opportunities = [
        {
            'title_ru': 'Семестровый обмен',
            'title_kg': 'Семестрлик алмашуу',
            'title_en': 'Semester Exchange',
            'description_ru': 'Обучение в зарубежном университете в течение одного семестра',
            'description_kg': 'Чет өлкөлүк университетте бир семестр окуу',
            'description_en': 'Study at a foreign university for one semester',
            'type': 'semester'
        },
        {
            'title_ru': 'Годовой обмен',
            'title_kg': 'Жылдык алмашуу',
            'title_en': 'Year-long Exchange',
            'description_ru': 'Обучение в зарубежном университете в течение академического года',
            'description_kg': 'Чет өлкөлүк университетте академиялык жыл бою окуу',
            'description_en': 'Study at a foreign university for an academic year',
            'type': 'year'
        }
    ]
    
    for opp_data in opportunities:
        opportunity = ExchangeOpportunity.objects.create(**opp_data)
        
        # Создаем преимущества для каждой возможности
        benefits = [
            {
                'text_ru': 'Получение международного опыта',
                'text_kg': 'Эл аралык тажрыйба алуу',
                'text_en': 'Gaining international experience',
                'order': 1
            },
            {
                'text_ru': 'Изучение новых методов обучения',
                'text_kg': 'Жаңы окутуу ыкмаларын үйрөнүү',
                'text_en': 'Learning new teaching methods',
                'order': 2
            },
            {
                'text_ru': 'Расширение академической сети',
                'text_kg': 'Академиялык тармакты кеңейтүү',
                'text_en': 'Expanding academic network',
                'order': 3
            }
        ]
        
        for benefit_data in benefits:
            ExchangeBenefit.objects.create(opportunity=opportunity, **benefit_data)
    
    print(f"✅ Создано {ExchangeOpportunity.objects.count()} возможностей обмена")
    print(f"✅ Создано {ExchangeBenefit.objects.count()} преимуществ")

def create_partner_organizations():
    """Создание организаций-партнеров для практики"""
    print("Создание организаций-партнеров для практики...")
    
    organizations = [
        {
            'name_ru': 'Национальный госпиталь',
            'name_kg': 'Улуттук госпиталь',
            'name_en': 'National Hospital',
            'description_ru': 'Ведущая государственная клиника страны',
            'description_kg': 'Өлкөнүн алдыңкы мамлекеттик клиникасы',
            'description_en': 'Leading state clinic of the country',
            'type': 'government',
            'location': 'Бишкек',
            'contact_person': 'Иванов И.И.',
            'phone': '+996 312 123456',
            'email': 'info@national-hospital.kg'
        },
        {
            'name_ru': 'Медицинский центр "Здоровье"',
            'name_kg': '"Ден соолук" медициналык борбору',
            'name_en': 'Health Medical Center',
            'description_ru': 'Современная частная клиника',
            'description_kg': 'Заманбап жеке клиника',
            'description_en': 'Modern private clinic',
            'type': 'private',
            'location': 'Бишкек',
            'contact_person': 'Петров П.П.',
            'phone': '+996 312 654321',
            'email': 'contact@health-center.kg'
        }
    ]
    
    for org_data in organizations:
        organization = PartnerOrganization.objects.create(**org_data)
        
        # Создаем специализации
        specializations = [
            {
                'name_ru': 'Кардиология',
                'name_kg': 'Кардиология',
                'name_en': 'Cardiology'
            },
            {
                'name_ru': 'Терапия',
                'name_kg': 'Терапия',
                'name_en': 'Therapy'
            }
        ]
        
        for spec_data in specializations:
            OrganizationSpecialization.objects.create(organization=organization, **spec_data)
    
    print(f"✅ Создано {PartnerOrganization.objects.count()} организаций-партнеров")
    print(f"✅ Создано {OrganizationSpecialization.objects.count()} специализаций")

def create_internship_requirements():
    """Создание требований к практике"""
    print("Создание требований к практике...")
    
    requirements = [
        {
            'title_ru': 'Академические требования',
            'title_kg': 'Академиялык талаптар',
            'title_en': 'Academic Requirements',
            'description_ru': 'Требования к академической успеваемости',
            'description_kg': 'Академиялык ийгиликке талаптар',
            'description_en': 'Academic performance requirements',
            'category': 'academic',
            'order': 1
        },
        {
            'title_ru': 'Необходимые документы',
            'title_kg': 'Керектүү документтер',
            'title_en': 'Required Documents',
            'description_ru': 'Документы для прохождения практики',
            'description_kg': 'Практика өтүү үчүн документтер',
            'description_en': 'Documents for internship',
            'category': 'documents',
            'order': 2
        }
    ]
    
    for req_data in requirements:
        requirement = InternshipRequirement.objects.create(**req_data)
        
        # Создаем элементы требований
        items = [
            {
                'text_ru': 'Средний балл не менее 3.5',
                'text_kg': 'Орточо баа 3.5тен кем эмес',
                'text_en': 'GPA not less than 3.5',
                'order': 1
            },
            {
                'text_ru': 'Завершение базовых курсов',
                'text_kg': 'Базалык курстарды аяктоо',
                'text_en': 'Completion of basic courses',
                'order': 2
            }
        ]
        
        for item_data in items:
            InternshipRequirementItem.objects.create(requirement=requirement, **item_data)
    
    print(f"✅ Создано {InternshipRequirement.objects.count()} требований к практике")
    print(f"✅ Создано {InternshipRequirementItem.objects.count()} элементов требований")

def create_report_templates():
    """Создание шаблонов отчетов"""
    print("Создание шаблонов отчетов...")
    
    templates = [
        {
            'name_ru': 'Отчет по клинической практике',
            'name_kg': 'Клиникалык практика боюнча отчет',
            'name_en': 'Clinical Practice Report',
            'description_ru': 'Стандартный шаблон отчета по клинической практике',
            'description_kg': 'Клиникалык практика боюнча стандарттык отчет үлгүсү',
            'description_en': 'Standard clinical practice report template'
        },
        {
            'name_ru': 'Отчет по исследовательской работе',
            'name_kg': 'Изилдөө иши боюнча отчет',
            'name_en': 'Research Work Report',
            'description_ru': 'Шаблон для отчета по исследовательской деятельности',
            'description_kg': 'Изилдөө ишмердүүлүгү боюнча отчет үлгүсү',
            'description_en': 'Research activity report template'
        }
    ]
    
    # Примечание: файлы нужно будет добавить отдельно
    for template_data in templates:
        # Добавляем поле file с заглушкой
        template_data['file'] = 'report_templates/placeholder.pdf'
        ReportTemplate.objects.create(**template_data)
    
    print(f"✅ Создано {ReportTemplate.objects.count()} шаблонов отчетов")

def create_student_appeals():
    """Создание тестовых обращений студентов"""
    print("Создание тестовых обращений студентов...")
    
    appeals = [
        {
            'full_name': 'Айтматов Чингиз Торекулович',
            'email': 'aitmatov@student.edu.kg',
            'phone': '+996 555 123456',
            'student_id': 'MED-2021-001',
            'category': 'academic',
            'subject': 'Вопрос по академической мобильности',
            'message': 'Хотел бы узнать подробности программы обмена с европейскими университетами.',
            'status': 'new'
        },
        {
            'full_name': 'Токтогулова Айсулуу Бакытовна',
            'email': 'toktogulova@student.edu.kg',
            'phone': '+996 555 654321',
            'student_id': 'MED-2020-045',
            'category': 'administrative',
            'subject': 'Справка для практики',
            'message': 'Необходима справка для прохождения практики в частной клинике.',
            'status': 'in_progress',
            'response': 'Справка будет готова в течение 3 рабочих дней.'
        }
    ]
    
    for appeal_data in appeals:
        StudentAppeal.objects.create(**appeal_data)
    
    print(f"✅ Создано {StudentAppeal.objects.count()} обращений студентов")

def main():
    """Основная функция"""
    print("🚀 Создание тестовых данных для student_life (академическая мобильность)...")
    print("=" * 60)
    
    try:
        create_mobility_requirements()
        create_partner_universities()
        create_exchange_opportunities()
        create_partner_organizations()
        create_internship_requirements()
        create_report_templates()
        create_student_appeals()
        
        print("=" * 60)
        print("✅ Все тестовые данные успешно созданы!")
        print("\nСтатистика:")
        print(f"- Требования мобильности: {MobilityRequirement.objects.count()}")
        print(f"- Университеты-партнеры: {PartnerUniversity.objects.count()}")
        print(f"- Программы обмена: {UniversityProgram.objects.count()}")
        print(f"- Возможности обмена: {ExchangeOpportunity.objects.count()}")
        print(f"- Преимущества: {ExchangeBenefit.objects.count()}")
        print(f"- Организации-партнеры: {PartnerOrganization.objects.count()}")
        print(f"- Специализации: {OrganizationSpecialization.objects.count()}")
        print(f"- Требования к практике: {InternshipRequirement.objects.count()}")
        print(f"- Элементы требований: {InternshipRequirementItem.objects.count()}")
        print(f"- Шаблоны отчетов: {ReportTemplate.objects.count()}")
        print(f"- Обращения студентов: {StudentAppeal.objects.count()}")
        
    except Exception as e:
        print(f"❌ Ошибка при создании данных: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
