from django.shortcuts import render, redirect
from .models import Note, NoteCategory
from .forms import NoteForm, NoteCategoryForm, SearchNoteForm

# Create your views here.
def home(request):
    notes_obj = Note.objects.all()
    note_category_objs = NoteCategory.objects.all()
    search_form = SearchNoteForm(request.GET)

    if search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        if query:
            notes_obj = notes_obj.filter(name__icontains=query)
    data = {'notes':notes_obj, 'note_categories': note_category_objs, 'search_form': search_form}
    return render(request, 'index.html',context=data)

def notes_form(request): 
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'notes_form.html',context= {'form':form}) #Error Handeling
    form = NoteForm()
    data = {'form':form}
    return render(request, 'notes_form.html',context=data)

def notes_category_form(request):
    if request.method == 'POST':
        form = NoteCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/#nav-note-category')
    form = NoteCategoryForm()
    data = {'form':form}
    return render(request, 'notes_category_form.html',context=data)

def edit_note(request, pk):
    note_obj = Note.objects.get(id=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note_obj)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'notes_form.html',context= {'form':form})
    form = NoteForm(instance = note_obj)
    data= {'form':form}
    return render(request, 'edit_note.html', context=data)

def edit_note_category(request, pk):
    note_category_obj = NoteCategory.objects.get(id=pk)
    if request.method == 'POST':
        form = NoteCategoryForm(request.POST, instance=note_category_obj)
        if form.is_valid():
            form.save()
            return redirect('/#nav-note-category')
        else:
            return render(request, 'edit_note_category.html', content={'form':form})
    form = NoteCategoryForm(instance= note_category_obj)
    data= {'form':form}
    return render(request, 'edit_note_category.html', context=data)

def delete_note(request, pk):
    note_obj = Note.objects.get(id=pk)
    note_obj.delete()
    return redirect('home')

def delete_note_category(request, pk):
    note_category_obj = NoteCategory.objects.get(id=pk)
    note_category_obj.delete()
    return redirect('/#nav-note-category')