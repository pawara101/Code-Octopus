from django.urls import path
from .views import CSVItemView

urlpatterns = [
    path('csv-items/', CSVItemView.as_view(), name='csv-items'),
]
