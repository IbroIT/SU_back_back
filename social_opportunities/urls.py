from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, ClubViewSet, ProjectViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'clubs', ClubViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('api/social-opportunities/', include(router.urls)),
]