from django import forms
from .models import Note, NoteCategory
from django.contrib.auth.models import User


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
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs= {'class': 'form-control mb-2'}),
            'password': forms.PasswordInput(attrs= {'class': 'form-control'}),
        }
