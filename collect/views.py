from rest_framework import generics

from .models import CollectedItem
from .serializers import CollectedItemSerializer


class ItemList(generics.ListAPIView):
    queryset = CollectedItem.objects.all()
    serializer_class = CollectedItemSerializer


class CollectItem(generics.CreateAPIView):
    queryset = CollectedItem.objects.all()
    serializer_class = CollectedItemSerializer
