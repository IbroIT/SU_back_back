#!/usr/bin/env python
import os
import django
import sys

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from about_section.models import Partner

def add_english_translations():
    """Add English translations for partners"""
    
    partners_data = [
        {
            'id': 1,
            'name_en': 'National Hospital',
            'description_en': 'Leading medical organization of the country',
        },
        {
            'id': 2,
            'name_en': 'City Hospital',
            'description_en': 'Main city medical hospital',
        },
        {
            'id': 3,
            'name_en': 'Medical Centers',
            'description_en': 'Network of specialized medical centers',
        },
        {
            'id': 4,
            'name_en': 'World Health Organization',
            'description_en': 'International health organization',
        },
        {
            'id': 5,
            'name_en': 'Red Cross',
            'description_en': 'International humanitarian organization',
        },
        {
            'id': 6,
            'name_en': 'Medical Association',
            'description_en': 'Professional medical association',
        },
        {
            'id': 7,
            'name_en': 'Health Institute',
            'description_en': 'Health research institute',
        },
        {
            'id': 8,
            'name_en': 'Research Foundation',
            'description_en': 'Medical research foundation',
        }
    ]
    
    for partner_data in partners_data:
        try:
            partner = Partner.objects.get(id=partner_data['id'])
            partner.name_en = partner_data['name_en']
            partner.description_en = partner_data['description_en']
            
            # Add English partnership areas
            if partner.partnership_areas:
                if 'клинич' in partner.partnership_areas.lower():
                    partner.partnership_areas = 'Clinical Practice, Internships, Medical Research'
                elif 'универ' in partner.partnership_areas.lower() or 'обмен' in partner.partnership_areas.lower():
                    partner.partnership_areas = 'Student Exchange, Joint Programs, Scientific Collaboration'
                else:
                    partner.partnership_areas = 'Medical Education, Research, Staff Development'
            
            partner.save()
            print(f"Updated translations for: {partner.name} -> {partner.name_en}")
            
        except Partner.DoesNotExist:
            print(f"Partner with ID {partner_data['id']} not found")
    
    print(f"\nSuccessfully updated English translations")

if __name__ == '__main__':
    add_english_translations()
