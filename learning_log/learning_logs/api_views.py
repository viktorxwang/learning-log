from rest_framework import viewsets

from .models import Topic, Entry
from .serializers import TopicSerializer, EntrySerializer


class TopicViewSet(viewsets.ModelViewSet):
    """
    Provides list, retrieve, create, update, destroy for Topics.
    GET    /api/topics/          -> list all topics
    POST   /api/topics/          -> create a topic
    GET    /api/topics/<id>/     -> a single topic, with its entries nested
    PUT    /api/topics/<id>/     -> update a topic
    DELETE /api/topics/<id>/     -> delete a topic (and its entries, cascade)
    """
    queryset = Topic.objects.order_by('date_added')
    serializer_class = TopicSerializer


class EntryViewSet(viewsets.ModelViewSet):
    """
    Provides list, retrieve, create, update, destroy for Entries.
    GET    /api/entries/               -> list all entries
    POST   /api/entries/               -> create an entry (pass topic id in body)
    GET    /api/entries/<id>/          -> a single entry
    PUT    /api/entries/<id>/          -> update an entry
    DELETE /api/entries/<id>/          -> delete an entry

    Supports ?topic=<id> to filter entries for one topic:
    GET /api/entries/?topic=3
    """
    serializer_class = EntrySerializer

    def get_queryset(self):
        queryset = Entry.objects.order_by('-date_added')
        topic_id = self.request.query_params.get('topic')
        if topic_id is not None:
            queryset = queryset.filter(topic_id=topic_id)
        return queryset
