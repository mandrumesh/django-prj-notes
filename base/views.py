from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note, NoteCategory
from .forms import NoteForm, NoteCategoryForm

# Create your views here.
def home(request):
    notes_obj = Note.objects.all()
    note_category_objs = NoteCategory.objects.all()
    data = {'notes':notes_obj, 'note_categories': note_category_objs}
    return render(request, 'index.html',context=data)

def notes_form(request): 
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = NoteForm()
    data = {'form':form}
    return render(request, 'notes_form.html',context=data)

def notes_category_form(request):
    if request.method == 'POST':
        form = NoteCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = NoteCategoryForm()
    data = {'form':form}
    return render(request, 'notes_category_form.html',context=data)