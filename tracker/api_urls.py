from django.urls import path
from . import api_views

urlpatterns = [
    path('workouts/', api_views.WorkoutListCreateAPI.as_view(), name='api-workouts'),
    path('workouts/<int:pk>/', api_views.WorkoutDetailAPI.as_view(), name='api-workout-detail'),
    path('categories/', api_views.CategoryListAPI.as_view(), name='api-categories'),
    path('summary/', api_views.api_summary, name='api-summary'),
]