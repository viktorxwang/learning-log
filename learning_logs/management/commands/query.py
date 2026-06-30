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
        else:
            self.stdout.write(self.style.SUCCESS(f"There are {len(topics)} topics."))
        for topic in topics:
            self.stdout.write(f"{topic.id} {topic}")