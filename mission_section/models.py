from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import json


class MissionSection(models.Model):
    """
    Основная модель для секции Mission
    Содержит основную информацию о миссии университета
    """
    
    # Основные поля миссии - Русский язык
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок (RU)',
        help_text='Основной заголовок секции миссии на русском языке'
    )
    
    subtitle = models.TextField(
        verbose_name='Подзаголовок (RU)',
        help_text='Описание под заголовком на русском языке',
        blank=True
    )
    
    mission_text = models.TextField(
        verbose_name='Текст миссии (RU)',
        help_text='Основной текст миссии университета на русском языке'
    )
    
    # Основные поля миссии - Английский язык
    title_en = models.CharField(
        max_length=200,
        verbose_name='Заголовок (EN)',
        help_text='Основной заголовок секции миссии на английском языке',
        blank=True
    )
    
    subtitle_en = models.TextField(
        verbose_name='Подзаголовок (EN)',
        help_text='Описание под заголовком на английском языке',
        blank=True
    )
    
    mission_text_en = models.TextField(
        verbose_name='Текст миссии (EN)',
        help_text='Основной текст миссии университета на английском языке',
        blank=True
    )
    
    # Основные поля миссии - Кыргызский язык
    title_ky = models.CharField(
        max_length=200,
        verbose_name='Заголовок (KY)',
        help_text='Основной заголовок секции миссии на кыргызском языке',
        blank=True
    )
    
    subtitle_ky = models.TextField(
        verbose_name='Подзаголовок (KY)',
        help_text='Описание под заголовком на кыргызском языке',
        blank=True
    )
    
    mission_text_ky = models.TextField(
        verbose_name='Текст миссии (KY)',
        help_text='Основной текст миссии университета на кыргызском языке',
        blank=True
    )
    
    # Видение и подход - Русский язык
    vision_title = models.CharField(
        max_length=200,
        verbose_name='Заголовок видения (RU)',
        default='Наше видение'
    )
    
    vision_text = models.TextField(
        verbose_name='Текст видения (RU)',
        help_text='Описание видения университета на русском языке'
    )
    
    approach_title = models.CharField(
        max_length=200,
        verbose_name='Заголовок подхода (RU)',
        default='Наш подход'
    )
    
    approach_text = models.TextField(
        verbose_name='Текст подхода (RU)',
        help_text='Описание подхода университета на русском языке'
    )
    
    # Видение и подход - Английский язык
    vision_title_en = models.CharField(
        max_length=200,
        verbose_name='Заголовок видения (EN)',
        default='Our Vision',
        blank=True
    )
    
    vision_text_en = models.TextField(
        verbose_name='Текст видения (EN)',
        help_text='Описание видения университета на английском языке',
        blank=True
    )
    
    approach_title_en = models.CharField(
        max_length=200,
        verbose_name='Заголовок подхода (EN)',
        default='Our Approach',
        blank=True
    )
    
    approach_text_en = models.TextField(
        verbose_name='Текст подхода (EN)',
        help_text='Описание подхода университета на английском языке',
        blank=True
    )
    
    # Видение и подход - Кыргызский язык
    vision_title_ky = models.CharField(
        max_length=200,
        verbose_name='Заголовок видения (KY)',
        default='Биздин көрүү',
        blank=True
    )
    
    vision_text_ky = models.TextField(
        verbose_name='Текст видения (KY)',
        help_text='Описание видения университета на кыргызском языке',
        blank=True
    )
    
    approach_title_ky = models.CharField(
        max_length=200,
        verbose_name='Заголовок подхода (KY)',
        default='Биздин мамиле',
        blank=True
    )
    
    approach_text_ky = models.TextField(
        verbose_name='Текст подхода (KY)',
        help_text='Описание подхода университета на кыргызском языке',
        blank=True
    )
    
    # Достижения - Русский язык
    achievements_subtitle = models.TextField(
        verbose_name='Подзаголовок достижений (RU)',
        help_text='Описание под заголовком достижений на русском языке',
        blank=True
    )
    
    impact_title = models.CharField(
        max_length=200,
        verbose_name='Заголовок вклада (RU)',
        default='Наш вклад'
    )
    
    impact_text = models.TextField(
        verbose_name='Текст вклада (RU)',
        help_text='Описание вклада университета на русском языке'
    )
    
    future_title = models.CharField(
        max_length=200,
        verbose_name='Заголовок перспектив (RU)',
        default='Перспективы развития'
    )
    
    future_text = models.TextField(
        verbose_name='Текст перспектив (RU)',
        help_text='Описание перспектив развития на русском языке'
    )
    
    # Достижения - Английский язык
    achievements_subtitle_en = models.TextField(
        verbose_name='Подзаголовок достижений (EN)',
        help_text='Описание под заголовком достижений на английском языке',
        blank=True
    )
    
    impact_title_en = models.CharField(
        max_length=200,
        verbose_name='Заголовок вклада (EN)',
        default='Our Impact',
        blank=True
    )
    
    impact_text_en = models.TextField(
        verbose_name='Текст вклада (EN)',
        help_text='Описание вклада университета на английском языке',
        blank=True
    )
    
    future_title_en = models.CharField(
        max_length=200,
        verbose_name='Заголовок перспектив (EN)',
        default='Future Prospects',
        blank=True
    )
    
    future_text_en = models.TextField(
        verbose_name='Текст перспектив (EN)',
        help_text='Описание перспектив развития на английском языке',
        blank=True
    )
    
    # Достижения - Кыргызский язык
    achievements_subtitle_ky = models.TextField(
        verbose_name='Подзаголовок достижений (KY)',
        help_text='Описание под заголовком достижений на кыргызском языке',
        blank=True
    )
    
    impact_title_ky = models.CharField(
        max_length=200,
        verbose_name='Заголовок вклада (KY)',
        default='Биздин салымыбыз',
        blank=True
    )
    
    impact_text_ky = models.TextField(
        verbose_name='Текст вклада (KY)',
        help_text='Описание вклада университета на кыргызском языке',
        blank=True
    )
    
    future_title_ky = models.CharField(
        max_length=200,
        verbose_name='Заголовок перспектив (KY)',
        default='Өнүгүү келечектери',
        blank=True
    )
    
    future_text_ky = models.TextField(
        verbose_name='Текст перспектив (KY)',
        help_text='Описание перспектив развития на кыргызском языке',
        blank=True
    )
    
    # Метаданные
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активно',
        help_text='Отображать на сайте'
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    class Meta:
        verbose_name = 'Секция Миссии'
        verbose_name_plural = 'Секции Миссии'
        ordering = ['-created_at']
    
    def get_display_title(self, language='ru'):
        """Get title based on language"""
        if language == 'en':
            return self.title_en or self.title
        elif language == 'kg':
            return self.title_ky or self.title
        return self.title
    
    def get_display_subtitle(self, language='ru'):
        """Get subtitle based on language"""
        if language == 'en':
            return self.subtitle_en or self.subtitle
        elif language == 'kg':
            return self.subtitle_ky or self.subtitle
        return self.subtitle
    
    def get_display_mission_text(self, language='ru'):
        """Get mission text based on language"""
        if language == 'en':
            return self.mission_text_en or self.mission_text
        elif language == 'kg':
            return self.mission_text_ky or self.mission_text
        return self.mission_text
    
    def get_display_vision_title(self, language='ru'):
        """Get vision title based on language"""
        if language == 'en':
            return self.vision_title_en or self.vision_title
        elif language == 'kg':
            return self.vision_title_ky or self.vision_title
        return self.vision_title
    
    def get_display_vision_text(self, language='ru'):
        """Get vision text based on language"""
        if language == 'en':
            return self.vision_text_en or self.vision_text
        elif language == 'kg':
            return self.vision_text_ky or self.vision_text
        return self.vision_text
    
    def get_display_approach_title(self, language='ru'):
        """Get approach title based on language"""
        if language == 'en':
            return self.approach_title_en or self.approach_title
        elif language == 'kg':
            return self.approach_title_ky or self.approach_title
        return self.approach_title
    
    def get_display_approach_text(self, language='ru'):
        """Get approach text based on language"""
        if language == 'en':
            return self.approach_text_en or self.approach_text
        elif language == 'kg':
            return self.approach_text_ky or self.approach_text
        return self.approach_text
    
    def get_display_achievements_subtitle(self, language='ru'):
        """Get achievements subtitle based on language"""
        if language == 'en':
            return self.achievements_subtitle_en or self.achievements_subtitle
        elif language == 'kg':
            return self.achievements_subtitle_ky or self.achievements_subtitle
        return self.achievements_subtitle
    
    def get_display_impact_title(self, language='ru'):
        """Get impact title based on language"""
        if language == 'en':
            return self.impact_title_en or self.impact_title
        elif language == 'kg':
            return self.impact_title_ky or self.impact_title
        return self.impact_title
    
    def get_display_impact_text(self, language='ru'):
        """Get impact text based on language"""
        if language == 'en':
            return self.impact_text_en or self.impact_text
        elif language == 'kg':
            return self.impact_text_ky or self.impact_text
        return self.impact_text
    
    def get_display_future_title(self, language='ru'):
        """Get future title based on language"""
        if language == 'en':
            return self.future_title_en or self.future_title
        elif language == 'kg':
            return self.future_title_ky or self.future_title
        return self.future_title
    
    def get_display_future_text(self, language='ru'):
        """Get future text based on language"""
        if language == 'en':
            return self.future_text_en or self.future_text
        elif language == 'kg':
            return self.future_text_ky or self.future_text
        return self.future_text

    def __str__(self):
        return self.title


class HistoryMilestone(models.Model):
    """
    Модель для исторических вех университета
    """
    
    # Русский язык
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок вехи (RU)',
        help_text='Название исторической вехи на русском языке'
    )
    
    description = models.TextField(
        verbose_name='Описание (RU)',
        help_text='Подробное описание исторической вехи на русском языке'
    )
    
    # Английский язык
    title_en = models.CharField(
        max_length=200,
        verbose_name='Заголовок вехи (EN)',
        help_text='Название исторической вехи на английском языке',
        blank=True
    )
    
    description_en = models.TextField(
        verbose_name='Описание (EN)',
        help_text='Подробное описание исторической вехи на английском языке',
        blank=True
    )
    
    # Кыргызский язык
    title_ky = models.CharField(
        max_length=200,
        verbose_name='Заголовок вехи (KY)',
        help_text='Название исторической вехи на кыргызском языке',
        blank=True
    )
    
    description_ky = models.TextField(
        verbose_name='Описание (KY)',
        help_text='Подробное описание исторической вехи на кыргызском языке',
        blank=True
    )
    
    year = models.CharField(
        max_length=20,
        verbose_name='Год',
        help_text='Год или период времени'
    )
    
    # Иконка (можно расширить в будущем)
    icon_class = models.CharField(
        max_length=100,
        verbose_name='CSS класс иконки',
        help_text='CSS класс для иконки (например, для Heroicons)',
        blank=True,
        default='CalendarIcon'
    )
    
    # Порядок отображения
    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок',
        help_text='Порядок отображения (чем меньше число, тем выше)'
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активно',
        help_text='Отображать на сайте'
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    class Meta:
        verbose_name = 'Историческая веха'
        verbose_name_plural = 'Исторические вехи'
        ordering = ['order', 'year']
    
    def get_display_title(self, language='ru'):
        """Get title based on language"""
        if language == 'en':
            return self.title_en or self.title
        elif language == 'kg':
            return self.title_ky or self.title
        return self.title
    
    def get_display_description(self, language='ru'):
        """Get description based on language"""
        if language == 'en':
            return self.description_en or self.description
        elif language == 'kg':
            return self.description_ky or self.description
        return self.description

    def __str__(self):
        return f"{self.year} - {self.title}"


class Value(models.Model):
    """
    Модель для ценностей университета
    """
    
    # Выбор типов ценностей (для соответствия фронтенду)
    VALUE_TYPES = [
        ('education', 'Образование'),
        ('science', 'Наука'),
        ('medicine', 'Медицина'),
        ('studentCare', 'Забота о студентах'),
    ]
    
    type = models.CharField(
        max_length=50,
        choices=VALUE_TYPES,
        verbose_name='Тип ценности',
        help_text='Тип ценности для соответствия фронтенду'
    )
    
    # Русский язык
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок (RU)',
        help_text='Название ценности на русском языке'
    )
    
    description = models.TextField(
        verbose_name='Описание (RU)',
        help_text='Подробное описание ценности на русском языке'
    )
    
    # Английский язык
    title_en = models.CharField(
        max_length=200,
        verbose_name='Заголовок (EN)',
        help_text='Название ценности на английском языке',
        blank=True
    )
    
    description_en = models.TextField(
        verbose_name='Описание (EN)',
        help_text='Подробное описание ценности на английском языке',
        blank=True
    )
    
    # Кыргызский язык
    title_ky = models.CharField(
        max_length=200,
        verbose_name='Заголовок (KY)',
        help_text='Название ценности на кыргызском языке',
        blank=True
    )
    
    description_ky = models.TextField(
        verbose_name='Описание (KY)',
        help_text='Подробное описание ценности на кыргызском языке',
        blank=True
    )
    
    # Порядок отображения
    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок',
        help_text='Порядок отображения (чем меньше число, тем выше)'
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активно',
        help_text='Отображать на сайте'
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    class Meta:
        verbose_name = 'Ценность'
        verbose_name_plural = 'Ценности'
        ordering = ['order']
        unique_together = ['type']  # Каждый тип может быть только один
    
    def get_display_title(self, language='ru'):
        """Get title based on language"""
        if language == 'en':
            return self.title_en or self.title
        elif language == 'kg':
            return self.title_ky or self.title
        return self.title
    
    def get_display_description(self, language='ru'):
        """Get description based on language"""
        if language == 'en':
            return self.description_en or self.description
        elif language == 'kg':
            return self.description_ky or self.description
        return self.description

    def __str__(self):
        return self.title


class Priority(models.Model):
    """
    Модель для приоритетов университета
    """
    
    # Русский язык
    text = models.TextField(
        verbose_name='Текст приоритета (RU)',
        help_text='Описание приоритета на русском языке'
    )
    
    # Английский язык
    text_en = models.TextField(
        verbose_name='Текст приоритета (EN)',
        help_text='Описание приоритета на английском языке',
        blank=True
    )
    
    # Кыргызский язык
    text_ky = models.TextField(
        verbose_name='Текст приоритета (KY)',
        help_text='Описание приоритета на кыргызском языке',
        blank=True
    )
    
    # Иконка
    icon_class = models.CharField(
        max_length=100,
        verbose_name='CSS класс иконки',
        help_text='CSS класс для иконки (например, для Heroicons)',
        blank=True,
        default='LightBulbIcon'
    )
    
    # Порядок отображения
    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок',
        help_text='Порядок отображения (чем меньше число, тем выше)'
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активно',
        help_text='Отображать на сайте'
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    class Meta:
        verbose_name = 'Приоритет'
        verbose_name_plural = 'Приоритеты'
        ordering = ['order']
    
    def get_display_text(self, language='ru'):
        """Get text based on language"""
        if language == 'en':
            return self.text_en or self.text
        elif language == 'kg':
            return self.text_ky or self.text
        return self.text

    def __str__(self):
        return self.text[:100] + '...' if len(self.text) > 100 else self.text


class Achievement(models.Model):
    """
    Модель для достижений университета (статистика)
    """
    
    number = models.CharField(
        max_length=20,
        verbose_name='Число',
        help_text='Числовое значение достижения (например, 50+, 1000+)'
    )
    
    # Русский язык
    label = models.CharField(
        max_length=200,
        verbose_name='Подпись (RU)',
        help_text='Описание достижения на русском языке'
    )
    
    # Английский язык
    label_en = models.CharField(
        max_length=200,
        verbose_name='Подпись (EN)',
        help_text='Описание достижения на английском языке',
        blank=True
    )
    
    # Кыргызский язык
    label_ky = models.CharField(
        max_length=200,
        verbose_name='Подпись (KY)',
        help_text='Описание достижения на кыргызском языке',
        blank=True
    )
    
    # Порядок отображения
    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок',
        help_text='Порядок отображения (чем меньше число, тем выше)'
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активно',
        help_text='Отображать на сайте'
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'
        ordering = ['order']
    
    def get_display_label(self, language='ru'):
        """Get label based on language"""
        if language == 'en':
            return self.label_en or self.label
        elif language == 'kg':
            return self.label_ky or self.label
        return self.label

    def __str__(self):
        return f"{self.number} - {self.label}"
