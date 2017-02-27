from django import forms
from datetime import datetime

from .models import Solution


class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        exclude = ['student']
        fields = ('url', 'task')
