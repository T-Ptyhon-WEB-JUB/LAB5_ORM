from django.shortcuts import redirect
from django.shortcuts import render

from .models import Note
from .forms import NoteForm

def home(request):
    notes = Note.objects.all()
    return render(request, "index.html", {"notes": notes})

def add_note(request):    
        
    note_form = NoteForm()
    if request.method == "POST":
        note_form = NoteForm(request.POST)
        print(note_form)
        if note_form.is_valid():
            note_form.save()
            return redirect("index")
       
    return render(request, "add-note.html", {"form": note_form})

def about(request):
    return render(request, "about.html", {"test": "xxx"})