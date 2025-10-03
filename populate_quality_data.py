#!/usr/bin/env python
"""
Скрипт для заполнения базы данных тестовыми данными для системы менеджмента качества (СМК).
"""

import os
import sys
import django
from datetime import date

# Настройка Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from hsm.models import (
    QualityPrinciple, QualityDocument, QualityProcessGroup,
    QualityProcess, QualityStatistic, QualityAdvantage, QualitySettings
)


def create_quality_settings():
    """Создать основные настройки системы качества"""
    settings, created = QualitySettings.objects.get_or_create(
        is_active=True,
        defaults={
            'title': 'Система менеджмента качества',
            'title_kg': 'Сапа менеджменті жүйесі',
            'title_en': 'Quality Management System',
            'description': 'Комплексная система управления качеством образовательных услуг в соответствии с международными стандартами ISO 9001:2015',
            'description_kg': 'Халықаралық ISO 9001:2015 стандарттарына сәйкес білім беру қызметтерінің сапасын басқарудың кешенді жүйесі',
            'description_en': 'Comprehensive quality management system for educational services in accordance with international ISO 9001:2015 standards',
            'about_text': 'Система менеджмента качества (СМК) Высшей школы медицины представляет собой совокупность организационной структуры, методик, процессов и ресурсов, необходимых для общего руководства качеством.',
            'about_text_kg': 'Жоғары медицина мектебінің сапа менеджменті жүйесі (СМЖ) сапаны жалпы басқару үшін қажетті ұйымдық құрылым, әдістемелер, процестер мен ресурстардың жиынтығын білдіреді.',
            'about_text_en': 'The Quality Management System (QMS) of the Higher School of Medicine is a set of organizational structure, methodologies, processes and resources necessary for overall quality management.',
            'iso_standard': 'ISO 9001:2015',
            'compliance_percentage': '100%'
        }
    )
    print(f"{'Создана' if created else 'Обновлена'} настройка системы качества")


def create_quality_principles():
    """Создать принципы качества"""
    principles_data = [
        {
            'title': 'Ориентация на потребителей',
            'title_kg': 'Тұтынушыларға бағдарлану',
            'title_en': 'Customer orientation',
            'description': 'Основное внимание уделяется потребностям и ожиданиям студентов, работодателей и других заинтересованных сторон.',
            'description_kg': 'Негізгі назар студенттердің, жұмыс берушілердің және басқа мүдделі тараптардың қажеттіліктері мен үміттеріне аударылады.',
            'description_en': 'Primary focus is placed on the needs and expectations of students, employers and other stakeholders.',
            'icon': '👥',
            'order': 1
        },
        {
            'title': 'Лидерство',
            'title_kg': 'Көшбасшылық',
            'title_en': 'Leadership',
            'description': 'Руководители на всех уровнях создают единство цели и направления деятельности организации.',
            'description_kg': 'Барлық деңгейдегі басшылар ұйымның мақсаты мен қызмет бағытының бірлігін жасайды.',
            'description_en': 'Leaders at all levels create unity of purpose and direction for the organization.',
            'icon': '🌟',
            'order': 2
        },
        {
            'title': 'Вовлечение персонала',
            'title_kg': 'Персоналды тарту',
            'title_en': 'Engagement of people',
            'description': 'Компетентный, наделенный полномочиями и вовлеченный персонал на всех уровнях организации.',
            'description_kg': 'Ұйымның барлық деңгейінде құзыретті, өкілеттіктері бар және тартылған персонал.',
            'description_en': 'Competent, empowered and engaged people at all levels throughout the organization.',
            'icon': '🤝',
            'order': 3
        },
        {
            'title': 'Процессный подход',
            'title_kg': 'Процестік тәсіл',
            'title_en': 'Process approach',
            'description': 'Последовательные и предсказуемые результаты достигаются более эффективно при понимании деятельности как взаимосвязанных процессов.',
            'description_kg': 'Дәйекті және болжамды нәтижелерге қызметті өзара байланысты процестер ретінде түсіну арқылы тиімдірек қол жеткізіледі.',
            'description_en': 'Consistent and predictable results are achieved more effectively when activities are understood as interrelated processes.',
            'icon': '🔄',
            'order': 4
        },
        {
            'title': 'Системный подход к менеджменту',
            'title_kg': 'Менеджментке жүйелік тәсіл',
            'title_en': 'System approach to management',
            'description': 'Выявление, понимание и управление взаимосвязанными процессами как системой способствует результативности и эффективности организации.',
            'description_kg': 'Өзара байланысты процестерді жүйе ретінде анықтау, түсіну және басқару ұйымның нәтижелілігі мен тиімділігіне ықпал етеді.',
            'description_en': 'Identifying, understanding and managing interrelated processes as a system contributes to the organization\'s effectiveness and efficiency.',
            'icon': '📊',
            'order': 5
        },
        {
            'title': 'Постоянное улучшение',
            'title_kg': 'Үнемі жетілдіру',
            'title_en': 'Continual improvement',
            'description': 'Постоянное улучшение общих показателей деятельности организации является неизменной целью организации.',
            'description_kg': 'Ұйымның жалпы қызмет көрсеткіштерін үнемі жақсарту ұйымның тұрақты мақсаты болып табылады.',
            'description_en': 'Continual improvement of the organization\'s overall performance is a permanent objective of the organization.',
            'icon': '📈',
            'order': 6
        }
    ]
    
    for data in principles_data:
        principle, created = QualityPrinciple.objects.get_or_create(
            title=data['title'],
            defaults=data
        )
        print(f"{'Создан' if created else 'Обновлен'} принцип: {principle.title}")


def create_quality_process_groups():
    """Создать группы процессов"""
    groups_data = [
        {
            'title': 'Основные процессы',
            'title_kg': 'Негізгі процестер',
            'title_en': 'Main processes',
            'description': 'Процессы, непосредственно связанные с предоставлением образовательных услуг',
            'description_kg': 'Білім беру қызметтерін ұсынумен тікелей байланысты процестер',
            'description_en': 'Processes directly related to the provision of educational services',
            'icon': '🎯',
            'order': 1
        },
        {
            'title': 'Вспомогательные процессы',
            'title_kg': 'Көмекші процестер',
            'title_en': 'Support processes',
            'description': 'Процессы, обеспечивающие ресурсы для основных процессов',
            'description_kg': 'Негізгі процестер үшін ресурстарды қамтамасыз ететін процестер',
            'description_en': 'Processes that provide resources for main processes',
            'icon': '⚙️',
            'order': 2
        },
        {
            'title': 'Процессы управления',
            'title_kg': 'Басқару процестері',
            'title_en': 'Management processes',
            'description': 'Процессы планирования, контроля и управления системой качества',
            'description_kg': 'Сапа жүйесін жоспарлау, бақылау және басқару процестері',
            'description_en': 'Processes of planning, monitoring and managing the quality system',
            'icon': '📋',
            'order': 3
        },
        {
            'title': 'Процессы улучшения',
            'title_kg': 'Жетілдіру процестері',
            'title_en': 'Improvement processes',
            'description': 'Процессы постоянного улучшения системы качества',
            'description_kg': 'Сапа жүйесін үнемі жетілдіру процестері',
            'description_en': 'Processes of continuous improvement of the quality system',
            'icon': '🚀',
            'order': 4
        }
    ]
    
    created_groups = []
    for data in groups_data:
        group, created = QualityProcessGroup.objects.get_or_create(
            title=data['title'],
            defaults=data
        )
        created_groups.append(group)
        print(f"{'Создана' if created else 'Обновлена'} группа процессов: {group.title}")
    
    return created_groups


def create_quality_processes(groups):
    """Создать процессы для каждой группы"""
    processes_data = [
        # Основные процессы
        {
            'group': groups[0],
            'title': 'Образовательный процесс',
            'title_kg': 'Білім беру процесі',
            'title_en': 'Educational process',
            'order': 1
        },
        {
            'group': groups[0],
            'title': 'Научно-исследовательская деятельность',
            'title_kg': 'Ғылыми-зерттеу қызметі',
            'title_en': 'Research activities',
            'order': 2
        },
        {
            'group': groups[0],
            'title': 'Воспитательная работа',
            'title_kg': 'Тәрбие жұмысы',
            'title_en': 'Educational work',
            'order': 3
        },
        {
            'group': groups[0],
            'title': 'Международная деятельность',
            'title_kg': 'Халықаралық қызмет',
            'title_en': 'International activities',
            'order': 4
        },
        # Вспомогательные процессы
        {
            'group': groups[1],
            'title': 'Управление человеческими ресурсами',
            'title_kg': 'Адами ресурстарды басқару',
            'title_en': 'Human resource management',
            'order': 1
        },
        {
            'group': groups[1],
            'title': 'Техническое обеспечение',
            'title_kg': 'Техникалық қамтамасыз ету',
            'title_en': 'Technical support',
            'order': 2
        },
        {
            'group': groups[1],
            'title': 'Информационное обеспечение',
            'title_kg': 'Ақпараттық қамтамасыз ету',
            'title_en': 'Information support',
            'order': 3
        },
        {
            'group': groups[1],
            'title': 'Финансовое управление',
            'title_kg': 'Қаржылық басқару',
            'title_en': 'Financial management',
            'order': 4
        },
        # Процессы управления
        {
            'group': groups[2],
            'title': 'Стратегическое планирование',
            'title_kg': 'Стратегиялық жоспарлау',
            'title_en': 'Strategic planning',
            'order': 1
        },
        {
            'group': groups[2],
            'title': 'Мониторинг и измерение',
            'title_kg': 'Мониторинг және өлшеу',
            'title_en': 'Monitoring and measurement',
            'order': 2
        },
        {
            'group': groups[2],
            'title': 'Внутренние аудиты',
            'title_kg': 'Ішкі аудиттер',
            'title_en': 'Internal audits',
            'order': 3
        },
        {
            'group': groups[2],
            'title': 'Анализ со стороны руководства',
            'title_kg': 'Басшылық тарапынан талдау',
            'title_en': 'Management review',
            'order': 4
        },
        # Процессы улучшения
        {
            'group': groups[3],
            'title': 'Управление несоответствиями',
            'title_kg': 'Сәйкессіздіктерді басқару',
            'title_en': 'Nonconformity management',
            'order': 1
        },
        {
            'group': groups[3],
            'title': 'Корректирующие действия',
            'title_kg': 'Түзету әрекеттері',
            'title_en': 'Corrective actions',
            'order': 2
        },
        {
            'group': groups[3],
            'title': 'Предупреждающие действия',
            'title_kg': 'Алдын алу әрекеттері',
            'title_en': 'Preventive actions',
            'order': 3
        },
        {
            'group': groups[3],
            'title': 'Постоянное улучшение',
            'title_kg': 'Үнемі жетілдіру',
            'title_en': 'Continuous improvement',
            'order': 4
        }
    ]
    
    for data in processes_data:
        process, created = QualityProcess.objects.get_or_create(
            group=data['group'],
            title=data['title'],
            defaults=data
        )
        print(f"{'Создан' if created else 'Обновлен'} процесс: {process.title}")


def create_quality_statistics():
    """Создать статистические данные"""
    statistics_data = [
        {
            'title': 'Документы СМК',
            'title_kg': 'СМЖ құжаттары',
            'title_en': 'QMS Documents',
            'value': '24+',
            'icon': '📋',
            'order': 1
        },
        {
            'title': 'Процессы качества',
            'title_kg': 'Сапа процестері',
            'title_en': 'Quality processes',
            'value': '16+',
            'icon': '🔄',
            'order': 2
        },
        {
            'title': 'Принципы качества',
            'title_kg': 'Сапа принциптері',
            'title_en': 'Quality principles',
            'value': '6',
            'icon': '🌟',
            'order': 3
        },
        {
            'title': 'Сертификаты',
            'title_kg': 'Сертификаттар',
            'title_en': 'Certificates',
            'value': '3+',
            'icon': '🏆',
            'order': 4
        }
    ]
    
    for data in statistics_data:
        statistic, created = QualityStatistic.objects.get_or_create(
            title=data['title'],
            defaults=data
        )
        print(f"{'Создана' if created else 'Обновлена'} статистика: {statistic.title}")


def create_quality_advantages():
    """Создать преимущества системы качества"""
    advantages_data = [
        {
            'title': 'Удовлетворенность студентов',
            'title_kg': 'Студенттердің қанағаттануы',
            'title_en': 'Student satisfaction',
            'description': 'Повышение уровня удовлетворенности образовательными услугами',
            'description_kg': 'Білім беру қызметтерінен қанағаттану деңгейін арттыру',
            'description_en': 'Increasing the level of satisfaction with educational services',
            'order': 1
        },
        {
            'title': 'Оптимизация процессов',
            'title_kg': 'Процестерді оңтайландыру',
            'title_en': 'Process optimization',
            'description': 'Совершенствование образовательных и управленческих процессов',
            'description_kg': 'Білім беру және басқару процестерін жетілдіру',
            'description_en': 'Improvement of educational and management processes',
            'order': 2
        },
        {
            'title': 'Улучшение академических результатов',
            'title_kg': 'Академиялық нәтижелерді жақсарту',
            'title_en': 'Improving academic results',
            'description': 'Повышение качества подготовки специалистов',
            'description_kg': 'Мамандар дайындау сапасын арттыру',
            'description_en': 'Improving the quality of specialist training',
            'order': 3
        },
        {
            'title': 'Международное признание',
            'title_kg': 'Халықаралық мойындау',
            'title_en': 'International recognition',
            'description': 'Соответствие международным стандартам качества',
            'description_kg': 'Халықаралық сапа стандарттарына сәйкестік',
            'description_en': 'Compliance with international quality standards',
            'order': 4
        },
        {
            'title': 'Эффективное использование ресурсов',
            'title_kg': 'Ресурстарды тиімді пайдалану',
            'title_en': 'Efficient use of resources',
            'description': 'Оптимальное распределение и использование ресурсов',
            'description_kg': 'Ресурстарды оңтайлы бөлу және пайдалану',
            'description_en': 'Optimal allocation and use of resources',
            'order': 5
        }
    ]
    
    for data in advantages_data:
        advantage, created = QualityAdvantage.objects.get_or_create(
            title=data['title'],
            defaults=data
        )
        print(f"{'Создано' if created else 'Обновлено'} преимущество: {advantage.title}")


def create_quality_documents():
    """Создать документы системы качества"""
    documents_data = [
        {
            'title': 'Политика в области качества',
            'title_kg': 'Сапа саласындағы саясат',
            'title_en': 'Quality Policy',
            'category': 'policy',
            'document_type': 'pdf',
            'file_size': '245 KB',
            'version': '2.1',
            'approval_date': date(2024, 1, 15),
            'order': 1
        },
        {
            'title': 'Руководство по качеству',
            'title_kg': 'Сапа жөніндегі нұсқаулық',
            'title_en': 'Quality Manual',
            'category': 'manual',
            'document_type': 'pdf',
            'file_size': '1.2 MB',
            'version': '3.0',
            'approval_date': date(2024, 2, 1),
            'order': 2
        },
        {
            'title': 'Процедура управления документацией',
            'title_kg': 'Құжаттаманы басқару процедурасы',
            'title_en': 'Document Control Procedure',
            'category': 'procedure',
            'document_type': 'docx',
            'file_size': '320 KB',
            'version': '1.5',
            'approval_date': date(2024, 1, 20),
            'order': 3
        },
        {
            'title': 'Процедура внутренних аудитов',
            'title_kg': 'Ішкі аудиттер процедурасы',
            'title_en': 'Internal Audit Procedure',
            'category': 'procedure',
            'document_type': 'pdf',
            'file_size': '450 KB',
            'version': '2.0',
            'approval_date': date(2024, 3, 10),
            'order': 4
        },
        {
            'title': 'Инструкция по заполнению анкет студентов',
            'title_kg': 'Студенттер сауалнамаларын толтыру жөніндегі нұсқаулық',
            'title_en': 'Student Survey Completion Instructions',
            'category': 'instruction',
            'document_type': 'doc',
            'file_size': '180 KB',
            'version': '1.3',
            'approval_date': date(2024, 2, 15),
            'order': 5
        },
        {
            'title': 'Положение о системе менеджмента качества',
            'title_kg': 'Сапа менеджменті жүйесі туралы ережелер',
            'title_en': 'Quality Management System Regulations',
            'category': 'regulation',
            'document_type': 'pdf',
            'file_size': '680 KB',
            'version': '4.0',
            'approval_date': date(2024, 1, 5),
            'order': 6
        }
    ]
    
    for data in documents_data:
        document, created = QualityDocument.objects.get_or_create(
            title=data['title'],
            defaults=data
        )
        print(f"{'Создан' if created else 'Обновлен'} документ: {document.title}")


def main():
    """Главная функция для запуска всех операций по заполнению данных"""
    print("Начинаем заполнение данных системы менеджмента качества...")
    
    try:
        create_quality_settings()
        create_quality_principles()
        groups = create_quality_process_groups()
        create_quality_processes(groups)
        create_quality_statistics()
        create_quality_advantages()
        create_quality_documents()
        
        print("\n✅ Все данные системы менеджмента качества успешно созданы!")
        print("\nСтатистика:")
        print(f"- Принципов качества: {QualityPrinciple.objects.count()}")
        print(f"- Групп процессов: {QualityProcessGroup.objects.count()}")
        print(f"- Процессов: {QualityProcess.objects.count()}")
        print(f"- Статистических показателей: {QualityStatistic.objects.count()}")
        print(f"- Преимуществ: {QualityAdvantage.objects.count()}")
        print(f"- Документов: {QualityDocument.objects.count()}")
        
    except Exception as e:
        print(f"❌ Ошибка при заполнении данных: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()