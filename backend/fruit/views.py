from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from fruit.models import Fruit, List
from .serializers.common import FruitSerializer, ListSerializer

# Create your views here.

class FruitListView(APIView):
  def get(self, _request):
    fruits = Fruit.objects.all()
    serialized_fruits = FruitSerializer(fruits, many=True)
    return Response(serialized_fruits.data, status=status.HTTP_200_OK)
  def post(self, request):
    print(request.data)
    serial = FruitSerializer(data=request.data)
    print(request.data)
    try:
      print(serial.data)
      serial.is_valid()
      serial.save()
      return Response(serial.data, status=status.HTTP_201_CREATED)
    except IntegrityError as e:
      print(e)
      return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    except AssertionError as e:
      print(e)
      return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    except:
      return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
class ListView(APIView):
  def get(self, _request):
    fruit_list = List.objects.all()
    serial = ListSerializer(fruit_list, many=True)
    return Response(serial.data, status=status.HTTP_200_OK)
  def post(self, request):
    serial = ListSerializer(data=request.data)
    print(request.data)
    try:
      print(serial.data)
      serial.is_valid()
      serial.save()
      return Response(serial.data, status=status.HTTP_201_CREATED)
    except IntegrityError as e:
      print(e)
      return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    except AssertionError as e:
      print(e)
      return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    except:
      return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)