from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import json


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


class Founder(models.Model):
    """Model for university founders"""
    
    name_ru = models.CharField(
        max_length=200,
        verbose_name='Имя (Русский)',
        help_text='Полное имя основателя на русском языке'
    )
    
    name_en = models.CharField(
        max_length=200,
        verbose_name='Name (English)',
        help_text='Full name in English',
        blank=True
    )
    
    name_ky = models.CharField(
        max_length=200,
        verbose_name='Аты (Кыргызча)',
        help_text='Full name in Kyrgyz',
        blank=True
    )
    
    position_ru = models.CharField(
        max_length=300,
        verbose_name='Должность (Русский)',
        help_text='Должность основателя на русском языке'
    )
    
    position_en = models.CharField(
        max_length=300,
        verbose_name='Position (English)',
        help_text='Position in English',
        blank=True
    )
    
    position_ky = models.CharField(
        max_length=300,
        verbose_name='Кызматы (Кыргызча)',
        help_text='Position in Kyrgyz',
        blank=True
    )
    
    years = models.CharField(
        max_length=50,
        verbose_name='Период деятельности',
        help_text='Например: 1995-2005',
        blank=True
    )
    
    image = models.ImageField(
        upload_to='founders/',
        verbose_name='Фотография',
        help_text='Фотография основателя',
        blank=True,
        null=True
    )
    
    description_ru = models.TextField(
        verbose_name='Описание (Русский)',
        help_text='Биография основателя на русском языке'
    )
    
    description_en = models.TextField(
        verbose_name='Description (English)',
        help_text='Biography in English',
        blank=True
    )
    
    description_ky = models.TextField(
        verbose_name='Сүрөттөмө (Кыргызча)',
        help_text='Biography in Kyrgyz',
        blank=True
    )
    
    achievements = models.JSONField(
        default=list,
        verbose_name='Достижения',
        help_text='JSON структура с достижениями на разных языках',
        blank=True
    )
    
    order = models.PositiveIntegerField(
        default=1,
        verbose_name='Порядок сортировки',
        help_text='Порядок отображения основателей'
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активен',
        help_text='Отображать основателя на сайте'
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
        verbose_name = 'Основатель'
        verbose_name_plural = 'Основатели'
        ordering = ['order', 'name_ru']
        
    def __str__(self):
        return self.name_ru
    
    def get_display_name(self, language='ru'):
        """Get name in specified language"""
        if language == 'en' and self.name_en:
            return self.name_en
        elif language == 'ky' and self.name_ky:
            return self.name_ky
        return self.name_ru
    
    def get_display_position(self, language='ru'):
        """Get position in specified language"""
        if language == 'en' and self.position_en:
            return self.position_en
        elif language == 'ky' and self.position_ky:
            return self.position_ky
        return self.position_ru
    
    def get_display_description(self, language='ru'):
        """Get description in specified language"""
        if language == 'en' and self.description_en:
            return self.description_en
        elif language == 'ky' and self.description_ky:
            return self.description_ky
        return self.description_ru
    
    def get_achievements_for_language(self, language='ru'):
        """Get achievements for specified language"""
        if not self.achievements:
            return []
        
        # If achievements is a list of dictionaries with language keys
        if isinstance(self.achievements, list) and self.achievements:
            if isinstance(self.achievements[0], dict):
                return [
                    achievement.get(f'achievement_{language}', 
                                    achievement.get('achievement_ru', ''))
                    for achievement in self.achievements
                ]
            else:
                # If it's a simple list of strings (legacy format)
                return self.achievements
        
        return []


class FounderAchievement(models.Model):
    """Model for individual founder achievements"""
    
    founder = models.ForeignKey(
        Founder,
        on_delete=models.CASCADE,
        related_name='achievement_set',
        verbose_name='Основатель'
    )
    
    achievement_ru = models.TextField(
        verbose_name='Достижение (Русский)',
        help_text='Описание достижения на русском языке'
    )
    
    achievement_en = models.TextField(
        verbose_name='Achievement (English)',
        help_text='Achievement description in English',
        blank=True
    )
    
    achievement_ky = models.TextField(
        verbose_name='Жетишкендик (Кыргызча)',
        help_text='Achievement description in Kyrgyz',
        blank=True
    )
    
    order = models.PositiveIntegerField(
        default=1,
        verbose_name='Порядок сортировки'
    )
    
    class Meta:
        verbose_name = 'Достижение основателя'
        verbose_name_plural = 'Достижения основателей'
        ordering = ['order']
    
    def __str__(self):
        return f"{self.founder.name_ru} - {self.achievement_ru[:50]}..."
    
    def get_display_achievement(self, language='ru'):
        """Get achievement in specified language"""
        if language == 'en' and self.achievement_en:
            return self.achievement_en
        elif language == 'ky' and self.achievement_ky:
            return self.achievement_ky
        return self.achievement_ru


class OrganizationStructure(models.Model):
    """Model for university organizational structure"""
    
    STRUCTURE_TYPES = [
        ('leadership', 'Руководство'),
        ('faculties', 'Факультеты'),
        ('administrative', 'Административные подразделения'),
        ('support', 'Вспомогательные подразделения'),
    ]
    
    name_ru = models.CharField(
        max_length=200,
        verbose_name='Название (Русский)',
        help_text='Название подразделения на русском языке'
    )
    
    name_en = models.CharField(
        max_length=200,
        verbose_name='Name (English)',
        help_text='Department name in English',
        blank=True
    )
    
    name_ky = models.CharField(
        max_length=200,
        verbose_name='Аталышы (Кыргызча)',
        help_text='Department name in Kyrgyz',
        blank=True
    )
    
    head_name_ru = models.CharField(
        max_length=200,
        verbose_name='Руководитель (Русский)',
        help_text='ФИО руководителя на русском языке',
        blank=True
    )
    
    head_name_en = models.CharField(
        max_length=200,
        verbose_name='Head (English)',
        help_text='Head name in English',
        blank=True
    )
    
    head_name_ky = models.CharField(
        max_length=200,
        verbose_name='Башчы (Кыргызча)',
        help_text='Head name in Kyrgyz',
        blank=True
    )
    
    structure_type = models.CharField(
        max_length=20,
        choices=STRUCTURE_TYPES,
        verbose_name='Тип подразделения',
        help_text='Категория организационной структуры'
    )
    
    phone = models.CharField(
        max_length=50,
        verbose_name='Телефон',
        blank=True
    )
    
    email = models.EmailField(
        verbose_name='Email',
        blank=True
    )
    
    icon = models.CharField(
        max_length=10,
        verbose_name='Иконка',
        help_text='Emoji иконка для отображения',
        default='🏢'
    )
    
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Родительское подразделение'
    )
    
    order = models.PositiveIntegerField(
        default=1,
        verbose_name='Порядок сортировки'
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активно',
        help_text='Отображать подразделение на сайте'
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
        verbose_name = 'Организационная структура'
        verbose_name_plural = 'Организационная структура'
        ordering = ['structure_type', 'order', 'name_ru']
        
    def __str__(self):
        return self.name_ru
    
    def get_display_name(self, language='ru'):
        """Get name in specified language"""
        if language == 'en' and self.name_en:
            return self.name_en
        elif language == 'ky' and self.name_ky:
            return self.name_ky
        return self.name_ru
    
    def get_display_head_name(self, language='ru'):
        """Get head name in specified language"""
        if language == 'en' and self.head_name_en:
            return self.head_name_en
        elif language == 'ky' and self.head_name_ky:
            return self.head_name_ky
        return self.head_name_ru


class Achievement(models.Model):
    """Model for university achievements"""
    
    CATEGORY_CHOICES = [
        ('education', 'Образование'),
        ('science', 'Наука'),
        ('international', 'Международное сотрудничество'),
        ('infrastructure', 'Инфраструктура'),
        ('awards', 'Награды'),
        ('research', 'Исследования'),
        ('innovation', 'Инновации'),
    ]
    
    ICON_COLOR_CHOICES = [
        ('bg-yellow-500', 'Желтый'),
        ('bg-red-500', 'Красный'),
        ('bg-blue-500', 'Синий'),
        ('bg-purple-500', 'Фиолетовый'),
        ('bg-green-500', 'Зеленый'),
        ('bg-emerald-500', 'Изумрудный'),
        ('bg-indigo-500', 'Индиго'),
        ('bg-pink-500', 'Розовый'),
        ('bg-orange-500', 'Оранжевый'),
        ('bg-teal-500', 'Бирюзовый'),
    ]
    
    title_ru = models.CharField(
        max_length=300,
        verbose_name='Заголовок (Русский)',
        help_text='Название достижения на русском языке'
    )
    
    title_en = models.CharField(
        max_length=300,
        verbose_name='Title (English)',
        help_text='Achievement title in English',
        blank=True
    )
    
    title_ky = models.CharField(
        max_length=300,
        verbose_name='Аталышы (Кыргызча)',
        help_text='Achievement title in Kyrgyz',
        blank=True
    )
    
    description_ru = models.TextField(
        verbose_name='Описание (Русский)',
        help_text='Подробное описание достижения на русском языке'
    )
    
    description_en = models.TextField(
        verbose_name='Description (English)',
        help_text='Achievement description in English',
        blank=True
    )
    
    description_ky = models.TextField(
        verbose_name='Сүрөттөмө (Кыргызча)',
        help_text='Achievement description in Kyrgyz',
        blank=True
    )
    
    year = models.PositiveIntegerField(
        verbose_name='Год',
        help_text='Год получения достижения'
    )
    
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        verbose_name='Категория',
        help_text='Категория достижения'
    )
    
    icon = models.CharField(
        max_length=10,
        verbose_name='Иконка',
        help_text='Emoji иконка для отображения',
        default='🏆'
    )
    
    icon_color = models.CharField(
        max_length=20,
        choices=ICON_COLOR_CHOICES,
        verbose_name='Цвет иконки',
        help_text='CSS класс цвета иконки',
        default='bg-yellow-500'
    )
    
    featured = models.BooleanField(
        default=False,
        verbose_name='Рекомендуемое',
        help_text='Отображать как основное достижение'
    )
    
    order = models.PositiveIntegerField(
        default=1,
        verbose_name='Порядок сортировки'
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активно',
        help_text='Отображать достижение на сайте'
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
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'
        ordering = ['-featured', '-year', 'order']
        
    def __str__(self):
        return f"{self.title_ru} ({self.year})"
    
    def get_display_title(self, language='ru'):
        """Get title in specified language"""
        if language == 'en' and self.title_en:
            return self.title_en
        elif language == 'ky' and self.title_ky:
            return self.title_ky
        return self.title_ru
    
    def get_display_description(self, language='ru'):
        """Get description in specified language"""
        if language == 'en' and self.description_en:
            return self.description_en
        elif language == 'ky' and self.description_ky:
            return self.description_ky
        return self.description_ru


class UniversityStatistic(models.Model):
    """Model for university statistics"""
    
    name_ru = models.CharField(
        max_length=200,
        verbose_name='Название (Русский)',
        help_text='Название статистики на русском языке'
    )
    
    name_en = models.CharField(
        max_length=200,
        verbose_name='Name (English)',
        help_text='Statistic name in English',
        blank=True
    )
    
    name_ky = models.CharField(
        max_length=200,
        verbose_name='Аталышы (Кыргызча)',
        help_text='Statistic name in Kyrgyz',
        blank=True
    )
    
    value = models.CharField(
        max_length=20,
        verbose_name='Значение',
        help_text='Числовое значение статистики'
    )
    
    unit = models.CharField(
        max_length=10,
        verbose_name='Единица измерения',
        help_text='Например: %, +, штук',
        blank=True
    )
    
    icon = models.CharField(
        max_length=10,
        verbose_name='Иконка',
        help_text='Emoji иконка для отображения',
        default='📊'
    )
    
    order = models.PositiveIntegerField(
        default=1,
        verbose_name='Порядок сортировки'
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активна',
        help_text='Отображать статистику на сайте'
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
        verbose_name = 'Статистика университета'
        verbose_name_plural = 'Статистика университета'
        ordering = ['order', 'name_ru']
        
    def __str__(self):
        return f"{self.name_ru}: {self.value}{self.unit}"
    
    def get_display_name(self, language='ru'):
        """Get name in specified language"""
        if language == 'en' and self.name_en:
            return self.name_en
        elif language == 'ky' and self.name_ky:
            return self.name_ky
        return self.name_ru