from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, ManagementViewSet

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)
router.register(r'management', ManagementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
