from rest_framework import serializers
from fruit.models import Fruit, List

class FruitSerializer(serializers.ModelSerializer):
  class Meta:
    model = Fruit
    fields = '__all__'

class ListSerializer(serializers.ModelSerializer):
  class Meta:
    model = List
    fields = '__all__'