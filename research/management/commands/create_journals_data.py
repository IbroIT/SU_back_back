from django.core.management.base import BaseCommand
from research.models import ScientificJournal
from django.utils import timezone


class Command(BaseCommand):
    help = 'Create test data for Scientific Journals'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creating Scientific Journals test data...'))

        # Clear existing data
        ScientificJournal.objects.all().delete()

        journals_data = [
            {
                'title_ru': 'Медицинский вестник Кыргызстана',
                'title_en': 'Medical Herald of Kyrgyzstan',
                'title_kg': 'Кыргызстандын медициналык кабарчысы',
                'description_ru': 'Ведущий медицинский журнал Кыргызской Республики, публикующий результаты фундаментальных и прикладных исследований в области медицины.',
                'description_en': 'Leading medical journal of the Kyrgyz Republic, publishing results of fundamental and applied research in medicine.',
                'description_kg': 'Кыргыз Республикасынын жетекчи медициналык журналы, медицина тармагындагы фундаменталдык жана колдонмо изилдөөлөрдүн натыйжаларын жарыялайт.',
                'issn': '1694-8475',
                'eissn': '2075-1478',
                'editor_in_chief_ru': 'Профессор Айтматов Талант Кубанычович',
                'editor_in_chief_en': 'Professor Aitmatov Talant Kubanychovich',
                'editor_in_chief_kg': 'Профессор Айтматов Талант Кубанычович',
                'editorial_board_ru': [
                    'Профессор Абдыкеримов С.К. - кардиология',
                    'Профессор Бейшеналиева Г.А. - педиатрия',
                    'Профессор Жунушов А.С. - хирургия',
                    'Профессор Токтосунова А.И. - неврология',
                    'Профессор Мамытов М.М. - онкология'
                ],
                'editorial_board_en': [
                    'Professor Abdykerimov S.K. - cardiology',
                    'Professor Beishenalieva G.A. - pediatrics',
                    'Professor Zhunushov A.S. - surgery',
                    'Professor Toktosunova A.I. - neurology',
                    'Professor Mamytov M.M. - oncology'
                ],
                'editorial_board_kg': [
                    'Профессор Абдыкеримов С.К. - кардиология',
                    'Профессор Бейшеналиева Г.А. - педиатрия',
                    'Профессор Жунушов А.С. - хирургия',
                    'Профессор Токтосунова А.И. - неврология',
                    'Профессор Мамытов М.М. - онкология'
                ],
                'publication_frequency_ru': 'Ежеквартально (4 раза в год)',
                'publication_frequency_en': 'Quarterly (4 times per year)',
                'publication_frequency_kg': 'Чейректик (жылына 4 жолу)',
                'scope_ru': 'Фундаментальная медицина, клиническая медицина, общественное здравоохранение, медицинская биология',
                'scope_en': 'Fundamental medicine, clinical medicine, public health, medical biology',
                'scope_kg': 'Фундаменталдык медицина, клиникалык медицина, коомдук саламаттык сактоо, медициналык биология',
                'submission_guidelines_ru': 'Статьи должны быть оригинальными, не публиковавшимися ранее. Объем до 15 страниц. Обязательные разделы: введение, материалы и методы, результаты, обсуждение, выводы.',
                'submission_guidelines_en': 'Articles must be original and previously unpublished. Volume up to 15 pages. Required sections: introduction, materials and methods, results, discussion, conclusions.',
                'submission_guidelines_kg': 'Макалалар түпнуска жана мурда жарыяланбаган болушу керек. Көлөмү 15 бараққа чейин. Милдеттүү бөлүмдөр: киришүү, материалдар жана ыкмалар, натыйжалар, талкуу, корутундулар.',
                'website': 'https://medjournal.kg',
                'contact_email': 'editor@medjournal.kg',
                'established_year': 1995,
                'impact_factor': 1.245,
                'is_open_access': True,
                'is_peer_reviewed': True,
            },
            {
                'title_ru': 'Журнал фармацевтических наук',
                'title_en': 'Journal of Pharmaceutical Sciences',
                'title_kg': 'Фармацевтикалык илимдердин журналы',
                'description_ru': 'Международный рецензируемый журнал, посвященный фармацевтическим исследованиям и разработкам.',
                'description_en': 'International peer-reviewed journal dedicated to pharmaceutical research and development.',
                'description_kg': 'Фармацевтикалык изилдөөлөргө жана иштеп чыгууларга арналган эл аралык рецензияланган журнал.',
                'issn': '2075-1486',
                'eissn': '2411-3654',
                'editor_in_chief_ru': 'Профессор Касымова Гульмира Орозбековна',
                'editor_in_chief_en': 'Professor Kasymova Gulmira Orozbekovna',
                'editor_in_chief_kg': 'Профессор Касымова Гүлмира Орозбек кызы',
                'editorial_board_ru': [
                    'Профессор Султанов К.А. - фармакология',
                    'Профессор Алиева Н.Б. - фармацевтическая химия',
                    'Профессор Осмонов Б.Э. - фармацевтическая технология',
                    'Профессор Жакыпова А.М. - клиническая фармация'
                ],
                'editorial_board_en': [
                    'Professor Sultanov K.A. - pharmacology',
                    'Professor Alieva N.B. - pharmaceutical chemistry',
                    'Professor Osmonov B.E. - pharmaceutical technology',
                    'Professor Zhakypova A.M. - clinical pharmacy'
                ],
                'editorial_board_kg': [
                    'Профессор Султанов К.А. - фармакология',
                    'Профессор Алиева Н.Б. - фармацевтикалык химия',
                    'Профессор Осмонов Б.Э. - фармацевтикалык технология',
                    'Профессор Жакыпова А.М. - клиникалык фармация'
                ],
                'publication_frequency_ru': 'Дважды в год',
                'publication_frequency_en': 'Twice a year',
                'publication_frequency_kg': 'Жылына эки жолу',
                'scope_ru': 'Фармакология, фармацевтическая химия, технология лекарственных препаратов, клиническая фармация',
                'scope_en': 'Pharmacology, pharmaceutical chemistry, drug technology, clinical pharmacy',
                'scope_kg': 'Фармакология, фармацевтикалык химия, дары каражаттарынын технологиясы, клиникалык фармация',
                'submission_guidelines_ru': 'Принимаются оригинальные исследования, обзоры, краткие сообщения. Объем 8-12 страниц для исследований, до 20 страниц для обзоров.',
                'submission_guidelines_en': 'Original research, reviews, brief communications are accepted. Volume 8-12 pages for research, up to 20 pages for reviews.',
                'submission_guidelines_kg': 'Түпнуска изилдөөлөр, сын-пикирлер, кыска кабарлар кабыл алынат. Изилдөөлөр үчүн 8-12 барак, сын-пикирлер үчүн 20 баракка чейин.',
                'website': 'https://pharmjournal.kg',
                'contact_email': 'editor@pharmjournal.kg',
                'established_year': 2003,
                'impact_factor': 0.785,
                'is_open_access': False,
                'is_peer_reviewed': True,
            },
            {
                'title_ru': 'Стоматологический вестник',
                'title_en': 'Dental Herald',
                'title_kg': 'Стоматологиялык кабарчы',
                'description_ru': 'Специализированный журнал по стоматологии и челюстно-лицевой хирургии.',
                'description_en': 'Specialized journal on dentistry and maxillofacial surgery.',
                'description_kg': 'Стоматология жана челюсть-жүз хирургиясы боюнча атайын журнал.',
                'issn': '1694-9870',
                'eissn': '2411-7890',
                'editor_in_chief_ru': 'Профессор Мамаджанов Рустам Ахмедович',
                'editor_in_chief_en': 'Professor Mamadzhanov Rustam Ahmedovich',
                'editor_in_chief_kg': 'Профессор Мамажанов Рустам Ахмед уулу',
                'editorial_board_ru': [
                    'Профессор Исаева М.К. - терапевтическая стоматология',
                    'Профессор Эргешов А.Т. - хирургическая стоматология',
                    'Профессор Курманова Л.С. - детская стоматология',
                    'Профессор Абдиев Н.М. - ортопедическая стоматология'
                ],
                'editorial_board_en': [
                    'Professor Isaeva M.K. - therapeutic dentistry',
                    'Professor Ergeshov A.T. - surgical dentistry',
                    'Professor Kurmanova L.S. - pediatric dentistry',
                    'Professor Abdiev N.M. - prosthetic dentistry'
                ],
                'editorial_board_kg': [
                    'Профессор Исаева М.К. - терапевтикалык стоматология',
                    'Профессор Эргешов А.Т. - хирургиялык стоматология',
                    'Профессор Курманова Л.С. - балдар стоматологиясы',
                    'Профессор Абдиев Н.М. - ортопедиялык стоматология'
                ],
                'publication_frequency_ru': 'Три раза в год',
                'publication_frequency_en': 'Three times a year',
                'publication_frequency_kg': 'Жылына үч жолу',
                'scope_ru': 'Терапевтическая стоматология, хирургическая стоматология, ортопедия, ортодонтия, детская стоматология',
                'scope_en': 'Therapeutic dentistry, surgical dentistry, prosthetics, orthodontics, pediatric dentistry',
                'scope_kg': 'Терапевтикалык стоматология, хирургиялык стоматология, протездөө, ортодонтия, балдар стоматологиясы',
                'submission_guidelines_ru': 'Клинические исследования, случаи из практики, обзоры литературы. Статьи на русском, английском или кыргызском языках.',
                'submission_guidelines_en': 'Clinical studies, case reports, literature reviews. Articles in Russian, English or Kyrgyz languages.',
                'submission_guidelines_kg': 'Клиникалык изилдөөлөр, практикадан алынган учурлар, адабияттарга сереп салуу. Орус, англис же кыргыз тилдериндеги макалалар.',
                'website': 'https://dentaljournal.kg',
                'contact_email': 'editor@dentaljournal.kg',
                'established_year': 2008,
                'impact_factor': 0.542,
                'is_open_access': True,
                'is_peer_reviewed': True,
            },
            {
                'title_ru': 'Архив патологии',
                'title_en': 'Archive of Pathology',
                'title_kg': 'Патология архиви',
                'description_ru': 'Журнал по патологической анатомии и судебной медицине.',
                'description_en': 'Journal of pathological anatomy and forensic medicine.',
                'description_kg': 'Патологиялык анатомия жана соттук медицина журналы.',
                'issn': '2075-1494',
                'eissn': '2411-3700',
                'editor_in_chief_ru': 'Профессор Токтогулов Нурлан Абдыкеримович',
                'editor_in_chief_en': 'Professor Toktogulov Nurlan Abdykerimovich',
                'editor_in_chief_kg': 'Профессор Токтогулов Нурлан Абдыкерим уулу',
                'editorial_board_ru': [
                    'Профессор Асанова К.Б. - онкопатология',
                    'Профессор Мураталиев Э.К. - кардиопатология',
                    'Профессор Садыкова А.Н. - нейропатология'
                ],
                'editorial_board_en': [
                    'Professor Asanova K.B. - oncopathology',
                    'Professor Murataliev E.K. - cardiopathology',
                    'Professor Sadykova A.N. - neuropathology'
                ],
                'editorial_board_kg': [
                    'Профессор Асанова К.Б. - онкопатология',
                    'Профессор Мураталиев Э.К. - кардиопатология',
                    'Профессор Садыкова А.Н. - нейропатология'
                ],
                'publication_frequency_ru': 'Дважды в год',
                'publication_frequency_en': 'Twice a year',
                'publication_frequency_kg': 'Жылына эки жолу',
                'scope_ru': 'Патологическая анатомия, судебная медицина, цитология, гистология',
                'scope_en': 'Pathological anatomy, forensic medicine, cytology, histology',
                'scope_kg': 'Патологиялык анатомия, соттук медицина, цитология, гистология',
                'submission_guidelines_ru': 'Оригинальные исследования по патологии, описания редких случаев, методические статьи.',
                'submission_guidelines_en': 'Original pathology research, rare case descriptions, methodological articles.',
                'submission_guidelines_kg': 'Патология боюнча түпнуска изилдөөлөр, сейрек учурлардын сыпаттамалары, методикалык макалалар.',
                'website': 'https://patharchive.kg',
                'contact_email': 'editor@patharchive.kg',
                'established_year': 2010,
                'impact_factor': 0.345,
                'is_open_access': False,
                'is_peer_reviewed': True,
            },
            {
                'title_ru': 'Журнал общественного здравоохранения',
                'title_en': 'Journal of Public Health',
                'title_kg': 'Коомдук саламаттык сактоо журналы',
                'description_ru': 'Междисциплинарный журнал по вопросам общественного здравоохранения и медицинской статистики.',
                'description_en': 'Interdisciplinary journal on public health and medical statistics.',
                'description_kg': 'Коомдук саламаттык сактоо жана медициналык статистика маселелери боюнча пландашкан журнал.',
                'issn': '2411-3720',
                'eissn': '2411-3739',
                'editor_in_chief_ru': 'Профессор Калыева Айгуль Мамытбековна',
                'editor_in_chief_en': 'Professor Kalyeva Aigul Mamytbekovna',
                'editor_in_chief_kg': 'Профессор Калыева Айгүл Мамытбек кызы',
                'editorial_board_ru': [
                    'Профессор Джолдубаев С.Д. - эпидемиология',
                    'Профессор Артыкова Г.Т. - социальная медицина',
                    'Профессор Турдумаматов А.К. - биостатистика',
                    'Профессор Назарова М.А. - медицинская экология'
                ],
                'editorial_board_en': [
                    'Professor Dzholdubaev S.D. - epidemiology',
                    'Professor Artykova G.T. - social medicine',
                    'Professor Turdumamatov A.K. - biostatistics',
                    'Professor Nazarova M.A. - medical ecology'
                ],
                'editorial_board_kg': [
                    'Профессор Жолдубаев С.Д. - эпидемиология',
                    'Профессор Артыкова Г.Т. - социалдык медицина',
                    'Профессор Турдумаматов А.К. - биостатистика',
                    'Профессор Назарова М.А. - медициналык экология'
                ],
                'publication_frequency_ru': 'Ежеквартально (4 раза в год)',
                'publication_frequency_en': 'Quarterly (4 times per year)',
                'publication_frequency_kg': 'Чейректик (жылына 4 жолу)',
                'scope_ru': 'Эпидемиология, биостатистика, социальная медицина, медицинская экология, управление здравоохранением',
                'scope_en': 'Epidemiology, biostatistics, social medicine, medical ecology, health management',
                'scope_kg': 'Эпидемиология, биостатистика, социалдык медицина, медициналык экология, саламаттык сактоону башкаруу',
                'submission_guidelines_ru': 'Эпидемиологические исследования, анализ медицинских данных, обзоры систем здравоохранения.',
                'submission_guidelines_en': 'Epidemiological studies, medical data analysis, healthcare system reviews.',
                'submission_guidelines_kg': 'Эпидемиологиялык изилдөөлөр, медициналык маалыматтарды талдоо, саламаттык сактоо системаларын карап чыгуу.',
                'website': 'https://pubhealth.kg',
                'contact_email': 'editor@pubhealth.kg',
                'established_year': 2012,
                'impact_factor': 0.923,
                'is_open_access': True,
                'is_peer_reviewed': True,
            }
        ]

        created_count = 0
        for journal_data in journals_data:
            journal, created = ScientificJournal.objects.get_or_create(
                title_ru=journal_data['title_ru'],
                defaults=journal_data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Created journal: {journal.title_ru}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'⚠ Journal already exists: {journal.title_ru}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\nSuccessfully created {created_count} scientific journals!')
        )
        self.stdout.write(
            self.style.SUCCESS(f'Total journals in database: {ScientificJournal.objects.count()}')
        )
