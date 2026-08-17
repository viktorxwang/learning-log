"""Defines URL patterns for users."""

from django.urls import path, include

from . import views

app_name = "users"
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')), # Sends the user to http://localhost:8000/users/login
    # Registration page.
    path('register/', views.register, name="register")

]