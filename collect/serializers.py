from rest_framework import serializers

from .models import CollectedItem


class CollectedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectedItem
        fields = '__all__'
