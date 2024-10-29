from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from pathlib import Path
import cloudpickle
from tflite_runtime import interpreter as tflite
from functools import partial

from .models import CollectedItem
from .serializers import CollectedItemSerializer


class ItemList(generics.ListAPIView):
    queryset = CollectedItem.objects.all()
    serializer_class = CollectedItemSerializer


class CollectItem(generics.CreateAPIView):
    queryset = CollectedItem.objects.all()
    serializer_class = CollectedItemSerializer


class TFLiteEstimator:
    def __init__(self, tflite_model):
        self.callable = tflite_model.get_signature_runner()
        self.signature_list = tflite_model.get_signature_list()

        self.input_tensor_name = self.signature_list['serving_default']['inputs'][0]
        self.output_tensor_name = self.signature_list['serving_default']['outputs'][0]


    def predict(self, input_data):
        return self.callable(**{self.input_tensor_name: input_data})[self.output_tensor_name]


def load_model(path, tflite_path=None):
    with open(path, 'rb') as f:
        model = cloudpickle.load(f)

    if tflite_path is not None:
        tflite_model = tflite.Interpreter(str(tflite_path))
        model = partial(model, model=TFLiteEstimator(tflite_model))

    return model


class SortList(APIView):
    base_model_path = Path('resources') / 'sort_func_REWE_Kreuzstrasse.cloudpickle'
    tflite_model_path = Path('resources') / 'sort_func_REWE_Kreuzstrasse.tflite'

    if not tflite_model_path.is_file():
        tflite_model_path = None

    sort_func = load_model(base_model_path, tflite_model_path)

    def post(self, request):
        list_to_sort = request.data['input_list']
        sorted_array, sorted_scores, sort_indices = self.sort_func(list_to_sort)
        sorted_list = sorted_array.tolist()
        sort_indices = sort_indices.tolist()

        return Response({"sorted_list": sorted_list, "sort_indices": sort_indices, "input_list": list_to_sort})
