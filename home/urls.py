from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("",  views.home, name="index"),
    path("notes/add/", views.add_note, name="add_note")
]