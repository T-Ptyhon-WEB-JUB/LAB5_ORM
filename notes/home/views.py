from django.shortcuts import render, redirect, resolve_url
from django.http import HttpResponse, HttpRequest
from .models import Notes
from .forms import AddNotesForm
# Create your views here.


def home(request: HttpRequest):
    notes = Notes.objects.all()
    return render(request, 'home/index.html', {'notes': notes})


def about(request: HttpRequest):
    return render(request, 'home/about.html')


def add_notes(request: HttpRequest):
    if request.method == 'POST':
        form = AddNotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(resolve_url('home:index'))
    form = AddNotesForm()
    return render(request, 'home/add_notes.html', {'form': form})
