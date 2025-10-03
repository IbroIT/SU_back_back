#!/usr/bin/env python3
"""
Скрипт для добавления тестовых данных о научных советах
"""
import os
import sys
import django

# Добавляем путь к проекту
sys.path.append('/home/adilhan/medicine/SU_back')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')

# Настраиваем Django
django.setup()

from research.models import ScientificCouncil

def create_councils_data():
    """Создает тестовые данные для научных советов"""
    
    # Проверяем, есть ли уже данные
    if ScientificCouncil.objects.count() > 0:
        print("Данные уже существуют. Очищаем старые данные...")
        ScientificCouncil.objects.all().delete()
    
    councils_data = [
        {
            'name_ru': 'Ученый совет Высшей медицинской школы',
            'name_en': 'Academic Council of Higher Medical School',
            'name_kg': 'Жогорку медициналык мектептин илимий кеңеши',
            
            'description_ru': 'Коллегиальный орган управления Высшей медицинской школы, решающий основные вопросы образовательной, научной и воспитательной деятельности.',
            'description_en': 'Collegial governing body of the Higher Medical School, deciding on the main issues of educational, scientific and educational activities.',
            'description_kg': 'Жогорку медициналык мектептин колл��гиалдык башкаруу органы, билим берүү, илимий жана тарбиялык ишмердүүлүктүн негизги маселелерин чечет.',
            
            'chairman_ru': 'Иванов Иван Иванович',
            'chairman_en': 'Ivanov Ivan Ivanovich',
            'chairman_kg': 'Иванов Иван Иванович',
            
            'secretary_ru': 'Петрова Мария Сергеевна',
            'secretary_en': 'Petrova Maria Sergeevna',
            'secretary_kg': 'Петрова Мария Сергеевна',
            
            'members_ru': [
                'Сидоров Петр Александрович - Заведующий кафедрой хирургии',
                'Козлова Анна Дмитриевна - Профессор кафедры терапии',
                'Мамытов Талант Маратович - Декан факультета',
                'Асанова Айгуль Токтосуновна - Заведующий кафедрой педиатрии'
            ],
            'members_en': [
                'Sidorov Petr Alexandrovich - Head of Surgery Department',
                'Kozlova Anna Dmitrievna - Professor of Therapy Department',
                'Mamytov Talant Maratovich - Dean of Faculty',
                'Asanova Aigul Toktosunovna - Head of Pediatrics Department'
            ],
            'members_kg': [
                'Сидоров Петр Александрович - Хирургия кафедрасынын башчысы',
                'Козлова Анна Дмитриевна - Терапия кафедрасынын профессору',
                'Мамытов Талант Маратович - Факультеттин деканы',
                'Асанова Айгуль Токтосуновна - Педиатрия кафедрасынын башчысы'
            ],
            
            'responsibilities_ru': 'Решение вопросов образовательной и научной деятельности, утверждение учебных планов, рассмотрение кандидатур для присуждения ученых степеней.',
            'responsibilities_en': 'Resolving issues of educational and scientific activities, approving curricula, considering candidates for awarding academic degrees.',
            'responsibilities_kg': 'Билим берүү жана илимий ишмердүүлүк маселелерин чечүү, окуу пландарын бекитүү, илимий даражаларды берүү үчүн талапкерлерди көрүү.',
            
            'meeting_schedule_ru': 'Каждый месяц, последняя пятница',
            'meeting_schedule_en': 'Every month, last Friday',
            'meeting_schedule_kg': 'Ар айда, акыркы жума',
            
            'contact_email': 'council@su.edu.kg',
            'contact_phone': '+996 312 123456'
        },
        {
            'name_ru': 'Этическая комиссия',
            'name_en': 'Ethics Committee',
            'name_kg': 'Этикалык комиссия',
            
            'description_ru': 'Комиссия по этике медицинских исследований и клинической практики, обеспечивающая соблюдение этических норм.',
            'description_en': 'Commission on ethics of medical research and clinical practice, ensuring compliance with ethical standards.',
            'description_kg': 'Медициналык изилдөөлөр жана клиникалык практиканын этикасы боюнча комиссия, этикалык нормалардын сакталышын камсыздайт.',
            
            'chairman_ru': 'Асанова Айгуль Токтосуновна',
            'chairman_en': 'Asanova Aigul Toktosunovna',
            'chairman_kg': 'Асанова Айгуль Токтосуновна',
            
            'secretary_ru': 'Садыков Марат Бакытович',
            'secretary_en': 'Sadykov Marat Bakytovich', 
            'secretary_kg': 'Садыков Марат Бакытович',
            
            'members_ru': [
                'Жумабекова Нургуль Асановна - Специалист по биоэтике',
                'Турганбаев Азамат Жолдошович - Юрист',
                'Исакова Гульмира Рыскуловна - Представитель пациентов'
            ],
            'members_en': [
                'Zhumabekova Nurgul Asanovna - Bioethics Specialist',
                'Turganbaev Azamat Zholdoshovich - Lawyer',
                'Isakova Gulmira Ryskulovna - Patient Representative'
            ],
            'members_kg': [
                'Жумабекова Нургуль Асановна - Биоэтика адиси',
                'Турганбаев Азамат Жолдошович - Юрист',
                'Исакова Гульмира Рыскуловна - Бейтаптардын өкүлү'
            ],
            
            'responsibilities_ru': 'Контроль этических аспектов медицинских исследований, рассмотрение протоколов исследований.',
            'responsibilities_en': 'Control of ethical aspects of medical research, review of research protocols.',
            'responsibilities_kg': 'Медициналык изилдөөлөрдүн этикалык аспектилерин көзөмөлдөө, изилдөө протоколдорун кароо.',
            
            'meeting_schedule_ru': 'По мере необходимости',
            'meeting_schedule_en': 'As needed',
            'meeting_schedule_kg': 'Керектөөгө жараша',
            
            'contact_email': 'ethics@su.edu.kg',
            'contact_phone': '+996 312 123457'
        },
        {
            'name_ru': 'Диссертационный совет',
            'name_en': 'Dissertation Council',
            'name_kg': 'Диссертациялык кеңеш',
            
            'description_ru': 'Совет по защите диссертаций на соискание ученых степеней кандидата и доктора медицинских наук.',
            'description_en': 'Council for the defense of dissertations for the degree of candidate and doctor of medical sciences.',
            'description_kg': 'Медицина илимдеринин кандидаты жана доктору илимий даражаларын алуу үчүн диссертацияларды коргоо кеңеши.',
            
            'chairman_ru': 'Мамытов Талант Маратович',
            'chairman_en': 'Mamytov Talant Maratovich',
            'chairman_kg': 'Мамытов Талант Маратович',
            
            'secretary_ru': 'Бекбосунова Мэлис Субанкуловна',
            'secretary_en': 'Bekbosunova Melis Subankulovna',
            'secretary_kg': 'Бекбосунова Мэлис Субанкуловна',
            
            'members_ru': [
                'Токтомышева Назгуль Рыскуловна - Доктор медицинских наук',
                'Абдиев Акылбек Маматович - Профессор',
                'Кудайбергенова Индира Олжобаевна - Доктор наук',
                'Исмаилов Тилек Токтогулович - Академик'
            ],
            'members_en': [
                'Toktomysheva Nazgul Ryskulovna - Doctor of Medical Sciences',
                'Abdiev Akylbek Mamatovich - Professor',
                'Kudaibergenova Indira Olzhobaevna - Doctor of Sciences',
                'Ismailov Tilek Toktogulovich - Academician'
            ],
            'members_kg': [
                'Токтомышева Назгуль Рыскуловна - Медицина илимдеринин доктору',
                'Абдиев Акылбек Маматович - Профессор',
                'Кудайбергенова Индира Олжобаевна - Илимдардын доктору',
                'Исмаилов Тилек Токтогулович - Академик'
            ],
            
            'responsibilities_ru': 'Проведение защит диссертационных работ, экспертиза научных исследований.',
            'responsibilities_en': 'Conducting dissertation defenses, expertise of scientific research.',
            'responsibilities_kg': 'Диссертациялык иштерди коргоону өткөрүү, илимий изилдөөлөргө экспертиза жүргүзүү.',
            
            'meeting_schedule_ru': 'Ежемесячно',
            'meeting_schedule_en': 'Monthly',
            'meeting_schedule_kg': 'Ай сайын',
            
            'contact_email': 'dissertation@su.edu.kg',
            'contact_phone': '+996 312 123458'
        }
    ]
    
    # Создаем записи
    created_count = 0
    for council_data in councils_data:
        council = ScientificCouncil.objects.create(**council_data)
        print(f"Создан совет: {council.name_ru}")
        created_count += 1
    
    print(f"\nВсего создано советов: {created_count}")
    print(f"Общее количество советов в базе: {ScientificCouncil.objects.count()}")

if __name__ == '__main__':
    create_councils_data()