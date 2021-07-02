from django.shortcuts import render
from .models import Difficulty
from .serializers import DifficultySerializer
from rest_framework import routers, serializers, viewsets

# Create your views here.
# ViewSets define the view behavior.
class DiffViewSet(viewsets.ModelViewSet):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer
