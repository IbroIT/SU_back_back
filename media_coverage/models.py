from django.db import models
from django.utils import timezone


class MediaCategory(models.Model):
    """Категории медиа-материалов"""
    TV = 'tv'
    NEWSPAPER = 'newspaper'
    ONLINE = 'online'
    RADIO = 'radio'
    MAGAZINE = 'magazine'
    
    CATEGORY_CHOICES = [
        (TV, 'Телевидение'),
        (NEWSPAPER, 'Газеты'),
        (ONLINE, 'Интернет'),
        (RADIO, 'Радио'),
        (MAGAZINE, 'Журналы'),
    ]
    
    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique=True, verbose_name='Тип медиа')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL slug')
    icon = models.CharField(max_length=10, default='📄', verbose_name='Иконка')
    
    # Мультиязычные поля
    name_ru = models.CharField(max_length=100, verbose_name='Название (русский)')
    name_kg = models.CharField(max_length=100, verbose_name='Название (кыргызский)')
    name_en = models.CharField(max_length=100, verbose_name='Название (английский)')
    
    description_ru = models.TextField(blank=True, verbose_name='Описание (русский)')
    description_kg = models.TextField(blank=True, verbose_name='Описание (кыргызский)')
    description_en = models.TextField(blank=True, verbose_name='Описание (английский)')
    
    # Метаданные
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_active = models.BooleanField(default=True, verbose_name='Активно')
    
    class Meta:
        verbose_name = 'Категория медиа'
        verbose_name_plural = 'Категории медиа'
        ordering = ['name']
    
    def __str__(self):
        return self.name_ru or self.get_name_display()


class MediaOutlet(models.Model):
    """Медиа-издания"""
    name = models.CharField(max_length=200, verbose_name='Название издания')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL slug')
    
    # Мультиязычные поля
    name_ru = models.CharField(max_length=200, verbose_name='Название (русский)')
    name_kg = models.CharField(max_length=200, verbose_name='Название (кыргызский)')
    name_en = models.CharField(max_length=200, verbose_name='Название (английский)')
    
    description_ru = models.TextField(blank=True, verbose_name='Описание (русский)')
    description_kg = models.TextField(blank=True, verbose_name='Описание (кыргызский)')
    description_en = models.TextField(blank=True, verbose_name='Описание (английский)')
    
    # Контактная информация
    website = models.URLField(blank=True, null=True, verbose_name='Веб-сайт')
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Телефон')
    
    # Логотип и изображения
    logo = models.ImageField(upload_to='media_outlets/logos/', blank=True, null=True, verbose_name='Логотип')
    logo_url = models.URLField(blank=True, null=True, verbose_name='URL логотипа')
    
    # Категория по умолчанию
    default_category = models.ForeignKey(MediaCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Категория по умолчанию')
    
    # Метаданные
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_active = models.BooleanField(default=True, verbose_name='Активно')
    
    # Статистика
    total_articles = models.PositiveIntegerField(default=0, verbose_name='Всего публикаций')
    
    class Meta:
        verbose_name = 'Медиа-издание'
        verbose_name_plural = 'Медиа-издания'
        ordering = ['name_ru']
    
    def __str__(self):
        return self.name_ru or self.name
    
    @property
    def logo_url_or_default(self):
        """Возвращает URL логотипа или дефолтный URL"""
        if self.logo:
            return self.logo.url
        elif self.logo_url:
            return self.logo_url
        return None


class MediaArticle(models.Model):
    """Основная модель для медиа-публикаций"""
    
    # Мультиязычные текстовые поля
    title_ru = models.CharField(max_length=300, verbose_name='Заголовок (русский)')
    title_kg = models.CharField(max_length=300, verbose_name='Заголовок (кыргызский)')
    title_en = models.CharField(max_length=300, verbose_name='Заголовок (английский)')
    
    slug = models.SlugField(max_length=300, unique=True, verbose_name='URL slug')
    
    description_ru = models.TextField(max_length=1000, verbose_name='Описание (русский)')
    description_kg = models.TextField(max_length=1000, verbose_name='Описание (кыргызский)')
    description_en = models.TextField(max_length=1000, verbose_name='Описание (английский)')
    
    # Опциональное полное содержание
    content_ru = models.TextField(blank=True, verbose_name='Полное содержание (русский)')
    content_kg = models.TextField(blank=True, verbose_name='Полное содержание (кыргызский)')
    content_en = models.TextField(blank=True, verbose_name='Полное содержание (английский)')
    
    # Связи
    category = models.ForeignKey(MediaCategory, on_delete=models.CASCADE, verbose_name='Категория')
    outlet = models.ForeignKey(MediaOutlet, on_delete=models.CASCADE, verbose_name='Издание')
    
    # Изображения
    image = models.ImageField(upload_to='media_coverage/images/', blank=True, null=True, verbose_name='Изображение')
    image_url = models.URLField(blank=True, null=True, verbose_name='URL изображения')
    
    # Ссылки
    original_url = models.URLField(verbose_name='Ссылка на оригинал')
    archive_url = models.URLField(blank=True, null=True, verbose_name='Архивная ссылка')
    official_site_url = models.URLField(blank=True, null=True, verbose_name='Ссылка на официальный сайт')
    
    # Автор/журналист
    author_ru = models.CharField(max_length=200, blank=True, verbose_name='Автор (русский)')
    author_kg = models.CharField(max_length=200, blank=True, verbose_name='Автор (кыргызский)')
    author_en = models.CharField(max_length=200, blank=True, verbose_name='Автор (английский)')
    
    journalist_name = models.CharField(max_length=200, blank=True, verbose_name='Имя журналиста')
    journalist_email = models.EmailField(blank=True, null=True, verbose_name='Email журналиста')
    
    # Временные поля
    publication_date = models.DateField(verbose_name='Дата публикации')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    # Статус и модерация
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    is_featured = models.BooleanField(default=False, verbose_name='Рекомендуемое')
    is_verified = models.BooleanField(default=False, verbose_name='Проверено')
    
    # Статистика и рейтинг
    views_count = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')
    importance_score = models.PositiveIntegerField(
        default=1, 
        help_text='Оценка важности от 1 до 10',
        verbose_name='Оценка важности'
    )
    
    # Дополнительные метаданные
    reach_estimate = models.PositiveIntegerField(blank=True, null=True, verbose_name='Оценочный охват')
    sentiment = models.CharField(
        max_length=20,
        choices=[
            ('positive', 'Позитивное'),
            ('neutral', 'Нейтральное'),
            ('negative', 'Негативное')
        ],
        default='neutral',
        verbose_name='Тональность'
    )
    
    # Теги и ключевые слова
    keywords = models.TextField(blank=True, help_text='Ключевые слова через запятую', verbose_name='Ключевые слова')
    
    class Meta:
        verbose_name = 'Медиа-публикация'
        verbose_name_plural = 'Медиа-публикации'
        ordering = ['-publication_date', '-created_at']
        unique_together = ['outlet', 'slug']
    
    def __str__(self):
        return f"{self.title_ru} - {self.outlet.name_ru}"
    
    @property
    def image_url_or_default(self):
        """Возвращает URL изображения или дефолтный URL"""
        if self.image:
            return self.image.url
        elif self.image_url:
            return self.image_url
        return None
    
    def save(self, *args, **kwargs):
        # Обновляем счетчик статей у издания
        is_new = self.pk is None
        super().save(*args, **kwargs)
        
        if is_new and self.is_published:
            self.outlet.total_articles += 1
            self.outlet.save(update_fields=['total_articles'])
    
    def delete(self, *args, **kwargs):
        # Уменьшаем счетчик статей у издания
        if self.is_published:
            self.outlet.total_articles = max(0, self.outlet.total_articles - 1)
            self.outlet.save(update_fields=['total_articles'])
        super().delete(*args, **kwargs)


class MediaTag(models.Model):
    """Теги для медиа-публикаций"""
    name_ru = models.CharField(max_length=50, verbose_name='Название тега (русский)')
    name_kg = models.CharField(max_length=50, verbose_name='Название тега (кыргызский)')
    name_en = models.CharField(max_length=50, verbose_name='Название тега (английский)')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL slug')
    color = models.CharField(max_length=7, default='#3B82F6', verbose_name='Цвет (hex)')
    
    # Метаданные
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    usage_count = models.PositiveIntegerField(default=0, verbose_name='Количество использований')
    
    class Meta:
        verbose_name = 'Тег медиа-публикации'
        verbose_name_plural = 'Теги медиа-публикаций'
        ordering = ['name_ru']
    
    def __str__(self):
        return self.name_ru


class MediaArticleTag(models.Model):
    """Связь между медиа-публикациями и тегами"""
    article = models.ForeignKey(MediaArticle, on_delete=models.CASCADE, related_name='tags')
    tag = models.ForeignKey(MediaTag, on_delete=models.CASCADE, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    
    class Meta:
        unique_together = ['article', 'tag']
        verbose_name = 'Связь публикации с тегом'
        verbose_name_plural = 'Связи публикаций с тегами'
    
    def save(self, *args, **kwargs):
        # Увеличиваем счетчик использования тега
        is_new = self.pk is None
        super().save(*args, **kwargs)
        
        if is_new:
            self.tag.usage_count += 1
            self.tag.save(update_fields=['usage_count'])
    
    def delete(self, *args, **kwargs):
        # Уменьшаем счетчик использования тега
        self.tag.usage_count = max(0, self.tag.usage_count - 1)
        self.tag.save(update_fields=['usage_count'])
        super().delete(*args, **kwargs)


class MediaView(models.Model):
    """Модель для отслеживания просмотров медиа-публикаций"""
    article = models.ForeignKey(MediaArticle, on_delete=models.CASCADE, related_name='article_views')
    ip_address = models.GenericIPAddressField(verbose_name='IP адрес')
    user_agent = models.TextField(blank=True, verbose_name='User Agent')
    viewed_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата просмотра')
    
    class Meta:
        verbose_name = 'Просмотр медиа-публикации'
        verbose_name_plural = 'Просмотры медиа-публикаций'
        unique_together = ['article', 'ip_address']  # Один просмотр с одного IP


class MediaStatistics(models.Model):
    """Агрегированная статистика по медиа-публикациям"""
    date = models.DateField(verbose_name='Дата')
    
    # Счетчики по категориям
    tv_articles = models.PositiveIntegerField(default=0, verbose_name='ТВ сюжеты')
    newspaper_articles = models.PositiveIntegerField(default=0, verbose_name='Статьи в прессе')
    online_articles = models.PositiveIntegerField(default=0, verbose_name='Онлайн публикации')
    radio_articles = models.PositiveIntegerField(default=0, verbose_name='Радио интервью')
    magazine_articles = models.PositiveIntegerField(default=0, verbose_name='Журнальные статьи')
    
    # Общие показатели
    total_articles = models.PositiveIntegerField(default=0, verbose_name='Всего публикаций')
    total_views = models.PositiveIntegerField(default=0, verbose_name='Всего просмотров')
    total_reach = models.PositiveIntegerField(default=0, verbose_name='Общий охват')
    
    # Анализ тональности
    positive_articles = models.PositiveIntegerField(default=0, verbose_name='Позитивные публикации')
    neutral_articles = models.PositiveIntegerField(default=0, verbose_name='Нейтральные публикации')
    negative_articles = models.PositiveIntegerField(default=0, verbose_name='Негативные публикации')
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    class Meta:
        verbose_name = 'Статистика медиа'
        verbose_name_plural = 'Статистика медиа'
        unique_together = ['date']
        ordering = ['-date']
    
    def __str__(self):
        return f"Статистика за {self.date}: {self.total_articles} публикаций"
