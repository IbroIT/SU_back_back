from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.http import HttpResponse, Http404, FileResponse
from django.utils.encoding import force_str
import os
import mimetypes
from .models import (
    PartnerOrganization, StudentAppeal, PhotoAlbum, Photo, 
    VideoContent, StudentLifeStatistic, InternshipRequirement, ReportTemplate,
    StudentGuide, GuideRequirement, GuideStep, GuideStepDetail
)
from .serializers import (
    PartnerOrganizationSerializer, StudentAppealSerializer,
    PhotoAlbumSerializer, PhotoSerializer, VideoContentSerializer,
    StudentLifeStatisticSerializer, InternshipRequirementSerializer,
    ReportTemplateSerializer, StudentGuideSerializer
)


class PartnerOrganizationViewSet(viewsets.ModelViewSet):
    queryset = PartnerOrganization.objects.filter(is_active=True)
    serializer_class = PartnerOrganizationSerializer
    permission_classes = [AllowAny]


class PhotoAlbumViewSet(viewsets.ModelViewSet):
    """ViewSet для фотоальбомов"""
    queryset = PhotoAlbum.objects.filter(is_active=True)
    serializer_class = PhotoAlbumSerializer
    permission_classes = [AllowAny]

    def get_serializer_context(self):
        return {'request': self.request}

    @action(detail=True, methods=['get'])
    def photos(self, request, pk=None):
        """Получить все фотографии альбома"""
        album = self.get_object()
        photos = album.photos.filter(is_active=True)
        serializer = PhotoSerializer(photos, many=True, context={'request': request})
        return Response(serializer.data)


class PhotoViewSet(viewsets.ModelViewSet):
    """ViewSet для фотографий"""
    queryset = Photo.objects.filter(is_active=True)
    serializer_class = PhotoSerializer
    permission_classes = [AllowAny]

    def get_serializer_context(self):
        return {'request': self.request}


class VideoContentViewSet(viewsets.ModelViewSet):
    """ViewSet для видеоконтента"""
    queryset = VideoContent.objects.filter(is_active=True)
    serializer_class = VideoContentSerializer
    permission_classes = [AllowAny]

    def get_serializer_context(self):
        return {'request': self.request}

    @action(detail=True, methods=['post'])
    def increment_views(self, request, pk=None):
        """Увеличить счетчик просмотров"""
        video = self.get_object()
        video.views_count += 1
        video.save()
        return Response({'views_count': video.views_count})


class StudentLifeStatisticViewSet(viewsets.ModelViewSet):
    """ViewSet для статистики студенческой жизни"""
    queryset = StudentLifeStatistic.objects.filter(is_active=True)
    serializer_class = StudentLifeStatisticSerializer
    permission_classes = [AllowAny]

    def get_serializer_context(self):
        return {'request': self.request}


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
        
        # Добавляем совместимость с фронтендом для specializations
        for org in organizations_data:
            org['name'] = org['name_ru']  # Добавляем name для совместимости
            org['description'] = org['description_ru']  # Добавляем description для совместимости
            
            # Обрабатываем specializations
            if 'specializations' in org:
                for spec in org['specializations']:
                    spec['name'] = spec['name_ru']  # Добавляем name для совместимости
        
        # Получаем требования к практике из базы данных
        internship_requirements = InternshipRequirement.objects.filter(is_active=True).prefetch_related('items')
        requirements_serializer = InternshipRequirementSerializer(internship_requirements, many=True, context={'request': request})
        requirements = {}
        
        for req_data in requirements_serializer.data:
            category = req_data['category']
            if category not in requirements:
                requirements[category] = []
            requirements[category].append(req_data)
        
        # Получаем шаблоны отчетов из базы данных
        templates = ReportTemplate.objects.filter(is_active=True)
        templates_serializer = ReportTemplateSerializer(templates, many=True, context={'request': request})
        report_templates = []
        
        for template_data in templates_serializer.data:
            # Определяем формат файла и размер
            file_format = 'DOC'
            file_size = 'N/A'
            
            if template_data['file']:
                file_url = template_data['file']
                if file_url.lower().endswith('.docx'):
                    file_format = 'DOCX'
                elif file_url.lower().endswith('.pdf'):
                    file_format = 'PDF'
            
            report_templates.append({
                'id': template_data['id'],
                'title': template_data['name'],
                'description': template_data['description'],
                'title_ru': template_data.get('name_ru', template_data['name']),
                'title_kg': template_data.get('name_kg', template_data['name']),
                'title_en': template_data.get('name_en', template_data['name']),
                'description_ru': template_data.get('description_ru', template_data['description']),
                'description_kg': template_data.get('description_kg', template_data['description']),
                'description_en': template_data.get('description_en', template_data['description']),
                'format': file_format,
                'file_size': file_size,  # Размер можно получить из файла
                'file': template_data['file_url'],
                'download_url': template_data['download_url']
            })
        
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
    Возвращает пошаговые руководства по важным процедурам из базы данных.
    """
    try:
        # Получаем все активные инструкции из базы данных
        guides = StudentGuide.objects.filter(is_active=True).prefetch_related(
            'requirements', 'steps__details'
        ).order_by('order')
        
        # Сериализуем данные
        serializer = StudentGuideSerializer(guides, many=True, context={'request': request})
        
        # Преобразуем данные в формат, ожидаемый фронтендом
        student_guides = []
        for guide_data in serializer.data:
            # Преобразуем требования в простой список строк для каждого языка
            requirements_ru = [req['text_ru'] for req in guide_data.get('requirements', [])]
            requirements_kg = [req['text_kg'] for req in guide_data.get('requirements', [])]
            requirements_en = [req['text_en'] for req in guide_data.get('requirements', [])]
            
            # Преобразуем шаги в нужный формат
            steps = []
            for step_data in guide_data.get('steps', []):
                # Преобразуем детали шага в простой список строк для каждого языка
                details_ru = [detail['text_ru'] for detail in step_data.get('details', [])]
                details_kg = [detail['text_kg'] for detail in step_data.get('details', [])]
                details_en = [detail['text_en'] for detail in step_data.get('details', [])]
                
                step = {
                    "step_number": step_data.get('step_number', 1),
                    "title_ru": step_data.get('title_ru', ''),
                    "title_kg": step_data.get('title_kg', ''),
                    "title_en": step_data.get('title_en', ''),
                    "description_ru": step_data.get('description_ru', ''),
                    "description_kg": step_data.get('description_kg', ''),
                    "description_en": step_data.get('description_en', ''),
                    "timeframe_ru": step_data.get('timeframe_ru', ''),
                    "timeframe_kg": step_data.get('timeframe_kg', ''),
                    "timeframe_en": step_data.get('timeframe_en', ''),
                    "details_ru": details_ru,
                    "details_kg": details_kg,
                    "details_en": details_en
                }
                steps.append(step)
            
            # Формируем данные инструкции в ожидаемом формате
            guide = {
                "id": guide_data['id'],
                "title_ru": guide_data.get('title_ru', ''),
                "title_kg": guide_data.get('title_kg', ''),
                "title_en": guide_data.get('title_en', ''),
                "description_ru": guide_data.get('description_ru', ''),
                "description_kg": guide_data.get('description_kg', ''),
                "description_en": guide_data.get('description_en', ''),
                "icon": guide_data.get('icon', 'DocumentTextIcon'),
                "estimated_time_ru": guide_data.get('estimated_time_ru', ''),
                "estimated_time_kg": guide_data.get('estimated_time_kg', ''),
                "estimated_time_en": guide_data.get('estimated_time_en', ''),
                "max_duration_ru": guide_data.get('max_duration_ru', ''),
                "max_duration_kg": guide_data.get('max_duration_kg', ''),
                "max_duration_en": guide_data.get('max_duration_en', ''),
                "contact_info_ru": guide_data.get('contact_info_ru', ''),
                "contact_info_kg": guide_data.get('contact_info_kg', ''),
                "contact_info_en": guide_data.get('contact_info_en', ''),
                "category": guide_data.get('category', 'academic'),
                "requirements_ru": requirements_ru,
                "requirements_kg": requirements_kg,
                "requirements_en": requirements_en,
                "steps": steps
            }
            student_guides.append(guide)
        
        response_data = {
            "student_guides": student_guides
        }
        
        return Response(response_data, status=status.HTTP_200_OK)
                            "step_number": 1,
                            "title_ru": "Подготовка документов",
                            "title_kg": "Документтерди даярдоо",
                            "title_en": "Document Preparation",
                            "description_ru": "Соберите все необходимые документы для подачи заявления",
                            "description_kg": "Арыз берүү үчүн бардык керектүү документтерди чогултуңуз",
                            "description_en": "Collect all necessary documents for application submission",
                            "timeframe_ru": "1-2 дня",
                            "timeframe_kg": "1-2 күн",
                            "timeframe_en": "1-2 days",
                            "details_ru": [
                                "Напишите заявление на имя ректора с указанием причины и сроков",
                                "Получите справку от врача (если отпуск по состоянию здоровья)",
                                "Соберите подтверждающие документы (справки, свидетельства)",
                                "Получите справку об отсутствии академических задолженностей"
                            ],
                            "details_kg": [
                                "Ректордун атына себеби жана мөөнөтү көрсөтүлгөн арыз жазыңыз",
                                "Врачтан справка алыңыз (эгер ден соолук абалына байланыштуу болсо)",
                                "Далилдөөчү документтерди чогултуңуз (справкалар, күбөлүктөр)",
                                "Академиялык карыз жок экендиги жөнүндө справка алыңыз"
                            ],
                            "details_en": [
                                "Write an application to the rector indicating the reason and timeframe",
                                "Get a medical certificate (if leave is for health reasons)",
                                "Collect supporting documents (certificates, testimonials)",
                                "Get a certificate of no academic debts"
                            ]
                        },
                        {
                            "step_number": 2,
                            "title_ru": "Подача документов",
                            "title_kg": "Документтерди берүү",
                            "title_en": "Document Submission",
                            "description_ru": "Подайте документы в деканат своего факультета",
                            "description_kg": "Документтерди өз факультетиңиздин деканатына бериңиз",
                            "description_en": "Submit documents to your faculty's dean's office",
                            "timeframe_ru": "30 минут",
                            "timeframe_kg": "30 мүнөт",
                            "timeframe_en": "30 minutes",
                            "details_ru": [
                                "Обратитесь в деканат в рабочие часы",
                                "Передайте все документы секретарю деканата",
                                "Получите расписку о приеме документов",
                                "Уточните сроки рассмотрения заявления"
                            ],
                            "details_kg": [
                                "Иш убагында деканатка кайрылыңыз",
                                "Бардык документтерди деканаттын катчысына өткөрүңүз",
                                "Документтерди кабыл алгандыгы жөнүндө расписка алыңыз",
                                "Арызды карап чыгуу мөөнөттөрүн так билиңиз"
                            ],
                            "details_en": [
                                "Contact the dean's office during working hours",
                                "Submit all documents to the dean's secretary",
                                "Get a receipt for document acceptance",
                                "Clarify the application review timeframe"
                            ]
                        },
                        {
                            "step_number": 3,
                            "title_ru": "Рассмотрение заявления",
                            "title_kg": "Арызды карап чыгуу",
                            "title_en": "Application Review",
                            "description_ru": "Ожидание решения администрации университета",
                            "description_kg": "Университеттин администрациясынын чечимин күтүү",
                            "description_en": "Waiting for university administration decision",
                            "timeframe_ru": "5-7 дней",
                            "timeframe_kg": "5-7 күн",
                            "timeframe_en": "5-7 days",
                            "details_ru": [
                                "Заявление рассматривается деканом факультета",
                                "При необходимости может потребоваться дополнительная документация",
                                "Решение утверждается ректором университета",
                                "Вам сообщат о принятом решении"
                            ],
                            "details_kg": [
                                "Арызды факультеттин деканы карайт",
                                "Зарылчылыгына жараша кошумча документация талап кылынышы мүмкүн",
                                "Чечимди университеттин ректору бекитет",
                                "Силерге кабыл алынган чечим жөнүндө кабарлайт"
                            ],
                            "details_en": [
                                "Application is reviewed by the faculty dean",
                                "Additional documentation may be required if necessary",
                                "Decision is approved by the university rector",
                                "You will be notified of the decision made"
                            ]
                        },
                        {
                            "step_number": 4,
                            "title_ru": "Получение приказа",
                            "title_kg": "Буйруктуу алуу",
                            "title_en": "Receiving the Order",
                            "description_ru": "Получение официального приказа об академическом отпуске",
                            "description_kg": "Академиялык эс алуу жөнүндө расмий буйруктуу алуу",
                            "description_en": "Receiving official order for academic leave",
                            "timeframe_ru": "1 день",
                            "timeframe_kg": "1 күн",
                            "timeframe_en": "1 day",
                            "details_ru": [
                                "Явитесь в деканат в указанное время",
                                "Получите копию приказа об академическом отпуске",
                                "Ознакомьтесь с условиями и сроками отпуска",
                                "Сохраните документ для дальнейшего восстановления"
                            ],
                            "details_kg": [
                                "Көрсөтүлгөн убакытта деканатка келиңиз",
                                "Академиялык эс алуу жөнүндө буйруктун көчүрмөсүн алыңыз",
                                "Эс алуунун шарттары жана мөөнөттөрү менен таанышыңыз",
                                "Кийинки калыбына келтирүү үчүн документти сактаңыз"
                            ],
                            "details_en": [
                                "Come to the dean's office at the specified time",
                                "Get a copy of the academic leave order",
                                "Familiarize yourself with leave conditions and terms",
                                "Keep the document for future restoration"
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
                    "estimated_time_ru": "1-2 недели",
                    "estimated_time_kg": "1-2 жума",
                    "estimated_time_en": "1-2 weeks",
                    "max_duration_ru": "До начала семестра",
                    "max_duration_kg": "Семестр башталганга чейин",
                    "max_duration_en": "Before the semester starts",
                    "contact_info_ru": "Учебная часть: +996 312 123-456 доб. 102",
                    "contact_info_kg": "Окуу бөлүмү: +996 312 123-456 кош. 102",
                    "contact_info_en": "Academic Office: +996 312 123-456 ext. 102",
                    "requirements_ru": [
                        "Заявление о переводе",
                        "Академическая справка",
                        "Выписка из зачетной книжки",
                        "Согласие принимающей кафедры"
                    ],
                    "requirements_kg": [
                        "Которуу жөнүндө арыз",
                        "Академиялык справка",
                        "Белгилер китебинен көчүрмө",
                        "Кабыл алуучу кафедранын макулдугу"
                    ],
                    "requirements_en": [
                        "Transfer application",
                        "Academic transcript",
                        "Excerpt from grade book",
                        "Consent from receiving department"
                    ],
                    "steps": [
                        {
                            "step_number": 1,
                            "title_ru": "Консультация с кафедрой",
                            "title_kg": "Кафедра менен консультация",
                            "title_en": "Department Consultation",
                            "description_ru": "Получите консультацию о возможности перевода",
                            "description_kg": "Которуу мүмкүнчүлүгү жөнүндө консультация алыңыз",
                            "description_en": "Get consultation about transfer possibility",
                            "timeframe_ru": "1-2 дня",
                            "timeframe_kg": "1-2 күн",
                            "timeframe_en": "1-2 days",
                            "details_ru": [
                                "Обратитесь на кафедру желаемой специальности",
                                "Уточните наличие свободных мест",
                                "Получите информацию о разнице в учебных планах",
                                "Узнайте о дополнительных требованиях"
                            ],
                            "details_kg": [
                                "Каалаган адистиктин кафедрасына кайрылыңыз",
                                "Бош орундардын барын так билиңиз",
                                "Окуу пландарынын айырмасы жөнүндө маалымат алыңыз",
                                "Кошумча талаптар жөнүндө билиңиз"
                            ],
                            "details_en": [
                                "Contact the department of desired specialty",
                                "Check availability of vacant places",
                                "Get information about curriculum differences",
                                "Learn about additional requirements"
                            ]
                        },
                        {
                            "step_number": 2,
                            "title_ru": "Подготовка документов",
                            "title_kg": "Документтерди даярдоо",
                            "title_en": "Document Preparation",
                            "description_ru": "Соберите все необходимые документы",
                            "description_kg": "Бардык керектүү документтерди чогултуңуз",
                            "description_en": "Collect all necessary documents",
                            "timeframe_ru": "2-3 дня",
                            "timeframe_kg": "2-3 күн",
                            "timeframe_en": "2-3 days",
                            "details_ru": [
                                "Напишите заявление о переводе",
                                "Получите академическую справку в деканате",
                                "Сделайте выписку из зачетной книжки",
                                "Получите согласие от принимающей кафедры"
                            ],
                            "details_kg": [
                                "Которуу жөнүндө арыз жазыңыз",
                                "Деканаттан академиялык справка алыңыз",
                                "Белгилер китебинен көчүрмө жасаңыз",
                                "Кабыл алуучу кафедрадан макулдук алыңыз"
                            ],
                            "details_en": [
                                "Write a transfer application",
                                "Get academic transcript from dean's office",
                                "Make excerpt from grade book",
                                "Get consent from receiving department"
                            ]
                        },
                        {
                            "step_number": 3,
                            "title_ru": "Сдача академической разности",
                            "title_kg": "Академиялык айырманы тапшыруу",
                            "title_en": "Academic Difference Examination",
                            "description_ru": "Ликвидация академической задолженности",
                            "description_kg": "Академиялык карызды жоюу",
                            "description_en": "Academic debt elimination",
                            "timeframe_ru": "1-4 недели",
                            "timeframe_kg": "1-4 жума",
                            "timeframe_en": "1-4 weeks",
                            "details_ru": [
                                "Сравните учебные планы специальностей",
                                "Определите перечень дополнительных дисциплин",
                                "Сдайте экзамены/зачеты по недостающим предметам",
                                "Получите справку о ликвидации разности"
                            ],
                            "details_kg": [
                                "Адистиктердин окуу пландарын салыштырыңыз",
                                "Кошумча дисциплиналардын тизмесин аныктаңыз",
                                "Жетишпеген сабактар боюнча экзамен/зачет тапшырыңыз",
                                "Айырманы жок кылуу жөнүндө справка алыңыз"
                            ],
                            "details_en": [
                                "Compare specialty curricula",
                                "Determine list of additional disciplines",
                                "Pass exams/credits for missing subjects",
                                "Get certificate of difference elimination"
                            ]
                        },
                        {
                            "step_number": 4,
                            "title_ru": "Оформление перевода",
                            "title_kg": "Которууну рөмеддөө",
                            "title_en": "Transfer Formalization",
                            "description_ru": "Официальное оформление перевода",
                            "description_kg": "Которуунун расмий рөмеддөлүшү",
                            "description_en": "Official transfer formalization",
                            "timeframe_ru": "3-5 дней",
                            "timeframe_kg": "3-5 күн",
                            "timeframe_en": "3-5 days",
                            "details_ru": [
                                "Подайте все документы в учебную часть",
                                "Дождитесь издания приказа о переводе",
                                "Получите новую зачетную книжку",
                                "Ознакомьтесь с новым расписанием"
                            ],
                            "details_kg": [
                                "Бардык документтерди окуу бөлүмүнө бериңиз",
                                "Которуу жөнүндө буйруктун чыгарылышын күтүңүз",
                                "Жаңы белгилер китебин алыңыз",
                                "Жаңы сабак расписаниясы менен таанышыңыз"
                            ],
                            "details_en": [
                                "Submit all documents to academic office",
                                "Wait for transfer order issuance",
                                "Get new grade book",
                                "Familiarize with new schedule"
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
                    "estimated_time_ru": "2-3 недели",
                    "estimated_time_kg": "2-3 жума",
                    "estimated_time_en": "2-3 weeks",
                    "max_duration_ru": "До начала семестра",
                    "max_duration_kg": "Семестр башталганга чейин",
                    "max_duration_en": "Before the semester starts",
                    "contact_info_ru": "Приемная комиссия: +996 312 123-456 доб. 101",
                    "contact_info_kg": "Кабыл алуу комиссиясы: +996 312 123-456 кош. 101",
                    "contact_info_en": "Admissions Committee: +996 312 123-456 ext. 101",
                    "requirements_ru": [
                        "Заявление о восстановлении",
                        "Копия приказа об отчислении",
                        "Академическая справка",
                        "Документ об образовании"
                    ],
                    "requirements_kg": [
                        "Калыбына келтирүү жөнүндө арыз",
                        "Чыгаруу жөнүндө буйруктун көчүрмөсү",
                        "Академиялык справка",
                        "Билим жөнүндө документ"
                    ],
                    "requirements_en": [
                        "Restoration application",
                        "Copy of expulsion order",
                        "Academic transcript",
                        "Education document"
                    ],
                    "steps": [
                        {
                            "step_number": 1,
                            "title_ru": "Подача заявления",
                            "title_kg": "Арыз берүү",
                            "title_en": "Application Submission",
                            "description_ru": "Подача документов для восстановления",
                            "description_kg": "Калыбына келтирүү үчүн документтерди берүү",
                            "description_en": "Document submission for restoration",
                            "timeframe_ru": "1 день",
                            "timeframe_kg": "1 күн",
                            "timeframe_en": "1 day",
                            "details_ru": [
                                "Напишите заявление на имя ректора",
                                "Приложите копию приказа об отчислении",
                                "Предоставьте академическую справку",
                                "Приложите документ об образовании"
                            ],
                            "details_kg": [
                                "Ректордун атына арыз жазыңыз",
                                "Чыгаруу жөнүндө буйруктун көчүрмөсүн тиркеңиз",
                                "Академиялык справканы бериңиз",
                                "Билим жөнүндө документти тиркеңиз"
                            ],
                            "details_en": [
                                "Write an application addressed to the rector",
                                "Attach a copy of the expulsion order",
                                "Provide academic transcript",
                                "Attach education document"
                            ]
                        },
                        {
                            "step_number": 2,
                            "title_ru": "Рассмотрение заявления",
                            "title_kg": "Арызды карап чыгуу",
                            "title_en": "Application Review",
                            "description_ru": "Проверка документов и принятие решения",
                            "description_kg": "Документтерди текшерүү жана чечим чыгаруу",
                            "description_en": "Document verification and decision making",
                            "timeframe_ru": "7-10 дней",
                            "timeframe_kg": "7-10 күн",
                            "timeframe_en": "7-10 days",
                            "details_ru": [
                                "Документы проверяются приемной комиссией",
                                "Анализируется академическая успеваемость",
                                "Учитывается причина отчисления",
                                "Принимается решение о возможности восстановления"
                            ],
                            "details_kg": [
                                "Документтерди кабыл алуу комиссиясы текшерет",
                                "Академиялык жетишкендик талданат",
                                "Чыгаруунун себеби эсепке алынат",
                                "Калыбына келтирүү мүмкүнчүлүгү жөнүндө чечим чыгарылат"
                            ],
                            "details_en": [
                                "Documents are reviewed by admissions committee",
                                "Academic performance is analyzed",
                                "Expulsion reason is considered",
                                "Decision about restoration possibility is made"
                            ]
                        },
                        {
                            "step_number": 3,
                            "title_ru": "Ликвидация задолженностей",
                            "title_kg": "Карыздарды жоюу",
                            "title_en": "Debt Elimination",
                            "description_ru": "Сдача академических задолженностей",
                            "description_kg": "Академиялык карыздарды тапшыруу",
                            "description_en": "Academic debt settlement",
                            "timeframe_ru": "1-2 недели",
                            "timeframe_kg": "1-2 жума",
                            "timeframe_en": "1-2 weeks",
                            "details_ru": [
                                "Получите список задолженностей",
                                "Согласуйте график сдачи с преподавателями",
                                "Сдайте все академические задолженности",
                                "Получите справку о ликвидации задолженностей"
                            ],
                            "details_kg": [
                                "Карыздардын тизмесин алыңыз",
                                "Мугалимдер менен тапшыруу графигин келишиңиз",
                                "Бардык академиялык карыздарды тапшырыңыз",
                                "Карыздарды жок кылуу жөнүндө справка алыңыз"
                            ],
                            "details_en": [
                                "Get list of debts",
                                "Coordinate submission schedule with teachers",
                                "Submit all academic debts",
                                "Get certificate of debt elimination"
                            ]
                        },
                        {
                            "step_number": 4,
                            "title_ru": "Зачисление",
                            "title_kg": "Кабыл алуу",
                            "title_en": "Enrollment",
                            "description_ru": "Официальное восстановление в университете",
                            "description_kg": "Университетке расмий калыбына келтирүү",
                            "description_en": "Official restoration at university",
                            "timeframe_ru": "2-3 дня",
                            "timeframe_kg": "2-3 күн",
                            "timeframe_en": "2-3 days",
                            "details_ru": [
                                "Издается приказ о восстановлении",
                                "Выдается новая зачетная книжка",
                                "Оформляется студенческий билет",
                                "Вы зачисляетесь в соответствующую группу"
                            ],
                            "details_kg": [
                                "Калыбына келтирүү жөнүндө буйрук чыгарылат",
                                "Жаңы белгилер китеби берилет",
                                "Студенттик билет рөмеддөлөт",
                                "Сиз тиешелүү топко кабыл алынасыз"
                            ],
                            "details_en": [
                                "Restoration order is issued",
                                "New grade book is issued",
                                "Student card is processed",
                                "You are enrolled in appropriate group"
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
                    "estimated_time_ru": "1-3 дня",
                    "estimated_time_kg": "1-3 күн",
                    "estimated_time_en": "1-3 days",
                    "max_duration_ru": "Зависит от типа документа",
                    "max_duration_kg": "Документтин түрүнө жараша",
                    "max_duration_en": "Depends on document type",
                    "contact_info_ru": "Канцелярия: +996 312 123-456 доб. 103",
                    "contact_info_kg": "Канцелярия: +996 312 123-456 кош. 103",
                    "contact_info_en": "Secretariat: +996 312 123-456 ext. 103",
                    "requirements_ru": [
                        "Заявление с указанием типа справки",
                        "Студенческий билет",
                        "Документ, удостоверяющий личность",
                        "Оплата государственной пошлины (при необходимости)"
                    ],
                    "requirements_kg": [
                        "Маалымат каттын түрүн көрсөткөн арыз",
                        "Студенттик билет",
                        "Жеке инсанды тастыктоочу документ",
                        "Мамлекеттик баж төлөө (зарылчылыгына жараша)"
                    ],
                    "requirements_en": [
                        "Application indicating certificate type",
                        "Student card",
                        "Identity document",
                        "State fee payment (if required)"
                    ],
                    "steps": [
                        {
                            "step_number": 1,
                            "title_ru": "Определение типа документа",
                            "title_kg": "Документтин түрүн аныктоо",
                            "title_en": "Document Type Determination",
                            "description_ru": "Выберите нужный тип справки или документа",
                            "description_kg": "Керектүү маалымат каттын же документтин түрүн тандаңыз",
                            "description_en": "Choose the required certificate or document type",
                            "timeframe_ru": "15 минут",
                            "timeframe_kg": "15 мүнөт",
                            "timeframe_en": "15 minutes",
                            "details_ru": [
                                "Справка об обучении",
                                "Справка о периоде обучения",
                                "Академическая справка",
                                "Справка для военкомата",
                                "Справка для получения стипендии",
                                "Дубликат студенческого билета"
                            ],
                            "details_kg": [
                                "Окуу жөнүндө маалымат кат",
                                "Окуу мезгили жөнүндө маалымат кат",
                                "Академиялык маалымат кат",
                                "Аскердик комиссариат үчүн маалымат кат",
                                "Стипендия алуу үчүн маалымат кат",
                                "Студенттик билеттин дубликаты"
                            ],
                            "details_en": [
                                "Study certificate",
                                "Study period certificate",
                                "Academic transcript",
                                "Certificate for military commissariat",
                                "Certificate for scholarship",
                                "Student card duplicate"
                            ]
                        },
                        {
                            "step_number": 2,
                            "title_ru": "Подача заявления",
                            "title_kg": "Арыз берүү",
                            "title_en": "Application Submission",
                            "description_ru": "Оформление заявления на получение документа",
                            "description_kg": "Документ алуу үчүн арыз рөмеддөө",
                            "description_en": "Application processing for document receipt",
                            "timeframe_ru": "30 минут",
                            "timeframe_kg": "30 мүнөт",
                            "timeframe_en": "30 minutes",
                            "details_ru": [
                                "Заполните заявление с указанием типа справки",
                                "Укажите цель получения документа",
                                "Предъявите студенческий билет",
                                "При необходимости оплатите госпошлину"
                            ],
                            "details_kg": [
                                "Маалымат каттын түрүн көрсөтүп арызды толтуруңуз",
                                "Документти алуу максатын көрсөтүңүз",
                                "Студенттик билетти көрсөтүңүз",
                                "Зарылчылыгына жараша мамлекеттик бажды төлөңүз"
                            ],
                            "details_en": [
                                "Fill out application indicating certificate type",
                                "Specify purpose of document receipt",
                                "Present student card",
                                "Pay state fee if necessary"
                            ]
                        },
                        {
                            "step_number": 3,
                            "title_ru": "Ожидание готовности",
                            "title_kg": "Даярдыкты күтүү",
                            "title_en": "Waiting for Readiness",
                            "description_ru": "Время обработки заявления",
                            "description_kg": "Арызды иштеп чыгуу убактысы",
                            "description_en": "Application processing time",
                            "timeframe_ru": "1-3 дня",
                            "timeframe_kg": "1-3 күн",
                            "timeframe_en": "1-3 days",
                            "details_ru": [
                                "Стандартные справки готовятся в течение 1-2 дней",
                                "Академические справки - до 3 дней",
                                "Дубликаты документов - до 5 дней",
                                "Вам сообщат о готовности по телефону"
                            ],
                            "details_kg": [
                                "Стандарттык маалымат каттар 1-2 күндүн ичинде даярдалат",
                                "Академиялык маалымат каттар - 3 күнгө чейин",
                                "Документтердин дубликаттары - 5 күнгө чейин",
                                "Даярдыгы жөнүндө телефон аркылуу кабарлайт"
                            ],
                            "details_en": [
                                "Standard certificates are prepared within 1-2 days",
                                "Academic transcripts - up to 3 days",
                                "Document duplicates - up to 5 days",
                                "You will be notified of readiness by phone"
                            ]
                        },
                        {
                            "step_number": 4,
                            "title_ru": "Получение документа",
                            "title_kg": "Документти алуу",
                            "title_en": "Document Receipt",
                            "description_ru": "Получение готовой справки или документа",
                            "description_kg": "Даяр маалымат катты же документти алуу",
                            "description_en": "Receiving ready certificate or document",
                            "timeframe_ru": "15 минут",
                            "timeframe_kg": "15 мүнөт",
                            "timeframe_en": "15 minutes",
                            "details_ru": [
                                "Явитесь в указанное время",
                                "Предъявите документ, удостоверяющий личность",
                                "Получите справку с печатью и подписью",
                                "Проверьте правильность данных в документе"
                            ],
                            "details_kg": [
                                "Көрсөтүлгөн убакытта келиңиз",
                                "Жеке инсанды тастыктоочу документти көрсөтүңүз",
                                "Мөөр жана кол коюлган маалымат катты алыңыз",
                                "Документтеги маалыматтардын туурасын текшериңиз"
                            ],
                            "details_en": [
                                "Come at the specified time",
                                "Present identity document",
                                "Receive certificate with stamp and signature",
                                "Check correctness of data in document"
                            ]
                        }
                    ]
                }
            ]
        }
        
    except Exception as e:
        return Response(
            {"error": f"Ошибка получения данных инструкций: {str(e)}"}, 
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
            
            # Support multiple email addresses (separated by commas)
            recipients = [email.strip() for email in settings.STUDENT_APPEALS_EMAIL_TO.split(',')]
            
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=recipients,
                fail_silently=False,
            )
        except Exception as e:
            print(f"Ошибка отправки email: {e}")


# =============================================================================
# НОВЫЕ API ENDPOINTS ДЛЯ ГАЛЕРЕИ И ОБЗОРА СТУДЕНЧЕСКОЙ ЖИЗНИ
# =============================================================================

@api_view(['GET'])
def gallery_data(request):
    """API endpoint для данных галереи"""
    try:
        albums = PhotoAlbum.objects.filter(is_active=True)
        photos = Photo.objects.filter(is_active=True)
        
        # Сериализация данных
        albums_serializer = PhotoAlbumSerializer(albums, many=True, context={'request': request})
        photos_serializer = PhotoSerializer(photos, many=True, context={'request': request})
        
        # Формируем структуру данных, совместимую с фронтендом
        albums_data = []
        for album_data in albums_serializer.data:
            # Преобразуем для совместимости с фронтендом
            album_compatible = {
                'id': album_data['id'],
                'titleKey': f"gallery.albums.album{album_data['id']}.title",
                'title': album_data['title'],
                'photoCount': album_data['photo_count'],
                'cover': album_data['cover'],
                'tagsKey': f"gallery.albums.album{album_data['id']}.tags",
                'tags': album_data['tags'],
                'event_date': album_data['event_date'],
                'order': album_data['order']
            }
            albums_data.append(album_compatible)
        
        photos_data = []
        for photo_data in photos_serializer.data:
            # Преобразуем для совместимости с фронтендом
            photo_compatible = {
                'id': photo_data['id'],
                'albumId': photo_data.get('album_id'),  # Нужно добавить это поле в сериализатор
                'url': photo_data['url'],
                'titleKey': f"gallery.photos.photo{photo_data['id']}.title",
                'title': photo_data['title'],
                'tagsKey': f"gallery.photos.photo{photo_data['id']}.tags",
                'tags': photo_data['tags'],
                'photographer': photo_data['photographer'],
                'uploaded_at': photo_data['uploaded_at']
            }
            photos_data.append(photo_compatible)
        
        response_data = {
            'albums': albums_data,
            'photos': photos_data
        }
        
        return Response(response_data)
        
    except Exception as e:
        return Response(
            {'error': f'Ошибка загрузки данных галереи: {str(e)}'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def life_overview_data(request):
    """API endpoint для данных обзора студенческой жизни"""
    try:
        # Получаем фотографии для коллажа (последние 12)
        recent_photos = Photo.objects.filter(is_active=True).order_by('-uploaded_at')[:12]
        photos_serializer = PhotoSerializer(recent_photos, many=True, context={'request': request})
        
        # Получаем видео (рекомендуемые или последние)
        featured_videos = VideoContent.objects.filter(is_active=True, is_featured=True)[:3]
        if featured_videos.count() < 3:
            # Если рекомендуемых видео недостаточно, дополняем последними
            additional_videos = VideoContent.objects.filter(is_active=True).exclude(
                id__in=featured_videos.values_list('id', flat=True)
            ).order_by('-created_at')[:3-featured_videos.count()]
            featured_videos = list(featured_videos) + list(additional_videos)
        
        videos_serializer = VideoContentSerializer(featured_videos, many=True, context={'request': request})
        
        # Получаем статистику
        statistics = StudentLifeStatistic.objects.filter(is_active=True).order_by('order')
        stats_serializer = StudentLifeStatisticSerializer(statistics, many=True, context={'request': request})
        
        # Формируем фото-URLs для коллажа
        photo_urls = [photo_data['url'] for photo_data in photos_serializer.data if photo_data['url']]
        
        # Формируем данные видео в формате, ожидаемом фронтендом
        video_data = []
        for video in videos_serializer.data:
            video_compatible = {
                'id': video['id'],
                'titleKey': f"life.videos.video{video['id']}.title",
                'title': video['title'],
                'thumbnail': video['thumbnail_url'],
                'url': video['video_source'],
                'durationKey': 'life.videos.duration',
                'duration': video['duration'] if video['duration'] else '3:24',
                'type': video['type'],
                'views_count': video['views_count']
            }
            video_data.append(video_compatible)
        
        # Формируем статистику в формате, ожидаемом фронтендом
        stats_data = []
        for stat in stats_serializer.data:
            stat_compatible = {
                'value': stat['value'],
                'labelKey': f"life.stats.{stat['type']}.label",
                'label': stat['label'],
                'type': stat['type'],
                'icon': stat['icon']
            }
            stats_data.append(stat_compatible)
        
        # Если статистики нет в базе, используем дефолтные значения
        if not stats_data:
            stats_data = [
                {
                    'value': '15+',
                    'labelKey': 'life.stats.clubs.label',
                    'label': 'Клубы и организации',
                    'type': 'clubs'
                },
                {
                    'value': '50+',
                    'labelKey': 'life.stats.events.label', 
                    'label': 'Мероприятий в год',
                    'type': 'events'
                },
                {
                    'value': f'{len(photo_urls)}+',
                    'labelKey': 'life.stats.photos.label',
                    'label': 'Фотографий',
                    'type': 'photos'
                }
            ]
        
        response_data = {
            'photo_urls': photo_urls,
            'video_data': video_data,
            'stats': stats_data,
            'total_photos': Photo.objects.filter(is_active=True).count(),
            'total_albums': PhotoAlbum.objects.filter(is_active=True).count(),
            'total_videos': VideoContent.objects.filter(is_active=True).count()
        }
        
        return Response(response_data)
        
    except Exception as e:
        return Response(
            {'error': f'Ошибка загрузки данных обзора: {str(e)}'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def download_file(request, file_id):
    """
    Безопасное скачивание файлов с правильной UTF-8 кодировкой
    """
    try:
        # Ищем файл среди шаблонов отчетов
        template = ReportTemplate.objects.get(id=file_id)
        
        if not template.file:
            raise Http404("Файл не найден")
        
        file_path = template.file.path
        
        if not os.path.exists(file_path):
            raise Http404("Файл не существует на сервере")
        
        # Определяем MIME тип
        content_type, encoding = mimetypes.guess_type(file_path)
        if content_type is None:
            content_type = 'application/octet-stream'
        
        # Читаем файл с правильной кодировкой
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                file_content = f.read()
            
            # Создаем response с UTF-8 кодировкой
            response = HttpResponse(file_content.encode('utf-8'), content_type=f'{content_type}; charset=utf-8')
            response['Content-Disposition'] = f'attachment; filename*=UTF-8\'\'{force_str(template.name_ru)}.txt'
            return response
            
        except UnicodeDecodeError:
            # Если файл не UTF-8, пробуем другие кодировки
            for encoding in ['cp1251', 'iso-8859-1']:
                try:
                    with open(file_path, 'r', encoding=encoding) as f:
                        file_content = f.read()
                    
                    response = HttpResponse(file_content.encode('utf-8'), content_type=f'{content_type}; charset=utf-8')
                    response['Content-Disposition'] = f'attachment; filename*=UTF-8\'\'{force_str(template.name_ru)}.txt'
                    return response
                except UnicodeDecodeError:
                    continue
            
            # Если ни одна кодировка не подошла, возвращаем как бинарный файл
            return FileResponse(open(file_path, 'rb'), content_type=content_type, as_attachment=True)
        
    except ReportTemplate.DoesNotExist:
        raise Http404("Шаблон не найден")
    except Exception as e:
        return HttpResponse(f'Ошибка при скачивании файла: {str(e)}', status=500)
