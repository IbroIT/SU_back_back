from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    FacultyViewSet, 
    AccreditationViewSet,
    LeadershipViewSet
)

router = DefaultRouter()
router.register(r'faculty', FacultyViewSet, basename='hsm-faculty')
router.register(r'accreditations', AccreditationViewSet, basename='hsm-accreditations')
router.register(r'leadership', LeadershipViewSet, basename='hsm-leadership')

urlpatterns = [
    path('hsm/', include(router.urls)),
]
