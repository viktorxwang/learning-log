from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm

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
    return render(request, 'learning_logs/new_topic.html')