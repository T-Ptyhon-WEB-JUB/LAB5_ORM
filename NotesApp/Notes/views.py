from django.shortcuts import render
from django.http import HttpResponse
from .forms import NotesModelForm
from .models import Note
from django.shortcuts import redirect, resolve_url

# Create your views here.
def home (request):
    note=Note.objects.all()
    return (
        render(request,'index.html',{'note':note})  #to return a templete
    )
def newNote (request):
    form=NotesModelForm()
    if request.method=='POST':
        notesModelForm=NotesModelForm(request.POST)
        if notesModelForm.is_valid():
            notesModelForm.save()
            return redirect(resolve_url('home:home')) #appName:pathNAme
    form=NotesModelForm()         
    return (render(request,'formPage.html',{'form':form}))

def about(request):
    return(render(request,'about.html'))