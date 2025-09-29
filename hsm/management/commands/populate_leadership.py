from django.core.management.base import BaseCommand
from hsm.models import Leadership


class Command(BaseCommand):
    help = 'Populate leadership data with sample records in 3 languages'

    def handle(self, *args, **options):
        # Очищаем существующие данные
        Leadership.objects.all().delete()
        
        # Создаем данные для руководства
        leadership_data = [
            {
                'name': 'Иванов Иван Иванович',
                'name_kg': 'Иванов Иван Иванович',
                'name_en': 'Ivanov Ivan Ivanovich',
                'position': 'Директор',
                'position_kg': 'Директор',
                'position_en': 'Director',
                'degree': 'Доктор медицинских наук',
                'degree_kg': 'Медицина илимдеринин доктору',
                'degree_en': 'Doctor of Medical Sciences',
                'experience': '25 лет',
                'experience_kg': '25 жыл',
                'experience_en': '25 years',
                'email': 'director@meduniversity.ru',
                'phone': '+7 (495) 123-45-67',
                'bio': 'Выдающийся медик и организатор здравоохранения',
                'bio_kg': 'Көрүнүктүү медик жана саламаттык сактоо уюштуруучу',
                'bio_en': 'Outstanding physician and healthcare organizer',
                'achievements': [
                    'Заслуженный врач РФ',
                    'Автор более 200 научных работ',
                    'Лауреат государственной премии'
                ],
                'achievements_kg': [
                    'РФнын кадырлуу доктору',
                    '200дөн ашык илимий иштердин автору',
                    'Мамлекеттик сыйлыктын лауреаты'
                ],
                'achievements_en': [
                    'Honored Doctor of RF',
                    'Author of over 200 scientific works',
                    'State Prize Laureate'
                ],
                'department': 'directorate',
                'department_kg': 'Дирекция',
                'department_en': 'Directorate',
                'leadership_type': 'director',
                'is_director': True,
                'order': 1
            },
            {
                'name': 'Петрова Мария Александровна',
                'name_kg': 'Петрова Мария Александровна',
                'name_en': 'Petrova Maria Alexandrovna',
                'position': 'Заместитель директора по учебной работе',
                'position_kg': 'Окуу иши боюнча директордун орун басары',
                'position_en': 'Deputy Director for Academic Affairs',
                'degree': 'Кандидат медицинских наук',
                'degree_kg': 'Медицина илимдеринин кандидаты',
                'degree_en': 'Candidate of Medical Sciences',
                'experience': '20 лет',
                'experience_kg': '20 жыл',
                'experience_en': '20 years',
                'email': 'study@meduniversity.ru',
                'phone': '+7 (495) 123-45-68',
                'bio': 'Специалист в области медицинского образования',
                'bio_kg': 'Медициналык билим берүү тармагынын адиси',
                'bio_en': 'Specialist in medical education',
                'achievements': [
                    'Отличник народного просвещения',
                    'Разработчик учебных программ',
                    'Эксперт Минздрава'
                ],
                'achievements_kg': [
                    'Эл агартуусунун мыктысы',
                    'Окуу программаларын иштеп чыгуучу',
                    'Саламаттык сактоо министрлигинин эксперти'
                ],
                'achievements_en': [
                    'Excellence in Public Education',
                    'Curriculum Developer',
                    'Ministry of Health Expert'
                ],
                'department': 'study_department',
                'department_kg': 'Окуу бөлүмү',
                'department_en': 'Study Department',
                'leadership_type': 'deputy_director',
                'is_director': True,
                'order': 2
            },
            {
                'name': 'Сидоров Петр Николаевич',
                'name_kg': 'Сидоров Петр Николаевич',
                'name_en': 'Sidorov Petr Nikolaevich',
                'position': 'Заместитель директора по научной работе',
                'position_kg': 'Илимий иш боюнча директордун орун басары',
                'position_en': 'Deputy Director for Research',
                'degree': 'Доктор медицинских наук',
                'degree_kg': 'Медицина илимдеринин доктору',
                'degree_en': 'Doctor of Medical Sciences',
                'experience': '22 года',
                'experience_kg': '22 жыл',
                'experience_en': '22 years',
                'email': 'science@meduniversity.ru',
                'phone': '+7 (495) 123-45-69',
                'bio': 'Ведущий научный сотрудник в области медицинских исследований',
                'bio_kg': 'Медициналык изилдөөлөр тармагындагы жетекчи илимий кызматкер',
                'bio_en': 'Leading researcher in medical studies',
                'achievements': [
                    'Руководитель 15 научных проектов',
                    'Автор 150 публикаций',
                    'Лауреат премии РАН'
                ],
                'achievements_kg': [
                    '15 илимий долбоордун жетекчиси',
                    '150 басылманын автору',
                    'РИА сыйлыгынын лауреаты'
                ],
                'achievements_en': [
                    'Head of 15 research projects',
                    'Author of 150 publications',
                    'RAS Prize Laureate'
                ],
                'department': 'science_department',
                'department_kg': 'Илимий бөлүм',
                'department_en': 'Science Department',
                'leadership_type': 'deputy_director',
                'is_director': True,
                'order': 3
            },
            {
                'name': 'Козлова Елена Викторовна',
                'name_kg': 'Козлова Елена Викторовна',
                'name_en': 'Kozlova Elena Viktorovna',
                'position': 'Заведующая кафедрой терапии',
                'position_kg': 'Терапия кафедрасынын башчысы',
                'position_en': 'Head of Therapy Department',
                'degree': 'Доктор медицинских наук',
                'degree_kg': 'Медицина илимдеринин доктору',
                'degree_en': 'Doctor of Medical Sciences',
                'experience': '18 лет',
                'experience_kg': '18 жыл',
                'experience_en': '18 years',
                'email': 'therapy@meduniversity.ru',
                'phone': '+7 (495) 123-45-70',
                'bio': 'Специалист по внутренним болезням и терапии',
                'bio_kg': 'Ички ооруларга жана терапияга адис',
                'bio_en': 'Specialist in internal medicine and therapy',
                'achievements': [
                    'Лучший преподаватель года',
                    'Автор 80 научных работ',
                    'Главный терапевт региона'
                ],
                'achievements_kg': [
                    'Жылдын эң мыкты мугалими',
                    '80 илимий иштин автору',
                    'Аймактын башкы терапевти'
                ],
                'achievements_en': [
                    'Best Teacher of the Year',
                    'Author of 80 scientific works',
                    'Chief Therapist of the Region'
                ],
                'department': 'therapy',
                'department_kg': 'Терапия',
                'department_en': 'Therapy',
                'specialization': 'Кардиология, пульмонология, гастроэнтерология',
                'specialization_kg': 'Кардиология, пульмонология, гастроэнтерология',
                'specialization_en': 'Cardiology, pulmonology, gastroenterology',
                'staff_count': '25 преподавателей',
                'staff_count_kg': '25 мугалим',
                'staff_count_en': '25 teachers',
                'leadership_type': 'department_head',
                'is_director': False,
                'order': 4
            },
            {
                'name': 'Николаев Андрей Сергеевич',
                'name_kg': 'Николаев Андрей Сергеевич',
                'name_en': 'Nikolaev Andrey Sergeevich',
                'position': 'Заведующий кафедрой хирургии',
                'position_kg': 'Хирургия кафедрасынын башчысы',
                'position_en': 'Head of Surgery Department',
                'degree': 'Доктор медицинских наук',
                'degree_kg': 'Медицина илимдеринин доктору',
                'degree_en': 'Doctor of Medical Sciences',
                'experience': '25 лет',
                'experience_kg': '25 жыл',
                'experience_en': '25 years',
                'email': 'surgery@meduniversity.ru',
                'phone': '+7 (495) 123-45-71',
                'bio': 'Ведущий хирург и преподаватель хирургии',
                'bio_kg': 'Жетекчи хирург жана хирургия мугалими',
                'bio_en': 'Leading surgeon and surgery instructor',
                'achievements': [
                    'Заслуженный врач РФ',
                    'Автор новых методик операций',
                    'Провел более 5000 операций'
                ],
                'achievements_kg': [
                    'РФнын кадырлуу доктору',
                    'Жаңы операция методдорунун автору',
                    '5000дөн ашык операция жасаган'
                ],
                'achievements_en': [
                    'Honored Doctor of RF',
                    'Author of new surgical techniques',
                    'Performed over 5000 operations'
                ],
                'department': 'surgery',
                'department_kg': 'Хирургия',
                'department_en': 'Surgery',
                'specialization': 'Общая хирургия, абдоминальная хирургия, лапароскопия',
                'specialization_kg': 'Жалпы хирургия, курсак хирургиясы, лапароскопия',
                'specialization_en': 'General surgery, abdominal surgery, laparoscopy',
                'staff_count': '30 преподавателей',
                'staff_count_kg': '30 мугалим',
                'staff_count_en': '30 teachers',
                'leadership_type': 'department_head',
                'is_director': False,
                'order': 5
            },
            {
                'name': 'Орлова Татьяна Михайловна',
                'name_kg': 'Орлова Татьяна Михайловна',
                'name_en': 'Orlova Tatyana Mikhailovna',
                'position': 'Заведующая кафедрой педиатрии',
                'position_kg': 'Педиатрия кафедрасынын башчысы',
                'position_en': 'Head of Pediatrics Department',
                'degree': 'Доктор медицинских наук',
                'degree_kg': 'Медицина илимдеринин доктору',
                'degree_en': 'Doctor of Medical Sciences',
                'experience': '20 лет',
                'experience_kg': '20 жыл',
                'experience_en': '20 years',
                'email': 'pediatrics@meduniversity.ru',
                'phone': '+7 (495) 123-45-72',
                'bio': 'Специалист по детским болезням и педиатрии',
                'bio_kg': 'Балдар ооруларына жана педиатрияга адис',
                'bio_en': 'Specialist in pediatric diseases and pediatrics',
                'achievements': [
                    'Лауреат премии в области педиатрии',
                    'Автор учебника по педиатрии',
                    'Главный педиатр города'
                ],
                'achievements_kg': [
                    'Педиатрия тармагындагы сыйлыктын лауреаты',
                    'Педиатрия боюнча окуу китебинин автору',
                    'Шаардын башкы педиатры'
                ],
                'achievements_en': [
                    'Pediatrics Award Laureate',
                    'Author of pediatrics textbook',
                    'Chief Pediatrician of the City'
                ],
                'department': 'pediatrics',
                'department_kg': 'Педиатрия',
                'department_en': 'Pediatrics',
                'specialization': 'Неонатология, детская кардиология, инфекционные болезни детей',
                'specialization_kg': 'Неонатология, балдар кардиологиясы, балдардын жугуштуу оорулары',
                'specialization_en': 'Neonatology, pediatric cardiology, pediatric infectious diseases',
                'staff_count': '20 преподавателей',
                'staff_count_kg': '20 мугалим',
                'staff_count_en': '20 teachers',
                'leadership_type': 'department_head',
                'is_director': False,
                'order': 6
            },
            {
                'name': 'Васильев Олег Петрович',
                'name_kg': 'Васильев Олег Петрович',
                'name_en': 'Vasiliev Oleg Petrovich',
                'position': 'Заведующий кафедрой неврологии',
                'position_kg': 'Неврология кафедрасынын башчысы',
                'position_en': 'Head of Neurology Department',
                'degree': 'Доктор медицинских наук',
                'degree_kg': 'Медицина илимдеринин доктору',
                'degree_en': 'Doctor of Medical Sciences',
                'experience': '22 года',
                'experience_kg': '22 жыл',
                'experience_en': '22 years',
                'email': 'neurology@meduniversity.ru',
                'phone': '+7 (495) 123-45-73',
                'bio': 'Ведущий невролог и исследователь нервной системы',
                'bio_kg': 'Жетекчи невролог жана нерв тутумунун изилдөөчүсү',
                'bio_en': 'Leading neurologist and nervous system researcher',
                'achievements': [
                    'Пионер в нейрохирургии',
                    'Разработчик новых методов диагностики',
                    'Автор 120 научных работ'
                ],
                'achievements_kg': [
                    'Нейрохирургиядагы пионер',
                    'Жаңы диагностика методдорунун иштеп чыгуучусу',
                    '120 илимий иштин автору'
                ],
                'achievements_en': [
                    'Pioneer in neurosurgery',
                    'Developer of new diagnostic methods',
                    'Author of 120 scientific works'
                ],
                'department': 'neurology',
                'department_kg': 'Неврология',
                'department_en': 'Neurology',
                'specialization': 'Клиническая неврология, нейрофизиология, эпилептология',
                'specialization_kg': 'Клиникалык неврология, нейрофизиология, эпилептология',
                'specialization_en': 'Clinical neurology, neurophysiology, epileptology',
                'staff_count': '18 преподавателей',
                'staff_count_kg': '18 мугалим',
                'staff_count_en': '18 teachers',
                'leadership_type': 'department_head',
                'is_director': False,
                'order': 7
            },
            {
                'name': 'Смирнова Анна Владимировна',
                'name_kg': 'Смирнова Анна Владимировна',
                'name_en': 'Smirnova Anna Vladimirovna',
                'position': 'Заведующая кафедрой стоматологии',
                'position_kg': 'Стоматология кафедрасынын башчысы',
                'position_en': 'Head of Dentistry Department',
                'degree': 'Кандидат медицинских наук',
                'degree_kg': 'Медицина илимдеринин кандидаты',
                'degree_en': 'Candidate of Medical Sciences',
                'experience': '15 лет',
                'experience_kg': '15 жыл',
                'experience_en': '15 years',
                'email': 'dentistry@meduniversity.ru',
                'phone': '+7 (495) 123-45-74',
                'bio': 'Специалист по стоматологии и челюстно-лицевой хирургии',
                'bio_kg': 'Стоматология жана жаак-жүз хирургиясына адис',
                'bio_en': 'Specialist in dentistry and maxillofacial surgery',
                'achievements': [
                    'Лучший стоматолог региона',
                    'Внедрение новых технологий',
                    'Автор 45 научных статей'
                ],
                'achievements_kg': [
                    'Аймактын эң мыкты стоматологу',
                    'Жаңы технологияларды киргизүү',
                    '45 илимий макаланын автору'
                ],
                'achievements_en': [
                    'Best Dentist in the Region',
                    'Implementation of new technologies',
                    'Author of 45 scientific articles'
                ],
                'department': 'dentistry',
                'department_kg': 'Стоматология',
                'department_en': 'Dentistry',
                'specialization': 'Терапевтическая стоматология, ортопедия, имплантология',
                'specialization_kg': 'Дарылоочу стоматология, ортопедия, имплантология',
                'specialization_en': 'Therapeutic dentistry, orthopedics, implantology',
                'staff_count': '22 преподавателя',
                'staff_count_kg': '22 мугалим',
                'staff_count_en': '22 teachers',
                'leadership_type': 'department_head',
                'is_director': False,
                'order': 8
            }
        ]

        created_count = 0
        for data in leadership_data:
            leadership, created = Leadership.objects.get_or_create(
                name=data['name'],
                defaults=data
            )
            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {created_count} leadership records'
            )
        )