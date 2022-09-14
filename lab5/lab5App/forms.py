from django import forms
# from . import addingNote
from .models import addingNote

class addingNoteModelForm(forms.ModelForm):
    class Meta:
        model = addingNote
        fields = '__all__' 