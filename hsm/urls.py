from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    HSMInfoViewSet, ProgramViewSet, FacultyViewSet, 
    AccreditationViewSet, LearningGoalViewSet
)

router = DefaultRouter()
router.register(r'info', HSMInfoViewSet, basename='hsm-info')
router.register(r'programs', ProgramViewSet, basename='hsm-programs')
router.register(r'faculty', FacultyViewSet, basename='hsm-faculty')
router.register(r'accreditations', AccreditationViewSet, basename='hsm-accreditations')
router.register(r'learning-goals', LearningGoalViewSet, basename='hsm-learning-goals')

urlpatterns = [
    path('api/hsm/', include(router.urls)),
]
