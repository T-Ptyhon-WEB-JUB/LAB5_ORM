from urllib.parse import urlparse
from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
    path("send/", views.send, name="send_msg"),
]   