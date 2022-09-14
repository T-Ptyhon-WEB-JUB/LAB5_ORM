from django.shortcuts import render, redirect, resolve_url
from django.http import HttpRequest, HttpResponse


# Create your views here.
from .forms import NoteForm
from .models import Note

def index (request : HttpRequest):

    notes = Note.objects.all()

    return render(request, 'home/index.html', {"notes" : notes})

def add_note(request : HttpRequest):
    if request.method == "POST":
        new_note = NoteForm(request.POST)

        if new_note.is_valid():
            new_note.save()
            return redirect(resolve_url("home:index"))

    note_Form = NoteForm()

    return render(request,'home/add_note.html', {"form" : note_Form})

def about(request : HttpRequest):

        return render (request, 'home/about.html', {"about" : about})