from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _


class PartnerOrganization(models.Model):
    """Организации-партнеры для практики"""
    TYPE_CHOICES = [
        ('government', _('Государственная больница')),
        ('private', _('Частная клиника')),
        ('specialized', _('Специализированный центр')),
    ]
    
    # Мультиязычные поля
    name_ru = models.CharField('Название (русский)', max_length=255)
    name_kg = models.CharField('Название (кыргызский)', max_length=255)
    name_en = models.CharField('Название (английский)', max_length=255)
    
    description_ru = models.TextField('Описание (русский)', blank=True)
    description_kg = models.TextField('Описание (кыргызский)', blank=True)
    description_en = models.TextField('Описание (английский)', blank=True)
    
    # Немультиязычные поля
    type = models.CharField(_('Тип'), max_length=20, choices=TYPE_CHOICES)
    location = models.CharField(_('Местоположение'), max_length=255)
    contact_person = models.CharField(_('Контактное лицо'), max_length=255)
    phone = models.CharField(_('Телефон'), max_length=50)
    email = models.EmailField(_('Email'))
    website = models.URLField(_('Веб-сайт'), blank=True, null=True)
    is_active = models.BooleanField(_('Активна'), default=True)
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Дата обновления'), auto_now=True)

    class Meta:
        verbose_name = _('Организация-партнер')
        verbose_name_plural = _('Организации-партнеры')
        ordering = ['name_ru']

    def __str__(self):
        return self.name_ru


class OrganizationSpecialization(models.Model):
    """Специализации организаций-партнеров"""
    organization = models.ForeignKey(
        PartnerOrganization, 
        on_delete=models.CASCADE,
        related_name='specializations'
    )
    # Мультиязычные поля
    name_ru = models.CharField('Название специализации (русский)', max_length=255)
    name_kg = models.CharField('Название специализации (кыргызский)', max_length=255)
    name_en = models.CharField('Название специализации (английский)', max_length=255)

    class Meta:
        verbose_name = _('Специализация')
        verbose_name_plural = _('Специализации')

    def __str__(self):
        return f"{self.organization.name_ru} - {self.name_ru}"


class InternshipRequirement(models.Model):
    """Требования к практике"""
    CATEGORY_CHOICES = [
        ('academic', _('Академические требования')),
        ('documents', _('Документы для практики')),
        ('duration', _('Продолжительность практики')),
    ]
    
    # Мультиязычные поля
    title_ru = models.CharField('Заголовок (русский)', max_length=255)
    title_kg = models.CharField('Заголовок (кыргызский)', max_length=255)
    title_en = models.CharField('Заголовок (английский)', max_length=255)
    
    description_ru = models.TextField('Описание (русский)', blank=True)
    description_kg = models.TextField('Описание (кыргызский)', blank=True)
    description_en = models.TextField('Описание (английский)', blank=True)
    
    # Немультиязычные поля
    category = models.CharField(_('Категория'), max_length=20, choices=CATEGORY_CHOICES)
    order = models.PositiveIntegerField(_('Порядок'), default=0)
    is_active = models.BooleanField(_('Активно'), default=True)

    class Meta:
        verbose_name = _('Требование к практике')
        verbose_name_plural = _('Требования к практике')
        ordering = ['category', 'order']

    def __str__(self):
        return self.title_ru


class InternshipRequirementItem(models.Model):
    """Элементы требований к практике"""
    requirement = models.ForeignKey(
        InternshipRequirement,
        on_delete=models.CASCADE,
        related_name='items'
    )
    # Мультиязычные поля
    text_ru = models.TextField('Текст (русский)')
    text_kg = models.TextField('Текст (кыргызский)')
    text_en = models.TextField('Текст (английский)')
    
    order = models.PositiveIntegerField(_('Порядок'), default=0)

    class Meta:
        verbose_name = _('Элемент требования')
        verbose_name_plural = _('Элементы требований')
        ordering = ['order']

    def __str__(self):
        return f"{self.requirement.title_ru} - {self.text_ru[:50]}..."


class ReportTemplate(models.Model):
    """Шаблоны отчетов по практике"""
    # Мультиязычные поля
    name_ru = models.CharField('Название шаблона (русский)', max_length=255)
    name_kg = models.CharField('Название шаблона (кыргызский)', max_length=255)
    name_en = models.CharField('Название шаблона (английский)', max_length=255)
    
    description_ru = models.TextField('Описание (русский)', blank=True)
    description_kg = models.TextField('Описание (кыргызский)', blank=True)
    description_en = models.TextField('Описание (английский)', blank=True)
    
    # Файл шаблона
    file = models.FileField(
        upload_to='report_templates/',
        validators=[FileExtensionValidator(['doc', 'docx', 'pdf'])],
        verbose_name=_('Файл шаблона')
    )
    
    # Немультиязычные поля
    is_active = models.BooleanField(_('Активен'), default=True)
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)

    class Meta:
        verbose_name = _('Шаблон отчета')
        verbose_name_plural = _('Шаблоны отчетов')
        ordering = ['name_ru']

    def __str__(self):
        return self.name_ru


# =============================================================================
# МОДЕЛИ ДЛЯ АКАДЕМИЧЕСКОЙ МОБИЛЬНОСТИ
# =============================================================================

class PartnerUniversity(models.Model):
    """Университеты-партнеры для академической мобильности"""
    # Мультиязычные поля
    name_ru = models.CharField('Название университета (русский)', max_length=255)
    name_kg = models.CharField('Название университета (кыргызский)', max_length=255)
    name_en = models.CharField('Название университета (английский)', max_length=255)
    
    description_ru = models.TextField('Описание (русский)', blank=True)
    description_kg = models.TextField('Описание (кыргызский)', blank=True)
    description_en = models.TextField('Описание (английский)', blank=True)
    
    # Немультиязычные поля
    country = models.CharField(_('Страна'), max_length=100)
    city = models.CharField(_('Город'), max_length=100)
    website = models.URLField(_('Веб-сайт'), blank=True)
    logo = models.ImageField(upload_to='universities/', blank=True, null=True, verbose_name=_('Логотип'))
    is_active = models.BooleanField(_('Активен'), default=True)
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)

    class Meta:
        verbose_name = _('Университет-партнер')
        verbose_name_plural = _('Университеты-партнеры')
        ordering = ['name_ru']

    def __str__(self):
        return f"{self.name_ru} ({self.country})"


class UniversityProgram(models.Model):
    """Программы обмена в университетах-партнерах"""
    university = models.ForeignKey(
        PartnerUniversity,
        on_delete=models.CASCADE,
        related_name='programs'
    )
    
    # Мультиязычные поля
    name_ru = models.CharField('Название программы (русский)', max_length=255)
    name_kg = models.CharField('Название программы (кыргызский)', max_length=255)
    name_en = models.CharField('Название программы (английский)', max_length=255)
    
    description_ru = models.TextField('Описание программы (русский)', blank=True)
    description_kg = models.TextField('Описание программы (кыргызский)', blank=True)
    description_en = models.TextField('Описание программы (английский)', blank=True)
    
    # Немультиязычные поля
    duration = models.CharField(_('Продолжительность'), max_length=100)
    language = models.CharField(_('Язык обучения'), max_length=100)

    class Meta:
        verbose_name = _('Программа обмена')
        verbose_name_plural = _('Программы обмена')

    def __str__(self):
        return f"{self.university.name_ru} - {self.name_ru}"


class ExchangeOpportunity(models.Model):
    """Возможности обмена для студентов"""
    TYPE_CHOICES = [
        ('semester', _('Семестровый обмен')),
        ('year', _('Годовой обмен')),
    ]
    
    # Мультиязычные поля
    title_ru = models.CharField('Заголовок (русский)', max_length=255)
    title_kg = models.CharField('Заголовок (кыргызский)', max_length=255)
    title_en = models.CharField('Заголовок (английский)', max_length=255)
    
    description_ru = models.TextField('Описание (русский)')
    description_kg = models.TextField('Описание (кыргызский)')
    description_en = models.TextField('Описание (английский)')
    
    # Немультиязычные поля
    type = models.CharField(_('Тип обмена'), max_length=20, choices=TYPE_CHOICES)
    is_active = models.BooleanField(_('Активна'), default=True)

    class Meta:
        verbose_name = _('Возможность обмена')
        verbose_name_plural = _('Возможности обмена')

    def __str__(self):
        return self.title_ru


class ExchangeBenefit(models.Model):
    """Преимущества программ обмена"""
    opportunity = models.ForeignKey(
        ExchangeOpportunity,
        on_delete=models.CASCADE,
        related_name='benefits'
    )
    
    # Мультиязычные поля
    text_ru = models.TextField('Текст преимущества (русский)')
    text_kg = models.TextField('Текст преимущества (кыргызский)')
    text_en = models.TextField('Текст преимущества (английский)')
    
    order = models.PositiveIntegerField(_('Порядок'), default=0)

    class Meta:
        verbose_name = _('Преимущество')
        verbose_name_plural = _('Преимущества')
        ordering = ['order']

    def __str__(self):
        return f"{self.opportunity.title_ru} - {self.text_ru[:50]}..."


class MobilityRequirement(models.Model):
    """Требования для участия в академической мобильности"""
    CATEGORY_CHOICES = [
        ('academic', _('Академические требования')),
        ('language', _('Языковые требования')),
        ('documents', _('Документы')),
    ]
    
    # Мультиязычные поля
    title_ru = models.CharField('Заголовок (русский)', max_length=255)
    title_kg = models.CharField('Заголовок (кыргызский)', max_length=255)
    title_en = models.CharField('Заголовок (английский)', max_length=255)
    
    description_ru = models.TextField('Описание (русский)', blank=True)
    description_kg = models.TextField('Описание (кыргызский)', blank=True)
    description_en = models.TextField('Описание (английский)', blank=True)
    
    # Немультиязычные поля
    category = models.CharField(_('Категория'), max_length=20, choices=CATEGORY_CHOICES)
    order = models.PositiveIntegerField(_('Порядок'), default=0)
    is_active = models.BooleanField(_('Активно'), default=True)

    class Meta:
        verbose_name = _('Требование мобильности')
        verbose_name_plural = _('Требования мобильности')
        ordering = ['category', 'order']

    def __str__(self):
        return self.title_ru


# =============================================================================
# МОДЕЛИ ДЛЯ РЕГЛАМЕНТОВ И ПРАВИЛ
# =============================================================================

class InternalRule(models.Model):
    """Правила внутреннего распорядка"""
    # Мультиязычные поля
    title_ru = models.CharField('Заголовок (русский)', max_length=255)
    title_kg = models.CharField('Заголовок (кыргызский)', max_length=255)
    title_en = models.CharField('Заголовок (английский)', max_length=255)
    
    description_ru = models.TextField('Описание (русский)', blank=True)
    description_kg = models.TextField('Описание (кыргызский)', blank=True)
    description_en = models.TextField('Описание (английский)', blank=True)
    
    # Немультиязычные поля
    order = models.PositiveIntegerField(_('Порядок'), default=0)
    is_active = models.BooleanField(_('Активно'), default=True)

    class Meta:
        verbose_name = _('Правило внутреннего распорядка')
        verbose_name_plural = _('Правила внутреннего распорядка')
        ordering = ['order']

    def __str__(self):
        return self.title_ru


class InternalRuleItem(models.Model):
    """Элементы правил внутреннего распорядка"""
    rule = models.ForeignKey(
        InternalRule,
        on_delete=models.CASCADE,
        related_name='items'
    )
    
    # Мультиязычные поля
    text_ru = models.TextField('Текст правила (русский)')
    text_kg = models.TextField('Текст правила (кыргызский)')
    text_en = models.TextField('Текст правила (английский)')
    
    order = models.PositiveIntegerField(_('Порядок'), default=0)

    class Meta:
        verbose_name = _('Элемент правила')
        verbose_name_plural = _('Элементы правил')
        ordering = ['order']

    def __str__(self):
        return f"{self.rule.title_ru} - {self.text_ru[:50]}..."


class AcademicRegulation(models.Model):
    """Учебные регламенты"""
    # Мультиязычные поля
    title_ru = models.CharField('Заголовок (русский)', max_length=255)
    title_kg = models.CharField('Заголовок (кыргызский)', max_length=255)
    title_en = models.CharField('Заголовок (английский)', max_length=255)
    
    description_ru = models.TextField('Описание (русский)', blank=True)
    description_kg = models.TextField('Описание (кыргызский)', blank=True)
    description_en = models.TextField('Описание (английский)', blank=True)
    
    # Немультиязычные поля
    version = models.CharField(_('Версия'), max_length=50)
    effective_date = models.DateField(_('Дата вступления в силу'))
    is_active = models.BooleanField(_('Активен'), default=True)

    class Meta:
        verbose_name = _('Учебный регламент')
        verbose_name_plural = _('Учебные регламенты')
        ordering = ['-effective_date']

    def __str__(self):
        return f"{self.title_ru} v{self.version}"


class AcademicRegulationSection(models.Model):
    """Разделы учебных регламентов"""
    regulation = models.ForeignKey(
        AcademicRegulation,
        on_delete=models.CASCADE,
        related_name='sections'
    )
    
    # Мультиязычные поля
    title_ru = models.CharField('Заголовок раздела (русский)', max_length=255)
    title_kg = models.CharField('Заголовок раздела (кыргызский)', max_length=255)
    title_en = models.CharField('Заголовок раздела (английский)', max_length=255)
    
    # Немультиязычные поля
    number = models.CharField(_('Номер раздела'), max_length=10)
    order = models.PositiveIntegerField(_('Порядок'), default=0)

    class Meta:
        verbose_name = _('Раздел регламента')
        verbose_name_plural = _('Разделы регламентов')
        ordering = ['order']

    def __str__(self):
        return f"{self.regulation.title_ru} - {self.number}. {self.title_ru}"


class AcademicRegulationRule(models.Model):
    """Правила в разделах учебных регламентов"""
    section = models.ForeignKey(
        AcademicRegulationSection,
        on_delete=models.CASCADE,
        related_name='rules'
    )
    
    # Мультиязычные поля
    text_ru = models.TextField('Текст правила (русский)')
    text_kg = models.TextField('Текст правила (кыргызский)')
    text_en = models.TextField('Текст правила (английский)')
    
    # Немультиязычные поля
    number = models.CharField(_('Номер правила'), max_length=10)
    order = models.PositiveIntegerField(_('Порядок'), default=0)

    class Meta:
        verbose_name = _('Правило регламента')
        verbose_name_plural = _('Правила регламентов')
        ordering = ['order']

    def __str__(self):
        return f"{self.section.title_ru} - {self.number}"


class DownloadableDocument(models.Model):
    """Документы для скачивания"""
    # Мультиязычные поля
    title_ru = models.CharField('Название документа (русский)', max_length=255)
    title_kg = models.CharField('Название документа (кыргызский)', max_length=255)
    title_en = models.CharField('Название документа (английский)', max_length=255)
    
    description_ru = models.TextField('Описание (русский)', blank=True)
    description_kg = models.TextField('Описание (кыргызский)', blank=True)
    description_en = models.TextField('Описание (английский)', blank=True)
    
    # Файл документа
    file = models.FileField(
        upload_to='documents/',
        validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])],
        verbose_name=_('Файл документа')
    )
    
    # Немультиязычные поля
    file_size = models.PositiveIntegerField(_('Размер файла (байты)'), null=True, blank=True)
    is_active = models.BooleanField(_('Активен'), default=True)
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)

    class Meta:
        verbose_name = _('Документ для скачивания')
        verbose_name_plural = _('Документы для скачивания')
        ordering = ['title_ru']

    def __str__(self):
        return self.title_ru


# =============================================================================
# МОДЕЛИ ДЛЯ ИНСТРУКЦИЙ
# =============================================================================

class StudentGuide(models.Model):
    """Инструкции для студентов"""
    # Мультиязычные поля
    title_ru = models.CharField('Заголовок (русский)', max_length=255)
    title_kg = models.CharField('Заголовок (кыргызский)', max_length=255)
    title_en = models.CharField('Заголовок (английский)', max_length=255)
    
    description_ru = models.TextField('Описание (русский)', blank=True)
    description_kg = models.TextField('Описание (кыргызский)', blank=True)
    description_en = models.TextField('Описание (английский)', blank=True)
    
    # Немультиязычные поля
    order = models.PositiveIntegerField(_('Порядок'), default=0)
    is_active = models.BooleanField(_('Активна'), default=True)
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)

    class Meta:
        verbose_name = _('Инструкция для студентов')
        verbose_name_plural = _('Инструкции для студентов')
        ordering = ['order']

    def __str__(self):
        return self.title_ru


class GuideRequirement(models.Model):
    """Требования в инструкциях"""
    guide = models.ForeignKey(
        StudentGuide,
        on_delete=models.CASCADE,
        related_name='requirements'
    )
    
    # Мультиязычные поля
    text_ru = models.TextField('Текст требования (русский)')
    text_kg = models.TextField('Текст требования (кыргызский)')
    text_en = models.TextField('Текст требования (английский)')
    
    order = models.PositiveIntegerField(_('Порядок'), default=0)

    class Meta:
        verbose_name = _('Требование инструкции')
        verbose_name_plural = _('Требования инструкций')
        ordering = ['order']

    def __str__(self):
        return f"{self.guide.title_ru} - {self.text_ru[:50]}..."


class GuideStep(models.Model):
    """Шаги в инструкциях"""
    guide = models.ForeignKey(
        StudentGuide,
        on_delete=models.CASCADE,
        related_name='steps'
    )
    
    # Мультиязычные поля
    title_ru = models.CharField('Заголовок шага (русский)', max_length=255)
    title_kg = models.CharField('Заголовок шага (кыргызский)', max_length=255)
    title_en = models.CharField('Заголовок шага (английский)', max_length=255)
    
    order = models.PositiveIntegerField(_('Порядок'), default=0)

    class Meta:
        verbose_name = _('Шаг инструкции')
        verbose_name_plural = _('Шаги инструкций')
        ordering = ['order']

    def __str__(self):
        return f"{self.guide.title_ru} - Шаг {self.order}: {self.title_ru}"


class GuideStepDetail(models.Model):
    """Детали шагов в инструкциях"""
    step = models.ForeignKey(
        GuideStep,
        on_delete=models.CASCADE,
        related_name='details'
    )
    
    # Мультиязычные поля
    text_ru = models.TextField('Текст детали (русский)')
    text_kg = models.TextField('Текст детали (кыргызский)')
    text_en = models.TextField('Текст детали (английский)')
    
    order = models.PositiveIntegerField(_('Порядок'), default=0)

    class Meta:
        verbose_name = _('Деталь шага')
        verbose_name_plural = _('Детали шагов')
        ordering = ['order']

    def __str__(self):
        return f"{self.step.title_ru} - {self.text_ru[:50]}..."


# =============================================================================
# МОДЕЛИ ДЛЯ ОБРАЩЕНИЙ СТУДЕНТОВ
# =============================================================================

class StudentAppeal(models.Model):
    """Обращения студентов"""
    STATUS_CHOICES = [
        ('new', _('Новое')),
        ('in_progress', _('В обработке')),
        ('resolved', _('Решено')),
        ('closed', _('Закрыто')),
    ]
    
    CATEGORY_CHOICES = [
        ('academic', _('Академические вопросы')),
        ('administrative', _('Административные вопросы')),
        ('financial', _('Финансовые вопросы')),
        ('technical', _('Технические вопросы')),
        ('other', _('Другое')),
    ]
    
    # Контактная информация
    full_name = models.CharField(_('ФИО'), max_length=255)
    email = models.EmailField(_('Email'))
    phone = models.CharField(_('Телефон'), max_length=50, blank=True)
    student_id = models.CharField(_('Студенческий билет'), max_length=50, blank=True)
    
    # Обращение
    category = models.CharField(_('Категория'), max_length=20, choices=CATEGORY_CHOICES)
    subject = models.CharField(_('Тема обращения'), max_length=255)
    message = models.TextField(_('Сообщение'))
    
    # Файлы
    attachment = models.FileField(
        upload_to='appeals/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png'])],
        verbose_name=_('Прикрепленный файл')
    )
    
    # Статус и метаданные
    status = models.CharField(_('Статус'), max_length=20, choices=STATUS_CHOICES, default='new')
    response = models.TextField(_('Ответ'), blank=True)
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Дата обновления'), auto_now=True)
    processed_by = models.CharField(_('Обработано'), max_length=255, blank=True)

    class Meta:
        verbose_name = _('Обращение студента')
        verbose_name_plural = _('Обращения студентов')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.subject}"
