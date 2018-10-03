from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('name', 'body')
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Note name',
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your thoughts here...'
            }),
        }

        labels = {
            'name': 'Name of your Note:',
            'body': 'Your thoughts:'
        }
