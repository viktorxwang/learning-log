# query.py

# # Makes sure that all imports happen locally
# import sys
# sys.path.append("./")

# Imports topic from the models of app learning_logs
from learning_logs.models import Topic

"""
Python scripts for requesting, manipulating, and outputting app data.
"""

# Looping over a Topic queryset
topics = Topic.objects.all()
for topic in topics:
    print(topic.id, topic)