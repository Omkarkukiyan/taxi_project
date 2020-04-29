from django.urls import path

from . import views



urlpatterns = [
    path('driver-login/', views.driver_login, name='driver_login'),
    path('driver-logout/', views.driver_logout, name='driver_logout'),
    path('driver-signup/', views.driver_signup, name='driver_signup'),
    path('driver-dashboard/', views.driver_dashboard, name='driver_dashboard'),
    path('request/<int:trip_id>', views.ride_request, name="ride_request"),
    path('completed/<int:trip_id>', views.recent_trip, name="recent_trip")
]    