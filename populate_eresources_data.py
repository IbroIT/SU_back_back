#!/usr/bin/env python
"""
Скрипт для добавления тестовых данных EResources
"""
import os
import sys
import django

# Настройка Django окружения
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from student_life.models import EResourceCategory, EResource, EResourceFeature

def create_eresources_data():
    """Создание тестовых данных для EResources"""
    
    print("🚀 Создание категорий EResources...")
    
    # Создание категорий
    categories_data = [
        {
            'name_ru': 'Библиотечные ресурсы',
            'name_kg': 'Китепкана ресурстары',
            'name_en': 'Library Resources',
            'icon': '📚',
            'color': 'from-blue-500 to-blue-600',
            'order': 1
        },
        {
            'name_ru': 'Научные базы данных',
            'name_kg': 'Илимий маалымат базалары',
            'name_en': 'Scientific Databases',
            'icon': '🔬',
            'color': 'from-green-500 to-green-600',
            'order': 2
        },
        {
            'name_ru': 'Образовательные платформы',
            'name_kg': 'Билим берүү платформалары',
            'name_en': 'Educational Platforms',
            'icon': '🎓',
            'color': 'from-purple-500 to-purple-600',
            'order': 3
        },
        {
            'name_ru': 'Медицинские ресурсы',
            'name_kg': 'Медициналык ресурстар',
            'name_en': 'Medical Resources',
            'icon': '⚕️',
            'color': 'from-red-500 to-red-600',
            'order': 4
        },
        {
            'name_ru': 'Исследовательские инструменты',
            'name_kg': 'Изилдөө куралдары',
            'name_en': 'Research Tools',
            'icon': '🔍',
            'color': 'from-orange-500 to-orange-600',
            'order': 5
        }
    ]
    
    categories = {}
    for cat_data in categories_data:
        category, created = EResourceCategory.objects.get_or_create(
            name_ru=cat_data['name_ru'],
            defaults=cat_data
        )
        categories[cat_data['name_ru']] = category
        if created:
            print(f"✅ Создана категория: {cat_data['name_ru']}")
        else:
            print(f"➡️ Категория уже существует: {cat_data['name_ru']}")
    
    print("\n📖 Создание ресурсов...")
    
    # Создание ресурсов
    resources_data = [
        {
            'category': 'Библиотечные ресурсы',
            'title_ru': 'Электронная библиотека SU',
            'title_kg': 'SU электрондук китепканасы',
            'title_en': 'SU Digital Library',
            'description_ru': 'Доступ к более чем 50,000 научных публикаций, учебников и журналов',
            'description_kg': '50,000дөн ашык илимий басылмаларга, окуу китептерине жана журналдарга жетүү',
            'description_en': 'Access to over 50,000 scientific publications, textbooks and journals',
            'icon': '📖',
            'color': 'from-blue-500 to-blue-600',
            'url': 'https://library.su.edu.kg',
            'users_count': 2500,
            'status': 'online',
            'is_popular': True,
            'order': 1,
            'features': [
                {
                    'text_ru': 'Круглосуточный доступ',
                    'text_kg': '24 саат жетүү',
                    'text_en': '24/7 access'
                },
                {
                    'text_ru': 'Мобильное приложение',
                    'text_kg': 'Мобилдик тиркеме',
                    'text_en': 'Mobile application'
                },
                {
                    'text_ru': 'Поиск по полному тексту',
                    'text_kg': 'Толук текст боюнча издөө',
                    'text_en': 'Full-text search'
                }
            ]
        },
        {
            'category': 'Научные базы данных',
            'title_ru': 'PubMed Central',
            'title_kg': 'PubMed Central',
            'title_en': 'PubMed Central',
            'description_ru': 'Бесплатная база данных биомедицинской и жизненно важной литературы',
            'description_kg': 'Биомедициналык жана өмүргө маанилүү адабияттын акысыз маалымат базасы',
            'description_en': 'Free database of biomedical and life sciences literature',
            'icon': '🧬',
            'color': 'from-green-500 to-green-600',
            'url': 'https://www.ncbi.nlm.nih.gov/pmc/',
            'users_count': 1800,
            'status': 'online',
            'is_popular': True,
            'order': 1,
            'features': [
                {
                    'text_ru': 'Рецензируемые статьи',
                    'text_kg': 'Рецензияланган макалалар',
                    'text_en': 'Peer-reviewed articles'
                },
                {
                    'text_ru': 'Регулярные обновления',
                    'text_kg': 'Үзгүлтүксүз жаңыртуулар',
                    'text_en': 'Regular updates'
                },
                {
                    'text_ru': 'Экспорт цитирований',
                    'text_kg': 'Шилтемелерди экспорттоо',
                    'text_en': 'Citation export'
                }
            ]
        },
        {
            'category': 'Образовательные платформы',
            'title_ru': 'Coursera для университетов',
            'title_kg': 'Университеттер үчүн Coursera',
            'title_en': 'Coursera for Universities',
            'description_ru': 'Доступ к тысячам онлайн-курсов от ведущих университетов мира',
            'description_kg': 'Дүйнөнүн алдыңкы университеттеринен миңдеген онлайн курстарга жетүү',
            'description_en': 'Access to thousands of online courses from leading world universities',
            'icon': '🎯',
            'color': 'from-purple-500 to-purple-600',
            'url': 'https://www.coursera.org/for-university-and-college-students',
            'users_count': 1200,
            'status': 'online',
            'is_popular': False,
            'order': 2,
            'features': [
                {
                    'text_ru': 'Сертификаты об окончании',
                    'text_kg': 'Бүтүрүү сертификаттары',
                    'text_en': 'Completion certificates'
                },
                {
                    'text_ru': 'Интерактивные задания',
                    'text_kg': 'Интерактивдүү тапшырмалар',
                    'text_en': 'Interactive assignments'
                },
                {
                    'text_ru': 'Форумы сообщества',
                    'text_kg': 'Коомчулук форумдары',
                    'text_en': 'Community forums'
                }
            ]
        },
        {
            'category': 'Медицинские ресурсы',
            'title_ru': 'UpToDate',
            'title_kg': 'UpToDate',
            'title_en': 'UpToDate',
            'description_ru': 'Клинический ресурс для принятия решений в области медицины',
            'description_kg': 'Медицина тармагында чечим кабыл алуу үчүн клиникалык ресурс',
            'description_en': 'Clinical decision support resource for medicine',
            'icon': '💊',
            'color': 'from-red-500 to-red-600',
            'url': 'https://www.uptodate.com',
            'users_count': 850,
            'status': 'online',
            'is_popular': True,
            'order': 1,
            'features': [
                {
                    'text_ru': 'Доказательная медицина',
                    'text_kg': 'Далилге негизделген медицина',
                    'text_en': 'Evidence-based medicine'
                },
                {
                    'text_ru': 'Клинические рекомендации',
                    'text_kg': 'Клиникалык сунуштар',
                    'text_en': 'Clinical recommendations'
                },
                {
                    'text_ru': 'Мобильное приложение',
                    'text_kg': 'Мобилдик тиркеме',
                    'text_en': 'Mobile application'
                }
            ]
        },
        {
            'category': 'Исследовательские инструменты',
            'title_ru': 'Mendeley Reference Manager',
            'title_kg': 'Mendeley шилтеме башкаргычы',
            'title_en': 'Mendeley Reference Manager',
            'description_ru': 'Инструмент для управления библиографическими ссылками и совместной работы',
            'description_kg': 'Библиографиялык шилтемелерди башкаруу жана биргелешип иштөө үчүн курал',
            'description_en': 'Tool for managing bibliographic references and collaboration',
            'icon': '📝',
            'color': 'from-orange-500 to-orange-600',
            'url': 'https://www.mendeley.com',
            'users_count': 950,
            'status': 'online',
            'is_popular': False,
            'order': 3,
            'features': [
                {
                    'text_ru': 'Автоматическое цитирование',
                    'text_kg': 'Автоматтык шилтеме',
                    'text_en': 'Automatic citation'
                },
                {
                    'text_ru': 'Облачная синхронизация',
                    'text_kg': 'Булут синхрондоштуруу',
                    'text_en': 'Cloud synchronization'
                },
                {
                    'text_ru': 'Совместная работа',
                    'text_kg': 'Биргелешип иштөө',
                    'text_en': 'Collaboration'
                }
            ]
        },
        {
            'category': 'Образовательные платформы',
            'title_ru': 'Khan Academy',
            'title_kg': 'Khan Academy',
            'title_en': 'Khan Academy',
            'description_ru': 'Бесплатные образовательные видео и упражнения по различным предметам',
            'description_kg': 'Ар түрдүү предметтер боюнча акысыз билим берүү видеолору жана көнүгүүлөр',
            'description_en': 'Free educational videos and exercises on various subjects',
            'icon': '🎬',
            'color': 'from-indigo-500 to-indigo-600',
            'url': 'https://www.khanacademy.org',
            'users_count': 1600,
            'status': 'online',
            'is_popular': False,
            'order': 4,
            'features': [
                {
                    'text_ru': 'Интерактивные упражнения',
                    'text_kg': 'Интерактивдүү көнүгүүлөр',
                    'text_en': 'Interactive exercises'
                },
                {
                    'text_ru': 'Персонализированное обучение',
                    'text_kg': 'Жекелештирилген окутуу',
                    'text_en': 'Personalized learning'
                },
                {
                    'text_ru': 'Отслеживание прогресса',
                    'text_kg': 'Өнүгүүнү көзөмөлдөө',
                    'text_en': 'Progress tracking'
                }
            ]
        }
    ]
    
    for res_data in resources_data:
        category = categories[res_data['category']]
        features_data = res_data.pop('features')
        
        resource, created = EResource.objects.get_or_create(
            title_ru=res_data['title_ru'],
            defaults={**res_data, 'category': category}
        )
        
        if created:
            print(f"✅ Создан ресурс: {res_data['title_ru']}")
            
            # Добавляем особенности
            for feature_data in features_data:
                EResourceFeature.objects.create(
                    resource=resource,
                    **feature_data
                )
            print(f"   📌 Добавлено {len(features_data)} особенностей")
        else:
            print(f"➡️ Ресурс уже существует: {res_data['title_ru']}")
    
    print("\n📊 Статистика:")
    print(f"   Категорий: {EResourceCategory.objects.count()}")
    print(f"   Ресурсов: {EResource.objects.count()}")
    print(f"   Особенностей: {EResourceFeature.objects.count()}")
    print("\n🎉 Тестовые данные EResources созданы успешно!")

if __name__ == '__main__':
    create_eresources_data()