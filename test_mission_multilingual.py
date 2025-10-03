#!/usr/bin/env python
"""
Тестирование мультиязычности API для mission_section
"""

import os
import sys
import django

# Добавляем путь к Django проекту
sys.path.append('/home/adilhan/medicine/SU_back')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')

# Инициализируем Django
django.setup()

from mission_section.models import MissionSection, HistoryMilestone, Value, Priority, Achievement
from mission_section.serializers import MissionCompleteSerializer
from django.test import RequestFactory


def create_test_data():
    """Создаем тестовые данные с мультиязычным контентом"""
    
    # Удаляем старые данные
    MissionSection.objects.all().delete()
    HistoryMilestone.objects.all().delete()
    Value.objects.all().delete()
    Priority.objects.all().delete()
    Achievement.objects.all().delete()
    
    # Создаем основную секцию миссии
    mission = MissionSection.objects.create(
        title="Наша миссия",
        title_en="Our Mission",
        title_ky="Биздин миссия",
        subtitle="Подзаголовок миссии",
        subtitle_en="Mission subtitle",
        subtitle_ky="Миссия подзаголовок",
        mission_text="Основной текст миссии университета",
        mission_text_en="Main university mission text",
        mission_text_ky="Университеттин негизги миссия тексти",
        vision_title="Наше видение",
        vision_title_en="Our Vision",
        vision_title_ky="Биздин көрүү",
        vision_text="Текст видения",
        vision_text_en="Vision text",
        vision_text_ky="Көрүү тексти",
        approach_title="Наш подход",
        approach_title_en="Our Approach",
        approach_title_ky="Биздин ыкма",
        approach_text="Текст подхода",
        approach_text_en="Approach text",
        approach_text_ky="Ыкма тексти"
    )
    
    # Создаем историческую веху
    history = HistoryMilestone.objects.create(
        title="Основание университета",
        title_en="University foundation",
        title_ky="Университеттин негизделиши",
        description="Описание основания",
        description_en="Foundation description",
        description_ky="Негизделүү сүрөттөлүшү",
        year="2020",
        order=1
    )
    
    # Создаем ценность
    value = Value.objects.create(
        type="education",
        title="Образование",
        title_en="Education",
        title_ky="Билим берүү",
        description="Описание образования",
        description_en="Education description",
        description_ky="Билим берүү сүрөттөлүшү",
        order=1
    )
    
    # Создаем приоритет
    priority = Priority.objects.create(
        text="Качественное образование",
        text_en="Quality education",
        text_ky="Сапаттуу билим берүү",
        order=1
    )
    
    # Создаем достижение
    achievement = Achievement.objects.create(
        number="100+",
        label="Студентов",
        label_en="Students",
        label_ky="Студенттер",
        order=1
    )
    
    return mission, history, value, priority, achievement


def test_multilingual_serialization():
    """Тестируем мультиязычную сериализацию"""
    
    print("=== Создаем тестовые данные ===")
    mission, history, value, priority, achievement = create_test_data()
    print("✅ Тестовые данные созданы")
    
    print("\n=== Тестируем русский язык (по умолчанию) ===")
    # Создаем фейковый запрос для русского языка
    factory = RequestFactory()
    request_ru = factory.get('/api/mission/complete/')
    
    data = {
        'mission': mission,
        'history': [history],
        'values': [value],
        'priorities': [priority],
        'achievements': [achievement],
    }
    
    serializer_ru = MissionCompleteSerializer(data, context={'request': request_ru})
    result_ru = serializer_ru.data
    
    print(f"Mission title (RU): {result_ru['mission']['display_title']}")
    print(f"History title (RU): {result_ru['history'][0]['display_title']}")
    print(f"Value title (RU): {result_ru['values'][0]['display_title']}")
    print(f"Priority text (RU): {result_ru['priorities'][0]['display_text']}")
    print(f"Achievement label (RU): {result_ru['achievements'][0]['display_label']}")
    
    print("\n=== Тестируем английский язык ===")
    # Создаем фейковый запрос для английского языка
    request_en = factory.get('/api/mission/complete/?lang=en')
    
    serializer_en = MissionCompleteSerializer(data, context={'request': request_en})
    result_en = serializer_en.data
    
    print(f"Mission title (EN): {result_en['mission']['display_title']}")
    print(f"History title (EN): {result_en['history'][0]['display_title']}")
    print(f"Value title (EN): {result_en['values'][0]['display_title']}")
    print(f"Priority text (EN): {result_en['priorities'][0]['display_text']}")
    print(f"Achievement label (EN): {result_en['achievements'][0]['display_label']}")
    
    print("\n=== Тестируем кыргызский язык ===")
    # Создаем фейковый запрос для кыргызского языка
    request_ky = factory.get('/api/mission/complete/?lang=ky')
    
    serializer_ky = MissionCompleteSerializer(data, context={'request': request_ky})
    result_ky = serializer_ky.data
    
    print(f"Mission title (KY): {result_ky['mission']['display_title']}")
    print(f"History title (KY): {result_ky['history'][0]['display_title']}")
    print(f"Value title (KY): {result_ky['values'][0]['display_title']}")
    print(f"Priority text (KY): {result_ky['priorities'][0]['display_text']}")
    print(f"Achievement label (KY): {result_ky['achievements'][0]['display_label']}")
    
    print("\n=== Проверяем что все поля включены в сериализацию ===")
    mission_fields = result_ru['mission'].keys()
    print(f"Mission fields: {sorted(mission_fields)}")
    
    # Проверяем наличие всех языковых полей
    expected_fields = ['title', 'title_en', 'title_ky', 'display_title']
    for field in expected_fields:
        if field in mission_fields:
            print(f"✅ {field} присутствует")
        else:
            print(f"❌ {field} отсутствует")
    
    print("\n=== Тест завершен ===")


if __name__ == "__main__":
    test_multilingual_serialization()