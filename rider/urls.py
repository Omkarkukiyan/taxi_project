from django.urls import path

from . import views


urlpatterns = [
    path('rider-login/', views.rider_login, name='rider_login'),
    path('rider-logout/', views.rider_logout, name='rider_logout'),
    path('rider-signup/', views.rider_signup, name='rider_signup'),
    path('rider-dashboard/', views.rider_dashboard, name='rider_dashboard')
]    