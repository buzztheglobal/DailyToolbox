from django.urls import path
from .views import health_check, protected_data

urlpatterns = [
    path('health-check/', health_check, name='health-check'),
    path('protected-data/', protected_data, name='protected-data'), # Add this line
]