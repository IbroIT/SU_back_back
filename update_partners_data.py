#!/usr/bin/env python
import os
import django
import sys

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from about_section.models import Partner

def update_partners():
    """Update partners with coordinates and additional data"""
    partners = Partner.objects.all()
    
    # Base coordinates for Bishkek, Kyrgyzstan
    base_lat = 42.8746
    base_lng = 74.5698
    
    for i, partner in enumerate(partners):
        # Add slight offset to each partner so they don't overlap on map
        partner.latitude = base_lat + (i * 0.01)
        partner.longitude = base_lng + (i * 0.01)
        
        # Set default location data
        partner.country = 'Кыргызстан'
        partner.country_en = 'Kyrgyzstan'
        partner.city = 'Бишкек'
        partner.city_en = 'Bishkek'
        
        # Set contact info
        partner.email = f'info@partner{partner.id}.kg'
        partner.phone = f'+996 312 {partner.id:03d}-000'
        
        # Set partner type based on name
        name_lower = partner.name.lower()
        if 'больница' in name_lower or 'клиника' in name_lower:
            partner.partner_type = 'clinical'
        elif 'университет' in name_lower or 'институт' in name_lower:
            partner.partner_type = 'university'
        elif 'организация' in name_lower or 'ассоциация' in name_lower:
            partner.partner_type = 'organization'
        else:
            partner.partner_type = 'academic'
        
        # Add partnership areas
        if partner.partner_type == 'clinical':
            partner.partnership_areas = 'Клиническая практика, Стажировки, Медицинские исследования'
        elif partner.partner_type == 'university':
            partner.partnership_areas = 'Обмен студентами, Совместные программы, Научное сотрудничество'
        else:
            partner.partnership_areas = 'Медицинское образование, Исследования, Развитие кадров'
        
        # Set establishment and cooperation years
        partner.established_year = 1990 + (i * 2)
        partner.cooperation_since = 2010 + i
        
        partner.save()
        print(f"Updated partner: {partner.name} ({partner.partner_type})")
    
    print(f"\nSuccessfully updated {partners.count()} partners")

if __name__ == '__main__':
    update_partners()
