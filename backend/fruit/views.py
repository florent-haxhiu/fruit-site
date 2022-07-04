from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import rest_framework.status
from fruit.models import Fruit
from .serializers.common import FruitSerializer

# Create your views here.

class FruitListView(APIView):
  def get(self, _request):
    fruits = Fruit.objects.all()
    serialized_fruits = FruitSerializer(fruits, many=True)
    return Response(serialized_fruits, status=status.HTTP_200_OK)