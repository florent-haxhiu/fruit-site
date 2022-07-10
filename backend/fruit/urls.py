from django.urls import path
from .views import FruitListView, ListView

urlpatterns = [
    path('', FruitListView.as_view()),
    path('list/', ListView.as_view())
]