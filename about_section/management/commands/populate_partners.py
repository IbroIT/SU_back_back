from django.core.management.base import BaseCommand
from about_section.models import Partner, AboutSection


class Command(BaseCommand):
    help = 'Create initial partners and about section data based on frontend component'
    
    def handle(self, *args, **options):
        # Create partners based on the frontend data
        partners_data = [
            {
                'name': 'Национальная больница',
                'name_en': 'National Hospital',
                'name_ky': 'Улуттук оорукана',
                'icon': '🏥',
                'color_theme': 'from-blue-500 to-indigo-600',
                'glow_effect': 'hover:shadow-blue-500/50',
                'order': 1,
                'description': 'Ведущая медицинская организация страны',
                'description_en': 'Leading medical organization of the country',
                'description_ky': 'Өлкөнүн алдыңкы медициналык уюму'
            },
            {
                'name': 'Городская больница',
                'name_en': 'City Hospital',
                'name_ky': 'Шаар оорукана',
                'icon': '🏨',
                'color_theme': 'from-purple-500 to-pink-600',
                'glow_effect': 'hover:shadow-purple-500/50',
                'order': 2,
                'description': 'Основная городская медицинская больница',
                'description_en': 'Main city medical hospital',
                'description_ky': 'Негизги шаар медициналык ооруканасы'
            },
            {
                'name': 'Медицинские центры',
                'name_en': 'Medical Centers',
                'name_ky': 'Медициналык борборлор',
                'icon': '⛑️',
                'color_theme': 'from-green-500 to-teal-600',
                'glow_effect': 'hover:shadow-green-500/50',
                'order': 3,
                'description': 'Сеть специализированных медицинских центров',
                'description_en': 'Network of specialized medical centers',
                'description_ky': 'Атайын медициналык борборлордун тармагы'
            },
            {
                'name': 'Всемирная организация здравоохранения',
                'name_en': 'World Health Organization (WHO)',
                'name_ky': 'Дүйнөлүк саламаттыкты сактоо уюму',
                'icon': '🌐',
                'color_theme': 'from-amber-500 to-orange-600',
                'glow_effect': 'hover:shadow-amber-500/50',
                'order': 4,
                'description': 'Международная организация здравоохранения',
                'description_en': 'International health organization',
                'description_ky': 'Эл аралык саламаттыкты сактоо уюму'
            },
            {
                'name': 'Красный Крест',
                'name_en': 'Red Cross',
                'name_ky': 'Кызыл Крест',
                'icon': '➕',
                'color_theme': 'from-red-500 to-rose-600',
                'glow_effect': 'hover:shadow-red-500/50',
                'order': 5,
                'description': 'Международная гуманитарная организация',
                'description_en': 'International humanitarian organization',
                'description_ky': 'Эл аралык гуманитардык уюм'
            },
            {
                'name': 'Медицинская ассоциация',
                'name_en': 'Medical Association',
                'name_ky': 'Медициналык ассоциация',
                'icon': '⚕️',
                'color_theme': 'from-indigo-500 to-blue-600',
                'glow_effect': 'hover:shadow-indigo-500/50',
                'order': 6,
                'description': 'Профессиональная медицинская ассоциация',
                'description_en': 'Professional medical association',
                'description_ky': 'Кесиптик медициналык ассоциация'
            },
            {
                'name': 'Институт здоровья',
                'name_en': 'Health Institute',
                'name_ky': 'Саламаттык институту',
                'icon': '🔬',
                'color_theme': 'from-pink-500 to-rose-600',
                'glow_effect': 'hover:shadow-pink-500/50',
                'order': 7,
                'description': 'Исследовательский институт здравоохранения',
                'description_en': 'Health research institute',
                'description_ky': 'Саламаттыкты изилдөө институту'
            },
            {
                'name': 'Исследовательский фонд',
                'name_en': 'Research Foundation',
                'name_ky': 'Изилдөө фонду',
                'icon': '💉',
                'color_theme': 'from-teal-500 to-emerald-600',
                'glow_effect': 'hover:shadow-teal-500/50',
                'order': 8,
                'description': 'Фонд медицинских исследований',
                'description_en': 'Medical research foundation',
                'description_ky': 'Медициналык изилдөөлөрдүн фонду'
            }
        ]
        
        self.stdout.write('Creating partners...')
        
        created_count = 0
        for partner_data in partners_data:
            partner, created = Partner.objects.get_or_create(
                name=partner_data['name'],
                defaults=partner_data
            )
            if created:
                created_count += 1
                self.stdout.write(f'  Created partner: {partner.name}')
            else:
                self.stdout.write(f'  Partner already exists: {partner.name}')
        
        # Create default about section
        about_data = {
            'title': 'Наши партнеры',
            'title_en': 'Our Partners',
            'title_ky': 'Биздин өнөктөштөр',
            'subtitle': 'Мы сотрудничаем с ведущими медицинскими организациями',
            'subtitle_en': 'We collaborate with leading medical organizations',
            'subtitle_ky': 'Биз алдыңкы медициналык уюмдар менен кызматташабыз',
            'content': 'СалымБеков Университет активно сотрудничает с международными и национальными медицинскими организациями для обеспечения качественного образования и практической подготовки студентов.',
            'content_en': 'Salymbekov University actively collaborates with international and national medical organizations to ensure quality education and practical training for students.',
            'content_ky': 'СалымБеков университети студенттердин сапаттуу билим алуусун жана практикалык даярдыгын камсыз кылуу үчүн эл аралык жана улуттук медициналык уюмдар менен активдүү кызматташат.',
            'is_active': True,
            'show_partners': True,
            'partners_animation_speed': 0.5
        }
        
        about_section, created = AboutSection.objects.get_or_create(
            title=about_data['title'],
            defaults=about_data
        )
        
        if created:
            self.stdout.write('Created default about section')
        else:
            self.stdout.write('About section already exists')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {created_count} new partners and initialized about section'
            )
        )
