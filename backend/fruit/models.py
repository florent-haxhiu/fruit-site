from django.db import models

# Create your models here.
class Fruit(models.Model):
  # type = models.TextField(max_length=20)
  name = models.TextField(max_length=50)
  
  def __str__(self) -> str:
    return f"{self.name} - {self.type}"

class List(models.Model):
  type = models.TextField(max_length=20)
  
  def __str__(self) -> str:
    return f"{self.type}"