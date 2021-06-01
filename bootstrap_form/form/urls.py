from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('registration/', views.registration_form, name='registration'),
    path('info/', views.registration_details, name='details'),
    path('register_user/', views.reguster_user, name='register_user'),
]