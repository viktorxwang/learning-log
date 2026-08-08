from rest_framework import serializers

from .models import Topic, Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id', 'topic', 'text', 'date_added']
        read_only_fields = ['id', 'date_added']


class TopicSerializer(serializers.ModelSerializer):
    # Nested, read-only list of this topic's entries (most recent first).
    entries = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = ['id', 'text', 'date_added', 'entries']
        read_only_fields = ['id', 'date_added']

    def get_entries(self, topic):
        entries = topic.entry_set.order_by('-date_added')
        return EntrySerializer(entries, many=True).data
