from django.urls import path
from .views import *

app_name = "home"

urlpatterns = [
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("", index, name="index"),
    path("contact/", contact, name="contact"),
    path("menu/", menu, name="menu"),
    path("about/", about, name="about"),
]