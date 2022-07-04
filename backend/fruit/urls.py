from django.urls import path
from .views import FruitListView

urlpatterns = [
    path('', FruitListView.as_view())
]