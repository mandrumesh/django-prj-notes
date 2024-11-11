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
        widget = {
            'name': forms.TextInput(attrs= {'class': 'form-control'})
        }

class SearchNoteForm(forms.Form):
    query = forms.CharField(
        max_length=300, 
        required=False,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search for Notes...'})
    )
        
