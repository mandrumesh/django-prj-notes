from django import forms
from .models import Note, NoteCategory


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        # fields = '__all__'
        fields = ['name','category','description']
        widgets = {
            'name': forms.TextInput(attrs= {'class': 'form-control mb-2'}),
            'category': forms.Select(choices=NoteCategory.objects.all, attrs={'class':'form-select mb-2'}),
            'description': forms.Textarea(attrs= {'class': 'form-control'}),
        }

class NoteCategoryForm(forms.ModelForm):
    class Meta:
        model = NoteCategory
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs= {'class': 'form-control'})
        }