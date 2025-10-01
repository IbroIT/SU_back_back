#!/usr/bin/env python3
"""
Скрипт для удаления старых моделей Founder и FounderAchievement из models.py
"""

def remove_old_models():
    models_file = '/home/adilhan/medicine/SU_back/about_section/models.py'
    
    with open(models_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Найдем начало и конец старых моделей
    start_founder = None
    end_founder = None
    
    for i, line in enumerate(lines):
        if 'class Founder(models.Model):' in line and start_founder is None:
            start_founder = i
        elif start_founder is not None and 'class OrganizationStructure(models.Model):' in line:
            end_founder = i
            break
    
    if start_founder is not None and end_founder is not None:
        print(f"Удаляю строки {start_founder + 1} - {end_founder}")
        
        # Удаляем строки от start_founder до end_founder (не включая end_founder)
        new_lines = lines[:start_founder] + lines[end_founder:]
        
        # Записываем обновленный файл
        with open(models_file, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        
        print("✅ Старые модели успешно удалены!")
        print(f"Удалено {end_founder - start_founder} строк")
    else:
        print("❌ Не удалось найти границы для удаления")

if __name__ == "__main__":
    remove_old_models()