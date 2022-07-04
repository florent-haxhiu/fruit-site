from dataclasses import field
from pyexpat import model
from rest_framework import serializers

from fruit.models import Fruit

class FruitSerializer(serializers.ModelSerializer):
  class Meta:
    model = Fruit
    fields = '__all__'