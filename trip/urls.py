from django.urls import path

from . import views


urlpatterns = [
    path('', views.trip_details, name='trip_details'),
    path('update-map', views.update_map, name='update_map')
]    