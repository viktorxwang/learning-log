from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry # We don't need to import Entry since it is implicit
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

"""
The topics view is created with the login_required decorator, meaning that 
the code in login_required will run before every call of topics.
The code in login_required() checks whether a user is logged in,
and Django runs the code in topics() only if they are. If the user isn't
logged in, they're redirected to the login page.
"""
@login_required
def topics(request):
    """Shows all topics."""
    # Only show the topics that belong to the logged in user
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")
    context = {"topics" : topics} # Passes info to the template
    return render(request, "learning_logs/topics.html", context)

@login_required
def topic(request, topic_id):
    """Shows one topic, which is at <int:topic_id>"""
    # Referring to a .models is a query.
    topic = Topic.objects.get(id = topic_id)
    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404 # creates http 404 error
    
    entries = topic.entry_set.order_by("-date_added") # The most recent entries appear at the topic
    # We need two elements in context, the topic, and its entries
    context = {"topic" : topic, "entries" : entries}
    return render(request, "learning_logs/topic.html", context)


@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != "POST":
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted, we will process the data
        form = TopicForm(data=request.POST) # TopicForm with data param is request.POST
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    # Display a blank or invalid form.
    context = {'form' : form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    # Get the topic from the topic_id
    topic = Topic.objects.get(id=topic_id)

    # If we aren't posting a entry somehow
    if request.method != "POST":
        # No data submitted, we create a blank form
        form = EntryForm()
    else:
        # POST data is submitted, we relay the data
        form = EntryForm(data = request.POST)
        if form.is_valid(): # is_valid() is a function
            new_entry = form.save(commit = False)
            new_entry.topic = topic # personal topic for new_entry
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Display a blank or invalid form.
    context = {'topic' : topic, 'form' : form}
    # topic id doesn't have to be restated within the link
    return render(request, "learning_logs/new_entry.html", context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry. We need the entry_id, which is found through the total entry list."""
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic

    # We need to protext this page so no one
    # can use the URL to gain access to someone else's entries.
    if topic.owner != request.user:
        raise Http404
    
    if request.method != "POST":
        # Initial request; prefill form with the current entry.
        form = EntryForm(instance = entry)
    else:
        # POST data submitted, process data
        form = EntryForm(instance = entry, data = request.POST)
        if form.is_valid():
            # We need to modify the new topic before saving to the database
            # form.save()
            new_topic = form.save(commit = False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    # Now we pass the context to render a template
    context = {"entry" : entry, "topic" : topic, "form" : form}
    return render(request, 'learning_logs/edit_entry.html', context)