from django.shortcuts import render, redirect

from .models import Topic # We don't need to import Entry since it is implicit
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Shows all topics."""
    topics = Topic.objects.order_by("date_added")
    context = {"topics" : topics} # Passes info to the template
    return render(request, "learning_logs/topics.html", context)

def topic(request, topic_id):
    """Shows one topic, which is at <int:topic_id>"""
    # Referring to a .models is a query.
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by("-date_added") # The most recent entries appear at the topic
    # We need two elements in context, the topic, and its entries
    context = {"topic" : topic, "entries" : entries}
    return render(request, "learning_logs/topic.html", context)

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
    