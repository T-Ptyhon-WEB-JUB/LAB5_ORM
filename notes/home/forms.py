from django import forms
from .models import Notes


class AddNotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'
