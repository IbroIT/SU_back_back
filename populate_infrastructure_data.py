#!/usr/bin/env python3
"""
Script to populate infrastructure data for testing the frontend integration
"""

import os
import sys
import django

# Add the project directory to Python path
sys.path.append('/home/adilhan/medicine/SU_back_back')

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from infrastructure.models import (
    ClassroomCategory, Classroom, ClassroomEquipment, ClassroomFeature,
    StartupCategory, Startup, StartupTeamMember, StartupInvestor, StartupAchievement
)

def create_classroom_data():
    """Create sample classroom data"""
    print("Creating classroom data...")
    
    # Create classroom categories
    lecture_cat, created = ClassroomCategory.objects.get_or_create(
        name_ru='Лекционные залы',
        name_kg='Лекция залдары', 
        name_en='Lecture Halls',
        defaults={'icon': '👨‍🏫', 'order': 1}
    )
    
    lab_cat, created = ClassroomCategory.objects.get_or_create(
        name_ru='Лаборатории',
        name_kg='Лабораториялар',
        name_en='Laboratories', 
        defaults={'icon': '🔬', 'order': 2}
    )
    
    practice_cat, created = ClassroomCategory.objects.get_or_create(
        name_ru='Практические залы',
        name_kg='Практикалык залдар',
        name_en='Practice Rooms',
        defaults={'icon': '💊', 'order': 3}
    )
    
    # Create classrooms
    room1, created = Classroom.objects.get_or_create(
        name_ru='Аудитория 101',
        name_kg='101 аудитория',
        name_en='Room 101',
        defaults={
            'category': lecture_cat,
            'description_ru': 'Большая лекционная аудитория с современным оборудованием',
            'description_kg': 'Заманбап жабдуулар менен чоң лекция аудиториясы',
            'description_en': 'Large lecture hall with modern equipment',
            'capacity': 120,
            'floor': '1',
            'size': 200,
            'image': '📊',
            'order': 1
        }
    )
    
    if created:
        # Add equipment
        ClassroomEquipment.objects.create(
            classroom=room1,
            name_ru='Проектор',
            name_kg='Проектор',
            name_en='Projector'
        )
        ClassroomEquipment.objects.create(
            classroom=room1,
            name_ru='Звуковая система',
            name_kg='Добуш системасы',
            name_en='Sound System'
        )
        
        # Add features
        ClassroomFeature.objects.create(
            classroom=room1,
            name_ru='Wi-Fi',
            name_kg='Wi-Fi',
            name_en='Wi-Fi'
        )
        ClassroomFeature.objects.create(
            classroom=room1,
            name_ru='Кондиционер',
            name_kg='Кондиционер',
            name_en='Air Conditioning'
        )
    
    # Create lab room
    lab_room, created = Classroom.objects.get_or_create(
        name_ru='Лаборатория 201',
        name_kg='201 лаборатория',
        name_en='Laboratory 201',
        defaults={
            'category': lab_cat,
            'description_ru': 'Современная лаборатория с микроскопами и оборудованием',
            'description_kg': 'Микроскоптор жана жабдуулар менен заманбап лаборатория',
            'description_en': 'Modern laboratory with microscopes and equipment',
            'capacity': 30,
            'floor': '2',
            'size': 80,
            'image': '🔬',
            'order': 2
        }
    )
    
    if created:
        ClassroomEquipment.objects.create(
            classroom=lab_room,
            name_ru='Микроскопы',
            name_kg='Микроскоптор',
            name_en='Microscopes'
        )
        ClassroomFeature.objects.create(
            classroom=lab_room,
            name_ru='Вентиляция',
            name_kg='Вентиляция',
            name_en='Ventilation'
        )


def create_startup_data():
    """Create sample startup data"""
    print("Creating startup data...")
    
    # Create startup categories
    medtech_cat, created = StartupCategory.objects.get_or_create(
        name_ru='Медтех',
        name_kg='Медтех',
        name_en='MedTech',
        defaults={'icon': '🩺', 'order': 1}
    )
    
    digital_cat, created = StartupCategory.objects.get_or_create(
        name_ru='Цифровое здоровье',
        name_kg='Санариптик ден соолук',
        name_en='Digital Health',
        defaults={'icon': '💻', 'order': 2}
    )
    
    biotech_cat, created = StartupCategory.objects.get_or_create(
        name_ru='Биотех',
        name_kg='Биотех',  
        name_en='BioTech',
        defaults={'icon': '🧬', 'order': 3}
    )
    
    # Create startups
    startup1, created = Startup.objects.get_or_create(
        name_ru='МедАпп',
        name_kg='МедАпп',
        name_en='MedApp',
        defaults={
            'category': digital_cat,
            'description_ru': 'Мобильное приложение для мониторинга здоровья',
            'description_kg': 'Ден соолукту көзөмөлдөө үчүн мобилдик тиркеме',
            'description_en': 'Mobile app for health monitoring',
            'full_description_ru': 'Инновационное мобильное приложение для комплексного мониторинга здоровья пациентов с использованием искусственного интеллекта',
            'full_description_kg': 'Жасалма акыл колдонуу менен бейтаптардын ден соолугун комплекстүү көзөмөлдөө үчүн инновациялык мобилдик тиркеме',
            'full_description_en': 'Innovative mobile application for comprehensive patient health monitoring using artificial intelligence',
            'stage': 'seed',
            'status': 'active',
            'funding': '$500K',
            'year': '2023',
            'image': '📱',
            'order': 1
        }
    )
    
    if created:
        # Add team members
        StartupTeamMember.objects.create(
            startup=startup1,
            name_ru='Доктор Алиев А.А.',
            name_kg='Доктор Алиев А.А.',
            name_en='Dr. Aliev A.A.'
        )
        StartupTeamMember.objects.create(
            startup=startup1,
            name_ru='Инженер Смирнов И.И.',
            name_kg='Инженер Смирнов И.И.',
            name_en='Engineer Smirnov I.I.'
        )
        
        # Add investors
        StartupInvestor.objects.create(
            startup=startup1,
            name_ru='Университетский фонд',
            name_kg='Университет фонду',
            name_en='University Fund'
        )
        
        # Add achievements
        StartupAchievement.objects.create(
            startup=startup1,
            achievement_ru='Победитель конкурса стартапов 2023',
            achievement_kg='2023-жылкы стартаптар сынагынын жеңүүчүсү',
            achievement_en='Winner of Startup Competition 2023'
        )
    
    # Create another startup
    startup2, created = Startup.objects.get_or_create(
        name_ru='БиоСенсор',
        name_kg='БиоСенсор',
        name_en='BioSensor',
        defaults={
            'category': medtech_cat,
            'description_ru': 'Портативные биосенсоры для диагностики',
            'description_kg': 'Диагностика үчүн көчмө биосенсорлор',
            'description_en': 'Portable biosensors for diagnostics',
            'full_description_ru': 'Разработка портативных биосенсоров для быстрой диагностики заболеваний в полевых условиях',
            'full_description_kg': 'Талаа шартында оорулардын тез диагностикасы үчүн көчмө биосенсорлорду иштеп чыгуу',
            'full_description_en': 'Development of portable biosensors for rapid disease diagnosis in field conditions',
            'stage': 'series_a',
            'status': 'scaling',
            'funding': '$1.2M',
            'year': '2022',
            'image': '📟',
            'order': 2
        }
    )
    
    if created:
        StartupTeamMember.objects.create(
            startup=startup2,
            name_ru='Профессор Иванов П.П.',
            name_kg='Профессор Иванов П.П.',
            name_en='Professor Ivanov P.P.'
        )
        StartupInvestor.objects.create(
            startup=startup2,
            name_ru='Венчурный капитал',
            name_kg='Венчурдук капитал',
            name_en='Venture Capital'
        )
        StartupAchievement.objects.create(
            startup=startup2,
            achievement_ru='Получен патент на технологию',
            achievement_kg='Технологияга патент алынды',
            achievement_en='Patent received for technology'
        )


def main():
    """Main function to create all test data"""
    print("Starting data population...")
    
    try:
        create_classroom_data()
        create_startup_data()
        print("Data population completed successfully!")
        
    except Exception as e:
        print(f"Error during data population: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()