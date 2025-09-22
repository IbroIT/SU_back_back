#!/usr/bin/env python
import os
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from student_life.models import InternshipRequirement, InternshipRequirementItem, ReportTemplate
from django.core.files.base import ContentFile
import tempfile

def create_internship_requirements():
    """Создание требований к практике"""
    
    # Удаляем существующие данные
    InternshipRequirement.objects.all().delete()
    print("Удалены существующие требования к практике")
    
    # 1. Академические требования
    academic_req = InternshipRequirement.objects.create(
        title_ru="Академические требования",
        title_kg="Академиялык талаптар", 
        title_en="Academic Requirements",
        description_ru="Требования к академической успеваемости для прохождения практики",
        description_kg="Практикадан өтүү үчүн академиялык жетишкендикке талаптар",
        description_en="Academic performance requirements for internship",
        category="academic",
        order=1
    )
    
    # Элементы академических требований
    academic_items = [
        {
            "text_ru": "Средний балл (GPA) не менее 3.0",
            "text_kg": "Орточо баа (GPA) 3.0дөн кем эмес",
            "text_en": "Minimum GPA of 3.0"
        },
        {
            "text_ru": "Успешное завершение всех обязательных предметов текущего курса",
            "text_kg": "Учурдагы курстун бардык милдеттүү предметтерин ийгиликтүү аяктоо",
            "text_en": "Successful completion of all mandatory subjects of current course"
        },
        {
            "text_ru": "Отсутствие академических задолженностей",
            "text_kg": "Академиялык карыздардын жоктугу",
            "text_en": "No academic debts"
        },
        {
            "text_ru": "Завершение не менее 50% учебной программы",
            "text_kg": "Окуу программасынын 50%дан кем эмесин аяктоо",
            "text_en": "Completion of at least 50% of the curriculum"
        }
    ]
    
    for i, item in enumerate(academic_items, 1):
        InternshipRequirementItem.objects.create(
            requirement=academic_req,
            text_ru=item["text_ru"],
            text_kg=item["text_kg"],
            text_en=item["text_en"],
            order=i
        )
    
    # 2. Документы для практики
    documents_req = InternshipRequirement.objects.create(
        title_ru="Документы для практики",
        title_kg="Практика үчүн документтер",
        title_en="Documents for Internship",
        description_ru="Список необходимых документов для оформления практики",
        description_kg="Практиканы түзүү үчүн керектүү документтердин тизмеси",
        description_en="List of required documents for internship registration",
        category="documents",
        order=2
    )
    
    # Элементы документов
    document_items = [
        {
            "text_ru": "Заявление на прохождение практики",
            "text_kg": "Практикадан өтүү үчүн арыз",
            "text_en": "Application for internship"
        },
        {
            "text_ru": "Справка об обучении с указанием курса и специальности",
            "text_kg": "Курсу жана адистиги көрсөтүлгөн окуу жөнүндө справка",
            "text_en": "Certificate of study indicating course and specialization"
        },
        {
            "text_ru": "Медицинская справка о состоянии здоровья",
            "text_kg": "Ден соолугунун абалы жөнүндө медициналык справка",
            "text_en": "Medical certificate of health status"
        },
        {
            "text_ru": "Направление от учебного отдела университета",
            "text_kg": "Университеттин окуу бөлүмүнөн багыт алуу",
            "text_en": "Referral from university academic department"
        },
        {
            "text_ru": "Страховка от несчастных случаев",
            "text_kg": "Кырсыктардан камсыздандыруу",
            "text_en": "Accident insurance"
        }
    ]
    
    for i, item in enumerate(document_items, 1):
        InternshipRequirementItem.objects.create(
            requirement=documents_req,
            text_ru=item["text_ru"],
            text_kg=item["text_kg"],
            text_en=item["text_en"],
            order=i
        )
    
    # 3. Продолжительность практики
    duration_req = InternshipRequirement.objects.create(
        title_ru="Продолжительность практики",
        title_kg="Практиканын узактыгы",
        title_en="Internship Duration",
        description_ru="Информация о сроках и продолжительности различных видов практики",
        description_kg="Практиканын түрдүү түрлөрүнүн мөөнөттөрү жана узактыгы жөнүндө маалымат",
        description_en="Information about terms and duration of different types of internship",
        category="duration",
        order=3
    )
    
    # Элементы продолжительности
    duration_items = [
        {
            "text_ru": "Учебная практика: 2-4 недели",
            "text_kg": "Окуу практикасы: 2-4 жума",
            "text_en": "Educational practice: 2-4 weeks"
        },
        {
            "text_ru": "Производственная практика: 4-6 недель",
            "text_kg": "Өндүрүш практикасы: 4-6 жума",
            "text_en": "Production practice: 4-6 weeks"
        },
        {
            "text_ru": "Преддипломная практика: 6-8 недель",
            "text_kg": "Диплом алдындагы практика: 6-8 жума",
            "text_en": "Pre-graduation practice: 6-8 weeks"
        },
        {
            "text_ru": "Стажировка по специальности: 1-3 месяца",
            "text_kg": "Адистик боюнча стажировка: 1-3 ай",
            "text_en": "Specialty internship: 1-3 months"
        }
    ]
    
    for i, item in enumerate(duration_items, 1):
        InternshipRequirementItem.objects.create(
            requirement=duration_req,
            text_ru=item["text_ru"],
            text_kg=item["text_kg"],
            text_en=item["text_en"],
            order=i
        )
    
    print(f"Создано {InternshipRequirement.objects.count()} требований к практике")
    print(f"Создано {InternshipRequirementItem.objects.count()} элементов требований")


def create_report_templates():
    """Создание шаблонов отчетов"""
    
    # Удаляем существующие данные
    ReportTemplate.objects.all().delete()
    print("Удалены существующие шаблоны отчетов")
    
    # Создаем фиктивные файлы шаблонов (в реальной ситуации здесь будут настоящие файлы)
    templates_data = [
        {
            "name_ru": "Шаблон отчета по учебной практике",
            "name_kg": "Окуу практикасы боюнча отчет үлгүсү",
            "name_en": "Educational Practice Report Template",
            "description_ru": "Стандартный шаблон для оформления отчета по учебной практике",
            "description_kg": "Окуу практикасы боюнча отчетту түзүү үчүн стандарттык үлгү",
            "description_en": "Standard template for educational practice report"
        },
        {
            "name_ru": "Шаблон отчета по производственной практике",
            "name_kg": "Өндүрүш практикасы боюнча отчет үлгүсү", 
            "name_en": "Production Practice Report Template",
            "description_ru": "Шаблон для составления отчета по производственной практике",
            "description_kg": "Өндүрүш практикасы боюнча отчет түзүү үчүн үлгү",
            "description_en": "Template for production practice report"
        },
        {
            "name_ru": "Дневник практиканта",
            "name_kg": "Практиканттын күндөлүгү",
            "name_en": "Intern's Diary",
            "description_ru": "Ежедневные записи о проделанной работе во время практики",
            "description_kg": "Практика учурунда жасалган иштер жөнүндө күн сайынкы жазуулар",
            "description_en": "Daily records of work done during practice"
        },
        {
            "name_ru": "Оценочный лист от руководителя практики",
            "name_kg": "Практика жетекчисинен баалоо барагы",
            "name_en": "Evaluation Sheet from Practice Supervisor",
            "description_ru": "Форма для оценки работы студента руководителем практики",
            "description_kg": "Студенттин ишин практика жетекчиси тарабынан баалоо формасы",
            "description_en": "Form for student work evaluation by practice supervisor"
        }
    ]
    
    for template_data in templates_data:
        # Создаем временный файл для демонстрации
        temp_content = f"""
ШАБЛОН ОТЧЕТА: {template_data['name_ru']}

Этот файл является примером шаблона отчета.
В реальной системе здесь будет настоящий документ Word или PDF.

Описание: {template_data['description_ru']}

Структура отчета:
1. Титульный лист
2. Содержание
3. Введение
4. Основная часть
5. Заключение
6. Приложения
"""
        
        # Создаем ContentFile для сохранения
        file_content = ContentFile(temp_content.encode('utf-8'))
        filename = f"{template_data['name_en'].lower().replace(' ', '_')}.txt"
        
        template = ReportTemplate.objects.create(
            name_ru=template_data['name_ru'],
            name_kg=template_data['name_kg'],
            name_en=template_data['name_en'],
            description_ru=template_data['description_ru'],
            description_kg=template_data['description_kg'],
            description_en=template_data['description_en']
        )
        
        # Сохраняем файл
        template.file.save(filename, file_content)
        template.save()
    
    print(f"Создано {ReportTemplate.objects.count()} шаблонов отчетов")


def main():
    print("Создание тестовых данных для практики...")
    print("=" * 50)
    
    create_internship_requirements()
    print()
    create_report_templates()
    
    print("=" * 50)
    print("Тестовые данные для практики созданы успешно!")


if __name__ == '__main__':
    main()
