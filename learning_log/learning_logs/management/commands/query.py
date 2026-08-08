# learning_logs/management/commands/query.py

from django.core.management.base import BaseCommand
from learning_logs.models import Topic

class Command(BaseCommand):
    help = "Prints all topics"

    def handle(self, *args, **options):
        print("Getting topics...")
        topics = Topic.objects.all()

        if len(topics) == 0:
            self.stdout.write(self.style.ERROR("Found no topics."))
            return
        else:
            self.stdout.write(self.style.SUCCESS(f"There are {len(topics)} topics."))
        
        # Enumerate the topics with their topic.id
        for topic in topics:
            self.stdout.write(f"{topic.id} {topic}")

        # We get the attributes of the topic with ID 1, this is the first topic. [0]
        t = Topic.objects.get(id=1)
        self.stdout.write("\nAttributes of the first topic:")
        self.stdout.write(f"Name: {t.text}")
        self.stdout.write(f"Date added: {t.date_added}")
        self.stdout.write(f"{t.entry_set.all()}")