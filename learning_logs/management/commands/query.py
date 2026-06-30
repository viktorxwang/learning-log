# learning_logs/management/commands/query.py

from django.core.management.base import BaseCommand
from learning_logs.models import Topic

class Command(BaseCommand):
    help = "Prints all topics"

    def handle(self, *args, **options):
        topics = Topic.objects.all()
        for topic in topics:
            self.stdout.write(f"{topic.id} {topic}")