from django.db import models

# A model tells Django how to work with the stored data within the app.

class Topic(models.Model):
    """A topic the user is learning about. Encompasses other objects within the Topic header."""
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation/description of the model."""
        return self.text