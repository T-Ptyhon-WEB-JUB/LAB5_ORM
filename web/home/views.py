from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, resolve_url
from .forms import NoteFrom
from .models import Note
def home(request : HttpRequest):
    note = Note.objects.all()
    return render(request , "home/index.html",{"note" : note} )

def send(request : HttpRequest):
    if request.method == "POST":
        new_notes = NoteFrom(request.POST)
        if new_notes.is_valid():
            new_notes.save()
            return redirect(resolve_url("home:home"))
    from_note = NoteFrom()
    return render(request , "home/notes.html",{"form" : from_note} )
