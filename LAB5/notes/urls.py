from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("add-note", views.add_note, name="add_note"),
    path("about", views.about, name="about")
]