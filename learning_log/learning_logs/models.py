from django.db import models
from django.contrib.auth.models import User

# A model tells Django how to work with the stored data within the app.

"""
We need to connect the data to the user who submitted it. 
We need to connect only the data highest in the hierarchy to a user, and the lower-level
data will follow. For example, topics are the highest level of data.
"""

class Topic(models.Model):
    """A topic the user is learning about. Encompasses other objects within the Topic header."""
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add=True)
    # If a user is deleted, all the topics associated with that user will be deleted as well.
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation/description of the model."""
        return self.text
    
class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Modifies the metadata of an Entry model."""
        verbose_name_plural = "entries"
    
    def __str__(self):
        """Return a string representation/description of the model when queried."""
        if len(self.text) >= 50:
            return f"{self.text[:50]}..."
        return f"{self.text[:50]}"