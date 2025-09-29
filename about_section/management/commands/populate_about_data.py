from django.core.management.base import BaseCommand
from django.db import transaction
from about_section.models import (
    Founder, FounderAchievement, OrganizationStructure, 
    Achievement, UniversityStatistic
)


class Command(BaseCommand):
    help = 'Populate database with founders, structure, achievements, and statistics data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before populating',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write('Clearing existing data...')
            Founder.objects.all().delete()
            OrganizationStructure.objects.all().delete()
            Achievement.objects.all().delete()
            UniversityStatistic.objects.all().delete()

        with transaction.atomic():
            self.populate_founders()
            self.populate_structure()
            self.populate_achievements()
            self.populate_statistics()

        self.stdout.write(
            self.style.SUCCESS('Successfully populated about section data!')
        )

    def populate_founders(self):
        """Populate founders data"""
        self.stdout.write('Populating founders...')
        
        founders_data = [
            {
                'name_ru': 'Салымбеков Мирбек Шыкмаматович',
                'name_en': 'Salymbekov Mirbek Shykmamatovich',
                'name_ky': 'Салымбеков Мирбек Шыкмаматович',
                'position_ru': 'Основатель и первый ректор Медицинского университета "Салымбеков Университет"',
                'position_en': 'Founder and First Rector of Medical University "Salymbekov University"',
                'position_ky': 'Негиздөөчү жана биринчи ректор "Салымбеков Университет" медициналык университетинин',
                'years': '1995-2005',
                'description_ru': 'Выдающийся врач и педагог, основатель частного медицинского образования в Кыргызстане. Доктор медицинских наук, профессор.',
                'description_en': 'Outstanding physician and educator, founder of private medical education in Kyrgyzstan. Doctor of Medical Sciences, Professor.',
                'description_ky': 'Кыргызстандагы жеке медициналык билим берүүнүн негиздөөчүсү, көрүнүктүү дарыгер жана педагог. Медицина илимдеринин доктору, профессор.',
                'order': 1,
                'achievements': [
                    {
                        'achievement_ru': 'Основал первый частный медицинский университет в Кыргызстане',
                        'achievement_en': 'Founded the first private medical university in Kyrgyzstan',
                        'achievement_ky': 'Кыргызстандагы биринчи жеке медициналык университетти түзгөн'
                    },
                    {
                        'achievement_ru': 'Подготовил более 500 врачей-специалистов',
                        'achievement_en': 'Trained over 500 medical specialists',
                        'achievement_ky': '500дөн ашык дарыгер-адистерди даярдаган'
                    },
                    {
                        'achievement_ru': 'Автор более 80 научных трудов по медицине',
                        'achievement_en': 'Author of over 80 scientific works in medicine',
                        'achievement_ky': 'Медицина боюнча 80дан ашык илимий эмгектин автору'
                    },
                    {
                        'achievement_ru': 'Заслуженный деятель науки Кыргызской Республики',
                        'achievement_en': 'Honored Scientist of the Kyrgyz Republic',
                        'achievement_ky': 'Кыргыз Республикасынын илимдин сыйлуу ишмери'
                    }
                ]
            },
            {
                'name_ru': 'Абдраимов Болот Жакипович',
                'name_en': 'Abdraimov Bolot Zhakipovich',
                'name_ky': 'Абдраимов Болот Жакипович',
                'position_ru': 'Второй ректор, развитие инфраструктуры университета',
                'position_en': 'Second Rector, University Infrastructure Development',
                'position_ky': 'Экинчи ректор, университеттин инфраструктурасын өнүктүрүү',
                'years': '2005-2015',
                'description_ru': 'Продолжил традиции качественного медицинского образования, значительно расширил материально-техническую базу университета.',
                'description_en': 'Continued the traditions of quality medical education and significantly expanded the university\'s material and technical base.',
                'description_ky': 'Сапаттуу медициналык билим берүү салттарын улантып, университеттин материалдык-техникалык базасын олуттуу кеңейтти.',
                'order': 2,
                'achievements': [
                    {
                        'achievement_ru': 'Построил новые учебные корпуса',
                        'achievement_en': 'Built new educational buildings',
                        'achievement_ky': 'Жаңы окуу имараттарын курган'
                    },
                    {
                        'achievement_ru': 'Создал современные лаборатории',
                        'achievement_en': 'Created modern laboratories',
                        'achievement_ky': 'Заманбап лабораторияларды түзгөн'
                    },
                    {
                        'achievement_ru': 'Развил международное сотрудничество',
                        'achievement_en': 'Developed international cooperation',
                        'achievement_ky': 'Эл аралык кызматташтыкты өнүктүргөн'
                    },
                    {
                        'achievement_ru': 'Увеличил количество студентов в 3 раза',
                        'achievement_en': 'Tripled the number of students',
                        'achievement_ky': 'Студенттердин санын 3 эсеге көбөйткөн'
                    }
                ]
            },
            {
                'name_ru': 'Касымова Гульнара Орозбековна',
                'name_en': 'Kasymova Gulnara Orozbekovna',
                'name_ky': 'Касымова Гүлнара Орозбековна',
                'position_ru': 'Третий ректор, инновационное развитие и цифровизация',
                'position_en': 'Third Rector, Innovation Development and Digitalization',
                'position_ky': 'Үчүнчү ректор, инновациялык өнүгүү жана санариптештирүү',
                'years': '2015-2020',
                'description_ru': 'Внедрила современные образовательные технологии и цифровые решения в учебный процесс.',
                'description_en': 'Implemented modern educational technologies and digital solutions in the educational process.',
                'description_ky': 'Окуу процессине заманбап билим берүү технологияларын жана санариптик чечимдерди ишке киргизген.',
                'order': 3,
                'achievements': [
                    {
                        'achievement_ru': 'Запустила онлайн-обучение',
                        'achievement_en': 'Launched online education',
                        'achievement_ky': 'Онлайн окутууну иштетип жиберген'
                    },
                    {
                        'achievement_ru': 'Создала научно-исследовательские центры',
                        'achievement_en': 'Created research centers',
                        'achievement_ky': 'Илимий-изилдөө борборлорун түзгөн'
                    },
                    {
                        'achievement_ru': 'Получила международную аккредитацию',
                        'achievement_en': 'Obtained international accreditation',
                        'achievement_ky': 'Эл аралык аккредитацияны алган'
                    },
                    {
                        'achievement_ru': 'Развила телемедицину',
                        'achievement_en': 'Developed telemedicine',
                        'achievement_ky': 'Телемедицинаны өнүктүргөн'
                    }
                ]
            },
            {
                'name_ru': 'Исаков Тимур Абдрахманович',
                'name_en': 'Isakov Timur Abdrakhmanovicн',
                'name_ky': 'Исаков Тимур Абдрахманович',
                'position_ru': 'Действующий ректор, современное развитие и расширение',
                'position_en': 'Current Rector, Modern Development and Expansion',
                'position_ky': 'Учурдагы ректор, заманбап өнүгүү жана кеңейүү',
                'years': '2020-н.в.',
                'description_ru': 'Продолжает развивать университет в соответствии с современными требованиями медицинского образования.',
                'description_en': 'Continues to develop the university in accordance with modern requirements of medical education.',
                'description_ky': 'Медициналык билим берүүнүн заманбап талаптарына ылайык университетти өнүктүрүүнү улантууда.',
                'order': 4,
                'achievements': [
                    {
                        'achievement_ru': 'Расширил клиническую базу',
                        'achievement_en': 'Expanded clinical facilities',
                        'achievement_ky': 'Клиникалык базаны кеңейтти'
                    },
                    {
                        'achievement_ru': 'Укрепил международные связи',
                        'achievement_en': 'Strengthened international relations',
                        'achievement_ky': 'Эл аралык байланыштарды күчөтө'
                    },
                    {
                        'achievement_ru': 'Внедрил новые образовательные программы',
                        'achievement_en': 'Implemented new educational programs',
                        'achievement_ky': 'Жаңы билим берүү программаларын ишке киргизген'
                    },
                    {
                        'achievement_ru': 'Развивает научную деятельность',
                        'achievement_en': 'Develops scientific activity',
                        'achievement_ky': 'Илимий иш-аракетти өнүктүрөт'
                    }
                ]
            }
        ]

        for founder_data in founders_data:
            achievements_data = founder_data.pop('achievements')
            founder, created = Founder.objects.get_or_create(
                name_ru=founder_data['name_ru'],
                defaults=founder_data
            )
            
            if created:
                # Create achievements
                for i, achievement_data in enumerate(achievements_data, 1):
                    FounderAchievement.objects.create(
                        founder=founder,
                        order=i,
                        **achievement_data
                    )
                
                self.stdout.write(f'  Created founder: {founder.name_ru}')

    def populate_structure(self):
        """Populate organization structure data"""
        self.stdout.write('Populating organization structure...')
        
        # Leadership
        leadership_data = [
            {
                'name_ru': 'Ректорат',
                'name_en': 'Rectorate',
                'name_ky': 'Ректорат',
                'head_name_ru': 'Исаков Тимур Абдрахманович',
                'head_name_en': 'Isakov Timur Abdrakhmanovicн',
                'head_name_ky': 'Исаков Тимур Абдрахманович',
                'structure_type': 'leadership',
                'phone': '+996 312 123456',
                'order': 1,
                'icon': '👑'
            },
            {
                'name_ru': 'Проректор по учебной работе',
                'name_en': 'Vice-Rector for Academic Affairs',
                'name_ky': 'Окуу иши боюнча проректор',
                'head_name_ru': 'Джумабеков Азамат Суранчиевич',
                'head_name_en': 'Dzhumabekov Azamat Suranchievich',
                'head_name_ky': 'Жүмабеков Азамат Суранчиевич',
                'structure_type': 'leadership',
                'phone': '+996 312 123457',
                'order': 2,
                'icon': '👑'
            },
            {
                'name_ru': 'Проректор по научной работе',
                'name_en': 'Vice-Rector for Research',
                'name_ky': 'Илимий иш боюнча проректор',
                'head_name_ru': 'Алиева Назира Токторовна',
                'head_name_en': 'Alieva Nazira Toktorovna',
                'head_name_ky': 'Алиева Назира Токторовна',
                'structure_type': 'leadership',
                'phone': '+996 312 123458',
                'order': 3,
                'icon': '👑'
            },
            {
                'name_ru': 'Проректор по клинической работе',
                'name_en': 'Vice-Rector for Clinical Affairs',
                'name_ky': 'Клиникалык иш боюнча проректор',
                'head_name_ru': 'Мамырбеков Эрлан Абдулазизович',
                'head_name_en': 'Mamyrbekov Erlan Abdulazizovich',
                'head_name_ky': 'Мамырбеков Эрлан Абдулазизович',
                'structure_type': 'leadership',
                'phone': '+996 312 123459',
                'order': 4,
                'icon': '👑'
            }
        ]

        # Faculties with departments
        faculties_data = [
            {
                'name_ru': 'Медицинский факультет',
                'name_en': 'Medical Faculty',
                'name_ky': 'Медициналык факультет',
                'head_name_ru': 'Абдыкеримов Темирлан Абдыкеримович',
                'head_name_en': 'Abdykerimov Temirlan Abdykerimovich',
                'head_name_ky': 'Абдыкеримов Темирлан Абдыкеримович',
                'structure_type': 'faculties',
                'order': 1,
                'icon': '🎓',
                'departments': [
                    'Кафедра внутренних болезней',
                    'Кафедра хирургии',
                    'Кафедра педиатрии',
                    'Кафедра акушерства и гинекологии'
                ]
            },
            {
                'name_ru': 'Педиатрический факультет',
                'name_en': 'Pediatric Faculty',
                'name_ky': 'Педиатрия факультети',
                'head_name_ru': 'Касымова Айгуль Мамитовна',
                'head_name_en': 'Kasymova Aigul Mamitovna',
                'head_name_ky': 'Касымова Айгүл Мамитовна',
                'structure_type': 'faculties',
                'order': 2,
                'icon': '🎓',
                'departments': [
                    'Кафедра детских болезней',
                    'Кафедра неонатологии',
                    'Кафедра детской хирургии'
                ]
            },
            {
                'name_ru': 'Стоматологический факультет',
                'name_en': 'Dental Faculty',
                'name_ky': 'Стоматология факультети',
                'head_name_ru': 'Токтогулов Марат Орозович',
                'head_name_en': 'Toktogulov Marat Orozovich',
                'head_name_ky': 'Токтогулов Марат Орозович',
                'structure_type': 'faculties',
                'order': 3,
                'icon': '🎓',
                'departments': [
                    'Кафедра терапевтической стоматологии',
                    'Кафедра ортопедической стоматологии',
                    'Кафедра хирургической стоматологии'
                ]
            },
            {
                'name_ru': 'Фармацевтический факультет',
                'name_en': 'Pharmaceutical Faculty',
                'name_ky': 'Фармацевтика факультети',
                'head_name_ru': 'Джумабаева Жамила Рысбековна',
                'head_name_en': 'Dzhumabaeva Zhamila Rysbekovna',
                'head_name_ky': 'Жүмабаева Жамила Рысбековна',
                'structure_type': 'faculties',
                'order': 4,
                'icon': '🎓',
                'departments': [
                    'Кафедра фармацевтической химии',
                    'Кафедра фармакогнозии',
                    'Кафедра технологии лекарств'
                ]
            }
        ]

        # Administrative departments
        administrative_data = [
            {
                'name_ru': 'Учебный отдел',
                'name_en': 'Academic Office',
                'name_ky': 'Окуу бөлүмү',
                'head_name_ru': 'Максутова Сымбат Алмазовна',
                'head_name_en': 'Maksutova Symbat Almazovna',
                'head_name_ky': 'Максутова Сымбат Алмазовна',
                'structure_type': 'administrative',
                'phone': '+996 312 123470',
                'order': 1,
                'icon': '🏢'
            },
            {
                'name_ru': 'Научный отдел',
                'name_en': 'Research Office',
                'name_ky': 'Илимий бөлүм',
                'head_name_ru': 'Турдубеков Адилет Болотович',
                'head_name_en': 'Turdubekov Adilet Bolotovich',
                'head_name_ky': 'Турдубеков Адилет Болотович',
                'structure_type': 'administrative',
                'phone': '+996 312 123471',
                'order': 2,
                'icon': '🏢'
            },
            {
                'name_ru': 'Отдел кадров',
                'name_en': 'Human Resources Department',
                'name_ky': 'Кадр бөлүмү',
                'head_name_ru': 'Омурзакова Нуржан Саматовна',
                'head_name_en': 'Omurzakova Nurzhan Samatovna',
                'head_name_ky': 'Омурзакова Нуржан Саматовна',
                'structure_type': 'administrative',
                'phone': '+996 312 123472',
                'order': 3,
                'icon': '🏢'
            },
            {
                'name_ru': 'Бухгалтерия',
                'name_en': 'Accounting Department',
                'name_ky': 'Эсептик бөлүм',
                'head_name_ru': 'Акматова Бурул Жакшылыковна',
                'head_name_en': 'Akmatova Burul Zhakshylykovna',
                'head_name_ky': 'Акматова Бурул Жакшылыковна',
                'structure_type': 'administrative',
                'phone': '+996 312 123473',
                'order': 4,
                'icon': '🏢'
            }
        ]

        # Create leadership
        for structure_data in leadership_data:
            structure, created = OrganizationStructure.objects.get_or_create(
                name_ru=structure_data['name_ru'],
                structure_type=structure_data['structure_type'],
                defaults=structure_data
            )
            if created:
                self.stdout.write(f'  Created leadership: {structure.name_ru}')

        # Create faculties and their departments
        for faculty_data in faculties_data:
            departments = faculty_data.pop('departments', [])
            faculty, created = OrganizationStructure.objects.get_or_create(
                name_ru=faculty_data['name_ru'],
                structure_type=faculty_data['structure_type'],
                defaults=faculty_data
            )
            
            if created:
                # Create departments for this faculty
                for i, dept_name in enumerate(departments, 1):
                    OrganizationStructure.objects.create(
                        name_ru=dept_name,
                        name_en=dept_name,  # Could be translated later
                        name_ky=dept_name,  # Could be translated later
                        structure_type='support',
                        parent=faculty,
                        order=i,
                        icon='📚'
                    )
                
                self.stdout.write(f'  Created faculty: {faculty.name_ru} with {len(departments)} departments')

        # Create administrative departments
        for structure_data in administrative_data:
            structure, created = OrganizationStructure.objects.get_or_create(
                name_ru=structure_data['name_ru'],
                structure_type=structure_data['structure_type'],
                defaults=structure_data
            )
            if created:
                self.stdout.write(f'  Created administrative: {structure.name_ru}')

    def populate_achievements(self):
        """Populate achievements data"""
        self.stdout.write('Populating achievements...')
        
        achievements_data = [
            {
                'title_ru': 'Получение государственной аккредитации',
                'title_en': 'Obtained State Accreditation',
                'title_ky': 'Мамлекеттик аккредитацияны алуу',
                'description_ru': 'Университет успешно прошел государственную аккредитацию и получил право на выдачу дипломов государственного образца.',
                'description_en': 'The university successfully passed state accreditation and received the right to issue state-recognized diplomas.',
                'description_ky': 'Университет мамлекеттик аккредитациядан ийгиликтүү өттү жана мамлекеттик үлгүдөгү дипломдорду берүү укугун алды.',
                'year': 2024,
                'category': 'education',
                'icon': '🏆',
                'icon_color': 'bg-yellow-500',
                'featured': True,
                'order': 1
            },
            {
                'title_ru': 'Открытие кардиохирургического центра',
                'title_en': 'Opening of Cardiac Surgery Center',
                'title_ky': 'Кардиохирургиялык борборду ачуу',
                'description_ru': 'На базе университета открыт современный кардиохирургический центр, оснащенный новейшим оборудованием.',
                'description_en': 'A modern cardiac surgery center equipped with the latest equipment was opened at the university.',
                'description_ky': 'Университеттин базасында эң заманбап шайманга жабдылган заманбап кардиохирургиялык борбор ачылды.',
                'year': 2023,
                'category': 'science',
                'icon': '❤️',
                'icon_color': 'bg-red-500',
                'featured': False,
                'order': 2
            },
            {
                'title_ru': 'Международное партнерство с ведущими вузами',
                'title_en': 'International Partnership with Leading Universities',
                'title_ky': 'Алдыңкы университеттер менен эл аралык өнөктөштүк',
                'description_ru': 'Подписаны соглашения о сотрудничестве с медицинскими университетами США, Германии, Турции и других стран.',
                'description_en': 'Cooperation agreements were signed with medical universities in the USA, Germany, Turkey and other countries.',
                'description_ky': 'АКШ, Германия, Түркия жана башка өлкөлөрдөгү медициналык университеттер менен кызматташтык келишимдери кол коюлду.',
                'year': 2024,
                'category': 'international',
                'icon': '🌍',
                'icon_color': 'bg-blue-500',
                'featured': True,
                'order': 3
            },
            {
                'title_ru': 'Публикация в журналах высокого импакт-фактора',
                'title_en': 'Publications in High Impact Factor Journals',
                'title_ky': 'Жогорку импакт-фактордуу журналдарда басылма чыгаруу',
                'description_ru': 'Преподаватели и студенты университета опубликовали более 50 статей в международных журналах с высоким импакт-фактором.',
                'description_en': 'University faculty and students published over 50 articles in international journals with high impact factors.',
                'description_ky': 'Университеттин мугалимдери жана студенттери жогорку импакт-фактордуу эл аралык журналдарда 50дөн ашык макала жарыялаган.',
                'year': 2023,
                'category': 'science',
                'icon': '📚',
                'icon_color': 'bg-purple-500',
                'featured': False,
                'order': 4
            },
            {
                'title_ru': 'Строительство нового учебного корпуса',
                'title_en': 'Construction of New Academic Building',
                'title_ky': 'Жаңы окуу имаратын курууу',
                'description_ru': 'Завершено строительство современного учебного корпуса площадью 5000 кв.м с новейшим оборудованием.',
                'description_en': 'Construction of a modern academic building with an area of 5000 sq.m with the latest equipment has been completed.',
                'description_ky': 'Эң заманбап шайман менен 5000 чарчы метр аянтка ээ заманбап окуу имаратынын курулушу аяктады.',
                'year': 2024,
                'category': 'infrastructure',
                'icon': '🏥',
                'icon_color': 'bg-green-500',
                'featured': False,
                'order': 5
            },
            {
                'title_ru': 'Получение международного гранта на исследования',
                'title_en': 'Receiving International Research Grant',
                'title_ky': 'Изилдөөлөр үчүн эл аралык грант алуу',
                'description_ru': 'Университет получил грант от Европейского союза в размере 500 000 евро на проведение медицинских исследований.',
                'description_en': 'The university received a grant of 500,000 euros from the European Union for conducting medical research.',
                'description_ky': 'Университет медициналык изилдөөлөрдү жүргүзүү үчүн Европа Биримдигинен 500 000 евро грант алды.',
                'year': 2023,
                'category': 'science',
                'icon': '💰',
                'icon_color': 'bg-emerald-500',
                'featured': False,
                'order': 6
            }
        ]

        for achievement_data in achievements_data:
            achievement, created = Achievement.objects.get_or_create(
                title_ru=achievement_data['title_ru'],
                year=achievement_data['year'],
                defaults=achievement_data
            )
            if created:
                self.stdout.write(f'  Created achievement: {achievement.title_ru}')

    def populate_statistics(self):
        """Populate university statistics data"""
        self.stdout.write('Populating statistics...')
        
        statistics_data = [
            {
                'name_ru': 'Научные публикации',
                'name_en': 'Scientific Publications',
                'name_ky': 'Илимий басылмалар',
                'value': '150',
                'unit': '+',
                'icon': '📚',
                'order': 1
            },
            {
                'name_ru': 'Партнерские организации',
                'name_en': 'Partner Organizations',
                'name_ky': 'Өнөктөш уюмдар',
                'value': '25',
                'unit': '+',
                'icon': '🤝',
                'order': 2
            },
            {
                'name_ru': 'Трудоустройство выпускников',
                'name_en': 'Graduate Employment Rate',
                'name_ky': 'Бүтүрүүчүлөрдүн иштеп орношуусу',
                'value': '95',
                'unit': '%',
                'icon': '👥',
                'order': 3
            },
            {
                'name_ru': 'Клинические базы',
                'name_en': 'Clinical Bases',
                'name_ky': 'Клиникалык базалар',
                'value': '50',
                'unit': '+',
                'icon': '🏥',
                'order': 4
            }
        ]

        for stat_data in statistics_data:
            statistic, created = UniversityStatistic.objects.get_or_create(
                name_ru=stat_data['name_ru'],
                defaults=stat_data
            )
            if created:
                self.stdout.write(f'  Created statistic: {statistic.name_ru}')