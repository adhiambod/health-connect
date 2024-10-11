from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('update_profile/', views.update_profile_view, name='update_profile'),
    path('doctors/', views.doctors_list_view, name='doctors_list'),
    path('appointments/', views.appointment_list_view, name='appointment_list'),
    path('book_appointment/', views.book_appointment_view, name='book_appointment'),
]
