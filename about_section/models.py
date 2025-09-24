from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Partner(models.Model):
    """Model for university partners"""
    
    COLOR_CHOICES = [
        ('from-blue-500 to-indigo-600', 'Blue to Indigo'),
        ('from-purple-500 to-pink-600', 'Purple to Pink'),
        ('from-green-500 to-teal-600', 'Green to Teal'),
        ('from-amber-500 to-orange-600', 'Amber to Orange'),
        ('from-red-500 to-rose-600', 'Red to Rose'),
        ('from-indigo-500 to-blue-600', 'Indigo to Blue'),
        ('from-pink-500 to-rose-600', 'Pink to Rose'),
        ('from-teal-500 to-emerald-600', 'Teal to Emerald'),
        ('from-cyan-500 to-blue-600', 'Cyan to Blue'),
        ('from-yellow-500 to-amber-600', 'Yellow to Amber'),
    ]
    
    GLOW_CHOICES = [
        ('hover:shadow-blue-500/50', 'Blue Glow'),
        ('hover:shadow-purple-500/50', 'Purple Glow'),
        ('hover:shadow-green-500/50', 'Green Glow'),
        ('hover:shadow-amber-500/50', 'Amber Glow'),
        ('hover:shadow-red-500/50', 'Red Glow'),
        ('hover:shadow-indigo-500/50', 'Indigo Glow'),
        ('hover:shadow-pink-500/50', 'Pink Glow'),
        ('hover:shadow-teal-500/50', 'Teal Glow'),
        ('hover:shadow-cyan-500/50', 'Cyan Glow'),
        ('hover:shadow-yellow-500/50', 'Yellow Glow'),
    ]
    
    name = models.CharField(
        max_length=200,
        verbose_name='Название партнера',
        help_text='Название партнера на русском языке'
    )
    
    name_en = models.CharField(
        max_length=200,
        verbose_name='Partner Name (English)',
        help_text='Partner name in English',
        blank=True
    )
    
    name_ky = models.CharField(
        max_length=200,
        verbose_name='Шериктештин аты (Кыргызча)',
        help_text='Partner name in Kyrgyz',
        blank=True
    )
    
    icon = models.CharField(
        max_length=10,
        verbose_name='категория',
        help_text='Эмодзи иконка партнера (например: 🏥, 🌐)',
        default='🤝'
    )
    
    logo = models.ImageField(
        upload_to='partners/logos/',
        verbose_name='Логотип',
        help_text='Логотип партнера (опционально, если не используется иконка)',
        blank=True,
        null=True
    )
    
    website = models.URLField(
        verbose_name='Веб-сайт',
        help_text='Официальный сайт партнера',
        blank=True
    )
    
    # Contact information
    email = models.EmailField(
        verbose_name='Email',
        help_text='Контактный email партнера',
        blank=True
    )
    
    phone = models.CharField(
        max_length=20,
        verbose_name='Телефон',
        help_text='Контактный телефон партнера',
        blank=True
    )
    
    # Location fields
    country = models.CharField(
        max_length=100,
        verbose_name='Страна',
        help_text='Страна расположения партнера',
        default='Кыргызстан'
    )
    
    country_en = models.CharField(
        max_length=100,
        verbose_name='Country (English)',
        help_text='Country name in English',
        blank=True
    )
    
    country_ky = models.CharField(
        max_length=100,
        verbose_name='Өлкө (Кыргызча)',
        help_text='Country name in Kyrgyz',
        blank=True
    )
    
    city = models.CharField(
        max_length=100,
        verbose_name='Город',
        help_text='Город расположения партнера',
        default='Бишкек'
    )
    
    city_en = models.CharField(
        max_length=100,
        verbose_name='City (English)',
        help_text='City name in English',
        blank=True
    )
    
    city_ky = models.CharField(
        max_length=100,
        verbose_name='Шаар (Кыргызча)',
        help_text='City name in Kyrgyz',
        blank=True
    )
    
    address = models.CharField(
        max_length=300,
        verbose_name='Адрес',
        help_text='Полный адрес партнера',
        blank=True
    )
    
    # GPS Coordinates
    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        verbose_name='Широта',
        help_text='GPS координата широты (например: 42.8746)',
        blank=True,
        null=True
    )
    
    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        verbose_name='Долгота',
        help_text='GPS координата долготы (например: 74.5698)',
        blank=True,
        null=True
    )
    
    # Partner type
    PARTNER_TYPE_CHOICES = [
        ('clinical', '🏥 Клинические базы'),
        ('university', '🎓 Университеты'),
        ('organization', '🔬 Организации'),
        ('business', '💼 Бизнес-партнеры'),
        ('academic', '📚 Академические'),
    ]
    
    partner_type = models.CharField(
        max_length=20,
        choices=PARTNER_TYPE_CHOICES,
        default='academic',
        verbose_name='Тип партнера',
        help_text='Категория партнера'
    )
    
    # Partnership details
    established_year = models.PositiveIntegerField(
        verbose_name='Год основания',
        help_text='Год основания организации-партнера',
        blank=True,
        null=True
    )
    
    cooperation_since = models.PositiveIntegerField(
        verbose_name='Сотрудничество с',
        help_text='Год начала сотрудничества',
        blank=True,
        null=True
    )
    
    partnership_areas = models.TextField(
        verbose_name='Области сотрудничества',
        help_text='Области сотрудничества через запятую',
        blank=True
    )
    
    description = models.TextField(
        verbose_name='Описание',
        help_text='Краткое описание партнера и сотрудничества',
        blank=True
    )
    
    description_en = models.TextField(
        verbose_name='Description (English)',
        help_text='Brief description in English',
        blank=True
    )
    
    description_ky = models.TextField(
        verbose_name='Сыпаттама (Кыргызча)',
        help_text='Brief description in Kyrgyz',
        blank=True
    )
    
    color_theme = models.CharField(
        max_length=50,
        choices=COLOR_CHOICES,
        default='from-blue-500 to-indigo-600',
        verbose_name='Цветовая схема',
        help_text='Градиентная цветовая схема для карточки партнера'
    )
    
    glow_effect = models.CharField(
        max_length=50,
        choices=GLOW_CHOICES,
        default='hover:shadow-blue-500/50',
        verbose_name='Эффект свечения',
        help_text='Эффект свечения при наведении'
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активен',
        help_text='Отображать партнера на сайте'
    )
    
    order = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(999)],
        verbose_name='Порядок отображения',
        help_text='Порядок отображения на сайте (0 - первый)'
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    
    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
        ordering = ['order', 'name']
        
    def __str__(self):
        return self.name
    
    def get_display_name(self, language='ru'):
        """Get partner name in specified language"""
        if language == 'en' and self.name_en:
            return self.name_en
        elif language == 'ky' and self.name_ky:
            return self.name_ky
        return self.name
    
    def get_display_description(self, language='ru'):
        """Get partner description in specified language"""
        if language == 'en' and self.description_en:
            return self.description_en
        elif language == 'ky' and self.description_ky:
            return self.description_ky
        return self.description
    
    def get_display_country(self, language='ru'):
        """Get country name in specified language"""
        if language == 'en' and self.country_en:
            return self.country_en
        elif language == 'ky' and self.country_ky:
            return self.country_ky
        return self.country
    
    def get_display_city(self, language='ru'):
        """Get city name in specified language"""
        if language == 'en' and self.city_en:
            return self.city_en
        elif language == 'ky' and self.city_ky:
            return self.city_ky
        return self.city


class AboutSection(models.Model):
    """Model for about section content and settings"""
    
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок',
        help_text='Заголовок секции "О нас"'
    )
    
    title_en = models.CharField(
        max_length=200,
        verbose_name='Title (English)',
        help_text='About section title in English',
        blank=True
    )
    
    title_ky = models.CharField(
        max_length=200,
        verbose_name='Аталышы (Кыргызча)',
        help_text='About section title in Kyrgyz',
        blank=True
    )
    
    subtitle = models.CharField(
        max_length=300,
        verbose_name='Подзаголовок',
        help_text='Подзаголовок секции',
        blank=True
    )
    
    subtitle_en = models.CharField(
        max_length=300,
        verbose_name='Subtitle (English)',
        help_text='About section subtitle in English',
        blank=True
    )
    
    subtitle_ky = models.CharField(
        max_length=300,
        verbose_name='Субаталышы (Кыргызча)',
        help_text='About section subtitle in Kyrgyz',
        blank=True
    )
    
    content = models.TextField(
        verbose_name='Содержание',
        help_text='Основной текст секции "О нас"',
        blank=True
    )
    
    content_en = models.TextField(
        verbose_name='Content (English)',
        help_text='About section content in English',
        blank=True
    )
    
    content_ky = models.TextField(
        verbose_name='Мазмуну (Кыргызча)',
        help_text='About section content in Kyrgyz',
        blank=True
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активна',
        help_text='Отображать секцию на сайте'
    )
    
    show_partners = models.BooleanField(
        default=True,
        verbose_name='Показывать партнеров',
        help_text='Отображать список партнеров в секции'
    )
    
    partners_animation_speed = models.FloatField(
        default=0.5,
        validators=[MinValueValidator(0.1), MaxValueValidator(10.0)],
        verbose_name='Скорость анимации партнеров',
        help_text='Скорость прокрутки партнеров (px per frame)'
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    
    class Meta:
        verbose_name = 'Секция "О нас"'
        verbose_name_plural = 'Секции "О нас"'
        
    def __str__(self):
        return self.title
    
    def get_display_title(self, language='ru'):
        """Get title in specified language"""
        if language == 'en' and self.title_en:
            return self.title_en
        elif language == 'ky' and self.title_ky:
            return self.title_ky
        return self.title
    
    def get_display_subtitle(self, language='ru'):
        """Get subtitle in specified language"""
        if language == 'en' and self.subtitle_en:
            return self.subtitle_en
        elif language == 'ky' and self.subtitle_ky:
            return self.subtitle_ky
        return self.subtitle
    
    def get_display_content(self, language='ru'):
        """Get content in specified language"""
        if language == 'en' and self.content_en:
            return self.content_en
        elif language == 'ky' and self.content_ky:
            return self.content_ky
        return self.content
