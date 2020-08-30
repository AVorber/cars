from django.conf.urls import url
from django.urls import path

from .views import car_list, car_detail, search

app_name = 'catalog_app'
urlpatterns = [
    path('', car_list, name='car-list'),
    url(r'^results/$', search, name='search'),
    path('car-detail/<slug:slug>', car_detail, name='car-detail')
]
