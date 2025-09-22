#!/usr/bin/env python
"""
Скрипт для создания тестовых данных для инструкций студентов
"""

import os
import sys
import django

# Добавляем корневую папку проекта в путь Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Настраиваем Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from student_life.models import StudentGuide, GuideRequirement, GuideStep, GuideStepDetail

def create_sample_instructions():
    """Создание образцов инструкций для студентов"""
    
    print("🚀 Создание инструкций для студентов...")
    
    # Очищаем существующие данные
    StudentGuide.objects.all().delete()
    print("✅ Очищены существующие инструкции")
    
    # 1. Академический отпуск
    guide1 = StudentGuide.objects.create(
        title_ru="Академический отпуск",
        title_kg="Академиялык эс алуу", 
        title_en="Academic Leave",
        description_ru="Пошаговое руководство по оформлению академического отпуска",
        description_kg="Академиялык эс алууну рөмеддөө боюнча кадам-кадам жетекчилик",
        description_en="Step-by-step guide for academic leave registration",
        estimated_time_ru="2-3 дня",
        estimated_time_kg="2-3 күн",
        estimated_time_en="2-3 days",
        max_duration_ru="30 дней",
        max_duration_kg="30 күн", 
        max_duration_en="30 days",
        contact_info_ru="Деканат: +996 312 123-456 доб. 105",
        contact_info_kg="Деканат: +996 312 123-456 кош. 105",
        contact_info_en="Dean's Office: +996 312 123-456 ext. 105",
        category="academic",
        icon="CalendarDaysIcon",
        order=1
    )
    
    # Требования для академического отпуска
    requirements1 = [
        ("Заявление на имя ректора", "Ректордун атына арыз", "Application to the rector"),
        ("Справка о состоянии здоровья (при необходимости)", "Ден соолук абалы жөнүндө справка (зарылчылыгына жараша)", "Health certificate (if necessary)"),
        ("Документы, подтверждающие причину отпуска", "Эс алуунун себебин тастыктоочу документтер", "Documents confirming reason for leave"),
        ("Справка об отсутствии академических задолженностей", "Академиялык карыз жок экендиги жөнүндө справка", "Certificate of no academic debts")
    ]
    
    for i, (req_ru, req_kg, req_en) in enumerate(requirements1):
        GuideRequirement.objects.create(
            guide=guide1,
            text_ru=req_ru,
            text_kg=req_kg,
            text_en=req_en,
            order=i + 1
        )
    
    # Шаги для академического отпуска
    steps1 = [
        {
            "title_ru": "Подготовка документов",
            "title_kg": "Документтерди даярдоо",
            "title_en": "Document Preparation",
            "description_ru": "Соберите все необходимые документы для подачи заявления",
            "description_kg": "Арыз берүү үчүн бардык керектүү документтерди чогултуңуз",
            "description_en": "Collect all necessary documents for application submission",
            "timeframe_ru": "1-2 дня",
            "timeframe_kg": "1-2 күн",
            "timeframe_en": "1-2 days",
            "details": [
                ("Напишите заявление на имя ректора с указанием причины и сроков", "Ректордун атына себеби жана мөөнөттөрүн көрсөткөн арыз жазыңыз", "Write an application to the rector indicating the reason and timeframe"),
                ("Получите медицинскую справку (если отпуск по состоянию здоровья)", "Медициналык справка алыңыз (денсоолук боюнча эс алуу болсо)", "Get a medical certificate (if leave is for health reasons)"),
                ("Соберите подтверждающие документы (справки, свидетельства)", "Далилдөөчү документтерди чогултуңуз (справкалар, күбөлүктөр)", "Collect supporting documents (certificates, testimonials)"),
                ("Получите справку об отсутствии академических задолженностей", "Академиялык карыз жок экендиги жөнүндө справка алыңыз", "Get a certificate of no academic debts")
            ]
        },
        {
            "title_ru": "Подача документов",
            "title_kg": "Документтерди берүү", 
            "title_en": "Document Submission",
            "description_ru": "Подайте документы в деканат своего факультета",
            "description_kg": "Документтерди өз факультетиңиздин деканатына бериңиз",
            "description_en": "Submit documents to your faculty's dean's office",
            "timeframe_ru": "30 минут",
            "timeframe_kg": "30 мүнөт",
            "timeframe_en": "30 minutes",
            "details": [
                ("Обратитесь в деканат в рабочие часы", "Иш убагында деканатка кайрылыңыз", "Contact the dean's office during working hours"),
                ("Передайте все документы секретарю деканата", "Бардык документтерди деканаттын катчысына өткөрүңүз", "Submit all documents to the dean's secretary"),
                ("Получите расписку о приеме документов", "Документтерди кабыл алгандыгы жөнүндө расписка алыңыз", "Get a receipt for document acceptance"),
                ("Уточните сроки рассмотрения заявления", "Арызды карап чыгуу мөөнөттөрүн так билиңиз", "Clarify the application review timeframe")
            ]
        }
    ]
    
    for step_num, step_data in enumerate(steps1, 1):
        step = GuideStep.objects.create(
            guide=guide1,
            title_ru=step_data["title_ru"],
            title_kg=step_data["title_kg"],
            title_en=step_data["title_en"],
            description_ru=step_data["description_ru"],
            description_kg=step_data["description_kg"],
            description_en=step_data["description_en"],
            timeframe_ru=step_data["timeframe_ru"],
            timeframe_kg=step_data["timeframe_kg"],
            timeframe_en=step_data["timeframe_en"],
            step_number=step_num,
            order=step_num
        )
        
        for detail_num, (detail_ru, detail_kg, detail_en) in enumerate(step_data["details"], 1):
            GuideStepDetail.objects.create(
                step=step,
                text_ru=detail_ru,
                text_kg=detail_kg,
                text_en=detail_en,
                order=detail_num
            )
    
    # 2. Перевод между специальностями
    guide2 = StudentGuide.objects.create(
        title_ru="Перевод между специальностями",
        title_kg="Адистиктердин ортосунда которуу",
        title_en="Transfer Between Specialties",
        description_ru="Процедура перевода с одной специальности на другую",
        description_kg="Бир адистиктен экинчисине которуу процедурасы",
        description_en="Procedure for transferring from one specialty to another",
        estimated_time_ru="1-2 недели",
        estimated_time_kg="1-2 жума",
        estimated_time_en="1-2 weeks",
        max_duration_ru="30 дней",
        max_duration_kg="30 күн",
        max_duration_en="30 days",
        contact_info_ru="Учебная часть: +996 312 123-456 доб. 110",
        contact_info_kg="Окуу бөлүмү: +996 312 123-456 кош. 110",
        contact_info_en="Academic Office: +996 312 123-456 ext. 110",
        category="academic",
        icon="UserGroupIcon",
        order=2
    )
    
    # Требования для перевода
    requirements2 = [
        ("Заявление о переводе", "Которуу жөнүндө арыз", "Transfer application"),
        ("Академическая справка", "Академиялык справка", "Academic transcript"),
        ("Выписка из зачетной книжки", "Белгилер китебинен көчүрмө", "Excerpt from grade book"),
        ("Согласие принимающей кафедры", "Кабыл алуучу кафедранын макулдугу", "Consent from receiving department")
    ]
    
    for i, (req_ru, req_kg, req_en) in enumerate(requirements2):
        GuideRequirement.objects.create(
            guide=guide2,
            text_ru=req_ru,
            text_kg=req_kg,
            text_en=req_en,
            order=i + 1
        )
    
    # 3. Получение справок и документов
    guide3 = StudentGuide.objects.create(
        title_ru="Получение справок и документов",
        title_kg="Маалымат каттары жана документтерди алуу",
        title_en="Obtaining Certificates and Documents",
        description_ru="Порядок получения различных справок и документов",
        description_kg="Ар кандай маалымат каттарын жана документтерди алуу тартиби",
        description_en="Procedure for obtaining various certificates and documents",
        estimated_time_ru="1-3 дня",
        estimated_time_kg="1-3 күн", 
        estimated_time_en="1-3 days",
        max_duration_ru="Зависит от типа документа",
        max_duration_kg="Документтин түрүнө жараша",
        max_duration_en="Depends on document type",
        contact_info_ru="Канцелярия: +996 312 123-456 доб. 103",
        contact_info_kg="Канцелярия: +996 312 123-456 кош. 103",
        contact_info_en="Secretariat: +996 312 123-456 ext. 103",
        category="documents",
        icon="DocumentTextIcon",
        order=3
    )
    
    # Требования для получения справок
    requirements3 = [
        ("Заявление с указанием типа справки", "Маалымат каттын түрүн көрсөткөн арыз", "Application indicating certificate type"),
        ("Студенческий билет", "Студенттик билет", "Student card"),
        ("Документ, удостоверяющий личность", "Жеке инсанды тастыктоочу документ", "Identity document"),
        ("Оплата государственной пошлины (при необходимости)", "Мамлекеттик баж төлөө (зарылчылыгына жараша)", "State fee payment (if required)")
    ]
    
    for i, (req_ru, req_kg, req_en) in enumerate(requirements3):
        GuideRequirement.objects.create(
            guide=guide3,
            text_ru=req_ru,
            text_kg=req_kg,
            text_en=req_en,
            order=i + 1
        )
    
    print(f"✅ Создано {StudentGuide.objects.count()} инструкций")
    print(f"✅ Создано {GuideRequirement.objects.count()} требований")
    print(f"✅ Создано {GuideStep.objects.count()} шагов")
    print(f"✅ Создано {GuideStepDetail.objects.count()} деталей шагов")

def main():
    """Главная функция"""
    print("=" * 50)
    print("СОЗДАНИЕ ОБРАЗЦОВ ИНСТРУКЦИЙ ДЛЯ СТУДЕНТОВ")
    print("=" * 50)
    
    try:
        create_sample_instructions()
        print("\n🎉 Образцы инструкций успешно созданы!")
        
    except Exception as e:
        print(f"\n❌ Ошибка при создании образцов: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
