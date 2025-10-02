from django.urls import path
from . import views

urlpatterns = [
    # Partner endpoints
    path('partners/', views.PartnerListView.as_view(), name='partner-list'),
    path('partners/<int:id>/', views.PartnerDetailView.as_view(), name='partner-detail'),
    path('partners/frontend/', views.partners_for_frontend, name='partners-frontend'),
    path('partners/stats/', views.partners_stats, name='partners-stats'),
    
    # About section endpoints
    path('about-sections/', views.AboutSectionListView.as_view(), name='about-section-list'),
    path('about-sections/<int:id>/', views.AboutSectionDetailView.as_view(), name='about-section-detail'),
    path('about-sections/<int:id>/with-partners/', views.AboutSectionWithPartnersView.as_view(), name='about-section-with-partners'),
    
    # Combined endpoint for frontend
    path('about-with-partners/', views.about_section_with_partners, name='about-with-partners'),
    
    # University Founders endpoints
    path('university-founders/', views.UniversityFounderListView.as_view(), name='university-founder-list'),
    path('university-founders/<int:id>/', views.UniversityFounderDetailView.as_view(), name='university-founder-detail'),
    
    # Organization structure endpoints
    path('structure/', views.OrganizationStructureListView.as_view(), name='structure-list'),
    path('structure/frontend/', views.structure_for_frontend, name='structure-frontend'),
    
    # Achievement endpoints
    path('achievements/', views.AchievementListView.as_view(), name='achievement-list'),
    path('achievements/frontend/', views.achievements_for_frontend, name='achievements-frontend'),
    
    # Statistics endpoints
    path('statistics/', views.UniversityStatisticListView.as_view(), name='statistics-list'),
    path('statistics/frontend/', views.statistics_for_frontend, name='statistics-frontend'),
]