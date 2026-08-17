from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# render allows the blank/invalid form to be displayed
# redirect moves to a different learning_logs: or users:
# login and UserCreationForm are builtin

def register(request):
    """Register a new user."""
    if request.method != "POST":
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process the completed form. Creates another user if information is valid.
        form = UserCreationForm(data = request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and redirect to home page.
            login(request, new_user) # Creates valid session for new user.
            return redirect("learning_logs:index") # Redirect the user to the home page.

    # Display a blank or invalid form
    context = {"form" : form}
    return render(request, "registration/register.html", context)