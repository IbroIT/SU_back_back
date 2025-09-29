from django.core.management.base import BaseCommand
from hsm.models import Leadership


class Command(BaseCommand):
    help = 'Обновить данные руководства с текстовыми значениями департаментов'

    def handle(self, *args, **options):
        # Удаляем старые данные
        Leadership.objects.all().delete()
        
        leadership_data = [
            {
                'name': 'Иванов Алексей Михайлович',
                'name_kg': 'Иванов Алексей Михайлович',
                'name_en': 'Ivanov Alexey Mikhailovich',
                'position': 'Директор ВШМ',
                'position_kg': 'ЖММ директору',
                'position_en': 'Director of HSM',
                'degree': 'Доктор медицинских наук',
                'degree_kg': 'Медицина илимдеринин доктору',
                'degree_en': 'Doctor of Medical Sciences',
                'experience': '15 лет',
                'experience_kg': '15 жыл',
                'experience_en': '15 years',
                'bio': 'Опытный руководитель с богатым опытом в области медицинского образования.',
                'bio_kg': 'Медициналык билим берүү тармагында байка тажрыйбасы бар тажрыйбалуу жетекчи.',
                'bio_en': 'Experienced leader with extensive experience in medical education.',
                'achievements': [
                    'Кандидат медицинских наук с 2008 года',
                    'Более 50 публикаций в международных журналах',
                    'Руководитель 10+ исследовательских проектов'
                ],
                'achievements_kg': [
                    '2008-жылдан бери медицина илимдеринин кандидаты',
                    'Эл аралык журналдарда 50дөн ашык басылма',
                    '10+ изилдөө долбоорлорунун жетекчиси'
                ],
                'achievements_en': [
                    'PhD in Medical Sciences since 2008',
                    'More than 50 publications in international journals',
                    'Head of 10+ research projects'
                ],
                'department': 'Дирекция',
                'department_kg': 'Дирекция',
                'department_en': 'Directorate',
                'email': 'director@meduniversity.ru',
                'phone': '+7 (495) 123-45-67',
                'leadership_type': 'director',
                'is_director': True,
                'order': 1
            },
            {
                'name': 'Петрова Екатерина Владимировна',
                'name_kg': 'Петрова Екатерина Владимировна',
                'name_en': 'Petrova Ekaterina Vladimirovna',
                'position': 'Заместитель директора по учебной работе',
                'position_kg': 'Окуу иши боюнча директордун орун басары',
                'position_en': 'Deputy Director for Academic Affairs',
                'degree': 'Кандидат педагогических наук',
                'degree_kg': 'Педагогика илимдеринин кандидаты',
                'degree_en': 'PhD in Educational Sciences',
                'experience': '12 лет',
                'experience_kg': '12 жыл',
                'experience_en': '12 years',
                'bio': 'Специалист в области медицинского образования и методологии обучения.',
                'bio_kg': 'Медициналык билим берүү жана окутуу методологиясы тармагынын адиси.',
                'bio_en': 'Specialist in medical education and teaching methodology.',
                'achievements': [
                    'Разработка новых учебных программ',
                    'Внедрение современных методов обучения',
                    'Международная аккредитация программ'
                ],
                'achievements_kg': [
                    'Жаңы окуу программаларын иштеп чыгуу',
                    'Замандаш окутуу методдорун киргизүү',
                    'Программалардын эл аралык аккредитациясы'
                ],
                'achievements_en': [
                    'Development of new curricula',
                    'Implementation of modern teaching methods',
                    'International accreditation of programs'
                ],
                'department': 'Учебный отдел',
                'department_kg': 'Окуу бөлүмү',
                'department_en': 'Academic Department',
                'email': 'study@meduniversity.ru',
                'phone': '+7 (495) 123-45-68',
                'leadership_type': 'deputy_director',
                'is_director': True,
                'order': 2
            },
            {
                'name': 'Сидоров Владимир Петрович',
                'name_kg': 'Сидоров Владимир Петрович',
                'name_en': 'Sidorov Vladimir Petrovich',
                'position': 'Заместитель директора по научной работе',
                'position_kg': 'Илимий иш боюнча директордун орун басары',
                'position_en': 'Deputy Director for Research',
                'degree': 'Доктор медицинских наук',
                'degree_kg': 'Медицина илимдеринин доктору',
                'degree_en': 'Doctor of Medical Sciences',
                'experience': '18 лет',
                'experience_kg': '18 жыл',
                'experience_en': '18 years',
                'bio': 'Ведущий исследователь в области кардиологии и внутренних болезней.',
                'bio_kg': 'Кардиология жана ички оорулар тармагындагы алдыңкы изилдөөчү.',
                'bio_en': 'Leading researcher in cardiology and internal medicine.',
                'achievements': [
                    'Более 100 научных публикаций',
                    'Руководство крупными исследованиями',
                    'Международное сотрудничество'
                ],
                'achievements_kg': [
                    '100дөн ашык илимий басылма',
                    'Ири изилдөөлөрдү жетектөө',
                    'Эл аралык кызматташуу'
                ],
                'achievements_en': [
                    'More than 100 scientific publications',
                    'Leading major research projects',
                    'International collaboration'
                ],
                'department': 'Научный отдел',
                'department_kg': 'Илимий бөлүм',
                'department_en': 'Research Department',
                'email': 'science@meduniversity.ru',
                'phone': '+7 (495) 123-45-69',
                'leadership_type': 'deputy_director',
                'is_director': True,
                'order': 3
            },
            {
                'name': 'Козлова Ирина Сергеевна',
                'name_kg': 'Козлова Ирина Сергеевна',
                'name_en': 'Kozlova Irina Sergeevna',
                'position': 'Заведующий кафедрой терапии',
                'position_kg': 'Терапия кафедрасынын башчысы',
                'position_en': 'Head of Therapy Department',
                'degree': 'Доктор медицинских наук, профессор',
                'degree_kg': 'Медицина илимдеринин доктору, профессор',
                'degree_en': 'Doctor of Medical Sciences, Professor',
                'experience': '20 лет',
                'experience_kg': '20 жыл',
                'experience_en': '20 years',
                'bio': 'Признанный специалист в области внутренних болезней.',
                'bio_kg': 'Ички оорулар тармагында таанылган адис.',
                'bio_en': 'Recognized specialist in internal medicine.',
                'achievements': [
                    'Лауреат государственных наград',
                    'Автор учебников по терапии',
                    'Подготовка кандидатов наук'
                ],
                'achievements_kg': [
                    'Мамлекеттик сыйлыктардын ээси',
                    'Терапия боюнча окуу китептеринин автору',
                    'Илим кандидаттарын даярдоо'
                ],
                'achievements_en': [
                    'State awards recipient',
                    'Author of therapy textbooks',
                    'Training PhD candidates'
                ],
                'department': 'Кафедра терапии',
                'department_kg': 'Терапия кафедрасы',
                'department_en': 'Therapy Department',
                'specialization': 'Кардиология, пульмонология, гастроэнтерология',
                'specialization_kg': 'Кардиология, пульмонология, гастроэнтерология',
                'specialization_en': 'Cardiology, pulmonology, gastroenterology',
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
                'name_en': 'Nikolaev Dmitry Alexandrovich',
                'position': 'Заведующий кафедрой хирургии',
                'position_kg': 'Хирургия кафедрасынын башчысы',
                'position_en': 'Head of Surgery Department',
                'degree': 'Доктор медицинских наук',
                'degree_kg': 'Медицина илимдеринин доктору',
                'degree_en': 'Doctor of Medical Sciences',
                'experience': '22 года',
                'experience_kg': '22 жыл',
                'experience_en': '22 years',
                'bio': 'Ведущий хирург с международным опытом.',
                'bio_kg': 'Эл аралык тажрыйбасы бар алдыңкы хирург.',
                'bio_en': 'Leading surgeon with international experience.',
                'achievements': [
                    'Более 3000 операций',
                    'Внедрение новых методик',
                    'Обучение молодых специалистов'
                ],
                'achievements_kg': [
                    '3000дөн ашык операция',
                    'Жаңы методикаларды киргизүү',
                    'Жаш адистерди үйрөтүү'
                ],
                'achievements_en': [
                    'More than 3000 operations',
                    'Implementation of new techniques',
                    'Training young specialists'
                ],
                'department': 'Кафедра хирургии',
                'department_kg': 'Хирургия кафедрасы',
                'department_en': 'Surgery Department',
                'specialization': 'Абдоминальная хирургия, лапароскопия',
                'specialization_kg': 'Абдоминалдык хирургия, лапароскопия',
                'specialization_en': 'Abdominal surgery, laparoscopy',
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
                'name': 'Орлова Мария Викторовна',
                'name_kg': 'Орлова Мария Викторовна',
                'name_en': 'Orlova Maria Viktorovna',
                'position': 'Заведующий кафедрой педиатрии',
                'position_kg': 'Педиатрия кафедрасынын башчысы',
                'position_en': 'Head of Pediatrics Department',
                'degree': 'Кандидат медицинских наук',
                'degree_kg': 'Медицина илимдеринин кандидаты',
                'degree_en': 'PhD in Medical Sciences',
                'experience': '16 лет',
                'experience_kg': '16 жыл',
                'experience_en': '16 years',
                'bio': 'Специалист по детским болезням с большим опытом.',
                'bio_kg': 'Балдар оорулары боюнча чоң тажрыйбасы бар адис.',
                'bio_en': 'Specialist in pediatric diseases with extensive experience.',
                'achievements': [
                    'Разработка протоколов лечения',
                    'Участие в международных конференциях',
                    'Научные исследования в педиатрии'
                ],
                'achievements_kg': [
                    'Дарылоо протоколдорун иштеп чыгуу',
                    'Эл аралык конференцияларга катышуу',
                    'Педиатриядагы илимий изилдөөлөр'
                ],
                'achievements_en': [
                    'Development of treatment protocols',
                    'Participation in international conferences',
                    'Scientific research in pediatrics'
                ],
                'department': 'Кафедра педиатрии',
                'department_kg': 'Педиатрия кафедрасы',
                'department_en': 'Pediatrics Department',
                'specialization': 'Неонатология, детская кардиология',
                'specialization_kg': 'Неонатология, балдар кардиологиясы',
                'specialization_en': 'Neonatology, pediatric cardiology',
                'staff_count': '20 сотрудников',
                'staff_count_kg': '20 кызматкер',
                'staff_count_en': '20 employees',
                'email': 'pediatrics@meduniversity.ru',
                'phone': '+7 (495) 123-45-72',
                'leadership_type': 'department_head',
                'is_director': False,
                'order': 6
            },
            {
                'name': 'Васильев Андрей Николаевич',
                'name_kg': 'Васильев Андрей Николаевич',
                'name_en': 'Vasiliev Andrey Nikolaevich',
                'position': 'Заведующий кафедрой неврологии',
                'position_kg': 'Неврология кафедрасынын башчысы',
                'position_en': 'Head of Neurology Department',
                'degree': 'Доктор медицинских наук',
                'degree_kg': 'Медицина илимдеринин доктору',
                'degree_en': 'Doctor of Medical Sciences',
                'experience': '19 лет',
                'experience_kg': '19 жыл',
                'experience_en': '19 years',
                'bio': 'Нейрохирург высшей категории.',
                'bio_kg': 'Жогорку категориядагы нейрохирург.',
                'bio_en': 'Neurosurgeon of the highest category.',
                'achievements': [
                    'Пионер в нейрохирургии',
                    'Международные стажировки',
                    'Обучение ординаторов'
                ],
                'achievements_kg': [
                    'Нейрохирургиянын пионери',
                    'Эл аралык стажировкалар',
                    'Ординаторлорду үйрөтүү'
                ],
                'achievements_en': [
                    'Pioneer in neurosurgery',
                    'International internships',
                    'Training residents'
                ],
                'department': 'Кафедра неврологии',
                'department_kg': 'Неврология кафедрасы',
                'department_en': 'Neurology Department',
                'specialization': 'Нейрохирургия, эпилептология',
                'specialization_kg': 'Нейрохирургия, эпилептология',
                'specialization_en': 'Neurosurgery, epileptology',
                'staff_count': '15 сотрудников',
                'staff_count_kg': '15 кызматкер',
                'staff_count_en': '15 employees',
                'email': 'neurology@meduniversity.ru',
                'phone': '+7 (495) 123-45-73',
                'leadership_type': 'department_head',
                'is_director': False,
                'order': 7
            },
            {
                'name': 'Смирнова Наталья Игоревна',
                'name_kg': 'Смирнова Наталья Игоревна',
                'name_en': 'Smirnova Natalia Igorevna',
                'position': 'Заведующий кафедрой стоматологии',
                'position_kg': 'Стоматология кафедрасынын башчысы',
                'position_en': 'Head of Dentistry Department',
                'degree': 'Кандидат медицинских наук',
                'degree_kg': 'Медицина илимдеринин кандидаты',
                'degree_en': 'PhD in Medical Sciences',
                'experience': '14 лет',
                'experience_kg': '14 жыл',
                'experience_en': '14 years',
                'bio': 'Врач-стоматолог высшей категории.',
                'bio_kg': 'Жогорку категориядагы стоматолог-дарыгер.',
                'bio_en': 'Dentist of the highest category.',
                'achievements': [
                    'Внедрение современных технологий',
                    'Сертификация по имплантологии',
                    'Участие в профессиональных ассоциациях'
                ],
                'achievements_kg': [
                    'Замандаш технологияларды киргизүү',
                    'Имплантология боюнча сертификация',
                    'Кесиптик бирикмелерге катышуу'
                ],
                'achievements_en': [
                    'Implementation of modern technologies',
                    'Certification in implantology',
                    'Participation in professional associations'
                ],
                'department': 'Кафедра стоматологии',
                'department_kg': 'Стоматология кафедрасы',
                'department_en': 'Dentistry Department',
                'specialization': 'Ортопедическая стоматология, имплантология',
                'specialization_kg': 'Ортопедиялык стоматология, имплантология',
                'specialization_en': 'Orthopedic dentistry, implantology',
                'staff_count': '18 сотрудников',
                'staff_count_kg': '18 кызматкер',
                'staff_count_en': '18 employees',
                'email': 'dentistry@meduniversity.ru',
                'phone': '+7 (495) 123-45-74',
                'leadership_type': 'department_head',
                'is_director': False,
                'order': 8
            }
        ]

        for data in leadership_data:
            Leadership.objects.create(**data)
            
        self.stdout.write(
            self.style.SUCCESS(f'Успешно загружено {len(leadership_data)} записей руководства с текстовыми департаментами')
        )