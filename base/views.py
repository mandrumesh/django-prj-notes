from django.shortcuts import render, redirect
from .models import Note, NoteCategory
from .forms import NoteForm, NoteCategoryForm, UserForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        notes_obj = Note.objects.all()
        note_category_objs = NoteCategory.objects.all()
        query = request.GET.get('query')
        if query:
            notes_obj = notes_obj.filter(name__icontains=query)
        data = {'notes':notes_obj, 'note_categories': note_category_objs}
        return render(request, 'index.html',context=data)
    else:
        return redirect('login')

def notes_form(request):
    if request.user.is_authenticated:
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
    else:
        return redirect('login')

def notes_category_form(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = NoteCategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/#nav-note-category')
        form = NoteCategoryForm()
        data = {'form':form}
        return render(request, 'notes_category_form.html',context=data)
    else:
        return redirect('login')

def edit_note(request, pk):
    if request.user.is_authenticated:
        note_obj = Note.objects.get(id=pk)
        if request.method == 'POST':
            form = NoteForm(request.POST, instance=note_obj)
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                return render(request, 'notes_form.html',context= {'form':form})
        form = NoteForm(instance = note_obj)
        data = {'form': form}
        return render(request, 'edit_note.html', context=data)
    else:
        return redirect('login')

def edit_note_category(request, pk):
    if request.user.is_authenticated:
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
    else:
        return redirect('login')

def delete_note(request, pk):
    if request.user.is_authenticated:
        note_obj = Note.objects.get(id=pk)
        note_obj.delete()
        return redirect('home')
    else:
        return redirect('login')
    
def delete_note_all(request):
    if request.user.is_authenticated:
        note_obj = Note.objects.all()
        note_obj.delete()
        return redirect('home')
    else:
        return redirect('login')

def delete_note_category(request, pk):
    if request.user.is_authenticated:
        note_category_obj = NoteCategory.objects.get(id=pk)
        note_category_obj.delete()
        return redirect('/#nav-note-category')
    else:
        return redirect('login')

def register(request):
    form = UserForm()
    if request.method == 'POST':
        password = request.POST.get('password')
        hash_password = make_password(password)
        data = request.POST.copy()
        data['password'] = hash_password
        form = UserForm(data)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'register.html', context= {'form': form})
    data = {'form': form}
    return render(request, 'register.html', context = data)

def user_login(request):
    form = UserForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user == None:
            data= {'form':form, 'error':'Invalid Username or Password'}
            return render(request, 'login.html', context= data)
        else:
            login(request, user)
            return redirect('home')

    data = {'form': form}
    return render(request, 'login.html', context= data)

def user_logout(request):
    logout(request)
    return redirect('login')
  