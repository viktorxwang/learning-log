from django.urls import path, include
from . import views

app_name = "users"

urlpatterns = [
    # Custom logout MUST come before Django's built-in auth URLs.
    path("logout/", views.logout_view, name="logout"),

    # Django's built-in login/password URLs.
    path("", include("django.contrib.auth.urls")),

    # Custom registration.
    path("register/", views.register, name="register"),
]