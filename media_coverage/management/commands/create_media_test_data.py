from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime, timedelta
import random
from media_coverage.models import (
    MediaCategory, MediaOutlet, MediaArticle, 
    MediaTag, MediaArticleTag, MediaStatistics
)


class Command(BaseCommand):
    help = 'Создает тестовые данные для медиа-покрытия'

    def add_arguments(self, parser):
        parser.add_argument(
            '--articles',
            type=int,
            default=50,
            help='Количество статей для создания (по умолчанию: 50)',
        )

    def handle(self, *args, **options):
        self.stdout.write('Создание тестовых данных для медиа-покрытия...')
        
        # Создаем категории
        self.create_categories()
        
        # Создаем медиа-издания
        self.create_outlets()
        
        # Создаем теги
        self.create_tags()
        
        # Создаем медиа-публикации
        self.create_articles(options['articles'])
        
        # Создаем статистику
        self.create_statistics()
        
        self.stdout.write(
            self.style.SUCCESS('✅ Тестовые данные для медиа-покрытия созданы успешно!')
        )

    def create_categories(self):
        """Создание категорий медиа"""
        categories_data = [
            {
                'name': MediaCategory.TV,
                'slug': 'tv',
                'icon': '📺',
                'name_ru': 'Телевидение',
                'name_kg': 'Телевидение',
                'name_en': 'Television',
                'description_ru': 'Телевизионные сюжеты и интервью',
                'description_kg': 'Телевизиялык сюжеттер жана интервьюлар',
                'description_en': 'Television stories and interviews'
            },
            {
                'name': MediaCategory.NEWSPAPER,
                'slug': 'newspaper',
                'icon': '📰',
                'name_ru': 'Газеты',
                'name_kg': 'Гезиттер',
                'name_en': 'Newspapers',
                'description_ru': 'Публикации в печатных изданиях',
                'description_kg': 'Басылма басмаларда чыккан макалалар',
                'description_en': 'Print media publications'
            },
            {
                'name': MediaCategory.ONLINE,
                'slug': 'online',
                'icon': '💻',
                'name_ru': 'Интернет',
                'name_kg': 'Интернет',
                'name_en': 'Online',
                'description_ru': 'Онлайн-публикации и новостные сайты',
                'description_kg': 'Онлайн басылмалар жана жаңылык сайттары',
                'description_en': 'Online publications and news websites'
            },
            {
                'name': MediaCategory.RADIO,
                'slug': 'radio',
                'icon': '📻',
                'name_ru': 'Радио',
                'name_kg': 'Радио',
                'name_en': 'Radio',
                'description_ru': 'Радиоинтервью и передачи',
                'description_kg': 'Радио интервьюлар жана программалар',
                'description_en': 'Radio interviews and programs'
            },
            {
                'name': MediaCategory.MAGAZINE,
                'slug': 'magazine',
                'icon': '📖',
                'name_ru': 'Журналы',
                'name_kg': 'Журналдар',
                'name_en': 'Magazines',
                'description_ru': 'Публикации в журналах',
                'description_kg': 'Журналдарда чыккан макалалар',
                'description_en': 'Magazine publications'
            }
        ]
        
        for cat_data in categories_data:
            category, created = MediaCategory.objects.get_or_create(
                name=cat_data['name'],
                defaults=cat_data
            )
            if created:
                self.stdout.write(f'Создана категория: {category.name_ru}')

    def create_outlets(self):
        """Создание медиа-изданий"""
        outlets_data = [
            {
                'name': 'ktrk',
                'slug': 'ktrk',
                'name_ru': 'КТРК',
                'name_kg': 'КТРК',
                'name_en': 'KTRK',
                'website': 'https://ktrk.kg',
                'default_category': MediaCategory.objects.get(name=MediaCategory.TV)
            },
            {
                'name': 'akipress',
                'slug': 'akipress',
                'name_ru': 'AKIpress',
                'name_kg': 'AKIpress',
                'name_en': 'AKIpress',
                'website': 'https://akipress.kg',
                'default_category': MediaCategory.objects.get(name=MediaCategory.ONLINE)
            },
            {
                'name': 'slovo-kg',
                'slug': 'slovo-kg',
                'name_ru': 'Слово Кыргызстана',
                'name_kg': 'Кыргызстан Сөзү',
                'name_en': 'Slovo Kyrgyzstana',
                'website': 'https://slovo.kg',
                'default_category': MediaCategory.objects.get(name=MediaCategory.NEWSPAPER)
            },
            {
                'name': 'kabar',
                'slug': 'kabar',
                'name_ru': 'Кабар',
                'name_kg': 'Кабар',
                'name_en': 'Kabar',
                'website': 'https://kabar.kg',
                'default_category': MediaCategory.objects.get(name=MediaCategory.ONLINE)
            },
            {
                'name': 'vesti-kg',
                'slug': 'vesti-kg',
                'name_ru': 'Вести.kg',
                'name_kg': 'Вести.kg',
                'name_en': 'Vesti.kg',
                'website': 'https://vesti.kg',
                'default_category': MediaCategory.objects.get(name=MediaCategory.ONLINE)
            },
            {
                'name': 'delo-kg',
                'slug': 'delo-kg',
                'name_ru': 'Дело №',
                'name_kg': 'Дело №',
                'name_en': 'Delo №',
                'website': 'https://delo.kg',
                'default_category': MediaCategory.objects.get(name=MediaCategory.NEWSPAPER)
            }
        ]
        
        for outlet_data in outlets_data:
            outlet, created = MediaOutlet.objects.get_or_create(
                name=outlet_data['name'],
                defaults=outlet_data
            )
            if created:
                self.stdout.write(f'Создано издание: {outlet.name_ru}')

    def create_tags(self):
        """Создание тегов"""
        tags_data = [
            {
                'slug': 'medicina',
                'name_ru': 'Медицина',
                'name_kg': 'Медицина',
                'name_en': 'Medicine',
                'color': '#E53E3E'
            },
            {
                'slug': 'obrazovanie',
                'name_ru': 'Образование',
                'name_kg': 'Билим берүү',
                'name_en': 'Education',
                'color': '#3182CE'
            },
            {
                'slug': 'nauka',
                'name_ru': 'Наука',
                'name_kg': 'Илим',
                'name_en': 'Science',
                'color': '#805AD5'
            },
            {
                'slug': 'studenty',
                'name_ru': 'Студенты',
                'name_kg': 'Студенттер',
                'name_en': 'Students',
                'color': '#38A169'
            },
            {
                'slug': 'universitet',
                'name_ru': 'Университет',
                'name_kg': 'Университет',
                'name_en': 'University',
                'color': '#D69E2E'
            },
            {
                'slug': 'praktika',
                'name_ru': 'Практика',
                'name_kg': 'Практика',
                'name_en': 'Practice',
                'color': '#319795'
            },
            {
                'slug': 'mezhdunarodnoye-sotrudnichestvo',
                'name_ru': 'Международное сотрудничество',
                'name_kg': 'Эл аралык кызматташуу',
                'name_en': 'International Cooperation',
                'color': '#E53E3E'
            },
            {
                'slug': 'konferentsii',
                'name_ru': 'Конференции',
                'name_kg': 'Конференциялар',
                'name_en': 'Conferences',
                'color': '#9F7AEA'
            }
        ]
        
        for tag_data in tags_data:
            tag, created = MediaTag.objects.get_or_create(
                slug=tag_data['slug'],
                defaults=tag_data
            )
            if created:
                self.stdout.write(f'Создан тег: {tag.name_ru}')

    def create_articles(self, count=50):
        """Создание медиа-публикаций"""
        categories = list(MediaCategory.objects.all())
        outlets = list(MediaOutlet.objects.all())
        tags = list(MediaTag.objects.all())
        
        sentiments = ['positive', 'neutral', 'negative']
        
        articles_data = [
            {
                'title_base': 'Салымбековский университет проводит медицинскую конференцию',
                'title_kg': 'Салымбек университети медициналык конференция өткөрөт',
                'title_en': 'Salymbekov University holds medical conference',
                'content_base': 'В Салымбековском университете прошла крупная медицинская конференция, посвященная современным методам лечения.',
            },
            {
                'title_base': 'Студенты СУ завоевали первое место в медицинской олимпиаде',
                'title_kg': 'СУ студенттери медициналык олимпиадада биринчи орунду ээледи',
                'title_en': 'SU students won first place in medical olympiad',
                'content_base': 'Команда студентов Салымбековского университета показала отличные результаты на республиканской олимпиаде.',
            },
            {
                'title_base': 'Новое международное партнерство СУ с европейскими вузами',
                'title_kg': 'СУнун европалык жогорку окуу жайлары менен жаңы эл аралык өнөктөштүгү',
                'title_en': 'New international partnership of SU with European universities',
                'content_base': 'Салымбековский университет подписал соглашение о сотрудничестве с ведущими медицинскими вузами Европы.',
            },
            {
                'title_base': 'Открытие нового медицинского центра при СУ',
                'title_kg': 'СУдагы жаңы медициналык борборунун ачылышы',
                'title_en': 'Opening of a new medical center at SU',
                'content_base': 'В Салымбековском университете открылся современный медицинский центр с новейшим оборудованием.',
            },
            {
                'title_base': 'Выпускники СУ успешно работают в ведущих клиниках',
                'title_kg': 'СУ бүтүрүүчүлөрү жетектүү клиникаларда ийгиликтүү иштеп жатышат',
                'title_en': 'SU graduates successfully work in leading clinics',
                'content_base': 'Выпускники Салымбековского университета трудоустроены в лучших медицинских учреждениях страны.',
            }
        ]
        
        for i in range(count):
            # Выбираем случайные данные
            template = random.choice(articles_data)
            category = random.choice(categories)
            outlet = random.choice(outlets)
            sentiment = random.choice(sentiments)
            
            # Генерируем дату в пределах последних 6 месяцев
            days_ago = random.randint(0, 180)
            pub_date = timezone.now().date() - timedelta(days=days_ago)
            
            article_data = {
                'title_ru': f"{template['title_base']} - {i+1}",
                'title_kg': f"{template['title_kg']} - {i+1}",
                'title_en': f"{template['title_en']} - {i+1}",
                'slug': f"media-article-{i+1}",
                'description_ru': f"Краткое описание медиа-публикации {i+1}. {template['content_base'][:100]}...",
                'description_kg': f"Медиа басылманын {i+1} кыскача баяндамасы...",
                'description_en': f"Brief description of media publication {i+1}...",
                'content_ru': f"Полное содержание публикации {i+1}. {template['content_base']} " * 3,
                'content_kg': f"Басылманын {i+1} толук мазмуну...",
                'content_en': f"Full content of publication {i+1}...",
                'category': category,
                'outlet': outlet,
                'original_url': f"https://{outlet.website.replace('https://', '')}/news/article-{i+1}",
                'official_site_url': f"https://salymbekov-university.edu.kg/news/article-{i+1}" if random.choice([True, False, False]) else None,
                'publication_date': pub_date,
                'importance_score': random.randint(1, 10),
                'sentiment': sentiment,
                'views_count': random.randint(0, 1000),
                'is_published': True,
                'is_featured': random.choice([True, False]) if i < 10 else False,
                'is_verified': random.choice([True, False]),
                'reach_estimate': random.randint(1000, 50000),
                'keywords': 'Салымбековский университет, медицина, образование, студенты',
                'journalist_name': random.choice([
                    'Айгуль Асанова', 'Бакыт Токтогулов', 'Виктория Петрова',
                    'Данияр Сманов', 'Елена Иванова', 'Жамила Омурбекова'
                ]),
                'author_ru': random.choice([
                    'Корреспондент', 'Специальный корреспондент', 'Редакция'
                ]),
                'author_kg': random.choice([
                    'Корреспондент', 'Атайын корреспондент', 'Редакция'
                ]),
                'author_en': random.choice([
                    'Correspondent', 'Special Correspondent', 'Editorial'
                ])
            }
            
            article, created = MediaArticle.objects.get_or_create(
                slug=article_data['slug'],
                defaults=article_data
            )
            
            if created:
                # Добавляем случайные теги
                article_tags = random.sample(tags, random.randint(1, 3))
                for tag in article_tags:
                    MediaArticleTag.objects.get_or_create(
                        article=article,
                        tag=tag
                    )
                
                self.stdout.write(f'Создана статья: {article.title_ru}')

    def create_statistics(self):
        """Создание статистики"""
        # Создаем статистику за последние 30 дней
        for days_ago in range(30):
            date = timezone.now().date() - timedelta(days=days_ago)
            
            # Получаем данные за этот день
            articles_on_date = MediaArticle.objects.filter(
                publication_date=date,
                is_published=True
            )
            
            if articles_on_date.exists():
                total_articles = articles_on_date.count()
                
                # Подсчет по категориям
                tv_articles = articles_on_date.filter(category__name=MediaCategory.TV).count()
                newspaper_articles = articles_on_date.filter(category__name=MediaCategory.NEWSPAPER).count()
                online_articles = articles_on_date.filter(category__name=MediaCategory.ONLINE).count()
                radio_articles = articles_on_date.filter(category__name=MediaCategory.RADIO).count()
                magazine_articles = articles_on_date.filter(category__name=MediaCategory.MAGAZINE).count()
                
                # Подсчет по тональности
                positive_articles = articles_on_date.filter(sentiment='positive').count()
                neutral_articles = articles_on_date.filter(sentiment='neutral').count()
                negative_articles = articles_on_date.filter(sentiment='negative').count()
                
                # Общие показатели
                total_views = sum([article.views_count for article in articles_on_date])
                total_reach = sum([article.reach_estimate or 0 for article in articles_on_date])
                
                # Создаем или обновляем статистику
                stats, created = MediaStatistics.objects.get_or_create(
                    date=date,
                    defaults={
                        'tv_articles': tv_articles,
                        'newspaper_articles': newspaper_articles,
                        'online_articles': online_articles,
                        'radio_articles': radio_articles,
                        'magazine_articles': magazine_articles,
                        'total_articles': total_articles,
                        'total_views': total_views,
                        'total_reach': total_reach,
                        'positive_articles': positive_articles,
                        'neutral_articles': neutral_articles,
                        'negative_articles': negative_articles
                    }
                )
                
                if created:
                    self.stdout.write(f'Создана статистика за {date}: {total_articles} статей')
