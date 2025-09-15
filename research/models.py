from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class ResearchArea(models.Model):
    """Области исследований"""
    title_ru = models.CharField("Название (рус)", max_length=200)
    title_en = models.CharField("Название (англ)", max_length=200)
    title_kg = models.CharField("Название (кыр)", max_length=200)
    
    description_ru = models.TextField("Описание (рус)")
    description_en = models.TextField("Описание (англ)")
    description_kg = models.TextField("Описание (кыр)")
    
    icon = models.CharField("Иконка", max_length=100, default="🔬")
    color = models.CharField("Цвет", max_length=50, default="blue")
    
    projects_count = models.IntegerField("Количество проектов", default=0)
    publications_count = models.IntegerField("Количество публикаций", default=0)
    researchers_count = models.IntegerField("Количество исследователей", default=0)
    
    is_active = models.BooleanField("Активно", default=True)
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    
    class Meta:
        verbose_name = "Область исследований"
        verbose_name_plural = "Области исследований"
        ordering = ['id']
        
    def __str__(self):
        return self.title_ru


class ResearchCenter(models.Model):
    """Исследовательские центры"""
    name_ru = models.CharField("Название (рус)", max_length=200)
    name_en = models.CharField("Название (англ)", max_length=200)
    name_kg = models.CharField("Название (кыр)", max_length=200)
    
    description_ru = models.TextField("Описание (рус)")
    description_en = models.TextField("Описание (англ)")
    description_kg = models.TextField("Описание (кыр)")
    
    director_ru = models.CharField("Директор (рус)", max_length=200)
    director_en = models.CharField("Директор (англ)", max_length=200)
    director_kg = models.CharField("Директор (кыр)", max_length=200)
    staff_count = models.IntegerField("Количество сотрудников", default=0)
    established_year = models.IntegerField("Год основания")
    
    equipment_ru = models.TextField("Оборудование (рус)", blank=True)
    equipment_en = models.TextField("Оборудование (англ)", blank=True)
    equipment_kg = models.TextField("Оборудование (кыр)", blank=True)
    
    image = models.ImageField("Изображение", upload_to='research/centers/', blank=True)
    website = models.URLField("Веб-сайт", blank=True)
    email = models.EmailField("Email", blank=True)
    phone = models.CharField("Телефон", max_length=20, blank=True)
    
    is_active = models.BooleanField("Активно", default=True)
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    
    class Meta:
        verbose_name = "Исследовательский центр"
        verbose_name_plural = "Исследовательские центры"
        ordering = ['name_ru']
        
    def __str__(self):
        return self.name_ru


class Grant(models.Model):
    """Гранты"""
    CATEGORY_CHOICES = [
        ('youth', 'Молодежные'),
        ('international', 'Международные'),
        ('fundamental', 'Фундаментальные'),
        ('applied', 'Прикладные'),
        ('innovative', 'Инновационные'),
        ('clinical', 'Клинические'),
    ]
    
    STATUS_CHOICES = [
        ('active', 'Активный'),
        ('upcoming', 'Предстоящий'),
        ('closed', 'Закрытый'),
    ]
    
    title_ru = models.CharField("Название (рус)", max_length=300)
    title_en = models.CharField("Название (англ)", max_length=300)
    title_kg = models.CharField("Название (кыр)", max_length=300)
    
    organization_ru = models.CharField("Организация (рус)", max_length=200)
    organization_en = models.CharField("Организация (англ)", max_length=200)
    organization_kg = models.CharField("Организация (кыр)", max_length=200)
    amount = models.CharField("Сумма", max_length=100)
    deadline = models.DateField("Дедлайн подачи")
    
    category = models.CharField("Категория", max_length=20, choices=CATEGORY_CHOICES)
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES, default='active')
    
    duration_ru = models.CharField("Срок реализации (рус)", max_length=100)
    duration_en = models.CharField("Срок реализации (англ)", max_length=100)
    duration_kg = models.CharField("Срок реализации (кыр)", max_length=100)
    
    requirements_ru = models.TextField("Требования (рус)")
    requirements_en = models.TextField("Требования (англ)")
    requirements_kg = models.TextField("Требования (кыр)")
    
    description_ru = models.TextField("Описание (рус)")
    description_en = models.TextField("Описание (англ)")
    description_kg = models.TextField("Описание (кыр)")
    
    contact = models.EmailField("Контактный email")
    website = models.URLField("Веб-сайт")
    
    is_active = models.BooleanField("Активно", default=True)
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)
    
    class Meta:
        verbose_name = "Грант"
        verbose_name_plural = "Гранты"
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.title_ru} ({self.organization_ru})"
    
    @property
    def is_deadline_soon(self):
        """Проверяет, скоро ли дедлайн (менее 30 дней)"""
        days_left = (self.deadline - timezone.now().date()).days
        return days_left <= 30


class Conference(models.Model):
    """Конференции"""
    STATUS_CHOICES = [
        ('registration-open', 'Регистрация открыта'),
        ('early-bird', 'Ранняя регистрация'),
        ('call-for-papers', 'Прием докладов'),
        ('completed', 'Завершена'),
    ]
    
    title_ru = models.CharField("Название (рус)", max_length=300)
    title_en = models.CharField("Название (англ)", max_length=300)
    title_kg = models.CharField("Название (кыр)", max_length=300)
    
    start_date = models.DateField("Дата начала")
    end_date = models.DateField("Дата окончания")
    
    location_ru = models.CharField("Место проведения (рус)", max_length=200)
    location_en = models.CharField("Место проведения (англ)", max_length=200)
    location_kg = models.CharField("Место проведения (кыр)", max_length=200)
    
    deadline = models.DateField("Дедлайн регистрации")
    website = models.URLField("Веб-сайт")
    
    description_ru = models.TextField("Описание (рус)")
    description_en = models.TextField("Описание (англ)")
    description_kg = models.TextField("Описание (кыр)")
    
    topics_ru = models.JSONField("Темы (рус)", default=list)
    topics_en = models.JSONField("Темы (англ)", default=list)
    topics_kg = models.JSONField("Темы (кыр)", default=list)
    
    speakers_ru = models.JSONField("Спикеры (рус)", default=list)
    speakers_en = models.JSONField("Спикеры (англ)", default=list)
    speakers_kg = models.JSONField("Спикеры (кыр)", default=list)
    
    speakers_count = models.IntegerField("Количество спикеров", default=0)
    participants_limit = models.IntegerField("Лимит участников", null=True, blank=True)
    
    image = models.ImageField("Изображение", upload_to='research/conferences/', blank=True)
    status = models.CharField("Статус", max_length=30, choices=STATUS_CHOICES, default='registration-open')
    
    is_active = models.BooleanField("Активно", default=True)
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    
    class Meta:
        verbose_name = "Конференция"
        verbose_name_plural = "Конференции"
        ordering = ['start_date']
        
    def __str__(self):
        return f"{self.title_ru} ({self.start_date})"
    
    @property
    def is_upcoming(self):
        """Проверяет, предстоящая ли конференция"""
        return self.start_date > timezone.now().date()


class Publication(models.Model):
    """Научные публикации"""
    PUBLICATION_TYPE_CHOICES = [
        ('article', 'Статья'),
        ('book', 'Книга'),
        ('conference', 'Конференция'),
        ('patent', 'Патент'),
        ('thesis', 'Диссертация'),
    ]
    
    title_ru = models.CharField("Название (рус)", max_length=500)
    title_en = models.CharField("Название (англ)", max_length=500)
    title_kg = models.CharField("Название (кыр)", max_length=500)
    
    authors_ru = models.CharField("Авторы (рус)", max_length=500)
    authors_en = models.CharField("Авторы (англ)", max_length=500)
    authors_kg = models.CharField("Авторы (кыр)", max_length=500)
    journal = models.CharField("Журнал/Издательство", max_length=300)
    
    publication_date = models.DateField("Дата публикации")
    publication_type = models.CharField("Тип публикации", max_length=20, choices=PUBLICATION_TYPE_CHOICES, default='article')
    
    impact_factor = models.DecimalField("Импакт-фактор", max_digits=5, decimal_places=2, null=True, blank=True)
    citations_count = models.IntegerField("Количество цитирований", default=0)
    
    doi = models.CharField("DOI", max_length=100, blank=True)
    url = models.URLField("Ссылка", blank=True)
    
    abstract_ru = models.TextField("Аннотация (рус)", blank=True)
    abstract_en = models.TextField("Аннотация (англ)", blank=True)
    abstract_kg = models.TextField("Аннотация (кыр)", blank=True)
    
    keywords_ru = models.JSONField("Ключевые слова (рус)", default=list)
    keywords_en = models.JSONField("Ключевые слова (англ)", default=list)
    keywords_kg = models.JSONField("Ключевые слова (кыр)", default=list)
    
    research_area = models.ForeignKey(ResearchArea, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Область исследований")
    research_center = models.ForeignKey(ResearchCenter, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Исследовательский центр")
    
    file = models.FileField("Файл", upload_to='research/publications/', blank=True)
    
    is_featured = models.BooleanField("Рекомендуемая", default=False)
    is_active = models.BooleanField("Активно", default=True)
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    
    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        ordering = ['-publication_date']
        
    def __str__(self):
        return f"{self.title_ru} ({self.publication_date.year})"


class GrantApplication(models.Model):
    """Заявки на гранты"""
    STATUS_CHOICES = [
        ('pending', 'На рассмотрении'),
        ('approved', 'Одобрено'),
        ('rejected', 'Отклонено'),
    ]
    
    grant = models.ForeignKey(Grant, on_delete=models.CASCADE, verbose_name="Грант")
    
    project_title = models.CharField("Название проекта", max_length=300)
    principal_investigator = models.CharField("Руководитель проекта", max_length=200)
    email = models.EmailField("Email")
    phone = models.CharField("Телефон", max_length=20, blank=True)
    department = models.CharField("Кафедра/Лаборатория", max_length=200)
    team_members = models.TextField("Члены команды", blank=True)
    
    project_description = models.TextField("Описание проекта")
    budget = models.IntegerField("Бюджет", validators=[MinValueValidator(0)])
    timeline = models.IntegerField("Срок реализации (месяцы)", validators=[MinValueValidator(1)])
    expected_results = models.TextField("Ожидаемые результаты")
    
    files = models.FileField("Прикрепленные файлы", upload_to='research/applications/', blank=True)
    
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES, default='pending')
    admin_notes = models.TextField("Заметки администратора", blank=True)
    
    submitted_at = models.DateTimeField("Подано", auto_now_add=True)
    reviewed_at = models.DateTimeField("Рассмотрено", null=True, blank=True)
    
    class Meta:
        verbose_name = "Заявка на грант"
        verbose_name_plural = "Заявки на гранты"
        ordering = ['-submitted_at']
        
    def __str__(self):
        return f"{self.project_title} - {self.principal_investigator}"


class ResearchManagementPosition(models.Model):
    """Должности в научном управлении"""
    POSITION_TYPE_CHOICES = [
        ('leadership', 'Руководство'),
        ('institute', 'Институт'),
        ('center', 'Центр'),
        ('department', 'Кафедра'),
        ('council', 'Научный совет'),
        ('commission', 'Комиссия'),
    ]

    title_ru = models.CharField("Должность (рус)", max_length=200)
    title_en = models.CharField("Должность (англ)", max_length=200)
    title_kg = models.CharField("Должность (кыр)", max_length=200)
    
    full_name_ru = models.CharField("ФИО (рус)", max_length=200)
    full_name_en = models.CharField("ФИО (англ)", max_length=200)
    full_name_kg = models.CharField("ФИО (кыр)", max_length=200)
    
    position_type = models.CharField("Тип должности", max_length=20, choices=POSITION_TYPE_CHOICES)
    
    bio_ru = models.TextField("Биография (рус)", blank=True)
    bio_en = models.TextField("Биография (англ)", blank=True)
    bio_kg = models.TextField("Биография (кыр)", blank=True)
    
    education_ru = models.TextField("Образование (рус)", blank=True)
    education_en = models.TextField("Образование (англ)", blank=True)
    education_kg = models.TextField("Образование (кыр)", blank=True)
    
    scientific_interests_ru = models.TextField("Научные интересы (рус)", blank=True)
    scientific_interests_en = models.TextField("Научные интересы (англ)", blank=True)
    scientific_interests_kg = models.TextField("Научные интересы (кыр)", blank=True)
    
    contact_email = models.EmailField("Email", blank=True)
    contact_phone = models.CharField("Телефон", max_length=20, blank=True)
    office_location = models.CharField("Кабинет", max_length=100, blank=True)
    
    photo = models.ImageField("Фотография", upload_to='research/management/', blank=True)
    
    order = models.PositiveIntegerField("Порядок отображения", default=0)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Подчиняется")
    
    is_active = models.BooleanField("Активно", default=True)
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    
    class Meta:
        verbose_name = "Должность в научном управлении"
        verbose_name_plural = "Должности в научном управлении"
        ordering = ['position_type', 'order', 'title_ru']
        
    def __str__(self):
        return f"{self.title_ru} - {self.full_name_ru}"
    
    def get_children(self):
        """Получить подчиненных"""
        return self.__class__.objects.filter(parent=self, is_active=True).order_by('order', 'title_ru')


class ScientificCouncil(models.Model):
    """Научные советы"""
    name_ru = models.CharField("Название (рус)", max_length=200)
    name_en = models.CharField("Название (англ)", max_length=200)
    name_kg = models.CharField("Название (кыр)", max_length=200)
    
    description_ru = models.TextField("Описание (рус)")
    description_en = models.TextField("Описание (англ)")
    description_kg = models.TextField("Описание (кыр)")
    
    chairman_ru = models.CharField("Председатель (рус)", max_length=200)
    chairman_en = models.CharField("Председатель (англ)", max_length=200)
    chairman_kg = models.CharField("Председатель (кыр)", max_length=200)
    
    secretary_ru = models.CharField("Секретарь (рус)", max_length=200, blank=True)
    secretary_en = models.CharField("Секретарь (англ)", max_length=200, blank=True)
    secretary_kg = models.CharField("Секретарь (кыр)", max_length=200, blank=True)
    
    members_ru = models.JSONField("Члены совета (рус)", default=list)
    members_en = models.JSONField("Члены совета (англ)", default=list)
    members_kg = models.JSONField("Члены совета (кыр)", default=list)
    
    responsibilities_ru = models.TextField("Функции и обязанности (рус)", blank=True)
    responsibilities_en = models.TextField("Функции и обязанности (англ)", blank=True)
    responsibilities_kg = models.TextField("Функции и обязанности (кыр)", blank=True)
    
    meeting_schedule_ru = models.CharField("График заседаний (рус)", max_length=200, blank=True)
    meeting_schedule_en = models.CharField("График заседаний (англ)", max_length=200, blank=True)
    meeting_schedule_kg = models.CharField("График заседаний (кыр)", max_length=200, blank=True)
    
    contact_email = models.EmailField("Email", blank=True)
    contact_phone = models.CharField("Телефон", max_length=20, blank=True)
    
    is_active = models.BooleanField("Активно", default=True)
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    
    class Meta:
        verbose_name = "Научный совет"
        verbose_name_plural = "Научные советы"
        ordering = ['name_ru']
        
    def __str__(self):
        return self.name_ru


class Commission(models.Model):
    """Комиссии"""
    COMMISSION_TYPE_CHOICES = [
        ('ethics', 'Этическая комиссия'),
        ('qualification', 'Квалификационная комиссия'),
        ('publication', 'Издательская комиссия'),
        ('grant', 'Грантовая комиссия'),
        ('dissertation', 'Диссертационная комиссия'),
        ('other', 'Другое'),
    ]
    
    name_ru = models.CharField("Название (рус)", max_length=200)
    name_en = models.CharField("Название (англ)", max_length=200)
    name_kg = models.CharField("Название (кыр)", max_length=200)
    
    commission_type = models.CharField("Тип комиссии", max_length=20, choices=COMMISSION_TYPE_CHOICES)
    
    description_ru = models.TextField("Описание (рус)")
    description_en = models.TextField("Описание (англ)")
    description_kg = models.TextField("Описание (кыр)")
    
    chairman_ru = models.CharField("Председатель (рус)", max_length=200)
    chairman_en = models.CharField("Председатель (англ)", max_length=200)
    chairman_kg = models.CharField("Председатель (кыр)", max_length=200)
    
    members_ru = models.JSONField("Члены комиссии (рус)", default=list)
    members_en = models.JSONField("Члены комиссии (англ)", default=list)
    members_kg = models.JSONField("Члены комиссии (кыр)", default=list)
    
    functions_ru = models.TextField("Функции (рус)", blank=True)
    functions_en = models.TextField("Функции (англ)", blank=True)
    functions_kg = models.TextField("Функции (кыр)", blank=True)
    
    contact_email = models.EmailField("Email", blank=True)
    contact_phone = models.CharField("Телефон", max_length=20, blank=True)
    
    is_active = models.BooleanField("Активно", default=True)
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    
    class Meta:
        verbose_name = "Комиссия"
        verbose_name_plural = "Комиссии"
        ordering = ['commission_type', 'name_ru']
        
    def __str__(self):
        return self.name_ru


class ScientificJournal(models.Model):
    """Научные журналы университета"""
    title_ru = models.CharField("Название (рус)", max_length=300)
    title_en = models.CharField("Название (англ)", max_length=300)
    title_kg = models.CharField("Название (кыр)", max_length=300)
    
    description_ru = models.TextField("Описание (рус)")
    description_en = models.TextField("Описание (англ)")
    description_kg = models.TextField("Описание (кыр)")
    
    issn = models.CharField("ISSN", max_length=20, blank=True)
    eissn = models.CharField("E-ISSN", max_length=20, blank=True)
    
    editor_in_chief_ru = models.CharField("Главный редактор (рус)", max_length=200)
    editor_in_chief_en = models.CharField("Главный редактор (англ)", max_length=200)
    editor_in_chief_kg = models.CharField("Главный редактор (кыр)", max_length=200)
    
    editorial_board_ru = models.JSONField("Редакционная коллегия (рус)", default=list)
    editorial_board_en = models.JSONField("Редакционная коллегия (англ)", default=list)
    editorial_board_kg = models.JSONField("Редакционная коллегия (кыр)", default=list)
    
    publication_frequency_ru = models.CharField("Периодичность (рус)", max_length=100)
    publication_frequency_en = models.CharField("Периодичность (англ)", max_length=100)
    publication_frequency_kg = models.CharField("Периодичность (кыр)", max_length=100)
    
    scope_ru = models.TextField("Тематика (рус)", blank=True)
    scope_en = models.TextField("Тематика (англ)", blank=True)
    scope_kg = models.TextField("Тематика (кыр)", blank=True)
    
    submission_guidelines_ru = models.TextField("Требования к публикации (рус)", blank=True)
    submission_guidelines_en = models.TextField("Требования к публикации (англ)", blank=True)
    submission_guidelines_kg = models.TextField("Требования к публикации (кыр)", blank=True)
    
    cover_image = models.ImageField("Обложка", upload_to='research/journals/', blank=True)
    website = models.URLField("Веб-сайт", blank=True)
    contact_email = models.EmailField("Email", blank=True)
    
    established_year = models.IntegerField("Год основания")
    impact_factor = models.DecimalField("Импакт-фактор", max_digits=5, decimal_places=3, null=True, blank=True)
    
    is_open_access = models.BooleanField("Открытый доступ", default=True)
    is_peer_reviewed = models.BooleanField("Рецензируемый", default=True)
    is_active = models.BooleanField("Активно", default=True)
    
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    
    class Meta:
        verbose_name = "Научный журнал"
        verbose_name_plural = "Научные журналы"
        ordering = ['title_ru']
        
    def __str__(self):
        return self.title_ru


class JournalIssue(models.Model):
    """Выпуски журналов"""
    journal = models.ForeignKey(ScientificJournal, on_delete=models.CASCADE, related_name='issues', verbose_name="Журнал")
    
    volume = models.PositiveIntegerField("Том")
    number = models.PositiveIntegerField("Номер")
    year = models.PositiveIntegerField("Год")
    
    title_ru = models.CharField("Название выпуска (рус)", max_length=300, blank=True)
    title_en = models.CharField("Название выпуска (англ)", max_length=300, blank=True)
    title_kg = models.CharField("Название выпуска (кыр)", max_length=300, blank=True)
    
    publication_date = models.DateField("Дата публикации")
    
    description_ru = models.TextField("Описание (рус)", blank=True)
    description_en = models.TextField("Описание (англ)", blank=True)
    description_kg = models.TextField("Описание (кыр)", blank=True)
    
    cover_image = models.ImageField("Обложка выпуска", upload_to='research/journal_issues/', blank=True)
    pdf_file = models.FileField("PDF файл", upload_to='research/journal_issues/pdf/', blank=True)
    
    doi = models.CharField("DOI выпуска", max_length=100, blank=True)
    pages_count = models.PositiveIntegerField("Количество страниц", null=True, blank=True)
    articles_count = models.PositiveIntegerField("Количество статей", default=0)
    
    is_published = models.BooleanField("Опубликован", default=False)
    is_active = models.BooleanField("Активно", default=True)
    
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)
    
    class Meta:
        verbose_name = "Выпуск журнала"
        verbose_name_plural = "Выпуски журналов"
        ordering = ['-year', '-volume', '-number']
        unique_together = ['journal', 'volume', 'number', 'year']
        
    def __str__(self):
        return f"{self.journal.title_ru} - Том {self.volume}, №{self.number} ({self.year})"


class JournalArticle(models.Model):
    """Статьи в журналах"""
    issue = models.ForeignKey(JournalIssue, on_delete=models.CASCADE, related_name='articles', verbose_name="Выпуск")
    
    title_ru = models.CharField("Название (рус)", max_length=500)
    title_en = models.CharField("Название (англ)", max_length=500)
    title_kg = models.CharField("Название (кыр)", max_length=500)
    
    authors_ru = models.CharField("Авторы (рус)", max_length=500)
    authors_en = models.CharField("Авторы (англ)", max_length=500)
    authors_kg = models.CharField("Авторы (кыр)", max_length=500)
    
    abstract_ru = models.TextField("Аннотация (рус)")
    abstract_en = models.TextField("Аннотация (англ)")
    abstract_kg = models.TextField("Аннотация (кыр)")
    
    keywords_ru = models.JSONField("Ключевые слова (рус)", default=list)
    keywords_en = models.JSONField("Ключевые слова (англ)", default=list)
    keywords_kg = models.JSONField("Ключевые слова (кыр)", default=list)
    
    pages_start = models.PositiveIntegerField("Страница начала")
    pages_end = models.PositiveIntegerField("Страница окончания")
    
    doi = models.CharField("DOI статьи", max_length=100, blank=True)
    pdf_file = models.FileField("PDF файл статьи", upload_to='research/journal_articles/', blank=True)
    
    received_date = models.DateField("Дата поступления", null=True, blank=True)
    accepted_date = models.DateField("Дата принятия", null=True, blank=True)
    published_date = models.DateField("Дата публикации", null=True, blank=True)
    
    citations_count = models.PositiveIntegerField("Количество цитирований", default=0)
    
    order = models.PositiveIntegerField("Порядок в выпуске", default=0)
    
    is_open_access = models.BooleanField("Открытый доступ", default=True)
    is_active = models.BooleanField("Активно", default=True)
    
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    
    class Meta:
        verbose_name = "Статья журнала"
        verbose_name_plural = "Статьи журналов"
        ordering = ['issue', 'order', 'pages_start']
        
    def __str__(self):
        return f"{self.title_ru} ({self.issue})"
