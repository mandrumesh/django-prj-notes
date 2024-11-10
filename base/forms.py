from django import forms
from .models import Note, NoteCategory


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        # fields = '__all__'
        fields = ['name','category','description']
        widgets = {
            'name': forms.TextInput(attrs= {'class': 'form-control'}),
            'category': forms.Select(choices=NoteCategory.objects.all, attrs={'class':'form-select'}),
            'description': forms.Textarea(attrs= {'class': 'form-control'}),
        }

class NoteCategoryForm(forms.ModelForm):
    class Meta:
        model = NoteCategory
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs= {'class': 'form-control'})
        }