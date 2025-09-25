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
    
    # Accreditation endpoints
    path('accreditations/', views.AccreditationListView.as_view(), name='accreditation-list'),
    path('accreditations/<int:id>/', views.AccreditationDetailView.as_view(), name='accreditation-detail'),
    path('accreditations/frontend/', views.accreditations_for_frontend, name='accreditations-frontend'),
    
    # Council endpoints
    path('councils/', views.CouncilTypeListView.as_view(), name='council-list'),
    path('councils/frontend/', views.councils_for_frontend, name='councils-frontend'),
    path('councils/frontend/<slug:slug>/', views.council_detail_for_frontend, name='council-detail-frontend'),
    path('councils/<slug:slug>/', views.CouncilTypeDetailView.as_view(), name='council-detail'),
    
    # Combined endpoint for frontend
    path('about-with-partners/', views.about_section_with_partners, name='about-with-partners'),
]
