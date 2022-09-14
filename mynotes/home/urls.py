from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("",  views.home, name="index"),
    path("add/note/", views.add_note, name="add_note"),
    path("about/", views.aboutpage, name="about"),
   
]