from django.url import path
from .views import views

app_name = 'home'

urlpatterns = [
    path('/', views.home, name='home'),
    path('/about', views.about, name='about'),
    path('/add_notes', views.add_notes, name='add_notes'),

]
