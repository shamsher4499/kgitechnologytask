from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.test, name='test'),
    path('information/', views.registration_info, name='information'),
    path('user-information/<int:aid>/', views.user_data, name='user-information'),
    path('contact-us/', views.contact_us),
]