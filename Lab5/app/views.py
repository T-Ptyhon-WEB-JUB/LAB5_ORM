from django.shortcuts import render, redirect, resolve_url
from django.http import HttpResponse, HttpRequest
from .forms import NoteForm
from .models import Note


# Create your views here.



def index(request : HttpRequest):

    notes = Note.objects.all()

    return render(request, 'app/index.html', {"notes" : notes})

def add_note(request : HttpRequest):

    if request.method == 'POST':
        
        note = NoteForm(request.POST)

        if note.is_valid():
            note.save()
            return redirect(resolve_url("app:index"))

    note_form = NoteForm()
    
    return render(request, 'app/add_note.html', {"NoteForm" : note_form})


def about(request):

    return render(request, 'app/about.html')


