from django.urls import path
from . import views

urlpatterns = [
    path('', views.workout_list, name='workout_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_workout, name='add_workout'),
    path('edit/<int:pk>/', views.edit_workout, name='edit_workout'),
    path('delete/<int:pk>/', views.delete_workout, name='delete_workout'),
]