from django.urls import path
from . import views

urlpatterns = [
    # Hospitals
    path('hospitals/', views.HospitalListCreateView.as_view(), name='hospital-list-create'),
    path('hospitals/<int:pk>/', views.HospitalDetailView.as_view(), name='hospital-detail'),
    
    # Laboratories
    path('laboratories/', views.LaboratoryListCreateView.as_view(), name='laboratory-list-create'),
    path('laboratories/<int:pk>/', views.LaboratoryDetailView.as_view(), name='laboratory-detail'),
    
    # Academic Buildings
    path('academic-buildings/', views.AcademicBuildingListCreateView.as_view(), name='academic-building-list-create'),
    path('academic-buildings/<int:pk>/', views.AcademicBuildingDetailView.as_view(), name='academic-building-detail'),
    
    # Dormitories
    path('dormitories/', views.DormitoryListCreateView.as_view(), name='dormitory-list-create'),
    path('dormitories/<int:pk>/', views.DormitoryDetailView.as_view(), name='dormitory-detail'),
    
    # Overview and Search
    path('overview/', views.infrastructure_overview, name='infrastructure-overview'),
    path('search/', views.search_infrastructure, name='infrastructure-search'),
]