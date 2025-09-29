from django.core.management.base import BaseCommand
from infrastructure.models import (
    ClassroomCategory, Classroom, ClassroomEquipment, ClassroomFeature,
    StartupCategory, Startup, StartupTeamMember, StartupInvestor, StartupAchievement
)


class Command(BaseCommand):
    help = 'Populate classrooms and startups data from frontend'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to populate classrooms and startups data...'))
        
        # Clear existing data
        ClassroomEquipment.objects.all().delete()
        ClassroomFeature.objects.all().delete()
        Classroom.objects.all().delete()
        ClassroomCategory.objects.all().delete()
        
        StartupAchievement.objects.all().delete()
        StartupInvestor.objects.all().delete()
        StartupTeamMember.objects.all().delete()
        Startup.objects.all().delete()
        StartupCategory.objects.all().delete()
        
        self.create_classroom_data()
        self.create_startup_data()
        
        self.stdout.write(self.style.SUCCESS('Successfully populated all data!'))

    def create_classroom_data(self):
        """Create classroom categories and classrooms data"""
        self.stdout.write('Creating classroom data...')
        
        # Create categories
        lecture_cat = ClassroomCategory.objects.create(
            name_ru="Лекционные залы",
            name_kg="Лекциялык залдар",
            name_en="Lecture Halls",
            icon="👨‍🏫",
            order=1
        )
        
        lab_cat = ClassroomCategory.objects.create(
            name_ru="Лаборатории",
            name_kg="Лабораториялар",
            name_en="Laboratories",
            icon="🔬",
            order=2
        )
        
        practice_cat = ClassroomCategory.objects.create(
            name_ru="Практические кабинеты",
            name_kg="Практикалык кабинеттер",
            name_en="Practice Rooms",
            icon="💊",
            order=3
        )
        
        # Create classrooms
        room101 = Classroom.objects.create(
            category=lecture_cat,
            name_ru="Аудитория 101",
            name_kg="101 аудитория",
            name_en="Room 101",
            description_ru="Большая лекционная аудитория с современным оборудованием для чтения лекций по медицинским дисциплинам",
            description_kg="Медициналык дисциплиналар боюнча лекция окуу үчүн заманбап жабдуу менен камтылган чоң лекциялык аудитория",
            description_en="Large lecture hall with modern equipment for medical lectures",
            capacity=120,
            floor="1",
            size=200,
            image="📊",
            order=1
        )
        
        # Equipment for room 101
        ClassroomEquipment.objects.create(classroom=room101, name_ru="Проектор", name_kg="Проектор", name_en="Projector", order=1)
        ClassroomEquipment.objects.create(classroom=room101, name_ru="Звуковая система", name_kg="Үн системасы", name_en="Sound System", order=2)
        ClassroomEquipment.objects.create(classroom=room101, name_ru="Микрофоны", name_kg="Микрофондор", name_en="Microphones", order=3)
        ClassroomEquipment.objects.create(classroom=room101, name_ru="Документ-камера", name_kg="Документ-камера", name_en="Document Camera", order=4)
        
        # Features for room 101
        ClassroomFeature.objects.create(classroom=room101, name_ru="Wi-Fi", name_kg="Wi-Fi", name_en="Wi-Fi", order=1)
        ClassroomFeature.objects.create(classroom=room101, name_ru="Кондиционер", name_kg="Кондиционер", name_en="Air Conditioning", order=2)
        ClassroomFeature.objects.create(classroom=room101, name_ru="Доступ для людей с ограниченными возможностями", name_kg="Мүмкүнчүлүгү чектелген адамдар үчүн кирүү", name_en="Disabled Access", order=3)
        
        room201 = Classroom.objects.create(
            category=lab_cat,
            name_ru="Лаборатория 201",
            name_kg="201 лаборатория",
            name_en="Laboratory 201",
            description_ru="Полностью оборудованная лаборатория для практических занятий по микробиологии и патологии",
            description_kg="Микробиология жана патология боюнча практикалык сабактар үчүн толук жабдылган лаборатория",
            description_en="Fully equipped laboratory for microbiology and pathology practical sessions",
            capacity=30,
            floor="2",
            size=80,
            image="🔬",
            order=2
        )
        
        # Equipment for room 201
        ClassroomEquipment.objects.create(classroom=room201, name_ru="Микроскопы", name_kg="Микроскоптор", name_en="Microscopes", order=1)
        ClassroomEquipment.objects.create(classroom=room201, name_ru="Лабораторное оборудование", name_kg="Лабораториялык жабдык", name_en="Lab Equipment", order=2)
        ClassroomEquipment.objects.create(classroom=room201, name_ru="Компьютеры", name_kg="Компьютерлер", name_en="Computers", order=3)
        ClassroomEquipment.objects.create(classroom=room201, name_ru="Образцы", name_kg="Үлгүлөр", name_en="Specimens", order=4)
        
        # Features for room 201
        ClassroomFeature.objects.create(classroom=room201, name_ru="Вентиляция", name_kg="Вентиляция", name_en="Ventilation", order=1)
        ClassroomFeature.objects.create(classroom=room201, name_ru="Оборудование безопасности", name_kg="Коопсуздук жабдыгы", name_en="Safety Equipment", order=2)
        
        room301 = Classroom.objects.create(
            category=practice_cat,
            name_ru="Кабинет практических навыков 301",
            name_kg="301 практикалык көндүм кабинети",
            name_en="Skills Practice Room 301",
            description_ru="Кабинет для отработки практических навыков с медицинскими тренажерами и симуляционным оборудованием",
            description_kg="Медициналык тренажерлер жана симуляциялык жабдыктар менен практикалык көндүмдөрдү иштетүү кабинети",
            description_en="Skills practice room with medical simulators and training equipment",
            capacity=25,
            floor="3",
            size=90,
            image="🩺",
            order=3
        )
        
        # Equipment for room 301
        ClassroomEquipment.objects.create(classroom=room301, name_ru="Больничные кровати", name_kg="Ооруканалык керебеттер", name_en="Hospital Beds", order=1)
        ClassroomEquipment.objects.create(classroom=room301, name_ru="Медицинские фантомы", name_kg="Медициналык фантомдор", name_en="Medical Phantoms", order=2)
        ClassroomEquipment.objects.create(classroom=room301, name_ru="Симуляционное оборудование", name_kg="Симуляциялык жабдыктар", name_en="Simulation Equipment", order=3)
        ClassroomEquipment.objects.create(classroom=room301, name_ru="Мониторы", name_kg="Мониторлор", name_en="Monitors", order=4)
        
        # Features for room 301
        ClassroomFeature.objects.create(classroom=room301, name_ru="Кондиционер", name_kg="Кондиционер", name_en="Air Conditioning", order=1)
        ClassroomFeature.objects.create(classroom=room301, name_ru="Хранилище", name_kg="Сактоочу жай", name_en="Storage", order=2)
        
        self.stdout.write(self.style.SUCCESS('✓ Classroom data created successfully!'))

    def create_startup_data(self):
        """Create startup categories and startups data"""
        self.stdout.write('Creating startup data...')
        
        # Create categories
        digital_cat = StartupCategory.objects.create(
            name_ru="Цифровое здравоохранение",
            name_kg="Санарип медицина",
            name_en="Digital Health",
            icon="💻",
            order=1
        )
        
        medtech_cat = StartupCategory.objects.create(
            name_ru="Медтех",
            name_kg="Медтех",
            name_en="MedTech",
            icon="🩺",
            order=2
        )
        
        biotech_cat = StartupCategory.objects.create(
            name_ru="Биотех",
            name_kg="Биотех", 
            name_en="BioTech",
            icon="🧬",
            order=3
        )
        
        # Create startups
        medapp = Startup.objects.create(
            category=digital_cat,
            name_ru="МедАпп",
            name_kg="МедАпп",
            name_en="MedApp",
            description_ru="Мобильное приложение для удаленного мониторинга здоровья пациентов",
            description_kg="Бейтаптардын ден-соолугун алыстан көзөмөлдөө үчүн мобилдик колдонмо",
            description_en="Mobile app for remote patient health monitoring",
            full_description_ru="Революционное мобильное приложение, которое позволяет врачам удаленно отслеживать жизненно важные показатели пациентов в режиме реального времени.",
            full_description_kg="Врачтарга бейтаптардын өмүрүн коргооучу көрсөткүчтөрүн реалдуу убакыт режиминде алыстан көзөмөлдөөгө мүмкүндүк берген революциялык мобилдик колдонмо.",
            full_description_en="Revolutionary mobile application that allows doctors to remotely track patients' vital signs in real-time.",
            stage="seed",
            status="active",
            funding="$500K",
            year="2023",
            image="📱",
            order=1
        )
        
        # Team members for MedApp
        StartupTeamMember.objects.create(startup=medapp, name_ru="Др. Смит", name_kg="Др. Смит", name_en="Dr. Smith", order=1)
        StartupTeamMember.objects.create(startup=medapp, name_ru="Проф. Джонсон", name_kg="Проф. Жонсон", name_en="Prof. Johnson", order=2)
        StartupTeamMember.objects.create(startup=medapp, name_ru="Инженер Ким", name_kg="Инженер Ким", name_en="Engineer Kim", order=3)
        
        # Investors for MedApp
        StartupInvestor.objects.create(startup=medapp, name_ru="Университетский фонд", name_kg="Университеттин фонду", name_en="University Fund", order=1)
        StartupInvestor.objects.create(startup=medapp, name_ru="Группа ангелов-инвесторов", name_kg="Ангел-инвесторлордун тобу", name_en="Angel Investor Group", order=2)
        
        # Achievements for MedApp
        StartupAchievement.objects.create(startup=medapp, achievement_ru="10,000+ загрузок", achievement_kg="10,000+ жүктөө", achievement_en="10,000+ downloads", order=1)
        StartupAchievement.objects.create(startup=medapp, achievement_ru="Партнерство с 5 больницами", achievement_kg="5 ооруканасы менен өнөктөштүк", achievement_en="Partnership with 5 hospitals", order=2)
        StartupAchievement.objects.create(startup=medapp, achievement_ru="Награда за инновации", achievement_kg="Инновация үчүн сыйлык", achievement_en="Innovation award", order=3)
        
        biosensor = Startup.objects.create(
            category=medtech_cat,
            name_ru="БиоСенсор",
            name_kg="БиоСенсор",
            name_en="BioSensor",
            description_ru="Портативные биосенсоры для быстрой диагностики заболеваний",
            description_kg="Ооруларды тез диагностикалоо үчүн портативдүү биосенсорлор",
            description_en="Portable biosensors for rapid disease diagnosis",
            full_description_ru="Инновационные портативные биосенсоры, способные диагностировать различные заболевания за считанные минуты.",
            full_description_kg="Ар түрдүү ооруларды бир нече минутта диагностикалай турган инновациялык портативдүү биосенсорлор.",
            full_description_en="Innovative portable biosensors capable of diagnosing various diseases within minutes.",
            stage="series_a",
            status="scaling",
            funding="$1.2M",
            year="2022",
            image="📟",
            order=2
        )
        
        # Team members for BioSensor
        StartupTeamMember.objects.create(startup=biosensor, name_ru="Проф. Браун", name_kg="Проф. Браун", name_en="Prof. Brown", order=1)
        StartupTeamMember.objects.create(startup=biosensor, name_ru="Др. Уилсон", name_kg="Др. Уилсон", name_en="Dr. Wilson", order=2)
        StartupTeamMember.objects.create(startup=biosensor, name_ru="Исследователь Ли", name_kg="Изилдөөчү Ли", name_en="Researcher Lee", order=3)
        
        # Investors for BioSensor
        StartupInvestor.objects.create(startup=biosensor, name_ru="Венчурный капитал", name_kg="Венчурдук капитал", name_en="Venture Capital", order=1)
        StartupInvestor.objects.create(startup=biosensor, name_ru="Технологический фонд", name_kg="Технологиялык фонд", name_en="Tech Fund", order=2)
        
        # Achievements for BioSensor
        StartupAchievement.objects.create(startup=biosensor, achievement_ru="FDA одобрение получено", achievement_kg="FDA макулдугу алынды", achievement_en="FDA approval received", order=1)
        StartupAchievement.objects.create(startup=biosensor, achievement_ru="50+ медицинских центров", achievement_kg="50+ медициналык борбор", achievement_en="50+ medical centers", order=2)
        StartupAchievement.objects.create(startup=biosensor, achievement_ru="Международная экспансия", achievement_kg="Эл аралык кеңейүү", achievement_en="International expansion", order=3)
        
        gene_therapy = Startup.objects.create(
            category=biotech_cat,
            name_ru="Генная терапия",
            name_kg="Гендик терапия",
            name_en="Gene Therapy",
            description_ru="Разработка генной терапии для редких заболеваний",
            description_kg="Сейрек учурайган оорулар үчүн гендик терапияны иштеп чыгуу",
            description_en="Developing gene therapy for rare diseases",
            full_description_ru="Передовые исследования в области генной терапии для лечения редких генетических заболеваний.",
            full_description_kg="Сейрек генетикалык ооруларды дарылоо үчүн гендик терапия тармагындагы алдыңкы изилдөөлөр.",
            full_description_en="Cutting-edge research in gene therapy for treating rare genetic diseases.",
            stage="research",
            status="research",
            funding="$600K",
            year="2023",
            image="🧬",
            order=3
        )
        
        # Team members for Gene Therapy
        StartupTeamMember.objects.create(startup=gene_therapy, name_ru="Др. Робертс", name_kg="Др. Робертс", name_en="Dr. Roberts", order=1)
        StartupTeamMember.objects.create(startup=gene_therapy, name_ru="Проф. Мартинез", name_kg="Проф. Мартинез", name_en="Prof. Martinez", order=2)
        StartupTeamMember.objects.create(startup=gene_therapy, name_ru="Генетик Ван", name_kg="Генетик Ван", name_en="Geneticist Wang", order=3)
        
        # Investors for Gene Therapy
        StartupInvestor.objects.create(startup=gene_therapy, name_ru="Исследовательский грант", name_kg="Изилдөө гранты", name_en="Research Grant", order=1)
        StartupInvestor.objects.create(startup=gene_therapy, name_ru="Биофонд", name_kg="Биофонд", name_en="Bio Fund", order=2)
        
        # Achievements for Gene Therapy
        StartupAchievement.objects.create(startup=gene_therapy, achievement_ru="3 публикации в Nature", achievement_kg="Nature журналында 3 басылма", achievement_en="3 publications in Nature", order=1)
        StartupAchievement.objects.create(startup=gene_therapy, achievement_ru="Получен патент", achievement_kg="Патент алынды", achievement_en="Patent obtained", order=2)
        
        self.stdout.write(self.style.SUCCESS('✓ Startup data created successfully!'))