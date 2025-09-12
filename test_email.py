#!/usr/bin/env python3
"""
Тест отправки email с вложениями через Django admissions API
"""

import requests
import os
from pathlib import Path

# Настройки
API_URL = "http://localhost:8000/api/admissions/applications/submit-email/"
TEST_FILES_DIR = Path(__file__).parent / "test_files"

def create_test_files():
    """Создать тестовые файлы для отправки"""
    TEST_FILES_DIR.mkdir(exist_ok=True)
    
    # Создать тестовый PDF файл
    pdf_content = b"%PDF-1.4\n1 0 obj\n<<\n/Type /Catalog\n/Pages 2 0 R\n>>\nendobj\n2 0 obj\n<<\n/Type /Pages\n/Kids [3 0 R]\n/Count 1\n>>\nendobj\n3 0 obj\n<<\n/Type /Page\n/Parent 2 0 R\n/MediaBox [0 0 612 792]\n>>\nendobj\nxref\n0 4\n0000000000 65535 f \n0000000009 00000 n \n0000000074 00000 n \n0000000120 00000 n \ntrailer\n<<\n/Size 4\n/Root 1 0 R\n>>\nstartxref\n178\n%%EOF"
    pdf_file = TEST_FILES_DIR / "test_document.pdf"
    pdf_file.write_bytes(pdf_content)
    
    # Создать тестовый текстовый файл как JPG
    jpg_file = TEST_FILES_DIR / "test_photo.jpg"
    jpg_file.write_bytes(b"\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00\xff\xdb\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\t\t\x08\n\x0c\x14\r\x0c\x0b\x0b\x0c\x19\x12\x13\x0f\x14\x1d\x1a\x1f\x1e\x1d\x1a\x1c\x1c $.' \",#\x1c\x1c(7),01444\x1f'9=82<.342\xff\xc0\x00\x11\x08\x00\x01\x00\x01\x01\x01\x11\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x14\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xff\xc4\x00\x14\x10\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00\x3f\x00\xaa\xff\xd9")
    
    return pdf_file, jpg_file

def test_email_submission():
    """Тестировать отправку заявки с вложениями"""
    print("🚀 Запуск теста отправки email с вложениями...")
    
    # Создать тестовые файлы
    pdf_file, jpg_file = create_test_files()
    
    # Данные для отправки
    data = {
        'firstName': 'Тест',
        'lastName': 'Тестов',
        'middleName': 'Тестович',
        'birthDate': '1995-05-15',
        'gender': 'M',
        'phone': '+996555123456',
        'email': 'test@example.com',
        'program': 'Лечебное дело',
        'schoolName': 'Тестовая школа №1',
        'graduationYear': '2013',
        'ortScore': '180',
        'address': 'г. Бишкек, ул. Тестовая, 123',
        'agreeTerms': 'true',
        'agreePrivacy': 'true',
        'document_descriptions': '{"certificate": "Аттестат об окончании школы (High school diploma)", "passport": "Копия паспорта (Passport ID copies)", "medical": "Медицинское заключение (Medical certificate 086u)", "photos": "Фотографии 3x4 см (3x4 cm photos)", "ortCertificate": "ОРТ сертификат (ORT certificate)"}'
    }
    
    # Файлы для отправки
    files = []
    try:
        with open(pdf_file, 'rb') as f:
            files.append(('certificate', ('test_document.pdf', f.read(), 'application/pdf')))
        with open(jpg_file, 'rb') as f:
            files.append(('passport', ('test_photo.jpg', f.read(), 'image/jpeg')))
        
        print("📤 Отправка POST запроса на API...")
        print(f"URL: {API_URL}")
        print(f"Данные: {data}")
        print(f"Файлы: {[f[1][0] for f in files]}")
        
        # Отправить запрос
        response = requests.post(API_URL, data=data, files=files)
        
        print(f"\n📊 Результат запроса:")
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        print(f"Response Text: {response.text}")
        
        if response.status_code == 200:
            print("✅ УСПЕХ! Email отправлен успешно!")
            print("📧 Проверьте почту adilhansatymkulov40@gmail.com")
        else:
            print("❌ ОШИБКА при отправке!")
            
    except requests.exceptions.ConnectionError:
        print("❌ ОШИБКА: Не удается подключиться к Django серверу!")
        print("Убедитесь, что Django сервер запущен на http://localhost:8000")
    except Exception as e:
        print(f"❌ ОШИБКА: {e}")
    finally:
        # Очистить тестовые файлы
        if pdf_file.exists():
            pdf_file.unlink()
        if jpg_file.exists():
            jpg_file.unlink()
        if TEST_FILES_DIR.exists():
            TEST_FILES_DIR.rmdir()

if __name__ == "__main__":
    test_email_submission()
