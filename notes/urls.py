"""
URL configuration for notes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base.views import home
from base.views import notes_form, notes_category_form, edit_note, edit_note_category, delete_note, delete_note_category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('notes_form/', notes_form, name='notes-form'),
    path('notes_category_form/', notes_category_form, name='notes-category-form'),
    path('edit_note/<int:pk>/', edit_note, name='edit-note'), #pass id value
    path('edit_note_category/<int:pk>/', edit_note_category, name='edit-note-category'),
    path('delete_note/<int:pk>/', delete_note, name='delete-note'),
    path('delete_note_category/<int:pk>/', delete_note_category, name='delete-note-category'),
]
