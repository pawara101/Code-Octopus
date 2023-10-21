from django.urls import path
from .views import CSVItemView

urlpatterns = [
    path('csvdata/', CSVItemView.as_view(), name='csvdata'),
]
