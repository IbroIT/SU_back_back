from django.core.management.base import BaseCommand
from teachers.models import Management, Teacher

class Command(BaseCommand):
    help = 'Create test data for management and teachers (multi-language)'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating test data...')

        # Clear existing data
        Management.objects.all().delete()
        Teacher.objects.all().delete()

        # Create Rector
        rector = Management.objects.create(
            full_name_ru='Иванов Иван Иванович',
            full_name_kg='Иванов Иван Иванович (ky)',
            full_name_en='Ivanov Ivan Ivanovich',
            position_ru='Ректор',
            position_kg='Ректор (ky)',
            position_en='Rector',
            bio_ru='Ректор университета с 20-летним опытом в образовании.',
            bio_kg='Ректор университети, 20 жылдык тажрыйба менен.',
            bio_en='University rector with 20 years of experience in education.'
        )

        # Create Vice-Rectors
        vice_rector_academic = Management.objects.create(
            full_name_ru='Петров Петр Петрович',
            full_name_kg='Петров Петр Петрович (ky)',
            full_name_en='Petrov Petr Petrovich',
            position_ru='Проректор по учебной работе',
            position_kg='Окуу иштери боюнча проректор',
            position_en='Vice-rector for Academic Affairs',
            parent=rector
        )
        vice_rector_science = Management.objects.create(
            full_name_ru='Сидоров Сергей Сергеевич',
            full_name_kg='Сидоров Сергей Сергеевич (ky)',
            full_name_en='Sidorov Sergey Sergeevich',
            position_ru='Проректор по научной работе',
            position_kg='Илимий иштер боюнча проректор',
            position_en='Vice-rector for Science',
            parent=rector
        )

        # Create Deans
        dean_medical = Management.objects.create(
            full_name_ru='Орлов Олег Олегович',
            full_name_kg='Орлов Олег Олегович (ky)',
            full_name_en='Orlov Oleg Olegovich',
            position_ru='Декан медицинского факультета',
            position_kg='Медицина факультетинин деканы',
            position_en='Dean of Medical Faculty',
            parent=vice_rector_academic
        )
        dean_pharmacy = Management.objects.create(
            full_name_ru='Морозов Михаил Михайлович',
            full_name_kg='Морозов Михаил Михайлович (ky)',
            full_name_en='Morozov Mikhail Mikhailovich',
            position_ru='Декан фармацевтического факультета',
            position_kg='Фармация факультетинин деканы',
            position_en='Dean of Pharmacy Faculty',
            parent=vice_rector_academic
        )

        # Create Teachers
        Teacher.objects.create(
            full_name_ru='Волков Владимир Владимирович',
            full_name_kg='Волков Владимир Владимирович (ky)',
            full_name_en='Volkov Vladimir Vladimirovich',
            position_ru='Профессор',
            position_kg='Профессор (ky)',
            position_en='Professor',
            bio_ru='Специалист в области кардиологии.',
            bio_kg='Кардиология боюнча адис.',
            bio_en='Specialist in cardiology.'
        )
        Teacher.objects.create(
            full_name_ru='Козлов Константин Константинович',
            full_name_kg='Козлов Константин Константинович (ky)',
            full_name_en='Kozlov Konstantin Konstantinovich',
            position_ru='Доцент',
            position_kg='Доцент (ky)',
            position_en='Associate Professor',
            bio_ru='Специалист в области гастроэнтерологии.',
            bio_kg='Гастроэнтерология боюнча адис.',
            bio_en='Specialist in gastroenterology.'
        )

        self.stdout.write(self.style.SUCCESS('Successfully created multi-language test data.'))
