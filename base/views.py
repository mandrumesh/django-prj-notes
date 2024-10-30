from django.shortcuts import render
from django.http import HttpResponse
from .models import Note

# Create your views here.
def home(request):
    notes_obj = Note.objects.all()
    data = {'notes':notes_obj}
    return render(request, 'index.html',context=data)

def notes_form(request):
    notes_obj = Note.objects.all()
    data = {'notes':notes_obj}
    return render(request, 'notes_form.html',context=data)