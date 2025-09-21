#!/usr/bin/env python
"""
Скрипт для создания тестовых данных для галереи и студенческой жизни
"""

import os
import sys
import django
from datetime import datetime, date, timedelta

# Добавляем путь к Django проекту
sys.path.append('/Users/adminbaike/medicine/SU_back_back')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')

# Настраиваем Django
django.setup()

from student_life.models import PhotoAlbum, Photo, VideoContent, StudentLifeStatistic


def create_photo_albums():
    """Создание фотоальбомов"""
    albums_data = [
        {
            'title_ru': 'Ориентация новых студентов 2023',
            'title_kg': '2023-жылы жаңы студенттердин ориентациясы',
            'title_en': 'New Students Orientation 2023',
            'description_ru': 'Мероприятие по знакомству первокурсников с университетом',
            'description_kg': 'Биринчи курс студенттерин университет менен тааныштыруу иш-чарасы',
            'description_en': 'Event to introduce freshmen to the university',
            'tags_ru': 'ориентация, студенты, университет, знакомство',
            'tags_kg': 'ориентация, студенттер, университет, тааныштыруу',
            'tags_en': 'orientation, students, university, introduction',
            'event_date': date(2023, 9, 1),
            'order': 1
        },
        {
            'title_ru': 'Выпускной 2023',
            'title_kg': '2023-жылкы бүтүрүү',
            'title_en': 'Graduation 2023',
            'description_ru': 'Торжественная церемония вручения дипломов выпускникам',
            'description_kg': 'Бүтүрүүчүлөргө дипломдорду салтанаттуу берүү аземи',
            'description_en': 'Solemn ceremony of diploma presentation to graduates',
            'tags_ru': 'выпускной, диплом, церемония, выпускники',
            'tags_kg': 'бүтүрүү, диплом, аземи, бүтүрүүчүлөр',
            'tags_en': 'graduation, diploma, ceremony, graduates',
            'event_date': date(2023, 6, 15),
            'order': 2
        },
        {
            'title_ru': 'Научный симпозиум молодых ученых',
            'title_kg': 'Жаш илимпоздордун илимий симпозиуму',
            'title_en': 'Young Scientists Symposium',
            'description_ru': 'Конференция с участием студентов и молодых исследователей',
            'description_kg': 'Студенттер жана жаш изилдөөчүлөр катышкан конференция',
            'description_en': 'Conference with participation of students and young researchers',
            'tags_ru': 'наука, исследования, конференция, молодые ученые',
            'tags_kg': 'илим, изилдөөлөр, конференция, жаш илимпоздор',
            'tags_en': 'science, research, conference, young scientists',
            'event_date': date(2023, 10, 20),
            'order': 3
        },
        {
            'title_ru': 'Спортивные мероприятия',
            'title_kg': 'Спорттук иш-чаралар',
            'title_en': 'Sports Events',
            'description_ru': 'Соревнования и спортивные праздники студентов',
            'description_kg': 'Студенттердин мелдештери жана спорттук майрамдары',
            'description_en': 'Competitions and sports festivals of students',
            'tags_ru': 'спорт, соревнования, здоровье, активность',
            'tags_kg': 'спорт, мелдештер, ден соолук, активдүүлүк',
            'tags_en': 'sports, competitions, health, activity',
            'event_date': date(2023, 11, 5),
            'order': 4
        },
        {
            'title_ru': 'Культурные мероприятия',
            'title_kg': 'Маданий иш-чаралар',
            'title_en': 'Cultural Events',
            'description_ru': 'Концерты, фестивали и творческие вечера',
            'description_kg': 'Концерттер, фестивалдар жана чыгармачылык кечелери',
            'description_en': 'Concerts, festivals and creative evenings',
            'tags_ru': 'культура, концерт, творчество, искусство',
            'tags_kg': 'маданият, концерт, чыгармачылык, искусство',
            'tags_en': 'culture, concert, creativity, art',
            'event_date': date(2023, 12, 10),
            'order': 5
        }
    ]
    
    created_albums = []
    for album_data in albums_data:
        album, created = PhotoAlbum.objects.get_or_create(
            title_ru=album_data['title_ru'],
            defaults=album_data
        )
        if created:
            print(f"✅ Создан альбом: {album.title_ru}")
        else:
            print(f"📁 Альбом уже существует: {album.title_ru}")
        created_albums.append(album)
    
    return created_albums


def create_photos(albums):
    """Создание фотографий для альбомов"""
    # Используем placeholder изображения для демонстрации
    photos_data = [
        # Фотографии для ориентации
        {
            'album': albums[0],
            'title_ru': 'Приветствие ректора',
            'title_kg': 'Ректордун куттуктоосу',
            'title_en': 'Rector\'s Welcome',
            'url': 'https://images.unsplash.com/photo-1523050854058-8df90110c9f1?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80',
            'tags_ru': 'ректор, приветствие, речь',
            'tags_kg': 'ректор, куттуктоо, сөз',
            'tags_en': 'rector, welcome, speech',
            'order': 1
        },
        {
            'album': albums[0],
            'title_ru': 'Знакомство с факультетами',
            'title_kg': 'Факультеттер менен тааныштыруу',
            'title_en': 'Faculty Introduction',
            'url': 'https://images.unsplash.com/photo-1523580494863-6f3031224c94?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80',
            'tags_ru': 'факультеты, знакомство, студенты',
            'tags_kg': 'факультеттер, тааныштыруу, студенттер',
            'tags_en': 'faculties, introduction, students',
            'order': 2
        },
        {
            'album': albums[0],
            'title_ru': 'Экскурсия по университету',
            'title_kg': 'Университет боюнча экскурсия',
            'title_en': 'University Tour',
            'url': 'https://images.unsplash.com/photo-1523240795612-9a054b0db644?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80',
            'tags_ru': 'экскурсия, университет, здания',
            'tags_kg': 'экскурсия, университет, имараттар',
            'tags_en': 'tour, university, buildings',
            'order': 3
        },
        
        # Фотографии для выпускного
        {
            'album': albums[1],
            'title_ru': 'Торжественная процессия',
            'title_kg': 'Салтанаттуу жүрүш',
            'title_en': 'Graduation Procession',
            'url': 'https://images.unsplash.com/photo-1535982337059-51a5b2d3c079?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80',
            'tags_ru': 'процессия, выпускники, мантии',
            'tags_kg': 'жүрүш, бүтүрүүчүлөр, мантиялар',
            'tags_en': 'procession, graduates, gowns',
            'order': 1
        },
        {
            'album': albums[1],
            'title_ru': 'Вручение дипломов',
            'title_kg': 'Дипломдорду берүү',
            'title_en': 'Diploma Presentation',
            'url': 'https://images.unsplash.com/photo-1567690346811-22291ebe92ed?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80',
            'tags_ru': 'диплом, вручение, награждение',
            'tags_kg': 'диплом, берүү, сыйлоо',
            'tags_en': 'diploma, presentation, award',
            'order': 2
        },
        {
            'album': albums[1],
            'title_ru': 'Семейные фотографии',
            'title_kg': 'Үй-бүлөлүк сүрөттөр',
            'title_en': 'Family Photos',
            'url': 'https://images.unsplash.com/photo-1588200908342-23b585c03e26?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80',
            'tags_ru': 'семья, выпускники, радость',
            'tags_kg': 'үй-бүлө, бүтүрүүчүлөр, кубаныч',
            'tags_en': 'family, graduates, joy',
            'order': 3
        },
        
        # Фотографии для симпозиума
        {
            'album': albums[2],
            'title_ru': 'Презентации исследований',
            'title_kg': 'Изилдөөлөрдү презентациялоо',
            'title_en': 'Research Presentations',
            'url': 'https://images.unsplash.com/photo-1553877522-43269d4ea984?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80',
            'tags_ru': 'исследования, презентация, наука',
            'tags_kg': 'изилдөөлөр, презентация, илим',
            'tags_en': 'research, presentation, science',
            'order': 1
        },
        {
            'album': albums[2],
            'title_ru': 'Постерная сессия',
            'title_kg': 'Постер сессиясы',
            'title_en': 'Poster Session',
            'url': 'https://images.unsplash.com/photo-1540575467063-178a50c2df87?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80',
            'tags_ru': 'постеры, исследования, обсуждение',
            'tags_kg': 'постерлер, изилдөөлөр, талкуулоо',
            'tags_en': 'posters, research, discussion',
            'order': 2
        },
    ]
    
    created_photos = []
    for photo_data in photos_data:
        # Для демонстрации используем placeholder URL
        image_url = f"https://picsum.photos/800/600?random={len(created_photos)+1}"
        
        # В реальном проекте здесь будет сохранение файла
        # Пока что создаем запись без файла изображения
        photo_data_copy = photo_data.copy()
        photo_data_copy.pop('image_url', None)
        
        photo, created = Photo.objects.get_or_create(
            album=photo_data['album'],
            title_ru=photo_data['title_ru'],
            defaults=photo_data_copy
        )
        
        if created:
            print(f"📸 Создана фотография: {photo.title_ru}")
        else:
            print(f"🖼️ Фотография уже существует: {photo.title_ru}")
        created_photos.append(photo)
    
    return created_photos


def create_video_content():
    """Создание видеоконтента"""
    videos_data = [
        {
            'title_ru': 'Фестиваль студенческого творчества',
            'title_kg': 'Студенттик чыгармачылык фестивалы',
            'title_en': 'Student Creativity Festival',
            'description_ru': 'Ежегодный фестиваль талантов студентов университета',
            'description_kg': 'Университеттин студенттеринин таланттарынын жыл сайынкы фестивалы',
            'description_en': 'Annual festival of university students\' talents',
            'thumbnail': 'https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80',
            'type': 'event',
            'duration': '15:30',
            'tags_ru': 'фестиваль, творчество, таланты, музыка',
            'tags_kg': 'фестиваль, чыгармачылык, таланттар, музыка',
            'tags_en': 'festival, creativity, talents, music',
            'is_featured': True,
            'order': 1,
            'event_date': date(2023, 11, 15)
        },
        {
            'title_ru': 'Научная конференция молодых исследователей',
            'title_kg': 'Жаш изилдөөчүлөрдүн илимий конференциясы',
            'title_en': 'Young Researchers Scientific Conference',
            'description_ru': 'Презентация лучших научных работ студентов',
            'description_kg': 'Студенттердин эң мыкты илимий иштеринин презентациясы',
            'description_en': 'Presentation of the best scientific works of students',
            'thumbnail': 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1f?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80',
            'type': 'documentary',
            'duration': '22:45',
            'tags_ru': 'конференция, наука, исследования, медицина',
            'tags_kg': 'конференция, илим, изилдөөлөр, медицина',
            'tags_en': 'conference, science, research, medicine',
            'is_featured': True,
            'order': 2,
            'event_date': date(2023, 10, 20)
        },
        {
            'title_ru': 'Спортивные достижения студентов',
            'title_kg': 'Студенттердин спорттук жетишкендиктери',
            'title_en': 'Students\' Sports Achievements',
            'description_ru': 'Обзор спортивных побед и достижений наших студентов',
            'description_kg': 'Биздин студенттердин спорттук жеңиштери жана жетишкендиктеринин сереби',
            'description_en': 'Overview of sports victories and achievements of our students',
            'thumbnail': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80',
            'type': 'event',
            'duration': '8:12',
            'tags_ru': 'спорт, достижения, соревнования, команда',
            'tags_kg': 'спорт, жетишкендиктер, мелдештер, команда',
            'tags_en': 'sports, achievements, competitions, team',
            'is_featured': True,
            'order': 3,
            'event_date': date(2023, 12, 5)
        },
        {
            'title_ru': 'Интервью с выпускниками',
            'title_kg': 'Бүтүрүүчүлөр менен маек',
            'title_en': 'Interviews with Graduates',
            'description_ru': 'Истории успеха наших выпускников в медицинской практике',
            'description_kg': 'Биздин бүтүрүүчүлөрдүн медициналык практикадагы ийгилик окуялары',
            'description_en': 'Success stories of our graduates in medical practice',
            'type': 'interview',
            'duration': '12:18',
            'tags_ru': 'интервью, выпускники, карьера, медицина',
            'tags_kg': 'маек, бүтүрүүчүлөр, карьера, медицина',
            'tags_en': 'interview, graduates, career, medicine',
            'is_featured': False,
            'order': 4,
            'event_date': date(2023, 9, 10)
        }
    ]
    
    created_videos = []
    for video_data in videos_data:
        video, created = VideoContent.objects.get_or_create(
            title_ru=video_data['title_ru'],
            defaults=video_data
        )
        if created:
            print(f"🎥 Создано видео: {video.title_ru}")
        else:
            print(f"📹 Видео уже существует: {video.title_ru}")
        created_videos.append(video)
    
    return created_videos


def create_statistics():
    """Создание статистики студенческой жизни"""
    statistics_data = [
        {
            'label_ru': 'Студенческих клубов',
            'label_kg': 'Студенттик клубдар',
            'label_en': 'Student Clubs',
            'description_ru': 'Активных студенческих организаций и клубов по интересам',
            'description_kg': 'Активдүү студенттик уюмдар жана кызыкчылыктар боюнча клубдар',
            'description_en': 'Active student organizations and interest clubs',
            'value': '15+',
            'type': 'clubs',
            'icon': 'UserGroupIcon',
            'order': 1
        },
        {
            'label_ru': 'Мероприятий в год',
            'label_kg': 'Жылдагы иш-чаралар',
            'label_en': 'Events per Year',
            'description_ru': 'Культурных, научных и спортивных мероприятий',
            'description_kg': 'Маданий, илимий жана спорттук иш-чаралар',
            'description_en': 'Cultural, scientific and sports events',
            'value': '50+',
            'type': 'events',
            'icon': 'CalendarDaysIcon',
            'order': 2
        },
        {
            'label_ru': 'Фотографий в галерее',
            'label_kg': 'Галереядагы сүрөттөр',
            'label_en': 'Photos in Gallery',
            'description_ru': 'Документирующих яркие моменты студенческой жизни',
            'description_kg': 'Студенттик турмуштун жаркын учурларын документалдаштыруучу',
            'description_en': 'Documenting bright moments of student life',
            'value': '1000+',
            'type': 'photos',
            'icon': 'PhotoIcon',
            'order': 3
        },
        {
            'label_ru': 'Активных студентов',
            'label_kg': 'Активдүү студенттер',
            'label_en': 'Active Students',
            'description_ru': 'Принимающих участие во внеучебной деятельности',
            'description_kg': 'Окуудан тышкары ишмердүүлүккө катышуучу',
            'description_en': 'Participating in extracurricular activities',
            'value': '800+',
            'type': 'students',
            'icon': 'AcademicCapIcon',
            'order': 4
        },
        {
            'label_ru': 'Наград и достижений',
            'label_kg': 'Сыйлыктар жана жетишкендиктер',
            'label_en': 'Awards and Achievements',
            'description_ru': 'Полученных студентами в различных конкурсах',
            'description_kg': 'Студенттер ар кандай конкурстарда алган',
            'description_en': 'Received by students in various competitions',
            'value': '25+',
            'type': 'achievements',
            'icon': 'TrophyIcon',
            'order': 5
        }
    ]
    
    created_stats = []
    for stat_data in statistics_data:
        stat, created = StudentLifeStatistic.objects.get_or_create(
            type=stat_data['type'],
            defaults=stat_data
        )
        if created:
            print(f"📊 Создана статистика: {stat.label_ru}")
        else:
            print(f"📈 Статистика уже существует: {stat.label_ru}")
        created_stats.append(stat)
    
    return created_stats


def main():
    """Основная функция для создания всех тестовых данных"""
    print("🚀 Создание тестовых данных для галереи и студенческой жизни...")
    print("=" * 60)
    
    # Создаем альбомы
    print("\n📁 Создание фотоальбомов...")
    albums = create_photo_albums()
    
    # Создаем фотографии
    print("\n📸 Создание фотографий...")
    photos = create_photos(albums)
    
    # Создаем видеоконтент
    print("\n🎥 Создание видеоконтента...")
    videos = create_video_content()
    
    # Создаем статистику
    print("\n📊 Создание статистики...")
    statistics = create_statistics()
    
    print("\n" + "=" * 60)
    print("✅ Тестовые данные успешно созданы!")
    print(f"📁 Альбомов: {len(albums)}")
    print(f"📸 Фотографий: {len(photos)}")
    print(f"🎥 Видео: {len(videos)}")
    print(f"📊 Показателей статистики: {len(statistics)}")
    
    print("\n🌐 Доступные API endpoints:")
    print("• GET /student_life/api/data/gallery_data/ - данные галереи")
    print("• GET /student_life/api/data/life_overview_data/ - данные обзора")
    print("• GET /student_life/api/photo-albums/ - альбомы")
    print("• GET /student_life/api/photos/ - фотографии")
    print("• GET /student_life/api/videos/ - видео")
    print("• GET /student_life/api/statistics/ - статистика")


if __name__ == '__main__':
    main()
