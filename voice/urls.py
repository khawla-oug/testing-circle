from django.urls import path
from . import views

urlpatterns = [
    path("landing/", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("contact/", views.contact, name="contact"),
    path("single/", views.single, name="single"),


]
