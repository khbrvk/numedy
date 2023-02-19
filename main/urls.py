from django.urls import path
from .views import get_report, home

urlpatterns = [
    path('', home),
    path('supplies', get_report)
]