from django import forms

from .models import Task
from courses.models import Course


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'course')
