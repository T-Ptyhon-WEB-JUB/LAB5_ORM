from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note

# Create your views here.


def index(request):
    # get all notes from the database and pass them to the template
    notes = Note.objects.all()
    return render(request, 'note/index.html', {'notes': notes})


def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note:index')

    form = NoteForm()
    return render(request, 'note/add_note.html', {'form': form})


def about(request):
    return render(request, 'note/about.html')
