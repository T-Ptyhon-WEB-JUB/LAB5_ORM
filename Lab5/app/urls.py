from django.urls import path
from . import views

app_name = 'app'


urlpatterns = [
    path('', views.index, name='index'),
    path('note/', views.add_note, name='add_note'),
    # path('about/', views.)

    
]
