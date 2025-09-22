# back_su_m/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('news.urls')),  # News API endpoints
    path('research/', include('research.urls')),  # Research API endpoints
    path('api/careers/', include('careers.urls')),  # Careers API endpoints
    path('api/banners/', include('banner.urls')),  # Banner API endpoints
    path('api/', include('teachers.urls')), # Teachers API endpoints
    path('api/admissions/', include('admissions.urls')),  # Admissions API endpoint for email with attachments
    path('api/infrastructure/', include('infrastructure.urls')),  # Infrastructure API endpoints
    path('api/documents/', include('documents.urls')),  # Documents API endpoints
    path('api/student-life/', include('student_life.urls')),  # Student Life API endpoints
    path('api/media-coverage/', include('media_coverage.urls')),  # Media Coverage API endpoints
    path('api/', include('hsm.urls')),  # HSM API endpoints
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)