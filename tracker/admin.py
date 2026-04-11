from django.contrib import admin
from .models import Workout, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'color', 'icon']
    search_fields = ['name']

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['activity', 'user', 'category', 'duration', 'date']
    list_filter = ['category', 'date', 'user']
    search_fields = ['activity', 'user__username']
    date_hierarchy = 'date'