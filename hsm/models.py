from django.db import models
from django.utils import timezone


class QualityPrinciple(models.Model):
    """Принципы системы менеджмента качества"""
    title = models.CharField(max_length=200, verbose_name="Название принципа")
    title_kg = models.CharField(max_length=200, verbose_name="Название принципа (кыргызский)", blank=True)
    title_en = models.CharField(max_length=200, verbose_name="Название принципа (английский)", blank=True)
    
    description = models.TextField(verbose_name="Описание принципа")
    description_kg = models.TextField(verbose_name="Описание принципа (кыргызский)", blank=True)
    description_en = models.TextField(verbose_name="Описание принципа (английский)", blank=True)
    
    icon = models.CharField(max_length=50, verbose_name="Иконка", default="🌟")
    order = models.PositiveIntegerField(verbose_name="Порядок отображения", default=0)
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Принцип качества"
        verbose_name_plural = "Принципы качества"
        ordering = ['order']
    
    def __str__(self):
        return self.title


class QualityDocument(models.Model):
    """Документы системы менеджмента качества"""
    DOCUMENT_TYPES = [
        ('pdf', 'PDF'),
        ('doc', 'DOC'),
        ('docx', 'DOCX'),
        ('xls', 'XLS'),
        ('xlsx', 'XLSX'),
    ]
    
    DOCUMENT_CATEGORIES = [
        ('policy', 'Политика качества'),
        ('manual', 'Руководство по качеству'),
        ('procedure', 'Процедуры'),
        ('instruction', 'Рабочие инструкции'),
        ('record', 'Записи'),
        ('regulation', 'Положения'),
        ('standard', 'Стандарты'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Название документа")
    title_kg = models.CharField(max_length=200, verbose_name="Название документа (KG)", blank=True)
    title_en = models.CharField(max_length=200, verbose_name="Название документа (EN)", blank=True)
    
    description = models.TextField(verbose_name="Описание", blank=True)
    description_kg = models.TextField(verbose_name="Описание (KG)", blank=True)
    description_en = models.TextField(verbose_name="Описание (EN)", blank=True)
    
    category = models.CharField(max_length=20, choices=DOCUMENT_CATEGORIES, verbose_name="Категория")
    document_type = models.CharField(max_length=10, choices=DOCUMENT_TYPES, verbose_name="Тип файла")
    file_size = models.CharField(max_length=20, verbose_name="Размер файла", blank=True)
    file_path = models.FileField(upload_to='hsm/documents/', verbose_name="Файл", blank=True, null=True)
    external_url = models.URLField(verbose_name="Внешняя ссылка", blank=True)
    
    version = models.CharField(max_length=20, verbose_name="Версия", default="1.0")
    approval_date = models.DateField(verbose_name="Дата утверждения", null=True, blank=True)
    effective_date = models.DateField(verbose_name="Дата вступления в силу", null=True, blank=True)
    expiry_date = models.DateField(verbose_name="Дата истечения", null=True, blank=True)
    
    order = models.PositiveIntegerField(verbose_name="Порядок отображения", default=0)
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    download_count = models.PositiveIntegerField(default=0, verbose_name="Количество скачиваний")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Документ качества"
        verbose_name_plural = "Документы качества"
        ordering = ['category', 'order']
    
    def __str__(self):
        return f"{self.title} v{self.version}"


class QualityProcessGroup(models.Model):
    """Группы процессов системы менеджмента качества"""
    title = models.CharField(max_length=200, verbose_name="Название группы процессов")
    title_kg = models.CharField(max_length=200, verbose_name="Название группы процессов (KG)", blank=True)
    title_en = models.CharField(max_length=200, verbose_name="Название группы процессов (EN)", blank=True)
    
    description = models.TextField(verbose_name="Описание группы", blank=True)
    description_kg = models.TextField(verbose_name="Описание группы (KG)", blank=True)
    description_en = models.TextField(verbose_name="Описание группы (EN)", blank=True)
    
    icon = models.CharField(max_length=50, verbose_name="Иконка", default="🔄")
    order = models.PositiveIntegerField(verbose_name="Порядок отображения", default=0)
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Группа процессов"
        verbose_name_plural = "Группы процессов"
        ordering = ['order']
    
    def __str__(self):
        return self.title


class QualityProcess(models.Model):
    """Процессы системы менеджмента качества"""
    group = models.ForeignKey(QualityProcessGroup, on_delete=models.CASCADE, related_name='processes', verbose_name="Группа процессов")
    
    title = models.CharField(max_length=200, verbose_name="Название процесса")
    title_kg = models.CharField(max_length=200, verbose_name="Название процесса (KG)", blank=True)
    title_en = models.CharField(max_length=200, verbose_name="Название процесса (EN)", blank=True)
    
    description = models.TextField(verbose_name="Описание процесса", blank=True)
    description_kg = models.TextField(verbose_name="Описание процесса (KG)", blank=True)
    description_en = models.TextField(verbose_name="Описание процесса (EN)", blank=True)
    
    responsible_person = models.CharField(max_length=200, verbose_name="Ответственное лицо", blank=True)
    responsible_department = models.CharField(max_length=200, verbose_name="Ответственное подразделение", blank=True)
    
    order = models.PositiveIntegerField(verbose_name="Порядок отображения", default=0)
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Процесс качества"
        verbose_name_plural = "Процессы качества"
        ordering = ['group__order', 'order']
    
    def __str__(self):
        return f"{self.group.title} - {self.title}"


class QualityStatistic(models.Model):
    """Статистика системы менеджмента качества"""
    title = models.CharField(max_length=200, verbose_name="Название показателя")
    title_kg = models.CharField(max_length=200, verbose_name="Название показателя (KG)", blank=True)
    title_en = models.CharField(max_length=200, verbose_name="Название показателя (EN)", blank=True)
    
    value = models.CharField(max_length=50, verbose_name="Значение")
    unit = models.CharField(max_length=50, verbose_name="Единица измерения", blank=True)
    
    description = models.TextField(verbose_name="Описание", blank=True)
    description_kg = models.TextField(verbose_name="Описание (KG)", blank=True)
    description_en = models.TextField(verbose_name="Описание (EN)", blank=True)
    
    icon = models.CharField(max_length=50, verbose_name="Иконка", default="📊")
    order = models.PositiveIntegerField(verbose_name="Порядок отображения", default=0)
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Статистика качества"
        verbose_name_plural = "Статистика качества"
        ordering = ['order']
    
    def __str__(self):
        return f"{self.title}: {self.value}"


class QualityAdvantage(models.Model):
    """Преимущества системы менеджмента качества"""
    title = models.CharField(max_length=200, verbose_name="Преимущество")
    title_kg = models.CharField(max_length=200, verbose_name="Преимущество (KG)", blank=True)
    title_en = models.CharField(max_length=200, verbose_name="Преимущество (EN)", blank=True)
    
    description = models.TextField(verbose_name="Описание", blank=True)
    description_kg = models.TextField(verbose_name="Описание (KG)", blank=True)
    description_en = models.TextField(verbose_name="Описание (EN)", blank=True)
    
    icon = models.CharField(max_length=50, verbose_name="Иконка", default="✓")
    order = models.PositiveIntegerField(verbose_name="Порядок отображения", default=0)
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Преимущество качества"
        verbose_name_plural = "Преимущества качества"
        ordering = ['order']
    
    def __str__(self):
        return self.title


class QualitySettings(models.Model):
    """Общие настройки системы менеджмента качества"""
    title = models.CharField(max_length=200, verbose_name="Заголовок страницы")
    title_kg = models.CharField(max_length=200, verbose_name="Заголовок страницы (KG)", blank=True)
    title_en = models.CharField(max_length=200, verbose_name="Заголовок страницы (EN)", blank=True)
    
    description = models.TextField(verbose_name="Описание")
    description_kg = models.TextField(verbose_name="Описание (KG)", blank=True)
    description_en = models.TextField(verbose_name="Описание (EN)", blank=True)
    
    about_text = models.TextField(verbose_name="О системе качества")
    about_text_kg = models.TextField(verbose_name="О системе качества (KG)", blank=True)
    about_text_en = models.TextField(verbose_name="О системе качества (EN)", blank=True)
    
    iso_standard = models.CharField(max_length=50, verbose_name="Стандарт ISO", default="ISO 9001:2015")
    compliance_percentage = models.CharField(max_length=10, verbose_name="Процент соответствия", default="100%")
    
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Настройки качества"
        verbose_name_plural = "Настройки качества"
    
    def __str__(self):
        return self.title


class Leadership(models.Model):
    """Руководство ВШМ"""
    LEADERSHIP_TYPES = [
        ('director', 'Директор'),
        ('deputy_director', 'Заместитель директора'),
        ('department_head', 'Заведующий кафедрой'),
        ('dean', 'Декан'),
        ('vice_dean', 'Заместитель декана'),
    ]
    
    
    # Имя
    name = models.CharField(max_length=200, verbose_name="ФИО")
    name_kg = models.CharField(max_length=200, verbose_name="ФИО (KG)", blank=True)
    name_en = models.CharField(max_length=200, verbose_name="ФИО (EN)", blank=True)
    
    # Должность
    position = models.CharField(max_length=200, verbose_name="Должность")
    position_kg = models.CharField(max_length=200, verbose_name="Должность (KG)", blank=True)
    position_en = models.CharField(max_length=200, verbose_name="Должность (EN)", blank=True)
    
    # Ученая степень
    degree = models.CharField(max_length=200, verbose_name="Ученая степень")
    degree_kg = models.CharField(max_length=200, verbose_name="Ученая степень (KG)", blank=True)
    degree_en = models.CharField(max_length=200, verbose_name="Ученая степень (EN)", blank=True)
    
    # Опыт работы
    experience = models.CharField(max_length=100, verbose_name="Опыт работы")
    experience_kg = models.CharField(max_length=100, verbose_name="Опыт работы (KG)", blank=True)
    experience_en = models.CharField(max_length=100, verbose_name="Опыт работы (EN)", blank=True)
    
    # Биография
    bio = models.TextField(verbose_name="Биография", blank=True)
    bio_kg = models.TextField(verbose_name="Биография (KG)", blank=True)
    bio_en = models.TextField(verbose_name="Биография (EN)", blank=True)
    
    # Достижения (JSON поле для списка достижений)
    achievements = models.JSONField(default=list, verbose_name="Достижения", blank=True)
    achievements_kg = models.JSONField(default=list, verbose_name="Достижения (KG)", blank=True)
    achievements_en = models.JSONField(default=list, verbose_name="Достижения (EN)", blank=True)
    
    # Департамент/кафедра
    department = models.CharField(max_length=50,  verbose_name="Департамент(RU)", blank=True)
    department_kg = models.CharField(max_length=200, verbose_name="Департамент (KG)", blank=True)
    department_en = models.CharField(max_length=200, verbose_name="Департамент (EN)", blank=True)
    
    # Специализация (для заведующих кафедрами)
    specialization = models.TextField(verbose_name="Специализация", blank=True)
    specialization_kg = models.TextField(verbose_name="Специализация (KG)", blank=True)
    specialization_en = models.TextField(verbose_name="Специализация (EN)", blank=True)
    
    # Количество сотрудников (для заведующих)
    staff_count = models.CharField(max_length=100, verbose_name="Количество сотрудников", blank=True)
    staff_count_kg = models.CharField(max_length=100, verbose_name="Количество сотрудников (KG)", blank=True)
    staff_count_en = models.CharField(max_length=100, verbose_name="Количество сотрудников (EN)", blank=True)
    
    # Контакты
    email = models.EmailField(verbose_name="Email", blank=True)
    phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True)
    
    # Фото
    image = models.ImageField(upload_to='leadership/photos/', verbose_name="Фото", blank=True)
    
    # Тип руководства и статус директора
    leadership_type = models.CharField(max_length=20, choices=LEADERSHIP_TYPES, verbose_name="Тип руководства")
    is_director = models.BooleanField(default=False, verbose_name="Является директором")
    
    # Системные поля
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    order = models.IntegerField(default=0, verbose_name="Порядок отображения")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Руководитель"
        verbose_name_plural = "Руководство"
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.name} - {self.position}"


class Faculty(models.Model):
    """Профессорско-преподавательский состав ВШМ"""
    ACADEMIC_DEGREES = [
        ('candidate', 'Кандидат наук'),
        ('doctor', 'Доктор наук'),
        ('phd', 'PhD'),
        ('master', 'Магистр'),
        ('bachelor', 'Бакалавр'),
    ]
    
    POSITIONS = [
        ('professor', 'Профессор'),
        ('associate_professor', 'Доцент'),
        ('senior_lecturer', 'Старший преподаватель'),
        ('lecturer', 'Преподаватель'),
        ('assistant', 'Ассистент'),
        ('head_of_department', 'Заведующий кафедрой'),
        ('dean', 'Декан'),
        ('vice_dean', 'Заместитель декана'),
    ]
    
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=100, verbose_name="Отчество", blank=True)
    
    first_name_kg = models.CharField(max_length=100, verbose_name="Имя (KG)", blank=True)
    last_name_kg = models.CharField(max_length=100, verbose_name="Фамилия (KG)", blank=True)
    middle_name_kg = models.CharField(max_length=100, verbose_name="Отчество (KG)", blank=True)
    
    first_name_en = models.CharField(max_length=100, verbose_name="Имя (EN)", blank=True)
    last_name_en = models.CharField(max_length=100, verbose_name="Фамилия (EN)", blank=True)
    middle_name_en = models.CharField(max_length=100, verbose_name="Отчество (EN)", blank=True)
    
    position = models.CharField(max_length=50, choices=POSITIONS, verbose_name="Должность")
    position_custom = models.CharField(max_length=200, verbose_name="Дополнительная должность", blank=True)
    position_kg = models.CharField(max_length=200, verbose_name="Должность (KG)", blank=True)
    position_en = models.CharField(max_length=200, verbose_name="Должность (EN)", blank=True)
    
    academic_degree = models.CharField(max_length=20, choices=ACADEMIC_DEGREES, verbose_name="Ученая степень", blank=True)
    academic_degree_kg = models.CharField(max_length=200, verbose_name="Ученая степень (KG)", blank=True)
    academic_degree_en = models.CharField(max_length=200, verbose_name="Ученая степень (EN)", blank=True)
    academic_title = models.CharField(max_length=200, verbose_name="Ученое звание", blank=True)
    academic_title_kg = models.CharField(max_length=200, verbose_name="Ученое звание (KG)", blank=True)
    academic_title_en = models.CharField(max_length=200, verbose_name="Ученое звание (EN)", blank=True)
    
    photo = models.ImageField(upload_to='faculty/photos/', verbose_name="Фото", blank=True)
    
    email = models.EmailField(verbose_name="Email", blank=True)
    phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True)
    office = models.CharField(max_length=100, verbose_name="Кабинет", blank=True)
    
    bio = models.TextField(verbose_name="Биография", blank=True)
    bio_kg = models.TextField(verbose_name="Биография (KG)", blank=True)
    bio_en = models.TextField(verbose_name="Биография (EN)", blank=True)
    
    specialization = models.TextField(verbose_name="Специализация", blank=True)
    specialization_kg = models.TextField(verbose_name="Специализация (KG)", blank=True)
    specialization_en = models.TextField(verbose_name="Специализация (EN)", blank=True)
    
    education = models.TextField(verbose_name="Образование", blank=True)
    education_kg = models.TextField(verbose_name="Образование (KG)", blank=True)
    education_en = models.TextField(verbose_name="Образование (EN)", blank=True)
    
    experience = models.TextField(verbose_name="Опыт работы", blank=True)
    experience_kg = models.TextField(verbose_name="Опыт работы (KG)", blank=True)
    experience_en = models.TextField(verbose_name="Опыт работы (EN)", blank=True)
    
    publications = models.TextField(verbose_name="Публикации", blank=True)
    publications_kg = models.TextField(verbose_name="Публикации (KG)", blank=True)
    publications_en = models.TextField(verbose_name="Публикации (EN)", blank=True)
    
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    order = models.IntegerField(default=0, verbose_name="Порядок отображения")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Профессорско-преподавательский состав"
        ordering = ['order', 'last_name', 'first_name']
    
    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}".strip()
    
    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}".strip()


class Accreditation(models.Model):
    """Аккредитации и сертификаты ВШМ"""
    ACCREDITATION_TYPES = [
        ('national', 'Национальная'),
        ('international', 'Международная'),
        ('institutional', 'Институциональная'),
        ('programmatic', 'Программная'),
    ]
    
    name = models.CharField(max_length=200, verbose_name="Название")
    name_kg = models.CharField(max_length=200, verbose_name="Название (KG)", blank=True)
    name_en = models.CharField(max_length=200, verbose_name="Название (EN)", blank=True)
    
    organization = models.CharField(max_length=200, verbose_name="Аккредитующая организация")
    organization_kg = models.CharField(max_length=200, verbose_name="Аккредитующая организация (KG)", blank=True)
    organization_en = models.CharField(max_length=200, verbose_name="Аккредитующая организация (EN)", blank=True)
    
    accreditation_type = models.CharField(max_length=20, choices=ACCREDITATION_TYPES, verbose_name="Тип аккредитации")
    accreditation_type_kg = models.CharField(max_length=100, verbose_name="Тип аккредитации (KG)", blank=True)
    accreditation_type_en = models.CharField(max_length=100, verbose_name="Тип аккредитации (EN)", blank=True)
    
    description = models.TextField(verbose_name="Описание", blank=True)
    description_kg = models.TextField(verbose_name="Описание (KG)", blank=True)
    description_en = models.TextField(verbose_name="Описание (EN)", blank=True)
    
    certificate_image = models.ImageField(upload_to='accreditations/certificates/', verbose_name="Сертификат", blank=True)
    organization_logo = models.ImageField(upload_to='accreditations/logos/', verbose_name="Логотип организации", blank=True)
    
    issue_date = models.DateField(verbose_name="Дата выдачи")
    expiry_date = models.DateField(verbose_name="Дата окончания", blank=True, null=True)
    
    certificate_number = models.CharField(max_length=100, verbose_name="Номер сертификата", blank=True)
    
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    order = models.IntegerField(default=0, verbose_name="Порядок отображения")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Аккредитация"
        verbose_name_plural = "Аккредитации"
        ordering = ['order', '-issue_date']
    
    def __str__(self):
        return f"{self.name} - {self.organization}"
    
    @property
    def is_valid(self):
        """Проверяет, действительна ли аккредитация"""
        if self.expiry_date:
            return timezone.now().date() <= self.expiry_date
        return True


