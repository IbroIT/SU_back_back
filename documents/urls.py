from django.urls import path
from . import views

app_name = 'documents'

urlpatterns = [
    # Публичные API
    path('categories/', views.DocumentCategoryListView.as_view(), name='category-list'),
    path('', views.DocumentListView.as_view(), name='document-list'),
    path('<int:pk>/', views.DocumentDetailView.as_view(), name='document-detail'),
    path('<int:pk>/download/', views.download_document, name='document-download'),
    path('stats/', views.document_stats, name='document-stats'),
    
    # Административные API
    path('create/', views.DocumentCreateView.as_view(), name='document-create'),
    path('<int:pk>/update/', views.DocumentUpdateView.as_view(), name='document-update'),
    path('<int:pk>/delete/', views.DocumentDeleteView.as_view(), name='document-delete'),
]
