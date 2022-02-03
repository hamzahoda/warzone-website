from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path("", views.index, name="home"),
    path("team", views.team, name="team"),
    path("contact", views.contact, name="contact"),


]

