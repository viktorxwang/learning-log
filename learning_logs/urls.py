"""Defines URL patterns for learning_logs."""

# Needed for mapping URLs to views
from django.urls import path

# Imports the views functions from learning_logs
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path("", views.index, name = "index"),
    # Page that shows all the topics. Uses a loop to list the topics.
    path("topics/", views.topics, name = "topics"),
]