from django.core.management.base import BaseCommand
from hsm.models import Leadership


class Command(BaseCommand):
    help = 'Загружает начальные данные для руководства ВШМ'
    
    def handle(self, *args, **options):
        # Очищаем существующие данные
        Leadership.objects.all().delete()
        
        # Данные руководства на трех языках
        leadership_data = [
            # Директора
            {
                'name': 'Иванов Алексей Петрович',
                'name_kg': 'Иванов Алексей Петрович',
                'name_en': 'Aleksey Petrovich Ivanov',
                'position': 'Директор Высшей школы медицины',
                'position_kg': 'Жогорку медицина мектебинин директору',
                'position_en': 'Director of the Higher School of Medicine',
                'degree': 'Доктор медицинских наук, профессор',
                'degree_kg': 'Медицина илимдеринин доктору, профессор',
                'degree_en': 'Doctor of Medical Sciences, Professor',
                'experience': '25 лет',
                'experience_kg': '25 жыл',
                'experience_en': '25 years',
                'bio': 'Ведущий специалист в области кардиохирургии с многолетним опытом руководящей работы.',
                'bio_kg': 'Жүрөк хирургиясы тармагындагы жетекчи адис, көп жылдык жетекчилик тажрыйбасы бар.',
                'bio_en': 'Leading specialist in cardiac surgery with many years of management experience.',
                'achievements': [
                    'Автор более 100 научных публикаций',
                    'Основатель современной кардиохирургии в регионе',
                    'Лауреат государственной премии в области медицины'
                ],
                'achievements_kg': [
                    '100дөн ашык илимий басылманын автору',
                    'Аймактагы заманбап жүрөк хирургиясынын негиздөөчүсү',
                    'Медицина тармагындагы мамлекеттик сыйлыктын лауреаты'
                ],
                'achievements_en': [
                    'Author of more than 100 scientific publications',
                    'Founder of modern cardiac surgery in the region',
                    'State Prize winner in medicine'
                ],
                'department': 'directorate',
                'department_kg': 'Дирекция',
                'department_en': 'Directorate',
                'email': 'director@meduniversity.ru',
                'phone': '+7 (495) 123-45-67',
                'leadership_type': 'director',
                'is_director': True,
                'order': 1
            },
            {
                'name': 'Петрова Мария Васильевна',
                'name_kg': 'Петрова Мария Васильевна',
                'name_en': 'Maria Vasilievna Petrova',
                'position': 'Заместитель директора по учебной работе',
                'position_kg': 'Директордун окуу иши боюнча орун басары',
                'position_en': 'Deputy Director for Academic Affairs',
                'degree': 'Доктор медицинских наук, доцент',
                'degree_kg': 'Медицина илимдеринин доктору, доцент',
                'degree_en': 'Doctor of Medical Sciences, Associate Professor',
                'experience': '18 лет',
                'experience_kg': '18 жыл',
                'experience_en': '18 years',
                'bio': 'Специалист по медицинскому образованию и инновационным методам обучения.',
                'bio_kg': 'Медициналык билим берүү жана инновациялык окутуу методдору боюнча адис.',
                'bio_en': 'Specialist in medical education and innovative teaching methods.',
                'achievements': [
                    'Разработчик новых учебных программ',
                    'Эксперт в области медицинского образования',
                    'Автор 80+ научных работ'
                ],
                'achievements_kg': [
                    'Жаңы окуу программаларынын иштеп чыгуучусу',
                    'Медициналык билим берүү тармагындагы эксперт',
                    '80дан ашык илимий эмгектин автору'
                ],
                'achievements_en': [
                    'Developer of new curricula',
                    'Expert in medical education',
                    'Author of 80+ scientific works'
                ],
                'department': 'study_department',
                'department_kg': 'Окуу бөлүмү',
                'department_en': 'Study Department',
                'email': 'study@meduniversity.ru',
                'phone': '+7 (495) 123-45-68',
                'leadership_type': 'deputy_director',
                'is_director': True,
                'order': 2
            },
            {
                'name': 'Сидоров Владимир Николаевич',
                'name_kg': 'Сидоров Владимир Николаевич',
                'name_en': 'Vladimir Nikolaevich Sidorov',
                'position': 'Заместитель директора по научной работе',
                'position_kg': 'Директордун илимий иш боюнча орун басары',
                'position_en': 'Deputy Director for Research',
                'degree': 'Доктор медицинских наук, профессор',
                'degree_kg': 'Медицина илимдеринин доктору, профессор',
                'degree_en': 'Doctor of Medical Sciences, Professor',
                'experience': '22 года',
                'experience_kg': '22 жыл',
                'experience_en': '22 years',
                'bio': 'Ведущий исследователь в области молекулярной медицины и биотехнологий.',
                'bio_kg': 'Молекулярдык медицина жана биотехнология тармагындагы жетекчи изилдөөчү.',
                'bio_en': 'Leading researcher in molecular medicine and biotechnology.',
                'achievements': [
                    'Руководитель 15+ международных проектов',
                    'Обладатель международных научных грантов',
                    'Автор 120+ публикаций'
                ],
                'achievements_kg': [
                    '15тен ашык эл аралык долбоордун жетекчиси',
                    'Эл аралык илимий гранттардын ээси',
                    '120дан ашык басылманын автору'
                ],
                'achievements_en': [
                    'Head of 15+ international projects',
                    'Holder of international research grants',
                    'Author of 120+ publications'
                ],
                'department': 'science_department',
                'department_kg': 'Илимий бөлүм',
                'department_en': 'Science Department',
                'email': 'science@meduniversity.ru',
                'phone': '+7 (495) 123-45-69',
                'leadership_type': 'deputy_director',
                'is_director': True,
                'order': 3
            },
            
            # Заведующие кафедрами
            {
                'name': 'Козлова Елена Сергеевна',
                'name_kg': 'Козлова Елена Сергеевна',
                'name_en': 'Elena Sergeevna Kozlova',
                'position': 'Заведующая кафедрой терапии',
                'position_kg': 'Терапия кафедрасынын башчысы',
                'position_en': 'Head of Internal Medicine Department',
                'degree': 'Кандидат медицинских наук, доцент',
                'degree_kg': 'Медицина илимдеринин кандидаты, доцент',
                'degree_en': 'Candidate of Medical Sciences, Associate Professor',
                'experience': '15 лет',
                'experience_kg': '15 жыл',
                'experience_en': '15 years',
                'bio': 'Опытный терапевт с глубокими знаниями внутренних болезней.',
                'bio_kg': 'Ички оорулар боюнча терең билими бар тажрыйбалуу терапевт.',
                'bio_en': 'Experienced therapist with deep knowledge of internal diseases.',
                'achievements': [
                    'Ведущий специалист по кардиологии',
                    'Автор методических пособий',
                    'Наставник молодых врачей'
                ],
                'achievements_kg': [
                    'Кардиология боюнча жетекчи адис',
                    'Методикалык колдонмолордун автору',
                    'Жаш дарыгерлердин устазы'
                ],
                'achievements_en': [
                    'Leading specialist in cardiology',
                    'Author of methodological manuals',
                    'Mentor for young doctors'
                ],
                'department': 'therapy',
                'department_kg': 'Терапия кафедрасы',
                'department_en': 'Department of Therapy',
                'specialization': 'Внутренние болезни, кардиология, гастроэнтерология',
                'specialization_kg': 'Ички оорулар, кардиология, гастроэнтерология',
                'specialization_en': 'Internal medicine, cardiology, gastroenterology',
                'staff_count': '25 сотрудников',
                'staff_count_kg': '25 кызматкер',
                'staff_count_en': '25 employees',
                'email': 'therapy@meduniversity.ru',
                'phone': '+7 (495) 123-45-70',
                'leadership_type': 'department_head',
                'is_director': False,
                'order': 4
            },
            {
                'name': 'Николаев Дмитрий Александрович',
                'name_kg': 'Николаев Дмитрий Александрович',
                'name_en': 'Dmitry Aleksandrovich Nikolaev',
                'position': 'Заведующий кафедрой хирургии',
                'position_kg': 'Хирургия кафедрасынын башчысы',
                'position_en': 'Head of Surgery Department',
                'degree': 'Доктор медицинских наук, профессор',
                'degree_kg': 'Медицина илимдеринин доктору, профессор',
                'degree_en': 'Doctor of Medical Sciences, Professor',
                'experience': '20 лет',
                'experience_kg': '20 жыл',
                'experience_en': '20 years',
                'bio': 'Высококвалифицированный хирург с международным опытом.',
                'bio_kg': 'Эл аралык тажрыйбасы бар жогорку квалификациялуу хирург.',
                'bio_en': 'Highly qualified surgeon with international experience.',
                'achievements': [
                    'Пионер лапароскопической хирургии',
                    'Более 3000 операций',
                    'Международные стажировки'
                ],
                'achievements_kg': [
                    'Лапароскопиялык хирургиянын пионери',
                    '3000дөн ашык операция',
                    'Эл аралык стажировкалар'
                ],
                'achievements_en': [
                    'Pioneer of laparoscopic surgery',
                    'More than 3000 operations',
                    'International internships'
                ],
                'department': 'surgery',
                'department_kg': 'Хирургия кафедрасы',
                'department_en': 'Department of Surgery',
                'specialization': 'Общая хирургия, лапароскопия, онкохирургия',
                'specialization_kg': 'Жалпы хирургия, лапароскопия, онкохирургия',
                'specialization_en': 'General surgery, laparoscopy, oncosurgery',
                'staff_count': '30 сотрудников',
                'staff_count_kg': '30 кызматкер',
                'staff_count_en': '30 employees',
                'email': 'surgery@meduniversity.ru',
                'phone': '+7 (495) 123-45-71',
                'leadership_type': 'department_head',
                'is_director': False,
                'order': 5
            },
            {
                'name': 'Орлова Анна Михайловна',
                'name_kg': 'Орлова Анна Михайловна',
                'name_en': 'Anna Mikhailovna Orlova',
                'position': 'Заведующая кафедрой педиатрии',
                'position_kg': 'Педиатрия кафедрасынын башчысы',
                'position_en': 'Head of Pediatrics Department',
                'degree': 'Кандидат медицинских наук, доцент',
                'degree_kg': 'Медицина илимдеринин кандидаты, доцент',
                'degree_en': 'Candidate of Medical Sciences, Associate Professor',
                'experience': '12 лет',
                'experience_kg': '12 жыл',
                'experience_en': '12 years',
                'bio': 'Специалист по детской медицине и неонатологии.',
                'bio_kg': 'Балдар медицинасы жана неонатология боюнча адис.',
                'bio_en': 'Specialist in pediatric medicine and neonatology.',
                'achievements': [
                    'Эксперт по детской кардиологии',
                    'Разработчик программ детской реабилитации',
                    'Автор детских медицинских протоколов'
                ],
                'achievements_kg': [
                    'Балдар кардиологиясы боюнча эксперт',
                    'Балдарды калыбына келтирүү программаларынын иштеп чыгуучусу',
                    'Балдар медициналык протоколдорунун автору'
                ],
                'achievements_en': [
                    'Expert in pediatric cardiology',
                    'Developer of pediatric rehabilitation programs',
                    'Author of pediatric medical protocols'
                ],
                'department': 'pediatrics',
                'department_kg': 'Педиатрия кафедрасы',
                'department_en': 'Department of Pediatrics',
                'specialization': 'Педиатрия, неонатология, детская кардиология',
                'specialization_kg': 'Педиатрия, неонатология, балдар кардиологиясы',
                'specialization_en': 'Pediatrics, neonatology, pediatric cardiology',
                'staff_count': '18 сотрудников',
                'staff_count_kg': '18 кызматкер',
                'staff_count_en': '18 employees',
                'email': 'pediatrics@meduniversity.ru',
                'phone': '+7 (495) 123-45-72',
                'leadership_type': 'department_head',
                'is_director': False,
                'order': 6
            },
            {
                'name': 'Васильев Игорь Владимирович',
                'name_kg': 'Васильев Игорь Владимирович',
                'name_en': 'Igor Vladimirovich Vasiliev',
                'position': 'Заведующий кафедрой неврологии',
                'position_kg': 'Неврология кафедрасынын башчысы',
                'position_en': 'Head of Neurology Department',
                'degree': 'Доктор медицинских наук, профессор',
                'degree_kg': 'Медицина илимдеринин доктору, профессор',
                'degree_en': 'Doctor of Medical Sciences, Professor',
                'experience': '17 лет',
                'experience_kg': '17 жыл',
                'experience_en': '17 years',
                'bio': 'Ведущий невролог с экспертизой в нейрохирургии.',
                'bio_kg': 'Нейрохирургия тармагында эксперттик билими бар жетекчи невролог.',
                'bio_en': 'Leading neurologist with expertise in neurosurgery.',
                'achievements': [
                    'Специалист по заболеваниям ЦНС',
                    'Разработчик методов нейровосстановления',
                    'Международные сертификаты'
                ],
                'achievements_kg': [
                    'БНС оорулары боюнча адис',
                    'Нейро калыбына келтирүү методдорунун иштеп чыгуучусу',
                    'Эл аралык сертификаттар'
                ],
                'achievements_en': [
                    'Specialist in CNS diseases',
                    'Developer of neurorehabilitation methods',
                    'International certificates'
                ],
                'department': 'neurology',
                'department_kg': 'Неврология кафедрасы',
                'department_en': 'Department of Neurology',
                'specialization': 'Неврология, нейрохирургия, нейрореабилитация',
                'specialization_kg': 'Неврология, нейрохирургия, нейрореабилитация',
                'specialization_en': 'Neurology, neurosurgery, neurorehabilitation',
                'staff_count': '22 сотрудника',
                'staff_count_kg': '22 кызматкер',
                'staff_count_en': '22 employees',
                'email': 'neurology@meduniversity.ru',
                'phone': '+7 (495) 123-45-73',
                'leadership_type': 'department_head',
                'is_director': False,
                'order': 7
            },
            {
                'name': 'Смирнова Ольга Петровна',
                'name_kg': 'Смирнова Ольга Петровна',
                'name_en': 'Olga Petrovna Smirnova',
                'position': 'Заведующая кафедрой стоматологии',
                'position_kg': 'Стоматология кафедрасынын башчысы',
                'position_en': 'Head of Dentistry Department',
                'degree': 'Кандидат медицинских наук, доцент',
                'degree_kg': 'Медицина илимдеринин кандидаты, доцент',
                'degree_en': 'Candidate of Medical Sciences, Associate Professor',
                'experience': '14 лет',
                'experience_kg': '14 жыл',
                'experience_en': '14 years',
                'bio': 'Опытный стоматолог с экспертизой в ортопедии и имплантологии.',
                'bio_kg': 'Ортопедия жана имплантология тармагында эксперттик билими бар тажрыйбалуу стоматолог.',
                'bio_en': 'Experienced dentist with expertise in orthopedics and implantology.',
                'achievements': [
                    'Сертифицированный имплантолог',
                    'Автор инновационных методик лечения',
                    'Международные награды'
                ],
                'achievements_kg': [
                    'Сертификаттуу имплантолог',
                    'Дарылоонун инновациялык методдорунун автору',
                    'Эл аралык сыйлыктар'
                ],
                'achievements_en': [
                    'Certified implantologist',
                    'Author of innovative treatment methods',
                    'International awards'
                ],
                'department': 'dentistry',
                'department_kg': 'Стоматология кафедрасы',
                'department_en': 'Department of Dentistry',
                'specialization': 'Стоматология, ортопедия, имплантология',
                'specialization_kg': 'Стоматология, ортопедия, имплантология',
                'specialization_en': 'Dentistry, orthopedics, implantology',
                'staff_count': '20 сотрудников',
                'staff_count_kg': '20 кызматкер',
                'staff_count_en': '20 employees',
                'email': 'dentistry@meduniversity.ru',
                'phone': '+7 (495) 123-45-74',
                'leadership_type': 'department_head',
                'is_director': False,
                'order': 8
            }
        ]
        
        # Создаем записи
        for data in leadership_data:
            Leadership.objects.create(**data)
            
        self.stdout.write(
            self.style.SUCCESS(
                f'Успешно загружено {len(leadership_data)} записей руководства'
            )
        )