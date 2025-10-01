#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Скрипт для заполнения реалистичными данными приложения mission_section
Создает данные для медицинского университета
Запуск: python populate_mission_data.py
"""

import os
import sys
import django

# Настройка Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from mission_section.models import MissionSection, HistoryMilestone, Value, Priority, Achievement


def clear_existing_data():
    """Очистка существующих данных"""
    print("Очистка существующих данных...")
    MissionSection.objects.all().delete()
    HistoryMilestone.objects.all().delete()
    Value.objects.all().delete()
    Priority.objects.all().delete()
    Achievement.objects.all().delete()
    print("Данные очищены.")


def create_mission_section():
    """Создание основной секции миссии"""
    print("Создание основной секции миссии...")
    
    mission = MissionSection.objects.create(
        # Русский язык
        title="Наша миссия - формирование будущего медицины",
        subtitle="Мы стремимся подготовить высококвалифицированных медицинских специалистов, способных отвечать на вызовы современного здравоохранения",
        mission_text="""Миссия Медицинского Университета заключается в подготовке компетентных, 
        сострадательных и инновационных медицинских специалистов, которые будут обслуживать разнообразные 
        потребности нашего общества в области здравоохранения. Мы стремимся к совершенству в образовании, 
        исследованиях и клинической практике, обеспечивая при этом, что наши выпускники обладают 
        критическим мышлением, этическими принципами и приверженностью непрерывному обучению.""",
        
        vision_title="Наше видение",
        vision_text="""Стать ведущим медицинским университетом региона, признанным за инновации в 
        медицинском образовании, прорывные исследования и выдающиеся клинические результаты. 
        Мы видим будущее, где наши выпускники являются лидерами в трансформации здравоохранения 
        и улучшении качества жизни пациентов по всему миру.""",
        
        approach_title="Наш подход",
        approach_text="""Мы применяем интегрированный подход к медицинскому образованию, сочетающий 
        теоретические знания с практическим опытом. Наша педагогика основана на доказательной медицине, 
        междисциплинарном сотрудничестве и использовании передовых технологий. Мы создаем среду обучения, 
        которая поощряет критическое мышление, эмпатию и профессиональное развитие.""",
        
        achievements_subtitle="""За годы своего существования наш университет достиг значительных 
        результатов в подготовке медицинских кадров и развитии медицинской науки""",
        
        impact_title="Наш вклад в медицину",
        impact_text="""Мы гордимся тем, что наши выпускники работают в ведущих медицинских учреждениях 
        по всему миру. Наши исследования способствуют развитию новых методов лечения и диагностики. 
        Мы активно участвуем в программах общественного здравоохранения и медицинской помощи 
        малообеспеченным слоям населения.""",
        
        future_title="Перспективы развития",
        future_text="""В ближайшие годы мы планируем расширить наши исследовательские программы, 
        внедрить новые технологии в образовательный процесс, включая виртуальную и дополненную реальность, 
        искусственный интеллект в диагностике. Мы также развиваем международные партнерства для 
        обмена опытом и лучшими практиками в медицинском образовании.""",
        
        # Английский язык
        title_en="Our Mission - Shaping the Future of Medicine",
        subtitle_en="We strive to prepare highly qualified medical professionals capable of meeting the challenges of modern healthcare",
        mission_text_en="""The mission of the Medical University is to prepare competent, compassionate and innovative 
        medical specialists who will serve the diverse healthcare needs of our society. We strive for excellence in education, 
        research and clinical practice, ensuring that our graduates possess critical thinking, ethical principles and 
        commitment to lifelong learning.""",
        
        vision_title_en="Our Vision",
        vision_text_en="""To become the leading medical university in the region, recognized for innovations in medical 
        education, breakthrough research and outstanding clinical outcomes. We envision a future where our graduates 
        are leaders in transforming healthcare and improving patients' quality of life worldwide.""",
        
        approach_title_en="Our Approach",
        approach_text_en="""We apply an integrated approach to medical education that combines theoretical knowledge 
        with practical experience. Our pedagogy is based on evidence-based medicine, interdisciplinary collaboration 
        and the use of advanced technologies. We create a learning environment that encourages critical thinking, 
        empathy and professional development.""",
        
        achievements_subtitle_en="""Over the years of its existence, our university has achieved significant results 
        in training medical personnel and developing medical science""",
        
        impact_title_en="Our Contribution to Medicine",
        impact_text_en="""We are proud that our graduates work in leading medical institutions around the world. 
        Our research contributes to the development of new methods of treatment and diagnosis. We actively participate 
        in public health programs and medical care for the underprivileged.""",
        
        future_title_en="Development Prospects",
        future_text_en="""In the coming years, we plan to expand our research programs, introduce new technologies 
        into the educational process, including virtual and augmented reality, artificial intelligence in diagnostics. 
        We are also developing international partnerships to exchange experience and best practices in medical education.""",
        
        # Кыргызский язык
        title_ky="Биздин миссиябыз - медицинанын келечегин калыптандыруу",
        subtitle_ky="Биз заманбап саламаттыкты сактоонун чакырыктарына жооп бере алган жогорку квалификациялуу медициналык адистерди даярдоого умтулабыз",
        mission_text_ky="""Медициналык университеттин миссиясы биздин коомдун ар түрдүү саламаттыкты сактоо керектөөлөрүн 
        канааттандыра турган компетенттүү, боорукер жана инновациялык медициналык адистерди даярдоо. Биз билим берүү, 
        изилдөө жана клиникалык практикада мыктылыкка умтулабыз, биздин бүтүрүүчүлөр сынчыл ой жүгүртүү, этикалык принциптер 
        жана өмүр бою үйрөнүүгө берилгендикке ээ болушун камсыз кылабыз.""",
        
        vision_title_ky="Биздин көрүү",
        vision_text_ky="""Медициналык билим берүүдөгү инновациялар, мыкты изилдөөлөр жана эң сонун клиникалык натыйжалар 
        үчүн таанылган аймактын жетекчи медициналык университети болуу. Биз биздин бүтүрүүчүлөр саламаттыкты сактоону 
        өзгөртүүдө жана дүйнө жүзүндөгү бейтаптардын жашоо сапатын жакшыртууда лидер болгон келечекти көрөбүз.""",
        
        approach_title_ky="Биздин мамиле",
        approach_text_ky="""Биз теориялык билимди практикалык тажрыйба менен айкалыштырган медициналык билим берүүгө 
        интеграцияланган мамилени колдонобуз. Биздин педагогика далилге негизделген медицинага, дисциплиналар аралык 
        кызматташууга жана алдыңкы технологияларды колдонууга негизделген. Биз сынчыл ой жүгүртүүнү, эмпатияны жана 
        кесиптик өнүгүүнү шыктандырган окуу чөйрөсүн түзөбүз.""",
        
        achievements_subtitle_ky="""Жылдар бою биздин университет медициналык кадрларды даярдоо жана медициналык илимди 
        өнүктүрүү тармагында олуттуу жетишкендиктерге жетти""",
        
        impact_title_ky="Медицинага биздин салымыбыз",
        impact_text_ky="""Биз биздин бүтүрүүчүлөр дүйнө жүзүндөгү жетекчи медициналык мекемелерде иштеши менен 
        сыймыктанабыз. Биздин изилдөөлөр дарылоонун жана диагностиканын жаңы методдорун өнүктүрүүгө салым кошот. 
        Биз коомдук саламаттыкты сактоо программаларына жана жакыр калктарга медициналык жардам көрсөтүүгө активдүү катышабыз.""",
        
        future_title_ky="Өнүгүү келечектери",
        future_text_ky="""Келерки жылдары биз изилдөө программаларыбызды кеңейтүүнү, билим берүү процессине жаңы 
        технологияларды, анын ичинде виртуалдык жана кошумча реалдуулукту, диагностикада жасалма интеллектти киргизүүнү 
        пландап жатабыз. Биз ошондой эле медициналык билим берүүдө тажрыйба жана эң мыкты практикалар алмашуу үчүн 
        эл аралык өнөктөштүктөрдү өнүктүрүп жатабыз.""",
        
        is_active=True
    )
    
    print(f"Создана основная секция миссии: {mission.title}")
    return mission


def create_history_milestones():
    """Создание исторических вех"""
    print("Создание исторических вех...")
    
    milestones_data = [
        {
            'year': '1995',
            'title': 'Основание университета',
            'description': 'Основан как первый частный медицинский университет в регионе с целью подготовки высококвалифицированных медицинских кадров.',
            'title_en': 'University Foundation',
            'description_en': 'Founded as the first private medical university in the region with the goal of training highly qualified medical personnel.',
            'title_ky': 'Университеттин негизделиши',
            'description_ky': 'Жогорку квалификациялуу медициналык кадрларды даярдоо максатында аймактагы биринчи жеке медициналык университет катары негизделди.',
            'icon_class': 'AcademicCapIcon',
            'order': 1
        },
        {
            'year': '2000',
            'title': 'Аккредитация программ',
            'description': 'Получена полная аккредитация всех медицинских программ и признание со стороны международных медицинских организаций.',
            'title_en': 'Program Accreditation',
            'description_en': 'Received full accreditation of all medical programs and recognition from international medical organizations.',
            'title_ky': 'Программалардын аккредитациясы',
            'description_ky': 'Бардык медициналык программалардын толук аккредитациясын жана эл аралык медициналык уюмдардын таануусун алды.',
            'icon_class': 'CertificateIcon', 
            'order': 2
        },
        {
            'year': '2005',
            'title': 'Открытие клиники',
            'description': 'Открыта собственная учебная клиника, обеспечивающая студентам практический опыт работы с реальными пациентами.',
            'title_en': 'Clinic Opening',
            'description_en': 'Opened its own training clinic, providing students with practical experience working with real patients.',
            'title_ky': 'Клиниканын ачылышы',
            'description_ky': 'Студенттерге чыныгы бейтаптар менен иштөөдө практикалык тажрыйба берген өз окуу клиникасы ачылды.',
            'icon_class': 'HeartIcon',
            'order': 3
        },
        {
            'year': '2010',
            'title': 'Исследовательский центр',
            'description': 'Создан современный исследовательский центр для проведения фундаментальных и прикладных медицинских исследований.',
            'title_en': 'Research Center',
            'description_en': 'Established a modern research center for conducting fundamental and applied medical research.',
            'title_ky': 'Изилдөө борбору',
            'description_ky': 'Фундаменталдык жана колдонмо медициналык изилдөөлөрдү жүргүзүү үчүн заманбап изилдөө борбору түзүлдү.',
            'icon_class': 'BeakerIcon',
            'order': 4
        },
        {
            'year': '2015',
            'title': 'Международное признание',
            'description': 'Университет получил международное признание и вошел в топ-100 медицинских университетов мира по версии QS World University Rankings.',
            'title_en': 'International Recognition',
            'description_en': 'The university received international recognition and entered the top 100 medical universities in the world according to QS World University Rankings.',
            'title_ky': 'Эл аралык таануу',
            'description_ky': 'Университет эл аралык таануу алып, QS World University Rankings боюнча дүйнөдөгү эң мыкты 100 медициналык университеттин катарына кирди.',
            'icon_class': 'GlobeIcon',
            'order': 5
        },
        {
            'year': '2020',
            'title': 'Цифровая трансформация',
            'description': 'Внедрены современные цифровые технологии в образовательный процесс, включая симуляционные центры и телемедицину.',
            'title_en': 'Digital Transformation',
            'description_en': 'Implemented modern digital technologies in the educational process, including simulation centers and telemedicine.',
            'title_ky': 'Санариптик трансформация',
            'description_ky': 'Билим берүү процессине симуляциялык борборлор жана телемедицинаны камтыган заманбап санариптик технологиялар киргизилди.',
            'icon_class': 'ComputerDesktopIcon',
            'order': 6
        },
        {
            'year': '2024',
            'title': 'Центр превосходства',
            'description': 'Открыт Центр превосходства в области персонализированной медицины и геномных исследований.',
            'title_en': 'Center of Excellence',
            'description_en': 'Opened the Center of Excellence in personalized medicine and genomic research.',
            'title_ky': 'Мыктылык борбору',
            'description_ky': 'Жекелештирилген медицина жана геном изилдөөлөрү тармагындагы Мыктылык борбору ачылды.',
            'icon_class': 'StarIcon',
            'order': 7
        }
    ]
    
    for milestone_data in milestones_data:
        milestone = HistoryMilestone.objects.create(**milestone_data)
        print(f"Создана веха: {milestone.year} - {milestone.title}")


def create_values():
    """Создание ценностей университета"""
    print("Создание ценностей университета...")
    
    values_data = [
        {
            'type': 'education',
            'title': 'Превосходство в образовании',
            'description': '''Мы стремимся к наивысшим стандартам медицинского образования, 
            используя инновационные методы обучения и современные технологии. Наша цель - 
            подготовить компетентных специалистов, способных решать сложные медицинские задачи.''',
            'title_en': 'Excellence in Education',
            'description_en': '''We strive for the highest standards of medical education, 
            using innovative teaching methods and modern technologies. Our goal is to prepare 
            competent specialists capable of solving complex medical problems.''',
            'title_ky': 'Билим берүүдөгү мыктылык',
            'description_ky': '''Биз инновациялык окутуу методдорун жана заманбап технологияларды 
            колдонуу менен медициналык билим берүүнүн эң жогорку стандарттарына умтулабыз. Биздин максат - 
            татаал медициналык маселелерди чече алган компетенттүү адистерди даярдоо.''',
            'order': 1
        },
        {
            'type': 'science',
            'title': 'Научные исследования',
            'description': '''Мы поддерживаем культуру научного исследования и инноваций, 
            поощряя студентов и преподавателей к участию в передовых исследованиях, 
            которые способствуют развитию медицинской науки и улучшению здравоохранения.''',
            'title_en': 'Scientific Research',
            'description_en': '''We support a culture of scientific research and innovation, 
            encouraging students and faculty to participate in cutting-edge research that 
            contributes to the advancement of medical science and healthcare improvement.''',
            'title_ky': 'Илимий изилдөөлөр',
            'description_ky': '''Биз илимий изилдөө жана инновациялар маданиятын колдойбуз, 
            студенттерди жана окутуучуларды медициналык илимдин өнүгүүсүнө жана саламаттыкты 
            сактоону жакшыртууга салым кошкон алдыңкы изилдөөлөргө катышууга шыктандырабыз.''',
            'order': 2
        },
        {
            'type': 'medicine',
            'title': 'Этика и сострадание',
            'description': '''В основе нашей деятельности лежат высокие этические стандарты 
            и глубокое сострадание к пациентам. Мы воспитываем в наших студентах понимание 
            важности человеческого достоинства и ответственности врача.''',
            'title_en': 'Ethics and Compassion',
            'description_en': '''Our work is based on high ethical standards and deep compassion 
            for patients. We instill in our students an understanding of the importance of human 
            dignity and physician responsibility.''',
            'title_ky': 'Этика жана боорукердик',
            'description_ky': '''Биздин ишибиздин негизинде бейтаптарга карата жогорку этикалык 
            стандарттар жана терең боорукердик жатат. Биз студенттерибизде адамдын кадыр-баркы 
            жана дарыгердин жоопкерчилигинин маанилүүлүгүн түшүнүүнү тарбиялайбыз.''',
            'order': 3
        },
        {
            'type': 'studentCare',
            'title': 'Забота о студентах',
            'description': '''Мы создаем поддерживающую среду для развития каждого студента, 
            предоставляя не только качественное образование, но и всестороннюю поддержку 
            их личностного и профессионального роста.''',
            'title_en': 'Student Care',
            'description_en': '''We create a supportive environment for the development of each 
            student, providing not only quality education but also comprehensive support for 
            their personal and professional growth.''',
            'title_ky': 'Студенттер жөнүндө кам көрүү',
            'description_ky': '''Биз ар бир студенттин өнүгүүсү үчүн колдоочу чөйрө түзөбүз, 
            сапаттуу билим берүүнүн эле эмес, алардын жеке жана кесиптик өсүшүнө жан-жактуу 
            колдоо көрсөтөбүз.''',
            'order': 4
        }
    ]
    
    for value_data in values_data:
        value = Value.objects.create(**value_data)
        print(f"Создана ценность: {value.title}")


def create_priorities():
    """Создание приоритетов университета"""
    print("Создание приоритетов университета...")
    
    priorities_data = [
        {
            'text': 'Развитие инновационных методов медицинского образования с использованием симуляционных технологий и виртуальной реальности',
            'text_en': 'Development of innovative medical education methods using simulation technologies and virtual reality',
            'text_ky': 'Симуляциялык технологиялар жана виртуалдык реалдуулукту колдонуу менен медициналык билим берүүнүн инновациялык методдорун өнүктүрүү',
            'icon_class': 'LightBulbIcon',
            'order': 1
        },
        {
            'text': 'Укрепление исследовательского потенциала через создание междисциплинарных научных центров и лабораторий',
            'text_en': 'Strengthening research capacity through the creation of interdisciplinary scientific centers and laboratories',
            'text_ky': 'Дисциплиналар аралык илимий борборлор жана лабораториялар түзүү аркылуу изилдөө потенциалын бекемдөө',
            'icon_class': 'BeakerIcon',
            'order': 2
        },
        {
            'text': 'Расширение международного сотрудничества и обмена студентами с ведущими медицинскими университетами мира',
            'text_en': 'Expanding international cooperation and student exchange with leading medical universities worldwide',
            'text_ky': 'Дүйнөнүн жетекчи медициналык университеттери менен эл аралык кызматташууну жана студенттер алмашууну кеңейтүү',
            'icon_class': 'GlobeIcon',
            'order': 3
        },
        {
            'text': 'Внедрение современных информационных технологий в клиническую практику и образовательный процесс',
            'text_en': 'Implementation of modern information technologies in clinical practice and educational process',
            'text_ky': 'Клиникалык практикага жана билим берүү процессине заманбап маалыматтык технологияларды киргизүү',
            'icon_class': 'ComputerDesktopIcon',
            'order': 4
        },
        {
            'text': 'Развитие программ непрерывного профессионального развития для практикующих врачей',
            'text_en': 'Development of continuing professional development programs for practicing physicians',
            'text_ky': 'Практикалык дарыгерлер үчүн үзгүлтүксүз кесиптик өнүктүрүү программаларын иштеп чыгуу',
            'icon_class': 'AcademicCapIcon',
            'order': 5
        },
        {
            'text': 'Создание центров превосходства в области персонализированной медицины и телемедицины',
            'text_en': 'Creating centers of excellence in personalized medicine and telemedicine',
            'text_ky': 'Жекелештирилген медицина жана телемедицина тармагында мыктылык борборлорун түзүү',
            'icon_class': 'HeartIcon',
            'order': 6
        }
    ]
    
    for priority_data in priorities_data:
        priority = Priority.objects.create(**priority_data)
        print(f"Создан приоритет: {priority.text[:50]}...")


def create_achievements():
    """Создание достижений (статистика)"""
    print("Создание достижений...")
    
    achievements_data = [
        {
            'number': '5000+',
            'label': 'Выпускников-врачей',
            'label_en': 'Medical Graduates',
            'label_ky': 'Дарыгер бүтүрүүчүлөр',
            'order': 1
        },
        {
            'number': '95%',
            'label': 'Трудоустройство выпускников',
            'label_en': 'Graduate Employment Rate',
            'label_ky': 'Бүтүрүүчүлөрдүн жумушка орношуусу',
            'order': 2
        },
        {
            'number': '150+',
            'label': 'Научных публикаций в год',
            'label_en': 'Scientific Publications per Year',
            'label_ky': 'Жылына илимий басылмалар',
            'order': 3
        },
        {
            'number': '25+',
            'label': 'Стран, где работают наши выпускники',
            'label_en': 'Countries where our graduates work',
            'label_ky': 'Биздин бүтүрүүчүлөр иштеген өлкөлөр',
            'order': 4
        },
        {
            'number': '50+',
            'label': 'Международных партнерств',
            'label_en': 'International Partnerships',
            'label_ky': 'Эл аралык өнөктөштүктөр',
            'order': 5
        },
        {
            'number': '15',
            'label': 'Исследовательских лабораторий',
            'label_en': 'Research Laboratories',
            'label_ky': 'Изилдөө лабораториялары',
            'order': 6
        }
    ]
    
    for achievement_data in achievements_data:
        achievement = Achievement.objects.create(**achievement_data)
        print(f"Создано достижение: {achievement.number} - {achievement.label}")


def main():
    """Основная функция"""
    print("=" * 60)
    print("СОЗДАНИЕ ДАННЫХ ДЛЯ MISSION_SECTION")
    print("=" * 60)
    
    try:
        # Очистка существующих данных
        clear_existing_data()
        
        # Создание новых данных
        create_mission_section()
        create_history_milestones()
        create_values()
        create_priorities()
        create_achievements()
        
        print("\n" + "=" * 60)
        print("УСПЕШНО СОЗДАНЫ ВСЕ ДАННЫЕ!")
        print("=" * 60)
        
        # Статистика
        print(f"\nСоздано объектов:")
        print(f"- MissionSection: {MissionSection.objects.count()}")
        print(f"- HistoryMilestone: {HistoryMilestone.objects.count()}")
        print(f"- Value: {Value.objects.count()}")
        print(f"- Priority: {Priority.objects.count()}")
        print(f"- Achievement: {Achievement.objects.count()}")
        
    except Exception as e:
        print(f"ОШИБКА: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()