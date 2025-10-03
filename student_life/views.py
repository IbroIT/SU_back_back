from rest_framework import viewsets, status, filters
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.http import HttpResponse, Http404, FileResponse
from django.utils.encoding import force_str
from django_filters.rest_framework import DjangoFilterBackend
import os
import mimetypes
from .models import (
    PartnerOrganization, StudentAppeal, PhotoAlbum, Photo, 
    VideoContent, StudentLifeStatistic, InternshipRequirement, ReportTemplate,
    StudentGuide, GuideRequirement, GuideStep, GuideStepDetail,
    EResourceCategory, EResource, EResourceFeature
)
from .serializers import (
    PartnerOrganizationSerializer, StudentAppealSerializer,
    PhotoAlbumSerializer, PhotoSerializer, VideoContentSerializer,
    StudentLifeStatisticSerializer, InternshipRequirementSerializer,
    ReportTemplateSerializer, StudentGuideSerializer,
    EResourceCategorySerializer, EResourceSerializer
)


class PartnerOrganizationViewSet(viewsets.ModelViewSet):
    queryset = PartnerOrganization.objects.filter(is_active=True)
    serializer_class = PartnerOrganizationSerializer
    permission_classes = [AllowAny]
    
    def get_serializer_context(self):
        return {'request': self.request}


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
        organizations_data = PartnerOrganizationSerializer(organizations, many=True, context={'request': request}).data
        
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
            ]
        }
        
        return Response(response_data)
        
    except Exception as e:
        return Response(
            {'error': f'Ошибка загрузки данных: {str(e)}'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def instructions_data(request):
    """API endpoint для инструкций студенческой жизни"""
    try:
        # Получаем все активные инструкции
        guides = StudentGuide.objects.filter(is_active=True).order_by('order')
        serializer = StudentGuideSerializer(guides, many=True, context={'request': request})
        
        return Response({
            'student_guides': serializer.data,
            'success': True,
            'message': 'Инструкции успешно загружены'
        })
        
    except Exception as e:
        # В случае ошибки возвращаем дефолтные данные
        return Response({
            'student_guides': [],
            'error': str(e),
            'success': False,
            'message': 'Ошибка загрузки инструкций'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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


# =============================================================================
# VIEWSETS ДЛЯ ЭЛЕКТРОННЫХ РЕСУРСОВ
# =============================================================================

class EResourceCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для категорий электронных ресурсов"""
    queryset = EResourceCategory.objects.filter(is_active=True).order_by('order', 'name_ru')
    serializer_class = EResourceCategorySerializer
    permission_classes = [AllowAny]
    
    @action(detail=True, methods=['get'])
    def resources(self, request, pk=None):
        """Получить все ресурсы категории"""
        category = self.get_object()
        resources = category.eresources.filter(is_active=True).order_by('order', 'title_ru')
        serializer = EResourceSerializer(resources, many=True, context={'request': request})
        return Response(serializer.data)


class EResourceViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для электронных ресурсов"""
    queryset = EResource.objects.filter(is_active=True).order_by('order', 'title_ru')
    serializer_class = EResourceSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'status', 'is_popular']
    search_fields = ['title_ru', 'title_kg', 'title_en', 'description_ru', 'description_kg', 'description_en']
    ordering_fields = ['order', 'title_ru', 'users_count', 'created_at']
    
    @action(detail=False, methods=['get'])
    def popular(self, request):
        """Получить популярные ресурсы"""
        popular_resources = self.queryset.filter(is_popular=True)
        serializer = self.get_serializer(popular_resources, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """Получить ресурсы сгруппированные по категориям"""
        categories = EResourceCategory.objects.filter(is_active=True).order_by('order', 'name_ru')
        result = []
        
        for category in categories:
            resources = self.queryset.filter(category=category)
            if resources.exists():
                category_data = EResourceCategorySerializer(category).data
                category_data['resources'] = EResourceSerializer(
                    resources, many=True, context={'request': request}
                ).data
                result.append(category_data)
        
        return Response(result)
    
    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """Получить статистику по ресурсам"""
        total = self.queryset.count()
        online = self.queryset.filter(status='online').count()
        popular = self.queryset.filter(is_popular=True).count()
        total_users = sum(resource.users_count for resource in self.queryset.all())
        
        stats = {
            'total': total,
            'online': online,
            'popular': popular,
            'total_users': total_users
        }
        
        return Response(stats)
