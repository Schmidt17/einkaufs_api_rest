from django.db import models


class CollectedItem(models.Model):
    class ActionType(models.TextChoices):
        CROSSED = 'CROSSED'
        UNCROSSED = 'UNCROSSED'

    action_type = models.CharField(max_length=255, choices=ActionType.choices)
    name = models.CharField(max_length=255)
    item_id = models.CharField(max_length=32)
    latitude = models.FloatField(null=True, blank=True, default=None)
    longitude = models.FloatField(null=True, blank=True, default=None)
    timestamp = models.DateTimeField(auto_now_add=True)