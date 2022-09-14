from django.shortcuts import render,resolve_url,redirect
from .forms import addingNoteModelForm
from .models import addingNote


# Create your views here.
def index(request):
    return render(request,'lab5App/index.html')

def addingNote(request):
    if request.method == 'POST':
        r = addingNoteModelForm(request.POST)
        if r.is_valid():
            r.save()
            return redirect(resolve_url("lab5App:index"))
    form = addingNoteModelForm()
    return render(request, 'lab5App/addingNote.html', {"form" : form})

def view_database(request):
    notes = addingNoteModelForm.objects.all()
    return render(request,'lab5App/index',{"notes":notes})

def about(request):
    name = 'Muath Al-Ghamdi'
    age = '22'
    email = 'csmuath.gh@gmail.com'
    return render(request,'lab5App/about.html',{"name":name,"age":age,"email":email})


