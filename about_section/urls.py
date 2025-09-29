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
    
    # Founders endpoints
    path('founders/', views.FounderListView.as_view(), name='founder-list'),
    path('founders/<int:id>/', views.FounderDetailView.as_view(), name='founder-detail'),
    path('founders/frontend/', views.founders_for_frontend, name='founders-frontend'),
    
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
