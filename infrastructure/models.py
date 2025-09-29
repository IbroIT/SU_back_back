from django.db import models
from django.utils.translation import gettext_lazy as _


class Hospital(models.Model):
    name_ru = models.CharField(max_length=200, verbose_name=_("Название (рус)"))
    name_kg = models.CharField(max_length=200, verbose_name=_("Название (кырг)"))
    name_en = models.CharField(max_length=200, verbose_name=_("Название (англ)"))
    
    description_ru = models.TextField(verbose_name=_("Описание (рус)"))
    description_kg = models.TextField(verbose_name=_("Описание (кырг)"))
    description_en = models.TextField(verbose_name=_("Описание (англ)"))
    
    address_ru = models.CharField(max_length=300, verbose_name=_("Адрес (рус)"))
    address_kg = models.CharField(max_length=300, verbose_name=_("Адрес (кырг)"))
    address_en = models.CharField(max_length=300, verbose_name=_("Адрес (англ)"))
    
    practice_opportunities_ru = models.TextField(verbose_name=_("Возможности практики (рус)"))
    practice_opportunities_kg = models.TextField(verbose_name=_("Возможности практики (кырг)"))
    practice_opportunities_en = models.TextField(verbose_name=_("Возможности практики (англ)"))
    
    contact_phone = models.CharField(max_length=50, verbose_name=_("Контактный телефон"))
    contact_email = models.EmailField(blank=True, verbose_name=_("Email"))
    
    photo = models.ImageField(upload_to='infrastructure/hospitals/', verbose_name=_("Фото"))
    
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name=_("Широта"))
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name=_("Долгота"))
    
    is_active = models.BooleanField(default=True, verbose_name=_("Активный"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))

    class Meta:
        ordering = ['order', 'name_ru']
        verbose_name = _("Больница")
        verbose_name_plural = _("Больницы")

    def __str__(self):
        return self.name_ru


class HospitalDepartment(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='departments', verbose_name=_("Больница"))
    
    name_ru = models.CharField(max_length=200, verbose_name=_("Название отделения (рус)"))
    name_kg = models.CharField(max_length=200, verbose_name=_("Название отделения (кырг)"))
    name_en = models.CharField(max_length=200, verbose_name=_("Название отделения (англ)"))
    
    description_ru = models.TextField(verbose_name=_("Описание (рус)"))
    description_kg = models.TextField(verbose_name=_("Описание (кырг)"))
    description_en = models.TextField(verbose_name=_("Описание (англ)"))
    
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))

    class Meta:
        ordering = ['order', 'name_ru']
        verbose_name = _("Отделение больницы")
        verbose_name_plural = _("Отделения больниц")

    def __str__(self):
        return f"{self.hospital.name_ru} - {self.name_ru}"


class Laboratory(models.Model):
    LAB_TYPES = [
        ('biochemistry', _('Биохимия')),
        ('anatomy', _('Анатомия')),
        ('pharmacy', _('Фармацевтика')),
        ('microbiology', _('Микробиология')),
        ('pathology', _('Патология')),
        ('physiology', _('Физиология')),
        ('other', _('Другое')),
    ]
    
    name_ru = models.CharField(max_length=200, verbose_name=_("Название (рус)"))
    name_kg = models.CharField(max_length=200, verbose_name=_("Название (кырг)"))
    name_en = models.CharField(max_length=200, verbose_name=_("Название (англ)"))
    
    type = models.CharField(max_length=20, choices=LAB_TYPES, verbose_name=_("Тип лаборатории"))
    
    description_ru = models.TextField(verbose_name=_("Описание (рус)"))
    description_kg = models.TextField(verbose_name=_("Описание (кырг)"))
    description_en = models.TextField(verbose_name=_("Описание (англ)"))
    
    schedule_ru = models.CharField(max_length=200, verbose_name=_("График работы (рус)"))
    schedule_kg = models.CharField(max_length=200, verbose_name=_("График работы (кырг)"))
    schedule_en = models.CharField(max_length=200, verbose_name=_("График работы (англ)"))
    
    requirements_ru = models.TextField(verbose_name=_("Требования (рус)"))
    requirements_kg = models.TextField(verbose_name=_("Требования (кырг)"))
    requirements_en = models.TextField(verbose_name=_("Требования (англ)"))
    
    capacity = models.PositiveIntegerField(verbose_name=_("Вместимость (студентов)"))
    
    photo = models.ImageField(upload_to='infrastructure/laboratories/', verbose_name=_("Фото"))
    
    is_active = models.BooleanField(default=True, verbose_name=_("Активный"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))

    class Meta:
        ordering = ['order', 'name_ru']
        verbose_name = _("Лаборатория")
        verbose_name_plural = _("Лаборатории")

    def __str__(self):
        return self.name_ru


class LaboratoryEquipment(models.Model):
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE, related_name='equipment', verbose_name=_("Лаборатория"))
    
    name_ru = models.CharField(max_length=200, verbose_name=_("Название оборудования (рус)"))
    name_kg = models.CharField(max_length=200, verbose_name=_("Название оборудования (кырг)"))
    name_en = models.CharField(max_length=200, verbose_name=_("Название оборудования (англ)"))
    
    description_ru = models.TextField(verbose_name=_("Описание (рус)"))
    description_kg = models.TextField(verbose_name=_("Описание (кырг)"))
    description_en = models.TextField(verbose_name=_("Описание (англ)"))
    
    photo = models.ImageField(upload_to='infrastructure/equipment/', blank=True, verbose_name=_("Фото оборудования"))
    
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))

    class Meta:
        ordering = ['order', 'name_ru']
        verbose_name = _("Оборудование лаборатории")
        verbose_name_plural = _("Оборудование лабораторий")

    def __str__(self):
        return f"{self.laboratory.name_ru} - {self.name_ru}"


class AcademicBuilding(models.Model):
    name_ru = models.CharField(max_length=200, verbose_name=_("Название (рус)"))
    name_kg = models.CharField(max_length=200, verbose_name=_("Название (кырг)"))
    name_en = models.CharField(max_length=200, verbose_name=_("Название (англ)"))
    
    description_ru = models.TextField(verbose_name=_("Описание (рус)"))
    description_kg = models.TextField(verbose_name=_("Описание (кырг)"))
    description_en = models.TextField(verbose_name=_("Описание (англ)"))
    
    address_ru = models.CharField(max_length=300, verbose_name=_("Адрес (рус)"))
    address_kg = models.CharField(max_length=300, verbose_name=_("Адрес (кырг)"))
    address_en = models.CharField(max_length=300, verbose_name=_("Адрес (англ)"))
    
    floors = models.PositiveIntegerField(verbose_name=_("Количество этажей"))
    
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name=_("Широта"))
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name=_("Долгота"))
    
    is_active = models.BooleanField(default=True, verbose_name=_("Активный"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))

    class Meta:
        ordering = ['order', 'name_ru']
        verbose_name = _("Учебный корпус")
        verbose_name_plural = _("Учебные корпуса")

    def __str__(self):
        return self.name_ru


class BuildingFacility(models.Model):
    building = models.ForeignKey(AcademicBuilding, on_delete=models.CASCADE, related_name='facilities', verbose_name=_("Здание"))
    
    name_ru = models.CharField(max_length=200, verbose_name=_("Название помещения (рус)"))
    name_kg = models.CharField(max_length=200, verbose_name=_("Название помещения (кырг)"))
    name_en = models.CharField(max_length=200, verbose_name=_("Название помещения (англ)"))
    
    count = models.PositiveIntegerField(verbose_name=_("Количество"))
    capacity_ru = models.CharField(max_length=100, verbose_name=_("Вместимость (рус)"))
    capacity_kg = models.CharField(max_length=100, verbose_name=_("Вместимость (кырг)"))
    capacity_en = models.CharField(max_length=100, verbose_name=_("Вместимость (англ)"))
    
    # Для совместимости со старыми данными
    capacity = models.CharField(max_length=100, verbose_name=_("Вместимость (устар.)"), blank=True, null=True)
    
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))

    class Meta:
        ordering = ['order', 'name_ru']
        verbose_name = _("Помещение здания")
        verbose_name_plural = _("Помещения зданий")

    def __str__(self):
        return f"{self.building.name_ru} - {self.name_ru}"


class BuildingPhoto(models.Model):
    PHOTO_TYPES = [
        ('facade', _('Фасад')),
        ('lobby', _('Холл')),
        ('lecture_hall', _('Лекционный зал')),
        ('library', _('Библиотека')),
        ('lab', _('Лаборатория')),
        ('anatomy', _('Анатомический зал')),
        ('simulation', _('Симуляционный центр')),
        ('conference', _('Конференц-зал')),
        ('office', _('Офис')),
        ('assembly', _('Актовый зал')),
        ('cafeteria', _('Столовая')),
        ('gym', _('Спортзал')),
        ('other', _('Другое')),
    ]
    
    building = models.ForeignKey(AcademicBuilding, on_delete=models.CASCADE, related_name='photos', verbose_name=_("Здание"))
    
    photo = models.ImageField(upload_to='infrastructure/buildings/', verbose_name=_("Фото"))
    type = models.CharField(max_length=20, choices=PHOTO_TYPES, verbose_name=_("Тип фото"))
    
    title_ru = models.CharField(max_length=200, blank=True, verbose_name=_("Заголовок (рус)"))
    title_kg = models.CharField(max_length=200, blank=True, verbose_name=_("Заголовок (кырг)"))
    title_en = models.CharField(max_length=200, blank=True, verbose_name=_("Заголовок (англ)"))
    
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))

    class Meta:
        ordering = ['order', 'type']
        verbose_name = _("Фото здания")
        verbose_name_plural = _("Фото зданий")

    def __str__(self):
        return f"{self.building.name_ru} - {self.get_type_display()}"


class Dormitory(models.Model):
    DORMITORY_TYPES = [
        ('male', _('Мужское')),
        ('female', _('Женское')),
        ('family', _('Семейное')),
        ('mixed', _('Смешанное')),
    ]
    
    name_ru = models.CharField(max_length=200, verbose_name=_("Название (рус)"))
    name_kg = models.CharField(max_length=200, verbose_name=_("Название (кырг)"))
    name_en = models.CharField(max_length=200, verbose_name=_("Название (англ)"))
    
    type = models.CharField(max_length=10, choices=DORMITORY_TYPES, verbose_name=_("Тип общежития"))
    
    description_ru = models.TextField(verbose_name=_("Описание (рус)"))
    description_kg = models.TextField(verbose_name=_("Описание (кырг)"))
    description_en = models.TextField(verbose_name=_("Описание (англ)"))
    
    address_ru = models.CharField(max_length=300, verbose_name=_("Адрес (рус)"))
    address_kg = models.CharField(max_length=300, verbose_name=_("Адрес (кырг)"))
    address_en = models.CharField(max_length=300, verbose_name=_("Адрес (англ)"))
    
    capacity = models.PositiveIntegerField(verbose_name=_("Общая вместимость"))
    available = models.PositiveIntegerField(verbose_name=_("Доступные места"))
    
    is_active = models.BooleanField(default=True, verbose_name=_("Активный"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))

    class Meta:
        ordering = ['order', 'name_ru']
        verbose_name = _("Общежитие")
        verbose_name_plural = _("Общежития")

    def __str__(self):
        return self.name_ru


class DormitoryRoom(models.Model):
    ROOM_TYPES = [
        ('single', _('Одноместная')),
        ('double', _('Двухместная')),
        ('triple', _('Трёхместная')),
        ('studio', _('Студия')),
        ('one_bedroom', _('Однокомнатная')),
        ('two_bedroom', _('Двухкомнатная')),
    ]
    
    dormitory = models.ForeignKey(Dormitory, on_delete=models.CASCADE, related_name='rooms', verbose_name=_("Общежитие"))
    
    type = models.CharField(max_length=20, choices=ROOM_TYPES, verbose_name=_("Тип комнаты"))
    
    name_ru = models.CharField(max_length=200, verbose_name=_("Название (рус)"))
    name_kg = models.CharField(max_length=200, verbose_name=_("Название (кырг)"))
    name_en = models.CharField(max_length=200, verbose_name=_("Название (англ)"))
    
    price_monthly = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Цена за месяц (сом)"))
    
    features_ru = models.TextField(verbose_name=_("Особенности (рус)"))
    features_kg = models.TextField(verbose_name=_("Особенности (кырг)"))
    features_en = models.TextField(verbose_name=_("Особенности (англ)"))
    
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))

    class Meta:
        ordering = ['order', 'price_monthly']
        verbose_name = _("Комната общежития")
        verbose_name_plural = _("Комнаты общежитий")

    def __str__(self):
        return f"{self.dormitory.name_ru} - {self.name_ru}"


class DormitoryFacility(models.Model):
    dormitory = models.ForeignKey(Dormitory, on_delete=models.CASCADE, related_name='facilities', verbose_name=_("Общежитие"))
    
    name_ru = models.CharField(max_length=200, verbose_name=_("Название удобства (рус)"))
    name_kg = models.CharField(max_length=200, verbose_name=_("Название удобства (кырг)"))
    name_en = models.CharField(max_length=200, verbose_name=_("Название удобства (англ)"))
    
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))

    class Meta:
        ordering = ['order', 'name_ru']
        verbose_name = _("Удобство общежития")
        verbose_name_plural = _("Удобства общежитий")

    def __str__(self):
        return f"{self.dormitory.name_ru} - {self.name_ru}"


class DormitoryPhoto(models.Model):
    PHOTO_TYPES = [
        ('exterior', _('Внешний вид')),
        ('room', _('Комната')),
        ('kitchen', _('Кухня')),
        ('common', _('Общая зона')),
        ('sports', _('Спортивная комната')),
        ('apartment', _('Квартира')),
        ('playground', _('Игровая площадка')),
        ('parking', _('Парковка')),
        ('other', _('Другое')),
    ]
    
    dormitory = models.ForeignKey(Dormitory, on_delete=models.CASCADE, related_name='photos', verbose_name=_("Общежитие"))
    
    photo = models.ImageField(upload_to='infrastructure/dormitories/', verbose_name=_("Фото"))
    type = models.CharField(max_length=20, choices=PHOTO_TYPES, verbose_name=_("Тип фото"))
    
    title_ru = models.CharField(max_length=200, blank=True, verbose_name=_("Заголовок (рус)"))
    title_kg = models.CharField(max_length=200, blank=True, verbose_name=_("Заголовок (кырг)"))
    title_en = models.CharField(max_length=200, blank=True, verbose_name=_("Заголовок (англ)"))
    
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))

    class Meta:
        ordering = ['order', 'type']
        verbose_name = _("Фото общежития")
        verbose_name_plural = _("Фото общежитий")

    def __str__(self):
        return f"{self.dormitory.name_ru} - {self.get_type_display()}"


# === CLASSROOM/AUDIENCE MODELS ===

class ClassroomCategory(models.Model):
    name_ru = models.CharField(max_length=100, verbose_name=_("Название (рус)"))
    name_kg = models.CharField(max_length=100, verbose_name=_("Название (кырг)"))
    name_en = models.CharField(max_length=100, verbose_name=_("Название (англ)"))
    
    icon = models.CharField(max_length=10, default='🏫', verbose_name=_("Иконка"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))

    class Meta:
        ordering = ['order', 'name_ru']
        verbose_name = _("Категория аудитории")
        verbose_name_plural = _("Категории аудиторий")

    def __str__(self):
        return self.name_ru


class Classroom(models.Model):
    category = models.ForeignKey(ClassroomCategory, on_delete=models.CASCADE, related_name='classrooms', verbose_name=_("Категория"))
    
    name_ru = models.CharField(max_length=200, verbose_name=_("Название (рус)"))
    name_kg = models.CharField(max_length=200, verbose_name=_("Название (кырг)"))
    name_en = models.CharField(max_length=200, verbose_name=_("Название (англ)"))
    
    description_ru = models.TextField(verbose_name=_("Описание (рус)"))
    description_kg = models.TextField(verbose_name=_("Описание (кырг)"))
    description_en = models.TextField(verbose_name=_("Описание (англ)"))
    
    capacity = models.PositiveIntegerField(verbose_name=_("Вместимость"))
    floor = models.CharField(max_length=10, verbose_name=_("Этаж"))
    size = models.PositiveIntegerField(verbose_name=_("Размер (м²)"))
    
    image = models.CharField(max_length=10, default='🏫', verbose_name=_("Эмодзи"))
    
    is_active = models.BooleanField(default=True, verbose_name=_("Активная"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))

    class Meta:
        ordering = ['order', 'name_ru']
        verbose_name = _("Аудитория")
        verbose_name_plural = _("Аудитории")

    def __str__(self):
        return self.name_ru


class ClassroomEquipment(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='equipment', verbose_name=_("Аудитория"))
    
    name_ru = models.CharField(max_length=200, verbose_name=_("Название оборудования (рус)"))
    name_kg = models.CharField(max_length=200, verbose_name=_("Название оборудования (кырг)"))
    name_en = models.CharField(max_length=200, verbose_name=_("Название оборудования (англ)"))
    
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))

    class Meta:
        ordering = ['order', 'name_ru']
        verbose_name = _("Оборудование аудитории")
        verbose_name_plural = _("Оборудование аудиторий")

    def __str__(self):
        return f"{self.classroom.name_ru} - {self.name_ru}"


class ClassroomFeature(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='features', verbose_name=_("Аудитория"))
    
    name_ru = models.CharField(max_length=200, verbose_name=_("Название особенности (рус)"))
    name_kg = models.CharField(max_length=200, verbose_name=_("Название особенности (кырг)"))
    name_en = models.CharField(max_length=200, verbose_name=_("Название особенности (англ)"))
    
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))

    class Meta:
        ordering = ['order', 'name_ru']
        verbose_name = _("Особенность аудитории")
        verbose_name_plural = _("Особенности аудиторий")

    def __str__(self):
        return f"{self.classroom.name_ru} - {self.name_ru}"


# === STARTUP MODELS ===

class StartupCategory(models.Model):
    name_ru = models.CharField(max_length=100, verbose_name=_("Название (рус)"))
    name_kg = models.CharField(max_length=100, verbose_name=_("Название (кырг)"))
    name_en = models.CharField(max_length=100, verbose_name=_("Название (англ)"))
    
    icon = models.CharField(max_length=10, default='🚀', verbose_name=_("Иконка"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))

    class Meta:
        ordering = ['order', 'name_ru']
        verbose_name = _("Категория стартапа")
        verbose_name_plural = _("Категории стартапов")

    def __str__(self):
        return self.name_ru


class Startup(models.Model):
    STAGE_CHOICES = [
        ('seed', _('Посевная стадия')),
        ('series_a', _('Серия A')),
        ('growth', _('Рост')),
        ('research', _('Исследования')),
        ('prototype', _('Прототип')),
        ('scaling', _('Масштабирование')),
    ]
    
    STATUS_CHOICES = [
        ('active', _('Активный')),
        ('development', _('В разработке')),
        ('scaling', _('Масштабирование')),
        ('research', _('Исследования')),
        ('prototype', _('Прототип')),
    ]
    
    category = models.ForeignKey(StartupCategory, on_delete=models.CASCADE, related_name='startups', verbose_name=_("Категория"))
    
    name_ru = models.CharField(max_length=200, verbose_name=_("Название (рус)"))
    name_kg = models.CharField(max_length=200, verbose_name=_("Название (кырг)"))
    name_en = models.CharField(max_length=200, verbose_name=_("Название (англ)"))
    
    description_ru = models.TextField(verbose_name=_("Краткое описание (рус)"))
    description_kg = models.TextField(verbose_name=_("Краткое описание (кырг)"))
    description_en = models.TextField(verbose_name=_("Краткое описание (англ)"))
    
    full_description_ru = models.TextField(verbose_name=_("Полное описание (рус)"))
    full_description_kg = models.TextField(verbose_name=_("Полное описание (кырг)"))
    full_description_en = models.TextField(verbose_name=_("Полное описание (англ)"))
    
    stage = models.CharField(max_length=20, choices=STAGE_CHOICES, verbose_name=_("Стадия"))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name=_("Статус"))
    
    funding = models.CharField(max_length=50, verbose_name=_("Финансирование"))
    year = models.CharField(max_length=4, verbose_name=_("Год основания"))
    
    image = models.CharField(max_length=10, default='🚀', verbose_name=_("Эмодзи"))
    
    is_active = models.BooleanField(default=True, verbose_name=_("Активный"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))

    class Meta:
        ordering = ['order', 'name_ru']
        verbose_name = _("Стартап")
        verbose_name_plural = _("Стартапы")

    def __str__(self):
        return self.name_ru


class StartupTeamMember(models.Model):
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE, related_name='team_members', verbose_name=_("Стартап"))
    
    name_ru = models.CharField(max_length=200, verbose_name=_("Имя участника (рус)"))
    name_kg = models.CharField(max_length=200, verbose_name=_("Имя участника (кырг)"))
    name_en = models.CharField(max_length=200, verbose_name=_("Имя участника (англ)"))
    
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))

    class Meta:
        ordering = ['order', 'name_ru']
        verbose_name = _("Участник команды")
        verbose_name_plural = _("Участники команды")

    def __str__(self):
        return f"{self.startup.name_ru} - {self.name_ru}"


class StartupInvestor(models.Model):
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE, related_name='investors', verbose_name=_("Стартап"))
    
    name_ru = models.CharField(max_length=200, verbose_name=_("Название инвестора (рус)"))
    name_kg = models.CharField(max_length=200, verbose_name=_("Название инвестора (кырг)"))
    name_en = models.CharField(max_length=200, verbose_name=_("Название инвестора (англ)"))
    
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))

    class Meta:
        ordering = ['order', 'name_ru']
        verbose_name = _("Инвестор")
        verbose_name_plural = _("Инвесторы")

    def __str__(self):
        return f"{self.startup.name_ru} - {self.name_ru}"


class StartupAchievement(models.Model):
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE, related_name='achievements', verbose_name=_("Стартап"))
    
    achievement_ru = models.CharField(max_length=300, verbose_name=_("Достижение (рус)"))
    achievement_kg = models.CharField(max_length=300, verbose_name=_("Достижение (кырг)"))
    achievement_en = models.CharField(max_length=300, verbose_name=_("Достижение (англ)"))
    
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))

    class Meta:
        ordering = ['order', 'achievement_ru']
        verbose_name = _("Достижение стартапа")
        verbose_name_plural = _("Достижения стартапов")

    def __str__(self):
        return f"{self.startup.name_ru} - {self.achievement_ru[:50]}..."
