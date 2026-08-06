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
    # Details page for a single topic.
    path("topics/<int:topic_id>/", views.topic, name = "topic"),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
]