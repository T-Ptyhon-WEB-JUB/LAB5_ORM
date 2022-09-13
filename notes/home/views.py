from django.shortcuts import render, redirect, resolve_url
from django.http import HttpResponse, HttpRequest
# Create your views here.


def home(request: HttpRequest):
    return render(request, 'home/index.html')


def about(request: HttpRequest):
    return render(request, 'home/about.html')


def add_notes(request: HttpRequest):
    return render(request, 'home/add_notes.html')
