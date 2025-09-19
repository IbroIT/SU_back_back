from django.db import models
from django.utils import timezone


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


