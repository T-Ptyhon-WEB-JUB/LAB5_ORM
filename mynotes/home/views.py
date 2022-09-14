from django.shortcuts import render, redirect, resolve_url
from django.http import HttpRequest, HttpResponse
from datetime import date
import random
import string
from django.views.generic import TemplateView
import datetime
from .forms import noteForm
from .models import note


# Create your views here.


def home(request: HttpRequest):
    notes = note.objects.all()
    currentdate = datetime.date.today()
    formatDate = currentdate.strftime("%d-%b-%y")
    return render(request, 'home/index.html', {"notes": notes, 'current_date':currentdate, 'format_date':formatDate} )
   

def add_note(request: HttpRequest):
    if request.method == "POST":
        new_note = noteForm(request.POST)
        if new_note.is_valid():
            new_note.save()
            return redirect(resolve_url("home:index"))
    note_form = noteForm()
    return render(request, 'home/add_notes.html', {"form": noteForm}) 

def aboutpage(request: HttpRequest):
    about = ["Reem, Computer Science student"]
    return render(request, 'home/about.html', {"about": about}) 

