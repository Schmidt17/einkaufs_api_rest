from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from pathlib import Path
import cloudpickle

from .models import CollectedItem
from .serializers import CollectedItemSerializer


class ItemList(generics.ListAPIView):
    queryset = CollectedItem.objects.all()
    serializer_class = CollectedItemSerializer


class CollectItem(generics.CreateAPIView):
    queryset = CollectedItem.objects.all()
    serializer_class = CollectedItemSerializer


def load_model(path):
    with open(path, 'rb') as f:
        model = cloudpickle.load(f)

    return model


class SortList(APIView):
    sort_func = load_model(Path('resources') / 'sort_func_REWE_Kreuzstrasse.cloudpickle')

    def post(self, request):
        list_to_sort = request.data['input_list']
        sorted_array, sorted_scores = self.sort_func(list_to_sort)
        sorted_list = sorted_array.tolist()

        return Response({"sorted_list": sorted_list})
