from django.core.management.base import BaseCommand
from infrastructure.models import (
    Hospital, HospitalDepartment, Laboratory, LaboratoryEquipment,
    AcademicBuilding, BuildingFacility, BuildingPhoto,
    Dormitory, DormitoryRoom, DormitoryFacility, DormitoryPhoto
)


class Command(BaseCommand):
    help = 'Create test data for infrastructure app'

    def handle(self, *args, **options):
        self.stdout.write('Creating infrastructure test data...')

        # Create Hospitals
        self.create_hospitals()
        
        # Create Laboratories
        self.create_laboratories()
        
        # Create Academic Buildings
        self.create_academic_buildings()
        
        # Create Dormitories
        self.create_dormitories()

        self.stdout.write(self.style.SUCCESS('Successfully created infrastructure test data'))

    def create_hospitals(self):
        # Hospital 1
        hospital1 = Hospital.objects.create(
            name_ru="Университетская клиника Салымбекова",
            name_kg="Салымбеков университетинин клиникасы",
            name_en="Salymbekov University Clinic",
            description_ru="Главная клиническая база университета для подготовки медицинских кадров",
            description_kg="Медициналык кадрларды даярдоо үчүн университеттин негизги клиникалык базасы",
            description_en="Main clinical base of the university for medical training",
            address_ru="г. Бишкек, ул. Ахунбаева, 92",
            address_kg="Бишкек шаары, Ахунбаев көчөсү, 92",
            address_en="Bishkek, Akhunbaev Street, 92",
            practice_opportunities_ru="Студенты могут участвовать в обходах врачей, наблюдать операции, работать с пациентами под контролем преподавателей",
            practice_opportunities_kg="Студенттер дарыгерлердин айланышына катыша алышат, операцияларды көрө алышат, мугалимдердин көзөмөлү астында пациенттер менен иштей алышат",
            practice_opportunities_en="Students can participate in medical rounds, observe surgeries, work with patients under supervision",
            contact_phone="+996 312 123-456",
            contact_email="clinic@salymbekov.edu.kg",
            latitude=42.8746,
            longitude=74.5698,
            order=1
        )

        # Hospital Departments
        HospitalDepartment.objects.create(
            hospital=hospital1,
            name_ru="Терапевтическое отделение",
            name_kg="Терапевтикалык бөлүм",
            name_en="Therapeutic Department",
            description_ru="Практика в общей терапии",
            description_kg="Жалпы терапиядагы практика",
            description_en="General therapy practice",
            order=1
        )

        HospitalDepartment.objects.create(
            hospital=hospital1,
            name_ru="Хирургическое отделение",
            name_kg="Хирургиялык бөлүм",
            name_en="Surgical Department",
            description_ru="Работа в операционных",
            description_kg="Операция бөлмөсүндө иштөө",
            description_en="Operating room work",
            order=2
        )

        HospitalDepartment.objects.create(
            hospital=hospital1,
            name_ru="Педиатрическое отделение",
            name_kg="Педиатриялык бөлүм",
            name_en="Pediatric Department",
            description_ru="Работа с детьми",
            description_kg="Балдар менен иштөө",
            description_en="Working with children",
            order=3
        )

        # Hospital 2
        hospital2 = Hospital.objects.create(
            name_ru="Детская клиническая больница",
            name_kg="Балдар клиникалык ооруканасы",
            name_en="Children's Clinical Hospital",
            description_ru="Специализированная детская больница для педиатрической практики",
            description_kg="Педиатриялык практика үчүн адистештирилген балдар ооруканасы",
            description_en="Specialized children's hospital for pediatric practice",
            address_ru="г. Бишкек, ул. Медицинская, 15",
            address_kg="Бишкек шаары, Медициналык көчөсү, 15",
            address_en="Bishkek, Medical Street, 15",
            practice_opportunities_ru="Практика по детской медицине, участие в лечении детей различных возрастов",
            practice_opportunities_kg="Балдар медицинасы боюнча практика, ар түрдүү курактагы балдарды дарылоого катышуу",
            practice_opportunities_en="Pediatric medicine practice, participation in treating children of various ages",
            contact_phone="+996 312 654-321",
            contact_email="children@salymbekov.edu.kg",
            latitude=42.8756,
            longitude=74.5708,
            order=2
        )

        HospitalDepartment.objects.create(
            hospital=hospital2,
            name_ru="Неонатология",
            name_kg="Неонатология",
            name_en="Neonatology",
            description_ru="Работа с новорожденными",
            description_kg="Жаңы төрөлгөн балдар менен иштөө",
            description_en="Working with newborns",
            order=1
        )

        HospitalDepartment.objects.create(
            hospital=hospital2,
            name_ru="Детская хирургия",
            name_kg="Балдар хирургиясы",
            name_en="Pediatric Surgery",
            description_ru="Хирургические вмешательства у детей",
            description_kg="Балдарда хирургиялык кийлигишүүлөр",
            description_en="Surgical interventions in children",
            order=2
        )

        self.stdout.write('Created hospitals and departments')

    def create_laboratories(self):
        # Laboratory 1 - Biochemistry
        lab1 = Laboratory.objects.create(
            name_ru="Лаборатория биохимии",
            name_kg="Биохимия лабораториясы",
            name_en="Biochemistry Laboratory",
            type="biochemistry",
            description_ru="Современная лаборатория для изучения биохимических процессов в организме",
            description_kg="Организмдеги биохимиялык процесстерди изилдөө үчүн заманбап лаборатория",
            description_en="Modern laboratory for studying biochemical processes in the body",
            schedule_ru="Понедельник-Пятница: 8:00-18:00, Суббота: 9:00-15:00",
            schedule_kg="Дүйшөмбү-Жума: 8:00-18:00, Ишемби: 9:00-15:00",
            schedule_en="Monday-Friday: 8:00-18:00, Saturday: 9:00-15:00",
            requirements_ru="Лабораторный халат, защитные очки, сменная обувь",
            requirements_kg="Лабораториялык халат, коргоочу көз айнек, алмаштырма бут кийим",
            requirements_en="Lab coat, safety goggles, indoor shoes",
            capacity=24,
            order=1
        )

        LaboratoryEquipment.objects.create(
            laboratory=lab1,
            name_ru="Спектрофотометр",
            name_kg="Спектрофотометр",
            name_en="Spectrophotometer",
            description_ru="Для анализа биохимических показателей",
            description_kg="Биохимиялык көрсөткүчтөрдү талдоо үчүн",
            description_en="For biochemical analysis",
            order=1
        )

        LaboratoryEquipment.objects.create(
            laboratory=lab1,
            name_ru="Центрифуга",
            name_kg="Центрифуга",
            name_en="Centrifuge",
            description_ru="Разделение биологических компонентов",
            description_kg="Биологиялык компоненттерди бөлүү",
            description_en="Separation of biological components",
            order=2
        )

        # Laboratory 2 - Anatomy
        lab2 = Laboratory.objects.create(
            name_ru="Анатомическая лаборатория",
            name_kg="Анатомиялык лаборатория",
            name_en="Anatomy Laboratory",
            type="anatomy",
            description_ru="Лаборатория для изучения строения человеческого тела",
            description_kg="Адам денесинин түзүлүшүн изилдөө үчүн лаборатория",
            description_en="Laboratory for studying human body structure",
            schedule_ru="Понедельник-Пятница: 9:00-17:00",
            schedule_kg="Дүйшөмбү-Жума: 9:00-17:00",
            schedule_en="Monday-Friday: 9:00-17:00",
            requirements_ru="Медицинский халат, перчатки, респиратор",
            requirements_kg="Медициналык халат, кол чаткычтар, респиратор",
            requirements_en="Medical coat, gloves, respirator",
            capacity=30,
            order=2
        )

        LaboratoryEquipment.objects.create(
            laboratory=lab2,
            name_ru="Анатомические препараты",
            name_kg="Анатомиялык препараттар",
            name_en="Anatomical specimens",
            description_ru="Коллекция органов и систем человека",
            description_kg="Адамдын органдарынын жана системаларынын коллекциясы",
            description_en="Collection of human organs and systems",
            order=1
        )

        # Laboratory 3 - Pharmacy
        lab3 = Laboratory.objects.create(
            name_ru="Фармацевтическая лаборатория",
            name_kg="Фармацевтикалык лаборатория",
            name_en="Pharmaceutical Laboratory",
            type="pharmacy",
            description_ru="Лаборатория для изучения фармацевтических технологий и анализа лекарств",
            description_kg="Фармацевтикалык технологияларды изилдөө жана дарыларды талдоо үчүн лаборатория",
            description_en="Laboratory for studying pharmaceutical technologies and drug analysis",
            schedule_ru="Понедельник-Пятница: 8:30-17:30",
            schedule_kg="Дүйшөмбү-Жума: 8:30-17:30",
            schedule_en="Monday-Friday: 8:30-17:30",
            requirements_ru="Лабораторный халат, защитные очки, резиновые перчатки",
            requirements_kg="Лабораториялык халат, коргоочу көз айнек, резина кол чаткычтар",
            requirements_en="Lab coat, safety goggles, rubber gloves",
            capacity=20,
            order=3
        )

        LaboratoryEquipment.objects.create(
            laboratory=lab3,
            name_ru="Хроматограф",
            name_kg="Хроматограф",
            name_en="Chromatograph",
            description_ru="Анализ лекарственных веществ",
            description_kg="Дары заттарын талдоо",
            description_en="Analysis of pharmaceutical substances",
            order=1
        )

        # Laboratory 4 - Microbiology
        lab4 = Laboratory.objects.create(
            name_ru="Лаборатория микробиологии",
            name_kg="Микробиология лабораториясы",
            name_en="Microbiology Laboratory",
            type="microbiology",
            description_ru="Лаборатория для изучения микроорганизмов и инфекционных заболеваний",
            description_kg="Микроорганизмдерди жана инфекциялык оорулардын изилдөө үчүн лаборатория",
            description_en="Laboratory for studying microorganisms and infectious diseases",
            schedule_ru="Понедельник-Пятница: 9:00-16:00",
            schedule_kg="Дүйшөмбү-Жума: 9:00-16:00",
            schedule_en="Monday-Friday: 9:00-16:00",
            requirements_ru="Стерильный халат, маска, перчатки, защитные очки",
            requirements_kg="Стерилдүү халат, маска, кол чаткычтар, коргоочу көз айнек",
            requirements_en="Sterile coat, mask, gloves, safety goggles",
            capacity=16,
            order=4
        )

        LaboratoryEquipment.objects.create(
            laboratory=lab4,
            name_ru="Автоклав",
            name_kg="Автоклав",
            name_en="Autoclave",
            description_ru="Стерилизация оборудования",
            description_kg="Жабдыктарды стерилдештирүү",
            description_en="Equipment sterilization",
            order=1
        )

        self.stdout.write('Created laboratories and equipment')

    def create_academic_buildings(self):
        # Building 1 - Main Academic Building
        building1 = AcademicBuilding.objects.create(
            name_ru="Главный учебный корпус",
            name_kg="Негизги окуу корпусу",
            name_en="Main Academic Building",
            description_ru="Основное здание университета с лекционными залами и административными офисами",
            description_kg="Университеттин негизги имараты лекциялык залдар жана административдик кеңселер менен",
            description_en="Main university building with lecture halls and administrative offices",
            address_ru="г. Бишкек, ул. Ахунбаева, 92",
            address_kg="Бишкек шаары, Ахунбаев көчөсү, 92",
            address_en="Bishkek, Akhunbaev Street, 92",
            floors=5,
            latitude=42.8746,
            longitude=74.5698,
            order=1
        )

        BuildingFacility.objects.create(
            building=building1,
            name_ru="Лекционные залы",
            name_kg="Лекциялык залдар",
            name_en="Lecture halls",
            count=12,
            capacity="50-200 человек",
            order=1
        )

        BuildingFacility.objects.create(
            building=building1,
            name_ru="Аудитории",
            name_kg="Аудиториялар",
            name_en="Classrooms",
            count=25,
            capacity="20-40 человек",
            order=2
        )

        BuildingFacility.objects.create(
            building=building1,
            name_ru="Библиотека",
            name_kg="Китепкана",
            name_en="Library",
            count=1,
            capacity="100 мест для чтения",
            order=3
        )

        BuildingPhoto.objects.create(
            building=building1,
            type="facade",
            title_ru="Фасад главного корпуса",
            title_kg="Негизги корпустун фасады",
            title_en="Main building facade",
            order=1
        )

        BuildingPhoto.objects.create(
            building=building1,
            type="lecture_hall",
            title_ru="Большой лекционный зал",
            title_kg="Чоң лекциялык зал",
            title_en="Main lecture hall",
            order=2
        )

        # Building 2 - Medical Building
        building2 = AcademicBuilding.objects.create(
            name_ru="Медицинский корпус",
            name_kg="Медициналык корпус",
            name_en="Medical Building",
            description_ru="Специализированное здание для медицинских факультетов с лабораториями",
            description_kg="Лабораториялары бар медициналык факультеттер үчүн адистештирилген имарат",
            description_en="Specialized building for medical faculties with laboratories",
            address_ru="г. Бишкек, ул. Медицинская, 15",
            address_kg="Бишкек шаары, Медициналык көчөсү, 15",
            address_en="Bishkek, Medical Street, 15",
            floors=4,
            latitude=42.8756,
            longitude=74.5708,
            order=2
        )

        BuildingFacility.objects.create(
            building=building2,
            name_ru="Анатомические залы",
            name_kg="Анатомиялык залдар",
            name_en="Anatomy halls",
            count=3,
            capacity="30-40 человек",
            order=1
        )

        BuildingFacility.objects.create(
            building=building2,
            name_ru="Лаборатории",
            name_kg="Лабораториялар",
            name_en="Laboratories",
            count=8,
            capacity="15-25 человек",
            order=2
        )

        self.stdout.write('Created academic buildings')

    def create_dormitories(self):
        # Dormitory 1 - Female
        dorm1 = Dormitory.objects.create(
            name_ru="Общежитие №1 (Женское)",
            name_kg="№1 жатакана (Аялдар)",
            name_en="Dormitory #1 (Female)",
            type="female",
            description_ru="Комфортабельное общежитие для студенток с современными удобствами",
            description_kg="Заманбап ыңгайлуулуктары бар студенттер үчүн ыңгайлуу жатакана",
            description_en="Comfortable dormitory for female students with modern amenities",
            address_ru="г. Бишкек, ул. Студенческая, 10",
            address_kg="Бишкек шаары, Студенттик көчө, 10",
            address_en="Bishkek, Student Street, 10",
            capacity=200,
            available=15,
            order=1
        )

        DormitoryRoom.objects.create(
            dormitory=dorm1,
            type="double",
            name_ru="Двухместная комната",
            name_kg="Эки жактуу бөлмө",
            name_en="Double room",
            price_monthly=3500.00,
            features_ru="2 кровати, 2 стола, шкаф, Wi-Fi",
            features_kg="2 керебет, 2 стол, шкаф, Wi-Fi",
            features_en="2 beds, 2 desks, wardrobe, Wi-Fi",
            order=1
        )

        DormitoryRoom.objects.create(
            dormitory=dorm1,
            type="triple",
            name_ru="Трёхместная комната",
            name_kg="Үч жактуу бөлмө",
            name_en="Triple room",
            price_monthly=2800.00,
            features_ru="3 кровати, 3 стола, шкаф, Wi-Fi",
            features_kg="3 керебет, 3 стол, шкаф, Wi-Fi",
            features_en="3 beds, 3 desks, wardrobe, Wi-Fi",
            order=2
        )

        DormitoryFacility.objects.create(
            dormitory=dorm1,
            name_ru="Общая кухня на этаже",
            name_kg="Кабатта жалпы ашкана",
            name_en="Shared kitchen per floor",
            order=1
        )

        DormitoryFacility.objects.create(
            dormitory=dorm1,
            name_ru="Прачечная",
            name_kg="Кир жуучу жай",
            name_en="Laundry room",
            order=2
        )

        DormitoryFacility.objects.create(
            dormitory=dorm1,
            name_ru="Круглосуточная охрана",
            name_kg="Тун-күн коргоо",
            name_en="24/7 security",
            order=3
        )

        DormitoryPhoto.objects.create(
            dormitory=dorm1,
            type="exterior",
            title_ru="Внешний вид общежития",
            title_kg="Жатакананын сырткы көрүнүшү",
            title_en="Dormitory exterior",
            order=1
        )

        DormitoryPhoto.objects.create(
            dormitory=dorm1,
            type="room",
            title_ru="Двухместная комната",
            title_kg="Эки жактуу бөлмө",
            title_en="Double room",
            order=2
        )

        # Dormitory 2 - Male
        dorm2 = Dormitory.objects.create(
            name_ru="Общежитие №2 (Мужское)",
            name_kg="№2 жатакана (Эркектер)",
            name_en="Dormitory #2 (Male)",
            type="male",
            description_ru="Современное общежитие для студентов с отличными условиями проживания",
            description_kg="Мыкты жашоо шарттары бар студенттер үчүн заманбап жатакана",
            description_en="Modern dormitory for male students with excellent living conditions",
            address_ru="г. Бишкек, ул. Студенческая, 12",
            address_kg="Бишкек шаары, Студенттик көчө, 12",
            address_en="Bishkek, Student Street, 12",
            capacity=180,
            available=8,
            order=2
        )

        DormitoryRoom.objects.create(
            dormitory=dorm2,
            type="double",
            name_ru="Двухместная комната",
            name_kg="Эки жактуу бөлмө",
            name_en="Double room",
            price_monthly=3500.00,
            features_ru="2 кровати, 2 стола, шкаф, Wi-Fi",
            features_kg="2 керебет, 2 стол, шкаф, Wi-Fi",
            features_en="2 beds, 2 desks, wardrobe, Wi-Fi",
            order=1
        )

        # Dormitory 3 - Family
        dorm3 = Dormitory.objects.create(
            name_ru="Семейное общежитие",
            name_kg="Үй-бүлөлүк жатакана",
            name_en="Family Dormitory",
            type="family",
            description_ru="Общежитие для семейных студентов с отдельными квартирами",
            description_kg="Өзүнчө батирлары бар үй-бүлөлүү студенттер үчүн жатакана",
            description_en="Dormitory for married students with separate apartments",
            address_ru="г. Бишкек, ул. Семейная, 5",
            address_kg="Бишкек шаары, Үй-бүлөлүк көчө, 5",
            address_en="Bishkek, Family Street, 5",
            capacity=50,
            available=3,
            order=3
        )

        DormitoryRoom.objects.create(
            dormitory=dorm3,
            type="studio",
            name_ru="Студия",
            name_kg="Студия",
            name_en="Studio",
            price_monthly=8000.00,
            features_ru="Спальня, кухня, санузел, Wi-Fi",
            features_kg="Уктоочу бөлмө, ашкана, даарет, Wi-Fi",
            features_en="Bedroom, kitchen, bathroom, Wi-Fi",
            order=1
        )

        DormitoryRoom.objects.create(
            dormitory=dorm3,
            type="one_bedroom",
            name_ru="Однокомнатная",
            name_kg="Бир бөлмөлүү",
            name_en="One bedroom",
            price_monthly=12000.00,
            features_ru="Отдельная спальня, кухня, санузел, Wi-Fi",
            features_kg="Өзүнчө спальня, ашкана, даарет, Wi-Fi",
            features_en="Separate bedroom, kitchen, bathroom, Wi-Fi",
            order=2
        )

        DormitoryFacility.objects.create(
            dormitory=dorm3,
            name_ru="Детская игровая площадка",
            name_kg="Балдар оюн аянты",
            name_en="Children's playground",
            order=1
        )

        DormitoryFacility.objects.create(
            dormitory=dorm3,
            name_ru="Парковочные места",
            name_kg="Унаа токтотуу жерлери",
            name_en="Parking spaces",
            order=2
        )

        self.stdout.write('Created dormitories with rooms and facilities')