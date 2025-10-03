k#!/usr/bin/env python
"""
Скрипт для обновления данных системы менеджмента качества с кыргызскими переводами.
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


def update_quality_settings():
    """Обновить настройки системы качества с кыргызскими переводами"""
    settings = QualitySettings.objects.filter(is_active=True).first()
    if settings:
        settings.title_kg = 'Сапаттуулукту башкаруу системасы'
        settings.description_kg = 'Эл аралык ISO 9001:2015 стандарттарына ылайык билим берүү кызматтарынын сапатын башкаруунун комплекстүү системасы'
        settings.about_text_kg = 'Жогорку медицина мектебинин сапат менеджменти системасы (СМС) сапатты жалпы башкаруу үчүн керектүү уюмдук түзүлүш, методикалар, процесстер жана ресурстардын жыйындысын билдирет.'
        settings.save()
        print("Обновлены настройки системы качества с кыргызскими переводами")


def update_quality_principles():
    """Обновить принципы качества с кыргызскими переводами"""
    principles_updates = {
        'Ориентация на потребителей': {
            'title_kg': 'Керектөөчүлөргө багыттоо',
            'description_kg': 'Негизги көңүл студенттердин, жумуш берүүчүлөрдүн жана башка кызыкдар тараптардын муктаждыктары менен күтүүлөрүнө бурулат.'
        },
        'Лидерство': {
            'title_kg': 'Жетекчилик',
            'description_kg': 'Бардык деңгээлдеги жетекчилер уюмдун максатынын жана иш-аракеттердин багытынын бирдигин түзүшөт.'
        },
        'Вовлечение персонала': {
            'title_kg': 'Персоналды тартуу',
            'description_kg': 'Уюмдун бардык деңгээлинде компетенттүү, ыйгарым укуктары бар жана тартылган персонал.'
        },
        'Процессный подход': {
            'title_kg': 'Процесстик мамиле',
            'description_kg': 'Ырааттуу жана алдын ала айтылып жаткан натыйжаларга иш-аракеттерди өз ара байланышкан процесстер катары түшүнүү аркылуу эффективдүү жетишүүгө болот.'
        },
        'Системный подход к менеджменту': {
            'title_kg': 'Менеджментке системалык мамиле',
            'description_kg': 'Өз ара байланышкан процесстерди система катары аныктоо, түшүнүү жана башкаруу уюмдун натыйжалуулугуна жана эффективдүүлүгүнө салым кошот.'
        },
        'Постоянное улучшение': {
            'title_kg': 'Туруктуу өнүктүрүү',
            'description_kg': 'Уюмдун жалпы иштөө көрсөткүчтөрүн туруктуу жакшыртуу уюмдун туруктуу максаты болуп саналат.'
        }
    }
    
    for title_ru, updates in principles_updates.items():
        principle = QualityPrinciple.objects.filter(title=title_ru).first()
        if principle:
            principle.title_kg = updates['title_kg']
            principle.description_kg = updates['description_kg']
            principle.save()
            print(f"Обновлен принцип: {title_ru}")


def update_quality_process_groups():
    """Обновить группы процессов с кыргызскими переводами"""
    groups_updates = {
        'Основные процессы': {
            'title_kg': 'Негизги процесстер',
            'description_kg': 'Билим берүү кызматтарын көрсөтүү менен түз байланышкан процесстер'
        },
        'Вспомогательные процессы': {
            'title_kg': 'Жардамчы процесстер',
            'description_kg': 'Негизги процесстер үчүн ресурстарды камсыз кылган процесстер'
        },
        'Процессы управления': {
            'title_kg': 'Башкаруу процесстери',
            'description_kg': 'Сапат системасын пландоо, көзөмөлдөө жана башкаруу процесстери'
        },
        'Процессы улучшения': {
            'title_kg': 'Өнүктүрүү процесстери',
            'description_kg': 'Сапат системасын туруктуу өнүктүрүү процесстери'
        }
    }
    
    for title_ru, updates in groups_updates.items():
        group = QualityProcessGroup.objects.filter(title=title_ru).first()
        if group:
            group.title_kg = updates['title_kg']
            group.description_kg = updates['description_kg']
            group.save()
            print(f"Обновлена группа процессов: {title_ru}")


def update_quality_processes():
    """Обновить процессы с кыргызскими переводами"""
    processes_updates = {
        # Основные процессы
        'Образовательный процесс': 'Билим берүү процесси',
        'Научно-исследовательская деятельность': 'Илимий-изилдөө иштери',
        'Воспитательная работа': 'Тарбиялык иш',
        'Международная деятельность': 'Эл аралык иштер',
        
        # Вспомогательные процессы
        'Управление человеческими ресурсами': 'Адам ресурстарын башкаруу',
        'Техническое обеспечение': 'Техникалык камсыздоо',
        'Информационное обеспечение': 'Маалыматтык камсыздоо',
        'Финансовое управление': 'Каржылык башкаруу',
        
        # Процессы управления
        'Стратегическое планирование': 'Стратегиялык пландоо',
        'Мониторинг и измерение': 'Мониторинг жана өлчөө',
        'Внутренние аудиты': 'Ички аудиттер',
        'Анализ со стороны руководства': 'Жетекчилик тарабынан анализ',
        
        # Процессы улучшения
        'Управление несоответствиями': 'Дал келбестиктерди башкаруу',
        'Корректирующие действия': 'Түзөтүүчү аракеттер',
        'Предупреждающие действия': 'Алдын алуучу аракеттер',
        'Постоянное улучшение': 'Туруктуу өнүктүрүү'
    }
    
    for title_ru, title_kg in processes_updates.items():
        process = QualityProcess.objects.filter(title=title_ru).first()
        if process:
            process.title_kg = title_kg
            process.save()
            print(f"Обновлен процесс: {title_ru}")


def update_quality_statistics():
    """Обновить статистику с кыргызскими переводами"""
    statistics_updates = {
        'Документы СМК': 'СМС документтери',
        'Процессы качества': 'Сапат процесстери',
        'Принципы качества': 'Сапат принциптери',
        'Сертификаты': 'Сертификаттар'
    }
    
    for title_ru, title_kg in statistics_updates.items():
        statistic = QualityStatistic.objects.filter(title=title_ru).first()
        if statistic:
            statistic.title_kg = title_kg
            statistic.save()
            print(f"Обновлена статистика: {title_ru}")


def update_quality_advantages():
    """Обновить преимущества с кыргызскими переводами"""
    advantages_updates = {
        'Удовлетворенность студентов': {
            'title_kg': 'Студенттердин канааттануусу',
            'description_kg': 'Билим берүү кызматтарынан канааттануу деңгээлин жогорулатуу'
        },
        'Оптимизация процессов': {
            'title_kg': 'Процесстерди оптималдаштыруу',
            'description_kg': 'Билим берүү жана башкаруу процесстерин өнүктүрүү'
        },
        'Улучшение академических результатов': {
            'title_kg': 'Академиялык натыйжаларды жакшыртуу',
            'description_kg': 'Адистерди даярдоо сапатын жогорулатуу'
        },
        'Международное признание': {
            'title_kg': 'Эл аралык таануу',
            'description_kg': 'Эл аралык сапат стандарттарына дал келүү'
        },
        'Эффективное использование ресурсов': {
            'title_kg': 'Ресурстарды эффективдүү пайдалануу',
            'description_kg': 'Ресурстарды оптималдуу бөлүштүрүү жана пайдалануу'
        }
    }
    
    for title_ru, updates in advantages_updates.items():
        advantage = QualityAdvantage.objects.filter(title=title_ru).first()
        if advantage:
            advantage.title_kg = updates['title_kg']
            advantage.description_kg = updates['description_kg']
            advantage.save()
            print(f"Обновлено преимущество: {title_ru}")


def update_quality_documents():
    """Обновить документы с кыргызскими переводами"""
    documents_updates = {
        'Политика в области качества': 'Сапат чөйрөсүндөгү саясат',
        'Руководство по качеству': 'Сапат боюнча жетекчилик',
        'Процедура управления документацией': 'Документтерди башкаруу процедурасы',
        'Процедура внутренних аудитов': 'Ички аудиттер процедурасы',
        'Инструкция по заполнению анкет студентов': 'Студенттердин анкеталарын толтуруу боюнча инструкция',
        'Положение о системе менеджмента качества': 'Сапат менеджмент системасы жөнүндө эреже'
    }
    
    for title_ru, title_kg in documents_updates.items():
        document = QualityDocument.objects.filter(title=title_ru).first()
        if document:
            document.title_kg = title_kg
            document.save()
            print(f"Обновлен документ: {title_ru}")


def main():
    """Главная функция для запуска всех операций по обновлению переводов"""
    print("Начинаем обновление данных системы менеджмента качества с кыргызскими переводами...")
    
    try:
        update_quality_settings()
        update_quality_principles()
        update_quality_process_groups()
        update_quality_processes()
        update_quality_statistics()
        update_quality_advantages()
        update_quality_documents()
        
        print("\n✅ Все данные успешно обновлены с кыргызскими переводами!")
        
    except Exception as e:
        print(f"❌ Ошибка при обновлении данных: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()