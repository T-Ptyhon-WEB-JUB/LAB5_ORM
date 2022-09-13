from django.shortcuts import render, redirect, resolve_url
from django.http import HttpRequest, HttpResponse
from datetime import date
import random
import string

from .forms import noteForm
from .models import note


# Create your views here.


def home(request: HttpRequest):
    notes = note.objects.all()
    return render(request, 'home/index.html', {"notes": notes})


def add_note(request: HttpRequest):
    if request.method == "POST":
        new_note = noteForm(request.POST)
        if new_note.is_valid():
            new_note.save()
            return redirect(resolve_url("home:index"))
    note_form = noteForm()
    return render(request, 'home/add.html', {"form": note_form})