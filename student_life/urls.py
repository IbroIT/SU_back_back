from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PartnerOrganizationViewSet, StudentAppealViewSet,
    internships_data, academic_mobility_data, regulations_data, instructions_data
)

router = DefaultRouter()
router.register(r'partner-organizations', PartnerOrganizationViewSet)
router.register(r'student-appeals', StudentAppealViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # Комбинированные endpoints для фронтенда
    path('api/data/internships_data/', internships_data, name='internships_data'),
    path('api/data/academic_mobility_data/', academic_mobility_data, name='academic_mobility_data'),
    path('api/data/regulations_data/', regulations_data, name='regulations_data'),
    path('api/data/instructions_data/', instructions_data, name='instructions_data'),
]
