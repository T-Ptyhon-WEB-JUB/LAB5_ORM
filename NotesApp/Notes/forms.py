from . import models
from django import forms
class NotesModelForm(forms.ModelForm):
    class Meta:
        model = models.Note
        fields = ['title','description'] #to include all fields

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control' }),
            'description':forms.Textarea(attrs={'class':'form-control' }),
        }    