"""Defines URL patterns for the learning_logs REST API."""

from rest_framework.routers import DefaultRouter

from .api_views import TopicViewSet, EntryViewSet

router = DefaultRouter()
router.register(r'topics', TopicViewSet, basename='topic')
router.register(r'entries', EntryViewSet, basename='entry')

urlpatterns = router.urls
