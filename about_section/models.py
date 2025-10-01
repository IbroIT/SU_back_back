from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import json


class Accreditation(models.Model):
    """Model for university accreditations"""
    
    TYPE_CHOICES = [
        ('government', 'Государственный'),
        ('international', 'Международный'), 
        ('regional', 'Региональный'),
        ('professional', 'Профессиональный'),
    ]
    
    COLOR_CHOICES = [
        ('from-blue-500 to-blue-600', 'Blue'),
        ('from-green-500 to-green-600', 'Green'),
        ('from-purple-500 to-purple-600', 'Purple'),
        ('from-orange-500 to-orange-600', 'Orange'),
        ('from-teal-500 to-teal-600', 'Teal'),
        ('from-indigo-500 to-indigo-600', 'Indigo'),
    ]
    
    BADGE_COLOR_CHOICES = [
        ('bg-blue-500', 'Blue Badge'),
        ('bg-green-500', 'Green Badge'),
        ('bg-purple-500', 'Purple Badge'),
        ('bg-orange-500', 'Orange Badge'),
        ('bg-teal-500', 'Teal Badge'),
        ('bg-indigo-500', 'Indigo Badge'),
    ]
    
    title = models.CharField(
        max_length=300,
        verbose_name='Название',
        help_text='Название аккредитующей организации'
    )
    
    title_en = models.CharField(
        max_length=300,
        verbose_name='Title (English)',
        help_text='Accreditation title in English',
        blank=True
    )
    
    title_ky = models.CharField(
        max_length=300,
        verbose_name='Аталышы (Кыргызча)',
        help_text='Accreditation title in Kyrgyz',
        blank=True
    )
    
    description = models.TextField(
        verbose_name='Описание',
        help_text='Краткое описание аккредитации'
    )
    
    description_en = models.TextField(
        verbose_name='Description (English)',
        help_text='Accreditation description in English',
        blank=True
    )
    
    description_ky = models.TextField(
        verbose_name='Сыпаттама (Кыргызча)',
        help_text='Accreditation description in Kyrgyz',
        blank=True
    )
    
    full_description = models.TextField(
        verbose_name='Полное описание',
        help_text='Подробное описание аккредитации'
    )
    
    full_description_en = models.TextField(
        verbose_name='Full Description (English)',
        help_text='Full accreditation description in English',
        blank=True
    )
    
    full_description_ky = models.TextField(
        verbose_name='Толук сыпаттама (Кыргызча)',
        help_text='Full accreditation description in Kyrgyz',
        blank=True
    )
    
    logo = models.CharField(
        max_length=10,
        verbose_name='Эмодзи иконка',
        help_text='Эмодзи иконка для аккредитации',
        default='🏛️'
    )
    
    year = models.CharField(
        max_length=10,
        verbose_name='Год получения',
        help_text='Год получения аккредитации'
    )
    
    status = models.CharField(
        max_length=100,
        verbose_name='Статус',
        help_text='Статус аккредитации (Активный, Истекший и т.д.)',
        default='Активный'
    )
    
    status_en = models.CharField(
        max_length=100,
        verbose_name='Status (English)',
        help_text='Accreditation status in English',
        blank=True
    )
    
    status_ky = models.CharField(
        max_length=100,
        verbose_name='Абалы (Кыргызча)',
        help_text='Accreditation status in Kyrgyz',
        blank=True
    )
    
    validity = models.CharField(
        max_length=100,
        verbose_name='Срок действия',
        help_text='Срок действия аккредитации'
    )
    
    validity_en = models.CharField(
        max_length=100,
        verbose_name='Validity (English)',
        help_text='Accreditation validity in English',
        blank=True
    )
    
    validity_ky = models.CharField(
        max_length=100,
        verbose_name='Жарактуулук мөөнөтү (Кыргызча)',
        help_text='Accreditation validity in Kyrgyz',
        blank=True
    )
    
    level = models.CharField(
        max_length=100,
        verbose_name='Уровень',
        help_text='Уровень аккредитации (Международный, Государственный и т.д.)'
    )
    
    level_en = models.CharField(
        max_length=100,
        verbose_name='Level (English)',
        help_text='Accreditation level in English',
        blank=True
    )
    
    level_ky = models.CharField(
        max_length=100,
        verbose_name='Деңгээли (Кыргызча)',
        help_text='Accreditation level in Kyrgyz',
        blank=True
    )
    
    accreditation_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        verbose_name='Тип аккредитации',
        help_text='Тип аккредитации для фильтрации'
    )
    
    benefits = models.JSONField(
        verbose_name='Преимущества',
        help_text='Список преимуществ аккредитации',
        default=list
    )
    
    benefits_en = models.JSONField(
        verbose_name='Benefits (English)',
        help_text='List of benefits in English',
        default=list
    )
    
    benefits_ky = models.JSONField(
        verbose_name='Артыкчылыктары (Кыргызча)',
        help_text='List of benefits in Kyrgyz',
        default=list
    )
    
    color = models.CharField(
        max_length=50,
        choices=COLOR_CHOICES,
        default='from-blue-500 to-blue-600',
        verbose_name='Цветовая схема',
        help_text='Градиентная цветовая схема для карточки'
    )
    
    icon_color = models.CharField(
        max_length=50,
        verbose_name='Цвет иконки',
        help_text='CSS класс для цвета иконки',
        default='text-blue-100'
    )
    
    badge_color = models.CharField(
        max_length=20,
        choices=BADGE_COLOR_CHOICES,
        default='bg-blue-500',
        verbose_name='Цвет индикатора',
        help_text='Цвет индикатора снизу карточки'
    )
    
    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок отображения',
        help_text='Порядок отображения на сайте'
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активен',
        help_text='Отображать аккредитацию на сайте'
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
        verbose_name = 'Аккредитация'
        verbose_name_plural = 'Аккредитации'
        ordering = ['order', 'title']
    
    def __str__(self):
        return self.title
    
    def get_display_title(self, language='ru'):
        """Get title in specified language"""
        if language == 'en' and self.title_en:
            return self.title_en
        elif language == 'ky' and self.title_ky:
            return self.title_ky
        return self.title
    
    def get_display_description(self, language='ru'):
        """Get description in specified language"""
        if language == 'en' and self.description_en:
            return self.description_en
        elif language == 'ky' and self.description_ky:
            return self.description_ky
        return self.description
    
    def get_display_full_description(self, language='ru'):
        """Get full description in specified language"""
        if language == 'en' and self.full_description_en:
            return self.full_description_en
        elif language == 'ky' and self.full_description_ky:
            return self.full_description_ky
        return self.full_description
    
    def get_display_status(self, language='ru'):
        """Get status in specified language"""
        if language == 'en' and self.status_en:
            return self.status_en
        elif language == 'ky' and self.status_ky:
            return self.status_ky
        return self.status
    
    def get_display_validity(self, language='ru'):
        """Get validity in specified language"""
        if language == 'en' and self.validity_en:
            return self.validity_en
        elif language == 'ky' and self.validity_ky:
            return self.validity_ky
        return self.validity
    
    def get_display_level(self, language='ru'):
        """Get level in specified language"""
        if language == 'en' and self.level_en:
            return self.level_en
        elif language == 'ky' and self.level_ky:
            return self.level_ky
        return self.level
    
    def get_display_benefits(self, language='ru'):
        """Get benefits in specified language"""
        if language == 'en' and self.benefits_en:
            return self.benefits_en
        elif language == 'ky' and self.benefits_ky:
            return self.benefits_ky
        return self.benefits


class CouncilType(models.Model):
    """Model for different types of councils/committees"""
    
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Название',
        help_text='Название типа совета/комиссии'
    )
    
    name_en = models.CharField(
        max_length=200,
        verbose_name='Name (English)',
        help_text='Council type name in English',
        blank=True
    )
    
    name_ky = models.CharField(
        max_length=200,
        verbose_name='Аты (Кыргызча)',
        help_text='Council type name in Kyrgyz',
        blank=True
    )
    
    slug = models.SlugField(
        unique=True,
        verbose_name='URL идентификатор',
        help_text='URL идентификатор для навигации'
    )
    
    description = models.TextField(
        verbose_name='Описание',
        help_text='Описание функций и задач совета/комиссии'
    )
    
    description_en = models.TextField(
        verbose_name='Description (English)',
        help_text='Council description in English',
        blank=True
    )
    
    description_ky = models.TextField(
        verbose_name='Сыпаттама (Кыргызча)',
        help_text='Council description in Kyrgyz',
        blank=True
    )
    
    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок отображения',
        help_text='Порядок отображения в навигации'
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активен',
        help_text='Отображать в навигации'
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
        verbose_name = 'Тип совета/комиссии'
        verbose_name_plural = 'Типы советов/комиссий'
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name
    
    def get_display_name(self, language='ru'):
        """Get name in specified language"""
        if language == 'en' and self.name_en:
            return self.name_en
        elif language == 'ky' and self.name_ky:
            return self.name_ky
        return self.name
    
    def get_display_description(self, language='ru'):
        """Get description in specified language"""
        if language == 'en' and self.description_en:
            return self.description_en
        elif language == 'ky' and self.description_ky:
            return self.description_ky
        return self.description


class CouncilMember(models.Model):
    """Model for council/committee members"""
    
    council_type = models.ForeignKey(
        CouncilType,
        on_delete=models.CASCADE,
        related_name='members',
        verbose_name='Тип совета/комиссии'
    )
    
    name = models.CharField(
        max_length=200,
        verbose_name='ФИО',
        help_text='Полное имя члена совета/комиссии'
    )
    
    name_en = models.CharField(
        max_length=200,
        verbose_name='Full Name (English)',
        help_text='Full name in English',
        blank=True
    )
    
    name_ky = models.CharField(
        max_length=200,
        verbose_name='Аты-жөнү (Кыргызча)',
        help_text='Full name in Kyrgyz',
        blank=True
    )
    
    position = models.CharField(
        max_length=300,
        verbose_name='Должность',
        help_text='Должность в совете/комиссии'
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
    
    department = models.CharField(
        max_length=300,
        verbose_name='Подразделение',
        help_text='Подразделение или организация'
    )
    
    department_en = models.CharField(
        max_length=300,
        verbose_name='Department (English)',
        help_text='Department in English',
        blank=True
    )
    
    department_ky = models.CharField(
        max_length=300,
        verbose_name='Бөлүмү (Кыргызча)',
        help_text='Department in Kyrgyz',
        blank=True
    )
    
    bio = models.TextField(
        verbose_name='Биография',
        help_text='Краткая биография и достижения'
    )
    
    bio_en = models.TextField(
        verbose_name='Biography (English)',
        help_text='Biography in English',
        blank=True
    )
    
    bio_ky = models.TextField(
        verbose_name='Өмүр баяны (Кыргызча)',
        help_text='Biography in Kyrgyz',
        blank=True
    )
    
    photo = models.ImageField(
        upload_to='council_members/',
        verbose_name='Фото',
        help_text='Фотография члена совета/комиссии',
        blank=True,
        null=True
    )
    
    email = models.EmailField(
        verbose_name='Email',
        help_text='Электронная почта',
        blank=True
    )
    
    phone = models.CharField(
        max_length=20,
        verbose_name='Телефон',
        help_text='Контактный телефон',
        blank=True
    )
    
    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок отображения',
        help_text='Порядок отображения в списке'
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активен',
        help_text='Отображать в списке'
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
        verbose_name = 'Член совета/комиссии'
        verbose_name_plural = 'Члены советов/комиссий'
        ordering = ['council_type', 'order', 'name']
    
    def __str__(self):
        return f"{self.name} - {self.council_type.name}"
    
    def get_display_name(self, language='ru'):
        """Get name in specified language"""
        if language == 'en' and self.name_en:
            return self.name_en
        elif language == 'ky' and self.name_ky:
            return self.name_ky
        return self.name
    
    def get_display_position(self, language='ru'):
        """Get position in specified language"""
        if language == 'en' and self.position_en:
            return self.position_en
        elif language == 'ky' and self.position_ky:
            return self.position_ky
        return self.position
    
    def get_display_department(self, language='ru'):
        """Get department in specified language"""
        if language == 'en' and self.department_en:
            return self.department_en
        elif language == 'ky' and self.department_ky:
            return self.department_ky
        return self.department
    
    def get_display_bio(self, language='ru'):
        """Get bio in specified language"""
        if language == 'en' and self.bio_en:
            return self.bio_en
        elif language == 'ky' and self.bio_ky:
            return self.bio_ky
        return self.bio


class CouncilDocument(models.Model):
    """Model for council-related documents"""
    
    council_type = models.ForeignKey(
        CouncilType,
        on_delete=models.CASCADE,
        related_name='documents',
        verbose_name='Тип совета/комиссии'
    )
    
    title = models.CharField(
        max_length=300,
        verbose_name='Название документа',
        help_text='Название документа'
    )
    
    title_en = models.CharField(
        max_length=300,
        verbose_name='Title (English)',
        help_text='Document title in English',
        blank=True
    )
    
    title_ky = models.CharField(
        max_length=300,
        verbose_name='Аталышы (Кыргызча)',
        help_text='Document title in Kyrgyz',
        blank=True
    )
    
    file = models.FileField(
        upload_to='council_documents/',
        verbose_name='Файл документа',
        help_text='Файл документа (PDF, DOC, DOCX)'
    )
    
    date = models.DateField(
        verbose_name='Дата документа',
        help_text='Дата создания или публикации документа'
    )
    
    size = models.CharField(
        max_length=20,
        verbose_name='Размер файла',
        help_text='Размер файла (например: 2.5 МБ)',
        blank=True
    )
    
    description = models.TextField(
        verbose_name='Описание',
        help_text='Краткое описание документа',
        blank=True
    )
    
    description_en = models.TextField(
        verbose_name='Description (English)',
        help_text='Document description in English',
        blank=True
    )
    
    description_ky = models.TextField(
        verbose_name='Сыпаттама (Кыргызча)',
        help_text='Document description in Kyrgyz',
        blank=True
    )
    
    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок отображения',
        help_text='Порядок отображения в списке'
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активен',
        help_text='Отображать в списке'
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
        verbose_name = 'Документ совета/комиссии'
        verbose_name_plural = 'Документы советов/комиссий'
        ordering = ['council_type', 'order', '-date']
    
    def __str__(self):
        return f"{self.title} - {self.council_type.name}"
    
    def get_display_title(self, language='ru'):
        """Get title in specified language"""
        if language == 'en' and self.title_en:
            return self.title_en
        elif language == 'ky' and self.title_ky:
            return self.title_ky
        return self.title
    
    def get_display_description(self, language='ru'):
        """Get description in specified language"""
        if language == 'en' and self.description_en:
            return self.description_en
        elif language == 'ky' and self.description_ky:
            return self.description_ky
        return self.description
    
    def save(self, *args, **kwargs):
        """Auto-calculate file size on save"""
        if self.file and not self.size:
            try:
                size_bytes = self.file.size
                if size_bytes < 1024:
                    self.size = f"{size_bytes} B"
                elif size_bytes < 1024 * 1024:
                    self.size = f"{size_bytes / 1024:.1f} KB"
                else:
                    self.size = f"{size_bytes / (1024 * 1024):.1f} MB"
            except:
                pass
        super().save(*args, **kwargs)


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


class UniversityFounder(models.Model):
    """Model for university founders"""
    
    # Name fields (multilingual)
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
    
    # Position fields (multilingual)
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
        verbose_name='Кызмат орду (Кыргызча)',
        help_text='Position in Kyrgyz',
        blank=True
    )
    
    # Years of service
    years_ru = models.CharField(
        max_length=100,
        verbose_name='Годы службы (Русский)',
        help_text='Период работы на русском языке (например: 1995-2010)',
        blank=True
    )
    
    years_en = models.CharField(
        max_length=100,
        verbose_name='Years of Service (English)',
        help_text='Period of service in English',
        blank=True
    )
    
    years_ky = models.CharField(
        max_length=100,
        verbose_name='Кызмат жылдары (Кыргызча)',
        help_text='Service period in Kyrgyz',
        blank=True
    )
    
    # Image
    image = models.ImageField(
        upload_to='founders/',
        verbose_name='Фотография',
        help_text='Фотография основателя',
        blank=True,
        null=True
    )
    
    # Description fields (multilingual)
    description_ru = models.TextField(
        verbose_name='Описание (Русский)',
        help_text='Подробное описание основателя на русском языке'
    )
    
    description_en = models.TextField(
        verbose_name='Description (English)',
        help_text='Detailed description in English',
        blank=True
    )
    
    description_ky = models.TextField(
        verbose_name='Сүрөттөө (Кыргызча)',
        help_text='Detailed description in Kyrgyz',
        blank=True
    )
    
    # Achievements (JSON field for multilingual support)
    achievements_ru = models.JSONField(
        verbose_name='Достижения (Русский)',
        help_text='Список достижений на русском языке (JSON массив)',
        default=list,
        blank=True
    )
    
    achievements_en = models.JSONField(
        verbose_name='Achievements (English)',
        help_text='List of achievements in English (JSON array)',
        default=list,
        blank=True
    )
    
    achievements_ky = models.JSONField(
        verbose_name='Жетишкендиктер (Кыргызча)',
        help_text='List of achievements in Kyrgyz (JSON array)',
        default=list,
        blank=True
    )
    
    # Order for sorting
    order = models.PositiveIntegerField(
        verbose_name='Порядок',
        help_text='Порядок отображения (чем меньше число, тем выше)',
        default=0
    )
    
    # Status
    is_active = models.BooleanField(
        verbose_name='Активен',
        help_text='Отображать основателя на сайте',
        default=True
    )
    
    # Timestamps
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    
    class Meta:
        verbose_name = 'Основатель университета'
        verbose_name_plural = 'Основатели университета'
        ordering = ['order', 'name_ru']
        
    def __str__(self):
        return self.name_ru
    
    def get_name(self, language='ru'):
        """Get name in specified language"""
        if language == 'en' and self.name_en:
            return self.name_en
        elif language == 'ky' and self.name_ky:
            return self.name_ky
        return self.name_ru
    
    def get_position(self, language='ru'):
        """Get position in specified language"""
        if language == 'en' and self.position_en:
            return self.position_en
        elif language == 'ky' and self.position_ky:
            return self.position_ky
        return self.position_ru
    
    def get_years(self, language='ru'):
        """Get years in specified language"""
        if language == 'en' and self.years_en:
            return self.years_en
        elif language == 'ky' and self.years_ky:
            return self.years_ky
        return self.years_ru
    
    def get_description(self, language='ru'):
        """Get description in specified language"""
        if language == 'en' and self.description_en:
            return self.description_en
        elif language == 'ky' and self.description_ky:
            return self.description_ky
        return self.description_ru
    
    def get_achievements(self, language='ru'):
        """Get achievements in specified language"""
        if language == 'en' and self.achievements_en:
            return self.achievements_en
        elif language == 'ky' and self.achievements_ky:
            return self.achievements_ky
        return self.achievements_ru