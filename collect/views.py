from rest_framework import generics
from rest_framework_api_key.permissions import HasAPIKey

from .models import CollectedItem
from .serializers import CollectedItemSerializer


class ItemList(generics.ListAPIView):
    queryset = CollectedItem.objects.all()
    serializer_class = CollectedItemSerializer


class CollectItem(generics.CreateAPIView):
    permission_classes = [HasAPIKey]
    queryset = CollectedItem.objects.all()
    serializer_class = CollectedItemSerializer
