#!/usr/bin/env python
import os
import sys
import django
from datetime import datetime, timedelta
from django.utils import timezone

# Добавляем путь к Django проекту
sys.path.append('/Users/adminbaike/medicine/SU_back_back')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')

# Инициализируем Django
django.setup()

from news.models import News, Event, Announcement

def create_additional_events():
    """Создает дополнительные события с разными изображениями"""
    
    # Получаем категорию событий
    from news.models import NewsCategory
    events_category, created = NewsCategory.objects.get_or_create(
        name='events',
        defaults={
            'slug': 'events',
            'name_ru': 'События',
            'name_kg': 'Окуялар',
            'name_en': 'Events'
        }
    )
    
    # Создаем базовые новости для событий
    news_data = [
        {
            'title_ru': 'День открытых дверей',
            'title_kg': 'Ачык эшиктер күнү',
            'title_en': 'Open Door Day',
            'content_ru': 'Приглашаем всех абитуриентов и их родителей на день открытых дверей нашего университета.',
            'content_kg': 'Бардык абитуриенттерди жана алардын ата-энелерин университетибизге ачык эшиктер күнүнө чакырабыз.',
            'content_en': 'We invite all applicants and their parents to the open door day of our university.',
            'summary_ru': 'Приглашаем на день открытых дверей',
            'summary_kg': 'Ачык эшиктер күнүнө чакырабыз', 
            'summary_en': 'We invite to open door day',
            'image_url': 'https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=600&h=400&fit=crop'
        },
        {
            'title_ru': 'Медицинская олимпиада',
            'title_kg': 'Медициналык олимпиада',
            'title_en': 'Medical Olympiad',
            'content_ru': 'Республиканская олимпиада по медицине среди студентов.',
            'content_kg': 'Студенттер арасында медицина боюнча республикалык олимпиада.',
            'content_en': 'Republican olympiad in medicine among students.',
            'summary_ru': 'Республиканская олимпиада по медицине',
            'summary_kg': 'Медицина боюнча республикалык олимпиада',
            'summary_en': 'Republican olympiad in medicine',
            'image_url': 'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=600&h=400&fit=crop'
        },
        {
            'title_ru': 'Выставка достижений',
            'title_kg': 'Жетишкендиктер көргөзмөсү',
            'title_en': 'Achievements Exhibition',
            'content_ru': 'Выставка научных достижений студентов и преподавателей.',
            'content_kg': 'Студенттердин жана мугалимдердин илимий жетишкендиктеринин көргөзмөсү.',
            'content_en': 'Exhibition of scientific achievements of students and teachers.',
            'summary_ru': 'Выставка научных достижений',
            'summary_kg': 'Илимий жетишкендиктер көргөзмөсү',
            'summary_en': 'Exhibition of scientific achievements',
            'image_url': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=600&h=400&fit=crop'
        }
    ]
    
    events_data = [
        {
            'slug': 'open-door-day-2025',
            'event_date': datetime.now().date() + timedelta(days=30),
            'event_time': '10:00:00',
            'location_ru': 'Главный корпус',
            'location_kg': 'Башкы корпус',
            'location_en': 'Main Building',
            'event_category': 'open-day',
            'status': 'upcoming',
            'max_participants': 100,
            'current_participants': 0,
            'registration_required': True,
            'image_url': 'https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=600&h=400&fit=crop'
        },
        {
            'slug': 'medical-olympiad-2025',
            'event_date': datetime.now().date() + timedelta(days=45),
            'event_time': '09:00:00',
            'location_ru': 'Медицинский корпус',
            'location_kg': 'Медициналык корпус',
            'location_en': 'Medical Building',
            'event_category': 'competition',
            'status': 'upcoming',
            'max_participants': 50,
            'current_participants': 0,
            'registration_required': True,
            'image_url': 'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=600&h=400&fit=crop'
        },
        {
            'slug': 'achievements-exhibition-2025',
            'event_date': datetime.now().date() + timedelta(days=60),
            'event_time': '14:00:00',
            'location_ru': 'Выставочный зал',
            'location_kg': 'Көргөзмө залы',
            'location_en': 'Exhibition Hall',
            'event_category': 'ceremony',
            'status': 'upcoming',
            'max_participants': 200,
            'current_participants': 0,
            'registration_required': False,
            'image_url': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=600&h=400&fit=crop'
        }
    ]
    
    for i, (news_item, event_item) in enumerate(zip(news_data, events_data)):
        # Проверяем, существует ли уже новость с таким slug
        existing_news = News.objects.filter(slug=event_item['slug']).first()
        if existing_news:
            print(f"⚠️ Событие с slug '{event_item['slug']}' уже существует, пропускаем...")
            continue
            
        # Создаем новость
        news = News.objects.create(
            category=events_category,
            slug=event_item['slug'],
            **news_item
        )
        
        # Создаем событие
        Event.objects.create(
            news=news,
            event_date=event_item['event_date'],
            event_time=event_item['event_time'],
            location_ru=event_item['location_ru'],
            location_kg=event_item['location_kg'],
            location_en=event_item['location_en'],
            event_category=event_item['event_category'],
            status=event_item['status'],
            max_participants=event_item['max_participants'],
            current_participants=event_item['current_participants'],
            registration_required=event_item['registration_required'],
            image_url=event_item['image_url']
        )
        
    print(f"✅ Создано {len(events_data)} новых событий")

def create_additional_announcements():
    """Создает дополнительные объявления с разными изображениями"""
    
    # Получаем категорию объявлений
    from news.models import NewsCategory
    announcements_category, created = NewsCategory.objects.get_or_create(
        name='announcements',
        defaults={
            'slug': 'announcements',
            'name_ru': 'Объявления',
            'name_kg': 'Жарыялар',
            'name_en': 'Announcements'
        }
    )
    
    news_data = [
        {
            'title_ru': 'Конкурс студенческих работ',
            'title_kg': 'Студенттик иштердин конкурсу',
            'title_en': 'Student Research Competition',
            'content_ru': 'Объявляется конкурс на лучшую студенческую научную работу.',
            'content_kg': 'Эң мыкты студенттик илимий иш үчүн конкурс жарыяланат.',
            'content_en': 'Competition for the best student research work is announced.',
            'summary_ru': 'Конкурс на лучшую научную работу',
            'summary_kg': 'Эң мыкты илимий иш үчүн конкурс',
            'summary_en': 'Competition for the best research work',
            'image_url': 'https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=600&h=400&fit=crop'
        },
        {
            'title_ru': 'Академический отпуск',
            'title_kg': 'Академиялык эс алуу',
            'title_en': 'Academic Leave',
            'content_ru': 'Информация о процедуре оформления академического отпуска.',
            'content_kg': 'Академиялык эс алууну рөөстөө процедурасы жөнүндө маалымат.',
            'content_en': 'Information about the academic leave registration procedure.',
            'summary_ru': 'Информация об академическом отпуске',
            'summary_kg': 'Академиялык эс алуу жөнүндө маалымат',
            'summary_en': 'Information about academic leave',
            'image_url': 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=600&h=400&fit=crop'
        },
        {
            'title_ru': 'Летняя практика',
            'title_kg': 'Жайкы практика',
            'title_en': 'Summer Practice',
            'content_ru': 'Распределение студентов на летнюю медицинскую практику.',
            'content_kg': 'Студенттерди жайкы медициналык практикага бөлүштүрүү.',
            'content_en': 'Distribution of students for summer medical practice.',
            'summary_ru': 'Распределение на летнюю практику',
            'summary_kg': 'Жайкы практикага бөлүштүрүү',
            'summary_en': 'Summer practice distribution',
            'image_url': 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1f?w=600&h=400&fit=crop'
        }
    ]
    
    announcements_data = [
        {
            'slug': 'student-research-competition-2025',
            'announcement_type': 'competition',
            'priority': 'medium',
            'deadline': timezone.now() + timedelta(days=40),
            'is_pinned': False,
            'image_url': 'https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=600&h=400&fit=crop'
        },
        {
            'slug': 'academic-leave-info-2025',
            'announcement_type': 'academic',
            'priority': 'high',
            'deadline': timezone.now() + timedelta(days=20),
            'is_pinned': True,
            'image_url': 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=600&h=400&fit=crop'
        },
        {
            'slug': 'summer-practice-2025',
            'announcement_type': 'academic',
            'priority': 'high',
            'deadline': timezone.now() + timedelta(days=50),
            'is_pinned': False,
            'image_url': 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1f?w=600&h=400&fit=crop'
        }
    ]
    
    for i, (news_item, announcement_item) in enumerate(zip(news_data, announcements_data)):
        # Проверяем, существует ли уже новость с таким slug
        existing_news = News.objects.filter(slug=announcement_item['slug']).first()
        if existing_news:
            print(f"⚠️ Объявление с slug '{announcement_item['slug']}' уже существует, пропускаем...")
            continue
            
        # Создаем новость
        news = News.objects.create(
            category=announcements_category,
            slug=announcement_item['slug'],
            is_pinned=announcement_item['is_pinned'],
            **news_item
        )
        
        # Создаем объявление
        Announcement.objects.create(
            news=news,
            announcement_type=announcement_item['announcement_type'],
            priority=announcement_item['priority'],
            deadline=announcement_item['deadline'],
            image_url=announcement_item['image_url']
        )
        
    print(f"✅ Создано {len(announcements_data)} новых объявлений")

if __name__ == "__main__":
    print("🚀 Добавляем дополнительный контент...")
    create_additional_events()
    create_additional_announcements()
    print("✅ Все дополнительные события и объявления созданы!")
