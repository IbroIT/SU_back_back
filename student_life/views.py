from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from .models import PartnerOrganization, StudentAppeal
from .serializers import PartnerOrganizationSerializer, StudentAppealSerializer


class PartnerOrganizationViewSet(viewsets.ModelViewSet):
    queryset = PartnerOrganization.objects.filter(is_active=True)
    serializer_class = PartnerOrganizationSerializer
    permission_classes = [AllowAny]


# =============================================================================
# КОМБИНИРОВАННЫЕ API ENDPOINTS ДЛЯ ФРОНТЕНДА
# =============================================================================

@api_view(['GET'])
def internships_data(request):
    """Комбинированные данные для страницы практики"""
    try:
        # Получаем организации-партнеры
        organizations = PartnerOrganization.objects.filter(is_active=True)
        organizations_data = PartnerOrganizationSerializer(organizations, many=True).data
        
        # Создаем структуру требований (пока заглушка)
        requirements = {
            'academic': {
                'title_ru': 'Академические требования',
                'title_kg': 'Академиялык талаптар',
                'title_en': 'Academic Requirements',
                'items': [
                    {'text_ru': 'Средний балл не ниже 3.0', 'text_kg': 'Орточо баа 3.0дон төмөн эмес', 'text_en': 'GPA not lower than 3.0'},
                    {'text_ru': 'Прохождение базовых курсов', 'text_kg': 'Негизги курстарды өтүү', 'text_en': 'Completion of basic courses'}
                ]
            },
            'documents': {
                'title_ru': 'Необходимые документы',
                'title_kg': 'Керектүү документтер',
                'title_en': 'Required Documents',
                'items': [
                    {'text_ru': 'Справка об обучении', 'text_kg': 'Окуу жөнүндө маалымат', 'text_en': 'Certificate of study'},
                    {'text_ru': 'Медицинская справка', 'text_kg': 'Медициналык справка', 'text_en': 'Medical certificate'}
                ]
            }
        }
        
        # Создаем шаблоны отчетов (пока заглушка)
        report_templates = [
            {
                'name_ru': 'Шаблон отчета по практике',
                'name_kg': 'Практика боюнча отчет үлгүсү',
                'name_en': 'Internship Report Template',
                'description_ru': 'Стандартный шаблон для отчета',
                'description_kg': 'Отчет үчүн стандарттык үлгү',
                'description_en': 'Standard template for report',
                'file': '/media/templates/internship_report.docx'
            }
        ]
        
        data = {
            'partner_organizations': organizations_data,
            'requirements': requirements,
            'report_templates': report_templates
        }
        
        return Response(data)
        
    except Exception as e:
        return Response(
            {'error': f'Ошибка загрузки данных: {str(e)}'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def academic_mobility_data(request):
    """Комбинированные данные для страницы академической мобильности"""
    try:
        # Создаем заглушки с мультиязычными данными
        partner_universities = [
            {
                'id': 1,
                'name_ru': 'Медицинский университет Турции',
                'name_kg': 'Түркиянын медициналык университети',
                'name_en': 'Turkey Medical University',
                'description_ru': 'Ведущий медицинский университет с международной аккредитацией',
                'description_kg': 'Эл аралык аккредитациясы бар алдыңкы медициналык университет',
                'description_en': 'Leading medical university with international accreditation',
                'country': 'Турция',
                'city': 'Анкара',
                'website': 'https://turkey-med.edu.tr',
                'programs': [
                    {
                        'name_ru': 'Хирургия',
                        'name_kg': 'Хирургия',
                        'name_en': 'Surgery',
                        'duration': '6 месяцев',
                        'language': 'Английский'
                    },
                    {
                        'name_ru': 'Кардиология',
                        'name_kg': 'Кардиология',
                        'name_en': 'Cardiology',
                        'duration': '1 год',
                        'language': 'Турецкий'
                    }
                ]
            },
            {
                'id': 2,
                'name_ru': 'Европейская медицинская академия',
                'name_kg': 'Европанын медициналык академиясы',
                'name_en': 'European Medical Academy',
                'description_ru': 'Современная академия с фокусом на инновационные методы лечения',
                'description_kg': 'Инновациялык дарылоо ыкмаларына багытталган заманбап академия',
                'description_en': 'Modern academy focused on innovative treatment methods',
                'country': 'Германия',
                'city': 'Берлин',
                'website': 'https://ema-berlin.de',
                'programs': [
                    {
                        'name_ru': 'Неврология',
                        'name_kg': 'Неврология',
                        'name_en': 'Neurology',
                        'duration': '1 семестр',
                        'language': 'Немецкий'
                    }
                ]
            }
        ]
        
        exchange_opportunities = [
            {
                'id': 1,
                'title_ru': 'Семестровый обмен',
                'title_kg': 'Семестрдик алмашуу',
                'title_en': 'Semester Exchange',
                'description_ru': 'Программа обмена на один семестр с возможностью изучения новых методик',
                'description_kg': 'Жаңы методикаларды үйрөнүү мүмкүнчүлүгү менен бир семестрге алмашуу программасы',
                'description_en': 'One semester exchange program with opportunity to learn new methodologies',
                'type': 'semester',
                'benefits': [
                    {
                        'text_ru': 'Получение международного опыта',
                        'text_kg': 'Эл аралык тажрыйба алуу',
                        'text_en': 'Gaining international experience'
                    },
                    {
                        'text_ru': 'Изучение новых медицинских технологий',
                        'text_kg': 'Жаңы медициналык технологияларды үйрөнүү',
                        'text_en': 'Learning new medical technologies'
                    },
                    {
                        'text_ru': 'Развитие языковых навыков',
                        'text_kg': 'Тил билүү көндүмдөрүн өнүктүрүү',
                        'text_en': 'Language skills development'
                    },
                    {
                        'text_ru': 'Расширение профессиональной сети',
                        'text_kg': 'Кесиптик байланыштарды кеңейтүү',
                        'text_en': 'Expanding professional network'
                    }
                ]
            },
            {
                'id': 2,
                'title_ru': 'Годовая программа обмена',
                'title_kg': 'Жылдык алмашуу программасы',
                'title_en': 'Annual Exchange Program',
                'description_ru': 'Годовая программа для углубленного изучения специализации',
                'description_kg': 'Адистикти терең үйрөнүү үчүн жылдык программа',
                'description_en': 'Annual program for in-depth specialization study',
                'type': 'year',
                'benefits': [
                    {
                        'text_ru': 'Полная интеграция в образовательный процесс',
                        'text_kg': 'Билим берүү процессине толук интеграция',
                        'text_en': 'Full integration into educational process'
                    },
                    {
                        'text_ru': 'Возможность прохождения стажировки',
                        'text_kg': 'Стажировкадан өтүү мүмкүнчүлүгү',
                        'text_en': 'Internship opportunities'
                    }
                ]
            }
        ]
        
        participation_requirements = [
            {
                'id': 1,
                'category': 'academic',
                'title_ru': 'Академические требования',
                'title_kg': 'Академиялык талаптар',
                'title_en': 'Academic Requirements',
                'description_ru': 'Требования к академической успеваемости',
                'description_kg': 'Академиялык жетишкендикке талаптар',
                'description_en': 'Academic performance requirements'
            },
            {
                'id': 2,
                'category': 'language',
                'title_ru': 'Языковые требования',
                'title_kg': 'Тилдик талаптар',
                'title_en': 'Language Requirements',
                'description_ru': 'Знание иностранного языка на уровне B2',
                'description_kg': 'Чет тилин B2 деңгээлинде билүү',
                'description_en': 'Foreign language proficiency at B2 level'
            },
            {
                'id': 3,
                'category': 'documents',
                'title_ru': 'Документы',
                'title_kg': 'Документтер',
                'title_en': 'Documents',
                'description_ru': 'Необходимые документы для участия',
                'description_kg': 'Катышуу үчүн керектүү документтер',
                'description_en': 'Required documents for participation'
            }
        ]
        
        data = {
            'partner_universities': partner_universities,
            'exchange_opportunities': exchange_opportunities,
            'participation_requirements': participation_requirements
        }
        
        return Response(data)
        
    except Exception as e:
        return Response(
            {'error': f'Ошибка загрузки данных: {str(e)}'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def regulations_data(request):
    """Комбинированные данные для страницы регламентов"""
    try:
        response_data = {
            "internal_rules": [
                {
                    "title_ru": "Правила поведения в университете",
                    "title_kg": "Университеттеги жүрүм-турум эрежелери",
                    "title_en": "University Conduct Rules",
                    "content": [
                        {
                            "text_ru": "Студенты обязаны соблюдать академическую честность во всех видах учебной деятельности",
                            "text_kg": "Студенттер окуу ишинин бардык түрлөрүндө академиялык адептүүлүктү сактоого милдеттүү",
                            "text_en": "Students must maintain academic integrity in all forms of educational activities"
                        },
                        {
                            "text_ru": "Посещение занятий является обязательным для всех студентов",
                            "text_kg": "Сабактарга катышуу бардык студенттер үчүн милдеттүү",
                            "text_en": "Class attendance is mandatory for all students"
                        },
                        {
                            "text_ru": "В учебных аудиториях должна соблюдаться тишина и порядок",
                            "text_kg": "Окуу аудиторияларында тынчтык жана тартип сакталышы керек",
                            "text_en": "Silence and order must be maintained in classrooms"
                        },
                        {
                            "text_ru": "Использование мобильных телефонов во время занятий запрещено",
                            "text_kg": "Сабак учурунда уюлдук телефондорду колдонуу тыйылган",
                            "text_en": "Use of mobile phones during classes is prohibited"
                        }
                    ]
                },
                {
                    "title_ru": "Дресс-код и внешний вид",
                    "title_kg": "Кийим-кече жана сырткы көрүнүш",
                    "title_en": "Dress Code and Appearance",
                    "content": [
                        {
                            "text_ru": "Студенты должны придерживаться делового стиля одежды",
                            "text_kg": "Студенттер иш кийимин кийүүгө милдеттүү",
                            "text_en": "Students must adhere to business casual dress code"
                        },
                        {
                            "text_ru": "Во время практических занятий обязательно ношение медицинской формы",
                            "text_kg": "Практикалык сабактар учурунда медициналык форма кийүү милдеттүү",
                            "text_en": "Medical uniform is mandatory during practical classes"
                        },
                        {
                            "text_ru": "Обувь должна быть закрытой и удобной для работы в клинике",
                            "text_kg": "Бут кийим жабык жана клиникада иштөө үчүн ыңгайлуу болушу керек",
                            "text_en": "Footwear should be closed and suitable for clinical work"
                        }
                    ]
                }
            ],
            "academic_regulations": [
                {
                    "title_ru": "Регламент проведения экзаменов",
                    "title_kg": "Экзамендерди өткөрүү регламенти",
                    "title_en": "Examination Regulations",
                    "sections": [
                        {
                            "subtitle_ru": "Допуск к экзаменам",
                            "subtitle_kg": "Экзаменге жол берүү",
                            "subtitle_en": "Admission to Examinations",
                            "rules": [
                                {
                                    "text_ru": "Студент допускается к экзамену при посещаемости не менее 75%",
                                    "text_kg": "Студент 75%дан кем эмес катышуу менен экзаменге жол берилет",
                                    "text_en": "Students are admitted to exams with attendance of at least 75%"
                                },
                                {
                                    "text_ru": "Все лабораторные работы должны быть выполнены и защищены",
                                    "text_kg": "Бардык лабораториялык иштер аткарылып, коргонулушу керек",
                                    "text_en": "All laboratory work must be completed and defended"
                                },
                                {
                                    "text_ru": "Задолженности по предыдущим семестрам должны быть ликвидированы",
                                    "text_kg": "Мурунку семестрлердеги карыздар жоюлушу керек",
                                    "text_en": "Debts from previous semesters must be cleared"
                                }
                            ]
                        },
                        {
                            "subtitle_ru": "Проведение экзамена",
                            "subtitle_kg": "Экзаменди өткөрүү",
                            "subtitle_en": "Exam Conduct",
                            "rules": [
                                {
                                    "text_ru": "Продолжительность экзамена составляет 90 минут",
                                    "text_kg": "Экзамендин узактыгы 90 мүнөт түзөт",
                                    "text_en": "Exam duration is 90 minutes"
                                },
                                {
                                    "text_ru": "Использование дополнительных материалов согласовывается с преподавателем",
                                    "text_kg": "Кошумча материалдарды колдонуу мугалим менен макулдашылат",
                                    "text_en": "Use of additional materials is agreed with the instructor"
                                },
                                {
                                    "text_ru": "Пересдача экзамена возможна не более 2 раз",
                                    "text_kg": "Экзаменди кайра тапшыруу 2 жолудан көп эмес мүмкүн",
                                    "text_en": "Exam retake is possible no more than 2 times"
                                }
                            ]
                        }
                    ]
                },
                {
                    "title_ru": "Регламент курсовых и дипломных работ",
                    "title_kg": "Курстук жана дипломдук иштердин регламенти",
                    "title_en": "Course and Diploma Work Regulations",
                    "sections": [
                        {
                            "subtitle_ru": "Требования к оформлению",
                            "subtitle_kg": "Түзүлүшкө талаптар",
                            "subtitle_en": "Formatting Requirements",
                            "rules": [
                                {
                                    "text_ru": "Объем курсовой работы должен составлять 30-40 страниц",
                                    "text_kg": "Курстук иштин көлөмү 30-40 барак болушу керек",
                                    "text_en": "Course work volume should be 30-40 pages"
                                },
                                {
                                    "text_ru": "Обязательно наличие практической части с анализом данных",
                                    "text_kg": "Маалыматтарды талдоо менен практикалык бөлүктүн болушу милдеттүү",
                                    "text_en": "Practical part with data analysis is mandatory"
                                },
                                {
                                    "text_ru": "Список литературы должен содержать не менее 25 источников",
                                    "text_kg": "Адабият тизмеси 25тен кем эмес булакты камтышы керек",
                                    "text_en": "Bibliography must contain at least 25 sources"
                                }
                            ]
                        }
                    ]
                }
            ],
            "downloadable_files": [
                {
                    "title_ru": "Устав университета",
                    "title_kg": "Университеттин уставы",
                    "title_en": "University Charter",
                    "description_ru": "Основной документ, регламентирующий деятельность университета",
                    "description_kg": "Университеттин ишин жөнгө салган негизги документ",
                    "description_en": "Main document regulating university activities",
                    "type": "PDF",
                    "format": "PDF",
                    "file_size": "2.5 MB",
                    "last_updated": "2024-01-15",
                    "download_url": "http://localhost:8000/media/documents/charter.pdf"
                },
                {
                    "title_ru": "Правила внутреннего распорядка",
                    "title_kg": "Ички тартип эрежелери",
                    "title_en": "Internal Regulations",
                    "description_ru": "Подробные правила поведения студентов и сотрудников",
                    "description_kg": "Студенттердин жана кызматкерлердин жүрүм-турумунун толук эрежелери",
                    "description_en": "Detailed behavior rules for students and staff",
                    "type": "PDF",
                    "format": "PDF",
                    "file_size": "1.8 MB",
                    "last_updated": "2024-02-01",
                    "download_url": "http://localhost:8000/media/documents/internal_rules.pdf"
                },
                {
                    "title_ru": "Положение об экзаменах",
                    "title_kg": "Экзамендер жөнүндө жобо",
                    "title_en": "Examination Regulations",
                    "description_ru": "Полное руководство по проведению промежуточной и итоговой аттестации",
                    "description_kg": "Аралык жана жыйынтыктоочу аттестацияны өткөрүү боюнча толук жетекчилик",
                    "description_en": "Complete guide for conducting intermediate and final assessments",
                    "type": "PDF",
                    "format": "PDF",
                    "file_size": "3.2 MB",
                    "last_updated": "2024-01-20",
                    "download_url": "http://localhost:8000/media/documents/exam_regulations.pdf"
                },
                {
                    "title_ru": "Методические рекомендации по написанию дипломной работы",
                    "title_kg": "Дипломдук иш жазуу боюнча методикалык сунуштар",
                    "title_en": "Guidelines for Writing Diploma Thesis",
                    "description_ru": "Требования к структуре, оформлению и защите выпускной квалификационной работы",
                    "description_kg": "Бүтүрүү квалификациялык ишинин түзүлүшү, түзүлүшү жана коргоого талаптар",
                    "description_en": "Requirements for structure, formatting and defense of graduation thesis",
                    "type": "DOCX",
                    "format": "DOCX",
                    "file_size": "850 KB",
                    "last_updated": "2024-02-10",
                    "download_url": "http://localhost:8000/media/documents/thesis_guidelines.docx"
                },
                {
                    "title_ru": "Академический календарь 2024-2025",
                    "title_kg": "2024-2025 академиялык календары",
                    "title_en": "Academic Calendar 2024-2025",
                    "description_ru": "Расписание учебного года, экзаменационных сессий и каникул",
                    "description_kg": "Окуу жылынын, экзамен сессияларынын жана эс алуулардын расписаниеси",
                    "description_en": "Schedule of academic year, examination sessions and holidays",
                    "type": "PDF",
                    "format": "PDF",
                    "file_size": "1.1 MB",
                    "last_updated": "2024-08-01",
                    "download_url": "http://localhost:8000/media/documents/academic_calendar.pdf"
                }
            ]
        }
        
        # Адаптируем данные под структуру, ожидаемую фронтендом
        # Фронтенд ожидает title, text без суффиксов, поэтому добавляем их для совместимости
        for rule in response_data["internal_rules"]:
            rule["title"] = rule["title_ru"]  # Добавляем для совместимости
            for content_item in rule["content"]:
                content_item["text"] = content_item["text_ru"]  # Добавляем для совместимости
        
        for regulation in response_data["academic_regulations"]:
            regulation["title"] = regulation["title_ru"]  # Добавляем для совместимости
            for section in regulation["sections"]:
                section["subtitle"] = section["subtitle_ru"]  # Добавляем для совместимости
                for rule in section["rules"]:
                    rule["text"] = rule["text_ru"]  # Добавляем для совместимости
        
        for file_item in response_data["downloadable_files"]:
            file_item["title"] = file_item["title_ru"]  # Добавляем для совместимости
            file_item["description"] = file_item["description_ru"]  # Добавляем для совместимости
        
        return Response(response_data)
        
    except Exception as e:
        return Response(
            {'error': f'Ошибка загрузки данных: {str(e)}'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def instructions_data(request):
    """
    API endpoint для данных инструкций для студентов.
    Возвращает пошаговые руководства по важным процедурам.
    """
    try:
        response_data = {
            "student_guides": [
                {
                    "id": 1,
                    "title_ru": "Академический отпуск",
                    "title_kg": "Академиялык эс алуу",
                    "title_en": "Academic Leave",
                    "description_ru": "Пошаговое руководство по оформлению академического отпуска",
                    "description_kg": "Академиялык эс алууну рөмеддөө боюнча кадам-кадам жетекчилик",
                    "description_en": "Step-by-step guide for academic leave registration",
                    "icon": "CalendarDaysIcon",
                    "estimated_time": "2-3 дня",
                    "max_duration": "30 дней",
                    "contact_info": "Деканат: +996 312 123-456 доб. 105",
                    "requirements": [
                        "Заявление на имя ректора",
                        "Справка о состоянии здоровья (при необходимости)",
                        "Документы, подтверждающие причину отпуска",
                        "Справка об отсутствии задолженностей"
                    ],
                    "steps": [
                        {
                            "step_number": 1,
                            "title": "Подготовка документов",
                            "description": "Соберите все необходимые документы для подачи заявления",
                            "timeframe": "1-2 дня",
                            "details": [
                                "Напишите заявление на имя ректора с указанием причины и сроков",
                                "Получите справку от врача (если отпуск по состоянию здоровья)",
                                "Соберите подтверждающие документы (справки, свидетельства)",
                                "Получите справку об отсутствии академических задолженностей"
                            ]
                        },
                        {
                            "step_number": 2,
                            "title": "Подача документов",
                            "description": "Подайте документы в деканат своего факультета",
                            "timeframe": "30 минут",
                            "details": [
                                "Обратитесь в деканат в рабочие часы",
                                "Передайте все документы секретарю деканата",
                                "Получите расписку о приеме документов",
                                "Уточните сроки рассмотрения заявления"
                            ]
                        },
                        {
                            "step_number": 3,
                            "title": "Рассмотрение заявления",
                            "description": "Ожидание решения администрации университета",
                            "timeframe": "5-7 дней",
                            "details": [
                                "Заявление рассматривается деканом факультета",
                                "При необходимости может потребоваться дополнительная документация",
                                "Решение утверждается ректором университета",
                                "Вам сообщат о принятом решении"
                            ]
                        },
                        {
                            "step_number": 4,
                            "title": "Получение приказа",
                            "description": "Получение официального приказа об академическом отпуске",
                            "timeframe": "1 день",
                            "details": [
                                "Явитесь в деканат в указанное время",
                                "Получите копию приказа об академическом отпуске",
                                "Ознакомьтесь с условиями и сроками отпуска",
                                "Сохраните документ для дальнейшего восстановления"
                            ]
                        }
                    ]
                },
                {
                    "id": 2,
                    "title_ru": "Перевод на другую специальность",
                    "title_kg": "Башка адистикке которуу",
                    "title_en": "Transfer to Another Specialty",
                    "description_ru": "Руководство по переводу на другую образовательную программу",
                    "description_kg": "Башка билим берүү программасына которуу боюнча жетекчилик",
                    "description_en": "Guide for transferring to another educational program",
                    "icon": "UserGroupIcon",
                    "estimated_time": "1-2 недели",
                    "max_duration": "До начала семестра",
                    "contact_info": "Учебная часть: +996 312 123-456 доб. 102",
                    "requirements": [
                        "Заявление о переводе",
                        "Академическая справка",
                        "Выписка из зачетной книжки",
                        "Согласие принимающей кафедры"
                    ],
                    "steps": [
                        {
                            "step_number": 1,
                            "title": "Консультация с кафедрой",
                            "description": "Получите консультацию о возможности перевода",
                            "timeframe": "1-2 дня",
                            "details": [
                                "Обратитесь на кафедру желаемой специальности",
                                "Уточните наличие свободных мест",
                                "Получите информацию о разнице в учебных планах",
                                "Узнайте о дополнительных требованиях"
                            ]
                        },
                        {
                            "step_number": 2,
                            "title": "Подготовка документов",
                            "description": "Соберите все необходимые документы",
                            "timeframe": "2-3 дня",
                            "details": [
                                "Напишите заявление о переводе",
                                "Получите академическую справку в деканате",
                                "Сделайте выписку из зачетной книжки",
                                "Получите согласие от принимающей кафедры"
                            ]
                        },
                        {
                            "step_number": 3,
                            "title": "Сдача академической разности",
                            "description": "Ликвидация академической задолженности",
                            "timeframe": "1-4 недели",
                            "details": [
                                "Сравните учебные планы специальностей",
                                "Определите перечень дополнительных дисциплин",
                                "Сдайте экзамены/зачеты по недостающим предметам",
                                "Получите справку о ликвидации разности"
                            ]
                        },
                        {
                            "step_number": 4,
                            "title": "Оформление перевода",
                            "description": "Официальное оформление перевода",
                            "timeframe": "3-5 дней",
                            "details": [
                                "Подайте все документы в учебную часть",
                                "Дождитесь издания приказа о переводе",
                                "Получите новую зачетную книжку",
                                "Ознакомьтесь с новым расписанием"
                            ]
                        }
                    ]
                },
                {
                    "id": 3,
                    "title_ru": "Восстановление после отчисления",
                    "title_kg": "Чыгарылгандан кийин калыбына келтирүү",
                    "title_en": "Restoration After Expulsion",
                    "description_ru": "Процедура восстановления в университете после отчисления",
                    "description_kg": "Чыгарылгандан кийин университетке калыбына келтирүү процедурасы",
                    "description_en": "Procedure for restoration at university after expulsion",
                    "icon": "ClipboardDocumentListIcon",
                    "estimated_time": "2-3 недели",
                    "max_duration": "До начала семестра",
                    "contact_info": "Приемная комиссия: +996 312 123-456 доб. 101",
                    "requirements": [
                        "Заявление о восстановлении",
                        "Копия приказа об отчислении",
                        "Академическая справка",
                        "Документ об образовании"
                    ],
                    "steps": [
                        {
                            "step_number": 1,
                            "title": "Подача заявления",
                            "description": "Подача документов для восстановления",
                            "timeframe": "1 день",
                            "details": [
                                "Напишите заявление на имя ректора",
                                "Приложите копию приказа об отчислении",
                                "Предоставьте академическую справку",
                                "Приложите документ об образовании"
                            ]
                        },
                        {
                            "step_number": 2,
                            "title": "Рассмотрение заявления",
                            "description": "Проверка документов и принятие решения",
                            "timeframe": "7-10 дней",
                            "details": [
                                "Документы проверяются приемной комиссией",
                                "Анализируется академическая успеваемость",
                                "Учитывается причина отчисления",
                                "Принимается решение о возможности восстановления"
                            ]
                        },
                        {
                            "step_number": 3,
                            "title": "Ликвидация задолженностей",
                            "description": "Сдача академических задолженностей",
                            "timeframe": "1-2 недели",
                            "details": [
                                "Получите список задолженностей",
                                "Согласуйте график сдачи с преподавателями",
                                "Сдайте все академические задолженности",
                                "Получите справку о ликвидации задолженностей"
                            ]
                        },
                        {
                            "step_number": 4,
                            "title": "Зачисление",
                            "description": "Официальное восстановление в университете",
                            "timeframe": "2-3 дня",
                            "details": [
                                "Издается приказ о восстановлении",
                                "Выдается новая зачетная книжка",
                                "Оформляется студенческий билет",
                                "Вы зачисляетесь в соответствующую группу"
                            ]
                        }
                    ]
                },
                {
                    "id": 4,
                    "title_ru": "Получение справок и документов",
                    "title_kg": "Маалымат каттары жана документтерди алуу",
                    "title_en": "Obtaining Certificates and Documents",
                    "description_ru": "Порядок получения различных справок и документов",
                    "description_kg": "Ар кандай маалымат каттарын жана документтерди алуу тартиби",
                    "description_en": "Procedure for obtaining various certificates and documents",
                    "icon": "DocumentTextIcon",
                    "estimated_time": "1-3 дня",
                    "max_duration": "Зависит от типа документа",
                    "contact_info": "Канцелярия: +996 312 123-456 доб. 103",
                    "requirements": [
                        "Заявление с указанием типа справки",
                        "Студенческий билет",
                        "Документ, удостоверяющий личность",
                        "Оплата государственной пошлины (при необходимости)"
                    ],
                    "steps": [
                        {
                            "step_number": 1,
                            "title": "Определение типа документа",
                            "description": "Выберите нужный тип справки или документа",
                            "timeframe": "15 минут",
                            "details": [
                                "Справка об обучении",
                                "Справка о периоде обучения",
                                "Академическая справка",
                                "Справка для военкомата",
                                "Справка для получения стипендии",
                                "Дубликат студенческого билета"
                            ]
                        },
                        {
                            "step_number": 2,
                            "title": "Подача заявления",
                            "description": "Оформление заявления на получение документа",
                            "timeframe": "30 минут",
                            "details": [
                                "Заполните заявление с указанием типа справки",
                                "Укажите цель получения документа",
                                "Предъявите студенческий билет",
                                "При необходимости оплатите госпошлину"
                            ]
                        },
                        {
                            "step_number": 3,
                            "title": "Ожидание готовности",
                            "description": "Время обработки заявления",
                            "timeframe": "1-3 дня",
                            "details": [
                                "Стандартные справки готовятся в течение 1-2 дней",
                                "Академические справки - до 3 дней",
                                "Дубликаты документов - до 5 дней",
                                "Вам сообщат о готовности по телефону"
                            ]
                        },
                        {
                            "step_number": 4,
                            "title": "Получение документа",
                            "description": "Получение готовой справки или документа",
                            "timeframe": "15 минут",
                            "details": [
                                "Явитесь в указанное время",
                                "Предъявите документ, удостоверяющий личность",
                                "Получите справку с печатью и подписью",
                                "Проверьте правильность данных в документе"
                            ]
                        }
                    ]
                }
            ]
        }
        
        # Адаптируем данные под структуру, ожидаемую фронтендом
        for guide in response_data["student_guides"]:
            guide["title"] = guide["title_ru"]  # Добавляем для совместимости
            guide["description"] = guide["description_ru"]  # Добавляем для совместимости
        
        return Response(response_data)
        
    except Exception as e:
        return Response(
            {'error': f'Ошибка загрузки данных: {str(e)}'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


class StudentAppealViewSet(viewsets.ModelViewSet):
    queryset = StudentAppeal.objects.all()
    serializer_class = StudentAppealSerializer
    permission_classes = [AllowAny]
    
    def perform_create(self, serializer):
        appeal = serializer.save()
        
        # Отправка email уведомления
        try:
            subject = f"Новое обращение: {appeal.subject}"
            message = f"""
Получено новое обращение от студента:

ФИО: {appeal.full_name}
Email: {appeal.email}
Телефон: {appeal.phone}
Студенческий билет: {appeal.student_id}
Категория: {appeal.get_category_display()}
Тема: {appeal.subject}

Сообщение:
{appeal.message}

Дата создания: {appeal.created_at}
            """
            
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMISSIONS_EMAIL_TO],
                fail_silently=False,
            )
        except Exception as e:
            print(f"Ошибка отправки email: {e}")
