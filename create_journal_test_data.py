#!/usr/bin/env python
import os
import django
from datetime import date, timedelta
import random

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from research.models import ScientificJournal, JournalIssue, JournalArticle

def create_journals_data():
    """Создает тестовые данные для научных журналов"""
    
    # Очищаем существующие данные
    ScientificJournal.objects.all().delete()
    
    # Список журналов для создания
    journals_data = [
        {
            'title_ru': 'Вестник Салымбековского университета',
            'title_en': 'Bulletin of Salymbekov University', 
            'title_kg': 'Салымбеков университетинин жарчысы',
            'description_ru': 'Научный журнал, освещающий актуальные вопросы медицины, образования и науки',
            'description_en': 'Scientific journal covering current issues in medicine, education and science',
            'description_kg': 'Медицина, билим берүү жана илимдин актуалдуу маселелерин камтыган илимий журнал',
            'issn': '1234-5678',
            'eissn': '1234-5679',
            'editor_in_chief_ru': 'Салымбеков Акылбек Салымбекович',
            'editor_in_chief_en': 'Salymbekov Akylbek Salymbekovich',
            'editor_in_chief_kg': 'Салымбеков Акылбек Салымбекович',
            'publication_frequency_ru': 'Ежеквартально',
            'publication_frequency_en': 'Quarterly',
            'publication_frequency_kg': 'Чейректе бир жолу',
            'scope_ru': 'Клиническая медицина, общественное здравоохранение, медицинская этика',
            'scope_en': 'Clinical medicine, public health, medical ethics',
            'scope_kg': 'Клиникалык медицина, коомдук саламаттык сактоо, медициналык этика',
            'established_year': 2010,
            'impact_factor': 1.25,
            'is_open_access': True,
            'is_peer_reviewed': True,
        },
        {
            'title_ru': 'Медицинские исследования',
            'title_en': 'Medical Research',
            'title_kg': 'Медициналык изилдөөлөр',
            'description_ru': 'Журнал фундаментальных и прикладных медицинских исследований',
            'description_en': 'Journal of fundamental and applied medical research',
            'description_kg': 'Фундаменталдык жана колдонмо медициналык изилдөөлөрдүн журналы',
            'issn': '2345-6789',
            'eissn': '2345-6790',
            'editor_in_chief_ru': 'Иванова Мария Петровна',
            'editor_in_chief_en': 'Ivanova Maria Petrovna',
            'editor_in_chief_kg': 'Иванова Мария Петровна',
            'publication_frequency_ru': 'Ежемесячно',
            'publication_frequency_en': 'Monthly',
            'publication_frequency_kg': 'Айда бир жолу',
            'scope_ru': 'Фундаментальная медицина, биохимия, молекулярная биология',
            'scope_en': 'Fundamental medicine, biochemistry, molecular biology',
            'scope_kg': 'Фундаменталдык медицина, биохимия, молекулалык биология',
            'established_year': 2015,
            'impact_factor': 2.15,
            'is_open_access': True,
            'is_peer_reviewed': True,
        },
        {
            'title_ru': 'Инновации в здравоохранении',
            'title_en': 'Healthcare Innovations',
            'title_kg': 'Саламаттык сактоодогу инновациялар',
            'description_ru': 'Журнал современных технологий и инноваций в медицине',
            'description_en': 'Journal of modern technologies and innovations in medicine',
            'description_kg': 'Медицинадагы заманбап технологиялар жана инновациялардын журналы',
            'issn': '3456-7890',
            'eissn': '3456-7891',
            'editor_in_chief_ru': 'Петров Сергей Александрович',
            'editor_in_chief_en': 'Petrov Sergey Aleksandrovich',
            'editor_in_chief_kg': 'Петров Сергей Александрович',
            'publication_frequency_ru': 'Два раза в год',
            'publication_frequency_en': 'Biannually',
            'publication_frequency_kg': 'Жылда эки жолу',
            'scope_ru': 'Медицинские технологии, цифровая медицина, телемедицина',
            'scope_en': 'Medical technologies, digital medicine, telemedicine',
            'scope_kg': 'Медициналык технологиялар, санариптик медицина, телемедицина',
            'established_year': 2018,
            'impact_factor': 1.85,
            'is_open_access': False,
            'is_peer_reviewed': True,
        }
    ]
    
    created_journals = []
    
    # Создаем журналы
    for journal_data in journals_data:
        journal = ScientificJournal.objects.create(**journal_data)
        created_journals.append(journal)
        print(f"✅ Создан журнал: {journal.title_ru}")
        
        # Создаем выпуски для каждого журнала
        create_issues_for_journal(journal)
    
    print(f"\n🎉 Успешно создано {len(created_journals)} журналов с выпусками и статьями!")


def create_issues_for_journal(journal):
    """Создает выпуски и статьи для журнала"""
    
    current_year = date.today().year
    years = [current_year - 2, current_year - 1, current_year]
    
    for year in years:
        # Определяем количество выпусков в зависимости от периодичности
        if 'ежемесячно' in journal.publication_frequency_ru.lower() or 'monthly' in journal.publication_frequency_en.lower():
            issues_count = 12
        elif 'ежеквартально' in journal.publication_frequency_ru.lower() or 'quarterly' in journal.publication_frequency_en.lower():
            issues_count = 4
        else:
            issues_count = 2
        
        for issue_num in range(1, issues_count + 1):
            # Создаем выпуск
            publication_date = date(year, min(issue_num * (12 // issues_count), 12), 1)
            
            issue = JournalIssue.objects.create(
                journal=journal,
                volume=year - journal.established_year + 1,
                number=issue_num,
                year=year,
                title_ru=f"Выпуск {issue_num}",
                title_en=f"Issue {issue_num}",
                title_kg=f"{issue_num}-чыгарылыш",
                publication_date=publication_date,
                description_ru=f"Научные статьи и исследования {year} года",
                description_en=f"Scientific articles and research of {year}",
                description_kg=f"{year}-жылдын илимий макалалары жана изилдөөлөрү",
                articles_count=random.randint(5, 12),
                pages_count=random.randint(80, 150),
                is_published=True,
                is_active=True
            )
            
            # Создаем статьи для выпуска
            create_articles_for_issue(issue)
    
    print(f"  📚 Созданы выпуски для журнала: {journal.title_ru}")


def create_articles_for_issue(issue):
    """Создает статьи для выпуска"""
    
    # Примеры статей
    articles_examples = [
        {
            'title_ru': 'Современные методы диагностики сердечно-сосудистых заболеваний',
            'title_en': 'Modern methods of cardiovascular disease diagnosis',
            'title_kg': 'Жүрөк-кан тамыр оорууларын диагностикалоонун заманбап ыкмалары',
            'authors_ru': 'Иванов И.И., Петров П.П., Сидоров С.С.',
            'authors_en': 'Ivanov I.I., Petrov P.P., Sidorov S.S.',
            'authors_kg': 'Иванов И.И., Петров П.П., Сидоров С.С.',
            'keywords': ['кардиология', 'диагностика', 'ЭКГ', 'УЗИ']
        },
        {
            'title_ru': 'Влияние стресса на иммунную систему человека',
            'title_en': 'The impact of stress on the human immune system',
            'title_kg': 'Стресстин адамдын иммундук системасына тийгизген таасири',
            'authors_ru': 'Николаева Н.Н., Михайлов М.М.',
            'authors_en': 'Nikolaeva N.N., Mikhailov M.M.',
            'authors_kg': 'Николаева Н.Н., Михайлов М.М.',
            'keywords': ['иммунология', 'стресс', 'психосоматика']
        },
        {
            'title_ru': 'Эффективность новых антибиотиков в лечении инфекций',
            'title_en': 'Effectiveness of new antibiotics in infection treatment',
            'title_kg': 'Жаңы антибиотиктердин инфекцияларды дарылоодогу эффективдүүлүгү',
            'authors_ru': 'Ковалев К.К., Федоров Ф.Ф.',
            'authors_en': 'Kovalev K.K., Fedorov F.F.',
            'authors_kg': 'Ковалев К.К., Федоров Ф.Ф.',
            'keywords': ['антибиотики', 'инфекция', 'лечение']
        },
        {
            'title_ru': 'Применение искусственного интеллекта в медицинской диагностике',
            'title_en': 'Application of artificial intelligence in medical diagnosis',
            'title_kg': 'Медициналык диагностикада жасалма интеллектти колдонуу',
            'authors_ru': 'Алексеев А.А., Романов Р.Р.',
            'authors_en': 'Alekseev A.A., Romanov R.R.',
            'authors_kg': 'Алексеев А.А., Романов Р.Р.',
            'keywords': ['ИИ', 'диагностика', 'машинное обучение']
        }
    ]
    
    articles_to_create = random.randint(3, min(len(articles_examples), issue.articles_count))
    selected_articles = random.sample(articles_examples, articles_to_create)
    
    page_start = 1
    
    for i, article_data in enumerate(selected_articles):
        pages_count = random.randint(8, 15)
        
        article = JournalArticle.objects.create(
            issue=issue,
            title_ru=article_data['title_ru'],
            title_en=article_data['title_en'],
            title_kg=article_data['title_kg'],
            authors_ru=article_data['authors_ru'],
            authors_en=article_data['authors_en'],
            authors_kg=article_data['authors_kg'],
            abstract_ru=f"Аннотация к статье '{article_data['title_ru']}'",
            abstract_en=f"Abstract for article '{article_data['title_en']}'",
            abstract_kg=f"'{article_data['title_kg']}' макаласынын аннотациясы",
            keywords_ru=article_data['keywords'],
            keywords_en=article_data['keywords'],
            keywords_kg=article_data['keywords'],
            pages_start=page_start,
            pages_end=page_start + pages_count - 1,
            doi=f"10.12345/{issue.journal.id}.{issue.year}.{issue.number}.{i+1}",
            received_date=issue.publication_date - timedelta(days=random.randint(30, 90)),
            accepted_date=issue.publication_date - timedelta(days=random.randint(10, 30)),
            published_date=issue.publication_date,
            citations_count=random.randint(0, 25),
            order=i + 1,
            is_open_access=issue.journal.is_open_access,
            is_active=True
        )
        
        page_start += pages_count


if __name__ == '__main__':
    create_journals_data()
