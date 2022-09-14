from django.urls import path
from . import views

app_name = "lab5App"

urlpatterns = [
    path('', views.index, name="index"),
    path('addingNote/', views.addingNote, name="addingNote"),
    path('about/', views.about, name="about"),
    # path("books/", views.books, name="books")
    
]
