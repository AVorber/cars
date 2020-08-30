from django.urls import path
from .views import api_detail_car_view

app_name = 'cars_api'

urlpatterns = [
    path('<slug>/', api_detail_car_view, name='cars-detail'),
]