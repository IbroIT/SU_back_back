#!/usr/bin/env python
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from research.models import ResearchManagementPosition, ScientificCouncil, Commission

def create_management_data():
    """Создает тестовые данные для научного управления"""
    
    # Очищаем существующие данные
    ResearchManagementPosition.objects.all().delete()
    ScientificCouncil.objects.all().delete()
    Commission.objects.all().delete()
    
    # Создаем позиции в научном управлении
    leadership_positions = [
        {
            'title_ru': 'Проректор по науке и инновациям',
            'title_en': 'Vice-Rector for Science and Innovation',
            'title_kg': 'Илим жана инновация боюнча проректор',
            'full_name_ru': 'Салымбеков Акылбек Салымбекович',
            'full_name_en': 'Salymbekov Akylbek Salymbekovich',
            'full_name_kg': 'Салымбеков Акылбек Салымбекович',
            'position_type': 'leadership',
            'bio_ru': 'Доктор медицинских наук, профессор. Специалист в области кардиологии и внутренних болезней.',
            'bio_en': 'Doctor of Medical Sciences, Professor. Specialist in cardiology and internal medicine.',
            'bio_kg': 'Медицина илимдеринин доктору, профессор. Кардиология жана ички оорулар боюнча адис.',
            'education_ru': 'КМИ им. И.К. Ахунбаева (1985), аспирантура КГМА (1990)',
            'education_en': 'Kyrgyz Medical Institute named after I.K. Akhunbaev (1985), postgraduate study at KSMA (1990)',
            'education_kg': 'И.К. Ахунбаев атындагы КМИ (1985), КММА аспирантурасы (1990)',
            'scientific_interests_ru': 'Кардиология, артериальная гипертензия, профилактическая медицина',
            'scientific_interests_en': 'Cardiology, arterial hypertension, preventive medicine',
            'scientific_interests_kg': 'Кардиология, артериялык гипертензия, алдын алуу медицинасы',
            'contact_email': 'prorector.science@salymbekov.edu.kg',
            'contact_phone': '+996 312 123456',
            'office_location': 'Главный корпус, каб. 201',
            'order': 1
        },
        {
            'title_ru': 'Директор НИИ медицинских проблем',
            'title_en': 'Director of Research Institute of Medical Problems',
            'title_kg': 'Медициналык көйгөйлөр илимий изилдөө институтунун директору',
            'full_name_ru': 'Иванова Мария Петровна',
            'full_name_en': 'Ivanova Maria Petrovna',
            'full_name_kg': 'Иванова Мария Петровна',
            'position_type': 'institute',
            'bio_ru': 'Кандидат медицинских наук, доцент. Ведущий специалист по биохимии и молекулярной биологии.',
            'bio_en': 'Candidate of Medical Sciences, Associate Professor. Leading specialist in biochemistry and molecular biology.',
            'bio_kg': 'Медицина илимдеринин кандидаты, доцент. Биохимия жана молекулалык биология боюнча жетекчи адис.',
            'education_ru': 'МГУ им. М.В. Ломоносова (1998), кандидатская диссертация (2003)',
            'education_en': 'Lomonosov Moscow State University (1998), PhD thesis (2003)',
            'education_kg': 'М.В. Ломоносов атындагы МДУ (1998), кандидаттык диссертация (2003)',
            'scientific_interests_ru': 'Биохимия, молекулярная биология, генетика',
            'scientific_interests_en': 'Biochemistry, molecular biology, genetics',
            'scientific_interests_kg': 'Биохимия, молекулалык биология, генетика',
            'contact_email': 'ivanova@salymbekov.edu.kg',
            'contact_phone': '+996 312 123457',
            'office_location': 'НИИ корпус, каб. 301',
            'order': 2
        }
    ]
    
    # Центры и институты
    centers_institutes = [
        {
            'title_ru': 'Центр молекулярной медицины',
            'title_en': 'Center for Molecular Medicine',
            'title_kg': 'Молекулалык медицина борбору',
            'full_name_ru': 'Петров Сергей Александрович',
            'full_name_en': 'Petrov Sergey Aleksandrovich',
            'full_name_kg': 'Петров Сергей Александрович',
            'position_type': 'center',
            'bio_ru': 'Доктор биологических наук, профессор. Специалист по молекулярной биологии.',
            'bio_en': 'Doctor of Biological Sciences, Professor. Specialist in molecular biology.',
            'bio_kg': 'Биология илимдеринин доктору, профессор. Молекулалык биология боюнча адис.',
            'contact_email': 'petrov@salymbekov.edu.kg',
            'contact_phone': '+996 312 123458',
            'office_location': 'Лабораторный корпус, каб. 401',
            'order': 1
        },
        {
            'title_ru': 'Институт кардиологии и сердечно-сосудистой хирургии',
            'title_en': 'Institute of Cardiology and Cardiovascular Surgery',
            'title_kg': 'Кардиология жана жүрөк-кан тамыр хирургиясы институту',
            'full_name_ru': 'Козлов Николай Иванович',
            'full_name_en': 'Kozlov Nikolai Ivanovich',
            'full_name_kg': 'Козлов Николай Иванович',
            'position_type': 'institute',
            'bio_ru': 'Доктор медицинских наук, профессор, академик МАНКПО. Кардиохирург высшей категории.',
            'bio_en': 'Doctor of Medical Sciences, Professor, Academician of IASPE. Cardiac surgeon of the highest category.',
            'bio_kg': 'Медицина илимдеринин доктору, профессор, МАНКПО академиги. Жогорку категориядагы кардиохирург.',
            'contact_email': 'kozlov@salymbekov.edu.kg',
            'contact_phone': '+996 312 123459',
            'office_location': 'Кардиоцентр, каб. 501',
            'order': 2
        }
    ]
    
    # Создаем руководящие позиции
    leadership_objects = []
    for pos_data in leadership_positions:
        pos = ResearchManagementPosition.objects.create(**pos_data)
        leadership_objects.append(pos)
        print(f"✅ Создана позиция: {pos.title_ru} - {pos.full_name_ru}")
    
    # Создаем центры и институты
    for center_data in centers_institutes:
        center = ResearchManagementPosition.objects.create(**center_data)
        print(f"✅ Создан центр/институт: {center.title_ru} - {center.full_name_ru}")
    
    # Создаем научные советы
    councils_data = [
        {
            'name_ru': 'Ученый совет по медицине',
            'name_en': 'Academic Council for Medicine',
            'name_kg': 'Медицина боюнча илимий кеңеш',
            'description_ru': 'Высший научный орган университета по вопросам медицинского образования и науки',
            'description_en': 'The highest scientific body of the university on medical education and science issues',
            'description_kg': 'Университеттин медициналык билим берүү жана илим маселелери боюнча эң жогорку илимий органы',
            'chairman_ru': 'Салымбеков Акылбек Салымбекович',
            'chairman_en': 'Salymbekov Akylbek Salymbekovich',
            'chairman_kg': 'Салымбеков Акылбек Салымбекович',
            'secretary_ru': 'Исаева Гульмира Токтогуловна',
            'secretary_en': 'Isaeva Gulmira Toktogulovn',
            'secretary_kg': 'Исаева Гүлмира Токтогуловна',
            'members_ru': [
                'Иванов Иван Иванович - д.м.н., профессор',
                'Петрова Анна Сергеевна - к.м.н., доцент',
                'Сидоров Михаил Петрович - д.м.н., профессор'
            ],
            'members_en': [
                'Ivanov Ivan Ivanovich - Doctor of Medical Sciences, Professor',
                'Petrova Anna Sergeevna - Candidate of Medical Sciences, Associate Professor',
                'Sidorov Mikhail Petrovich - Doctor of Medical Sciences, Professor'
            ],
            'members_kg': [
                'Иванов Иван Иванович - м.и.д., профессор',
                'Петрова Анна Сергеевна - м.и.к., доцент',
                'Сидоров Михаил Петрович - м.и.д., профессор'
            ],
            'responsibilities_ru': 'Определение стратегии научного развития, экспертиза диссертационных работ, аттестация научных кадров',
            'responsibilities_en': 'Determining the strategy of scientific development, examination of dissertations, certification of scientific personnel',
            'responsibilities_kg': 'Илимий өнүктүрүү стратегиясын аныктоо, диссертациялык иштерди экспертиза кылуу, илимий кадрларды аттестациялоо',
            'meeting_schedule_ru': 'Каждый второй четверг месяца',
            'meeting_schedule_en': 'Every second Thursday of the month',
            'meeting_schedule_kg': 'Айдын ар экинчи бейшемби күнү',
            'contact_email': 'council@salymbekov.edu.kg',
            'contact_phone': '+996 312 123460'
        },
        {
            'name_ru': 'Диссертационный совет по специальности 14.01.05',
            'name_en': 'Dissertation Council for specialty 14.01.05',
            'name_kg': '14.01.05 адистиги боюнча диссертациялык кеңеш',
            'description_ru': 'Совет по защите диссертаций по кардиологии',
            'description_en': 'Council for defense of dissertations in cardiology',
            'description_kg': 'Кардиология боюнча диссертацияларды коргоо кеңеши',
            'chairman_ru': 'Козлов Николай Иванович',
            'chairman_en': 'Kozlov Nikolai Ivanovich',
            'chairman_kg': 'Козлов Николай Иванович',
            'secretary_ru': 'Федорова Елена Викторовна',
            'secretary_en': 'Fedorova Elena Viktorovna',
            'secretary_kg': 'Федорова Елена Викторовна',
            'members_ru': [
                'Алиев Бакыт Маматович - д.м.н., профессор',
                'Жусупова Айгуль Токтосуновна - д.м.н., профессор',
                'Мамбетов Уланбек Касымович - д.м.н., профессор'
            ],
            'members_en': [
                'Aliev Bakyt Mamatovich - Doctor of Medical Sciences, Professor',
                'Zhusupova Aigul Toksunovna - Doctor of Medical Sciences, Professor',
                'Mambetov Ulanbek Kasymovich - Doctor of Medical Sciences, Professor'
            ],
            'members_kg': [
                'Алиев Бакыт Маматович - м.и.д., профессор',
                'Жусупова Айгүл Токтосуновна - м.и.д., профессор',
                'Мамбетов Уланбек Касымович - м.и.д., профессор'
            ],
            'responsibilities_ru': 'Рассмотрение и утверждение диссертационных работ по кардиологии',
            'responsibilities_en': 'Review and approval of dissertation works in cardiology',
            'responsibilities_kg': 'Кардиология боюнча диссертациялык иштерди карап чыгуу жана бекитүү',
            'meeting_schedule_ru': 'По мере поступления диссертаций',
            'meeting_schedule_en': 'As dissertations are received',
            'meeting_schedule_kg': 'Диссертациялар келип түшкөн сайын',
            'contact_email': 'diss.council@salymbekov.edu.kg',
            'contact_phone': '+996 312 123461'
        }
    ]
    
    for council_data in councils_data:
        council = ScientificCouncil.objects.create(**council_data)
        print(f"✅ Создан научный совет: {council.name_ru}")
    
    # Создаем комиссии
    commissions_data = [
        {
            'name_ru': 'Этическая комиссия',
            'name_en': 'Ethics Committee',
            'name_kg': 'Этикалык комиссия',
            'commission_type': 'ethics',
            'description_ru': 'Комиссия по биомедицинской этике для проведения экспертизы научных исследований',
            'description_en': 'Biomedical ethics committee for scientific research expertise',
            'description_kg': 'Илимий изилдөөлөрдү экспертиза кылуу үчүн биомедициналык этика комиссиясы',
            'chairman_ru': 'Джапарова Динара Мукашевна',
            'chairman_en': 'Dzhaparova Dinara Mukashevna',
            'chairman_kg': 'Жапарова Динара Мукашевна',
            'members_ru': [
                'Токтогулов Нурлан Арстанбекович - юрист',
                'Мамытова Айнура Бакировна - д.м.н.',
                'Осмонова Жыпар Кылычбековна - к.ф.н.'
            ],
            'members_en': [
                'Toktogulov Nurlan Arstanbekovich - lawyer',
                'Mamytova Ainura Bakirovna - Doctor of Medical Sciences',
                'Osmonova Zhypar Kylychbekovna - Candidate of Philosophical Sciences'
            ],
            'members_kg': [
                'Токтогулов Нурлан Арстанбекович - юрист',
                'Мамытова Айнура Бакировна - м.и.д.',
                'Осмонова Жыпар Кыличбековна - ф.и.к.'
            ],
            'functions_ru': 'Этическая экспертиза медицинских исследований, контроль соблюдения прав пациентов',
            'functions_en': 'Ethical review of medical research, monitoring compliance with patient rights',
            'functions_kg': 'Медициналык изилдөөлөрдү этикалык экспертиза кылуу, бейтаптардын укуктарынын сакталышын көзөмөлдөө',
            'contact_email': 'ethics@salymbekov.edu.kg',
            'contact_phone': '+996 312 123462'
        },
        {
            'name_ru': 'Издательская комиссия',
            'name_en': 'Publishing Committee',
            'name_kg': 'Басма комиссиясы',
            'commission_type': 'publication',
            'description_ru': 'Комиссия по рецензированию и отбору научных публикаций',
            'description_en': 'Committee for reviewing and selecting scientific publications',
            'description_kg': 'Илимий басмаларды рецензиялоо жана тандоо комиссиясы',
            'chairman_ru': 'Иванова Мария Петровна',
            'chairman_en': 'Ivanova Maria Petrovna',
            'chairman_kg': 'Иванова Мария Петровна',
            'members_ru': [
                'Петров Сергей Александрович - д.б.н.',
                'Сидорова Ольга Николаевна - к.м.н.',
                'Алиев Бакыт Маматович - д.м.н.'
            ],
            'members_en': [
                'Petrov Sergey Aleksandrovich - Doctor of Biological Sciences',
                'Sidorova Olga Nikolaevna - Candidate of Medical Sciences',
                'Aliev Bakyt Mamatovich - Doctor of Medical Sciences'
            ],
            'members_kg': [
                'Петров Сергей Александрович - б.и.д.',
                'Сидорова Ольга Николаевна - м.и.к.',
                'Алиев Бакыт Маматович - м.и.д.'
            ],
            'functions_ru': 'Рецензирование научных статей, контроль качества публикаций',
            'functions_en': 'Reviewing scientific articles, quality control of publications',
            'functions_kg': 'Илимий макалаларды рецензиялоо, басмалардын сапатын көзөмөлдөө',
            'contact_email': 'publishing@salymbekov.edu.kg',
            'contact_phone': '+996 312 123463'
        },
        {
            'name_ru': 'Квалификационная комиссия',
            'name_en': 'Qualification Committee',
            'name_kg': 'Квалификация комиссиясы',
            'commission_type': 'qualification',
            'description_ru': 'Комиссия по аттестации научно-педагогических кадров',
            'description_en': 'Committee for certification of scientific and pedagogical personnel',
            'description_kg': 'Илимий-педагогикалык кадрларды аттестациялоо комиссиясы',
            'chairman_ru': 'Козлов Николай Иванович',
            'chairman_en': 'Kozlov Nikolai Ivanovich',
            'chairman_kg': 'Козлов Николай Иванович',
            'members_ru': [
                'Салымбеков Акылбек Салымбекович - д.м.н.',
                'Жусупова Айгуль Токтосуновна - д.м.н.',
                'Мамбетов Уланбек Касымович - д.м.н.'
            ],
            'members_en': [
                'Salymbekov Akylbek Salymbekovich - Doctor of Medical Sciences',
                'Zhusupova Aigul Toksunovna - Doctor of Medical Sciences',
                'Mambetov Ulanbek Kasymovich - Doctor of Medical Sciences'
            ],
            'members_kg': [
                'Салымбеков Акылбек Салымбекович - м.и.д.',
                'Жусупова Айгүл Токтосуновна - м.и.д.',
                'Мамбетов Уланбек Касымович - м.и.д.'
            ],
            'functions_ru': 'Присвоение ученых званий, аттестация преподавателей',
            'functions_en': 'Assignment of academic titles, certification of teachers',
            'functions_kg': 'Илимий наамдарды ыйгаруу, мугалимдерди аттестациялоо',
            'contact_email': 'qualification@salymbekov.edu.kg',
            'contact_phone': '+996 312 123464'
        }
    ]
    
    for commission_data in commissions_data:
        commission = Commission.objects.create(**commission_data)
        print(f"✅ Создана комиссия: {commission.name_ru}")
    
    print(f"\n🎉 Успешно создано:")
    print(f"   📋 {len(leadership_positions) + len(centers_institutes)} позиций управления")
    print(f"   🏛️ {len(councils_data)} научных советов")
    print(f"   👥 {len(commissions_data)} комиссий")


if __name__ == '__main__':
    create_management_data()
