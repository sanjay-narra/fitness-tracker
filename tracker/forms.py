from django import forms
from .models import Workout, Category

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['activity', 'duration', 'date', 'category']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'activity': forms.TextInput(attrs={'placeholder': 'e.g. Morning Run, Push-ups'}),
            'duration': forms.NumberInput(attrs={'placeholder': 'Duration in minutes'}),
            'category': forms.Select(attrs={'class': 'category-select'}),
        }