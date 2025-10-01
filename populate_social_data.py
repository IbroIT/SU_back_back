#!/usr/bin/env python
"""
Скрипт для добавления тестовых данных в базу данных
"""
import os
import sys
import django
from datetime import datetime, timedelta

# Добавляем корневую директорию проекта в Python path
sys.path.append('/home/adilhan/medicine/SU_back')

# Настраиваем Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from social_opportunities.models import Event, Club, Project


def create_events():
    """Создание тестовых событий"""
    events_data = [
        {
            'title': 'Международная медицинская конференция',
            'title_en': 'International Medical Conference',
            'title_ky': 'Эл аралык медициналык конференция',
            'description': 'Конференция с участием ведущих специалистов в области медицины. Обсуждение современных методов диагностики и лечения.',
            'description_en': 'Conference with leading medical specialists. Discussion of modern diagnostic and treatment methods.',
            'description_ky': 'Медицина тармагынын алдыңкы адистери катышкан конференция. Заманбап диагностика жана дарылоо ыкмаларын талкуулоо.',
            'date': datetime.now() + timedelta(days=30),
            'location': 'Главный корпус, Актовый зал',
            'location_en': 'Main Building, Assembly Hall',
            'location_ky': 'Башкы корпус, Жыйын залы',
            'organizer': 'Медицинский факультет',
            'organizer_en': 'Medical Faculty',
            'organizer_ky': 'Медицина факультети',
            'participants': '200+',
            'category': 'conference',
            'status': 'upcoming',
            'registration': 'open',
            'image': '🏥',
            'color': 'bg-blue-500',
            'popular': True
        },
        {
            'title': 'Студенческий научный форум',
            'title_en': 'Student Scientific Forum',
            'title_ky': 'Студенттик илимий форум',
            'description': 'Презентация исследовательских проектов студентов и молодых ученых.',
            'description_en': 'Presentation of research projects by students and young scientists.',
            'description_ky': 'Студенттердин жана жаш илимпоздордун изилдөө долбоорлорун презентациялоо.',
            'date': datetime.now() + timedelta(days=15),
            'location': 'Научный центр',
            'location_en': 'Research Center',
            'location_ky': 'Илимий борбор',
            'organizer': 'Студенческий совет',
            'organizer_en': 'Student Council',
            'organizer_ky': 'Студенттик кеңеш',
            'participants': '150+',
            'category': 'forum',
            'status': 'upcoming',
            'registration': 'open',
            'image': '🔬',
            'color': 'bg-green-500',
            'popular': False
        },
        {
            'title': 'Ярмарка карьеры в медицине',
            'title_en': 'Medical Career Fair',
            'title_ky': 'Медицинадагы карьера жармаңкеси',
            'description': 'Встреча с работодателями, презентация вакансий и стажировок.',
            'description_en': 'Meeting with employers, presentation of vacancies and internships.',
            'description_ky': 'Жумуш берүүчүлөр менен жолугушуу, бош орундарды жана практиканы тааныштыруу.',
            'date': datetime.now() + timedelta(days=45),
            'location': 'Центр карьеры',
            'location_en': 'Career Center',
            'location_ky': 'Карьера борбору',
            'organizer': 'Отдел трудоустройства',
            'organizer_en': 'Employment Department',
            'organizer_ky': 'Жумушка орноштуруу бөлүмү',
            'participants': '300+',
            'category': 'career',
            'status': 'upcoming',
            'registration': 'open',
            'image': '💼',
            'color': 'bg-purple-500',
            'popular': True
        }
    ]
    
    for event_data in events_data:
        event, created = Event.objects.get_or_create(
            title=event_data['title'],
            defaults=event_data
        )
        if created:
            print(f"Создано событие: {event.title}")
        else:
            print(f"Событие уже существует: {event.title}")


def create_clubs():
    """Создание тестовых клубов"""
    clubs_data = [
        {
            'title': 'Медицинское волонтерское сообщество',
            'title_en': 'Medical Volunteer Community',
            'title_ky': 'Медициналык волонтердук коомчулук',
            'description': 'Помощь медицинским учреждениям и проведение акций по охране здоровья.',
            'description_en': 'Assistance to medical institutions and health promotion campaigns.',
            'description_ky': 'Медициналык мекемелерге жардам берүү жана ден соолукту сактоо боюнча акцияларды өткөрүү.',
            'members': '85',
            'meetings': 'Каждую среду в 18:00',
            'meetings_en': 'Every Wednesday at 18:00',
            'meetings_ky': 'Ар шаршемби саат 18:00дө',
            'leader': 'Анна Иванова (4 курс)',
            'leader_en': 'Anna Ivanova (4th year)',
            'leader_ky': 'Анна Иванова (4-курс)',
            'achievements': ['Провели 15 медосмотров', 'Помогли 500+ людям', 'Награда "Лучший клуб года"'],
            'achievements_en': ['Conducted 15 medical examinations', 'Helped 500+ people', 'Best Club of the Year Award'],
            'achievements_ky': ['15 медкароого өткөрдүк', '500+ адамга жардам бердик', '"Жылдын эң мыкты клубу" сыйлыгы'],
            'category': 'social',
            'status': 'active',
            'image': '🏥',
            'color': 'bg-green-500',
            'popular': True
        },
        {
            'title': 'Научное студенческое общество',
            'title_en': 'Scientific Student Society',
            'title_ky': 'Илимий студенттик коом',
            'description': 'Исследования, конференции и научные публикации для студентов.',
            'description_en': 'Research, conferences and scientific publications for students.',
            'description_ky': 'Студенттер үчүн изилдөөлөр, конференциялар жана илимий жарыялоолор.',
            'members': '45',
            'meetings': 'Пятница в 16:00',
            'meetings_en': 'Friday at 16:00',
            'meetings_ky': 'Жума күнү саат 16:00дө',
            'leader': 'Максим Петров (5 курс)',
            'leader_en': 'Maxim Petrov (5th year)',
            'leader_ky': 'Максим Петров (5-курс)',
            'achievements': ['20 научных статей', 'Участие в 5 конференциях', 'Грант на исследования'],
            'achievements_en': ['20 scientific articles', 'Participation in 5 conferences', 'Research grant'],
            'achievements_ky': ['20 илимий макала', '5 конференцияга катышуу', 'Изилдөө гранты'],
            'category': 'academic',
            'status': 'active',
            'image': '🔬',
            'color': 'bg-blue-500',
            'popular': False
        },
        {
            'title': 'Спортивный клуб "Медик"',
            'title_en': 'Sports Club "Medic"',
            'title_ky': '"Медик" спорт клубу',
            'description': 'Тренировки, соревнования и пропаганда здорового образа жизни.',
            'description_en': 'Training, competitions and promotion of healthy lifestyle.',
            'description_ky': 'Машыгуулар, мелдештер жана дени сак жашоо образын илгерилетүү.',
            'members': '120',
            'meetings': 'Понедельник, среда, пятница в 17:00',
            'meetings_en': 'Monday, Wednesday, Friday at 17:00',
            'meetings_ky': 'Дүйшөмбү, шаршемби, жума саат 17:00дө',
            'leader': 'Елена Сидорова (3 курс)',
            'leader_en': 'Elena Sidorova (3rd year)',
            'leader_ky': 'Елена Сидорова (3-курс)',
            'achievements': ['1 место в университетской лиге', 'Организовали 5 турниров', 'Команда года'],
            'achievements_en': ['1st place in university league', 'Organized 5 tournaments', 'Team of the year'],
            'achievements_ky': ['Университет лигасында 1-орун', '5 турнир уюштурдук', 'Жылдын командасы'],
            'category': 'sports',
            'status': 'active',
            'image': '⚽',
            'color': 'bg-red-500',
            'popular': True
        }
    ]
    
    for club_data in clubs_data:
        club, created = Club.objects.get_or_create(
            title=club_data['title'],
            defaults=club_data
        )
        if created:
            print(f"Создан клуб: {club.title}")
        else:
            print(f"Клуб уже существует: {club.title}")


def create_projects():
    """Создание тестовых проектов"""
    projects_data = [
        {
            'title': 'Мобильное приложение для пациентов',
            'title_en': 'Mobile App for Patients',
            'title_ky': 'Бейтаптар үчүн мобилдик колдонмо',
            'description': 'Разработка приложения для записи к врачу и отслеживания медицинских показателей.',
            'description_en': 'Development of an app for doctor appointments and health metrics tracking.',
            'description_ky': 'Дарыгерге жазылуу жана медициналык көрсөткүчтөрдү көзөмөлдөө үчүн колдонмо иштеп чыгуу.',
            'team': '7',
            'progress': 65,
            'needs': ['Flutter разработчик', 'UI/UX дизайнер', 'Backend разработчик'],
            'needs_en': ['Flutter developer', 'UI/UX designer', 'Backend developer'],
            'needs_ky': ['Flutter иштеп чыгуучу', 'UI/UX дизайнер', 'Backend иштеп чыгуучу'],
            'category': 'technology',
            'status': 'active',
            'image': '📱',
            'color': 'bg-purple-500',
            'popular': True
        },
        {
            'title': 'Исследование влияния стресса на иммунитет',
            'title_en': 'Stress Impact on Immunity Research',
            'title_ky': 'Стресстин иммунитетке тийгизген таасирин изилдөө',
            'description': 'Научный проект по изучению взаимосвязи между уровнем стресса и иммунной системой.',
            'description_en': 'Research project studying the relationship between stress levels and immune system.',
            'description_ky': 'Стресс деңгээли менен иммундук система ортосундагы байланышты изилдөөчү илимий долбоор.',
            'team': '4',
            'progress': 40,
            'needs': ['Статистик', 'Лаборант', 'Студенты-волонтеры'],
            'needs_en': ['Statistician', 'Lab technician', 'Student volunteers'],
            'needs_ky': ['Статистик', 'Лаборант', 'Студент волонтерлер'],
            'category': 'research',
            'status': 'active',
            'image': '🧬',
            'color': 'bg-green-500',
            'popular': False
        },
        {
            'title': 'Социальная программа "Здоровое питание"',
            'title_en': 'Healthy Nutrition Social Program',
            'title_ky': '"Дени сак тамактануу" социалдык программасы',
            'description': 'Программа пропаганды здорового питания среди студентов и местного населения.',
            'description_en': 'Program promoting healthy nutrition among students and local population.',
            'description_ky': 'Студенттер жана жергиликтүү калк арасында дени сак тамактанууну илгерилетүү программасы.',
            'team': '12',
            'progress': 80,
            'needs': ['Нутрициолог', 'Маркетолог', 'Координатор мероприятий'],
            'needs_en': ['Nutritionist', 'Marketer', 'Event coordinator'],
            'needs_ky': ['Нутрициолог', 'Маркетолог', 'Иш-чара координатору'],
            'category': 'social',
            'status': 'active',
            'image': '🥗',
            'color': 'bg-amber-500',
            'popular': True
        }
    ]
    
    for project_data in projects_data:
        project, created = Project.objects.get_or_create(
            title=project_data['title'],
            defaults=project_data
        )
        if created:
            print(f"Создан проект: {project.title}")
        else:
            print(f"Проект уже существует: {project.title}")


def main():
    """Основная функция"""
    print("Начинаем создание тестовых данных...")
    
    # Создаем события
    print("\n=== Создание событий ===")
    create_events()
    
    # Создаем клубы
    print("\n=== Создание клубов ===")
    create_clubs()
    
    # Создаем проекты
    print("\n=== Создание проектов ===")
    create_projects()
    
    print("\nТестовые данные успешно созданы!")


if __name__ == '__main__':
    main()