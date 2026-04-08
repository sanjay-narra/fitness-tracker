from django import forms
from .models import Workout


class WorkoutForm(forms.ModelForm):

    class Meta:
        model = Workout
        fields = ['activity', 'duration', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

        