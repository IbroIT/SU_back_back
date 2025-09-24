#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append('/Users/adminbaike/medicine/SU_back_back')

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_su_m.settings')
django.setup()

from infrastructure.models import BuildingFacility

def update_facilities_capacity():
    facilities = BuildingFacility.objects.all()
    updated_count = 0
    
    for facility in facilities:
        if facility.capacity:
            facility.capacity_ru = facility.capacity
            
            if 'человек' in facility.capacity:
                facility.capacity_en = facility.capacity.replace('человек', 'people')
                facility.capacity_kg = facility.capacity.replace('человек', 'адам')
            else:
                facility.capacity_en = facility.capacity
                facility.capacity_kg = facility.capacity
            
            facility.save()
            print(f'Updated {facility.name_ru}: {facility.capacity_ru}')
            updated_count += 1
    
    print(f'Total facilities updated: {updated_count}')

if __name__ == '__main__':
    update_facilities_capacity()
