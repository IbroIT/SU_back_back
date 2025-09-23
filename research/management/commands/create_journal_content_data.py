from django.core.management.base import BaseCommand
from research.models import ScientificJournal, JournalIssue, JournalArticle
from django.utils import timezone
from datetime import date


class Command(BaseCommand):
    help = 'Create test data for Journal Issues and Articles'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creating Journal Issues and Articles test data...'))

        # Clear existing data
        JournalArticle.objects.all().delete()
        JournalIssue.objects.all().delete()

        # Get journals
        journals = ScientificJournal.objects.all()
        if not journals.exists():
            self.stdout.write(self.style.ERROR('No journals found! Please run create_journals_data first.'))
            return

        created_issues = 0
        created_articles = 0

        for journal in journals:
            # Create 2-3 issues for each journal
            for volume in range(1, 3):
                for number in range(1, 4):
                    issue_data = {
                        'journal': journal,
                        'volume': volume,
                        'number': number,
                        'year': 2024 if volume == 1 else 2025,
                        'title_ru': f'Специальный выпуск по {journal.title_ru.split()[0].lower()}',
                        'title_en': f'Special issue on {journal.title_en.split()[0].lower()}',
                        'title_kg': f'{journal.title_kg.split()[0]} боюнча атайын чыгарылыш',
                        'publication_date': date(2024 if volume == 1 else 2025, number * 3, 15),
                        'description_ru': f'Данный выпуск содержит актуальные исследования в области медицины.',
                        'description_en': f'This issue contains current research in the field of medicine.',
                        'description_kg': f'Бул чыгарылыш медицина тармагындагы актуалдуу изилдөөлөрдү камтыйт.',
                        'pages_count': 120 + (number * 10),
                        'articles_count': 8 + number,
                        'is_published': True,
                    }
                    
                    issue, created = JournalIssue.objects.get_or_create(
                        journal=journal,
                        volume=volume,
                        number=number,
                        year=2024 if volume == 1 else 2025,
                        defaults=issue_data
                    )
                    
                    if created:
                        created_issues += 1
                        self.stdout.write(
                            self.style.SUCCESS(f'✓ Created issue: {issue}')
                        )

                        # Create 3-5 articles for each issue
                        articles_data = [
                            {
                                'title_ru': f'Клинические исследования в {journal.title_ru.split()[0].lower()}',
                                'title_en': f'Clinical studies in {journal.title_en.split()[0].lower()}',
                                'title_kg': f'{journal.title_kg.split()[0]} тармагындагы клиникалык изилдөөлөр',
                                'authors_ru': 'Иванов И.И., Петров П.П., Сидоров С.С.',
                                'authors_en': 'Ivanov I.I., Petrov P.P., Sidorov S.S.',
                                'authors_kg': 'Иванов И.И., Петров П.П., Сидоров С.С.',
                                'abstract_ru': 'В данной работе представлены результаты клинических исследований, проведенных в течение 2 лет.',
                                'abstract_en': 'This work presents the results of clinical studies conducted over 2 years.',
                                'abstract_kg': 'Бул иште 2 жыл бою жүргүзүлгөн клиникалык изилдөөлөрдүн натыйжалары көрсөтүлгөн.',
                                'keywords_ru': ['клинические исследования', 'медицина', 'терапия'],
                                'keywords_en': ['clinical studies', 'medicine', 'therapy'],
                                'keywords_kg': ['клиникалык изилдөөлөр', 'медицина', 'терапия'],
                                'pages_start': 5,
                                'pages_end': 15,
                                'order': 1,
                            },
                            {
                                'title_ru': f'Новые методы диагностики в {journal.title_ru.split()[0].lower()}',
                                'title_en': f'New diagnostic methods in {journal.title_en.split()[0].lower()}',
                                'title_kg': f'{journal.title_kg.split()[0]} тармагындагы жаңы диагностика ыкмалары',
                                'authors_ru': 'Алиев А.А., Мамытов М.М.',
                                'authors_en': 'Aliev A.A., Mamytov M.M.',
                                'authors_kg': 'Алиев А.А., Мамытов М.М.',
                                'abstract_ru': 'Статья посвящена разработке новых методов диагностики заболеваний.',
                                'abstract_en': 'The article is devoted to the development of new methods for diagnosing diseases.',
                                'abstract_kg': 'Макала ооруларды диагностикалоонун жаңы ыкмаларын иштеп чыгууга арналган.',
                                'keywords_ru': ['диагностика', 'методы', 'заболевания'],
                                'keywords_en': ['diagnostics', 'methods', 'diseases'],
                                'keywords_kg': ['диагностика', 'ыкмалар', 'оорулар'],
                                'pages_start': 16,
                                'pages_end': 28,
                                'order': 2,
                            },
                            {
                                'title_ru': f'Фармакологические аспекты лечения',
                                'title_en': f'Pharmacological aspects of treatment',
                                'title_kg': f'Дарылоонун фармакологиялык аспектилери',
                                'authors_ru': 'Касымова Г.О., Токтогулов Н.А.',
                                'authors_en': 'Kasymova G.O., Toktogulov N.A.',
                                'authors_kg': 'Касымова Г.О., Токтогулов Н.А.',
                                'abstract_ru': 'Обзор современных фармакологических подходов к лечению.',
                                'abstract_en': 'Review of modern pharmacological approaches to treatment.',
                                'abstract_kg': 'Дарылоого болгон заманбап фармакологиялык мамилелерге сереп салуу.',
                                'keywords_ru': ['фармакология', 'лечение', 'препараты'],
                                'keywords_en': ['pharmacology', 'treatment', 'drugs'],
                                'keywords_kg': ['фармакология', 'дарылоо', 'дары каражаттары'],
                                'pages_start': 29,
                                'pages_end': 42,
                                'order': 3,
                            }
                        ]

                        for i, article_data in enumerate(articles_data):
                            article_data.update({
                                'issue': issue,
                                'received_date': date(issue.year, issue.publication_date.month - 2, 10),
                                'accepted_date': date(issue.year, issue.publication_date.month - 1, 15),
                                'published_date': issue.publication_date,
                                'citations_count': (i + 1) * 5,
                            })
                            
                            article, created = JournalArticle.objects.get_or_create(
                                issue=issue,
                                title_ru=article_data['title_ru'],
                                defaults=article_data
                            )
                            
                            if created:
                                created_articles += 1

        self.stdout.write(
            self.style.SUCCESS(f'\nSuccessfully created {created_issues} journal issues!')
        )
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_articles} journal articles!')
        )
        self.stdout.write(
            self.style.SUCCESS(f'Total issues in database: {JournalIssue.objects.count()}')
        )
        self.stdout.write(
            self.style.SUCCESS(f'Total articles in database: {JournalArticle.objects.count()}')
        )
