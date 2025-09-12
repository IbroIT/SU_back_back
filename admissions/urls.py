from django.urls import path
from .views import submit_application_email

urlpatterns = [
    path('applications/submit-email/', submit_application_email, name='submit_application_email'),
]
