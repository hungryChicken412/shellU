from django.shortcuts import render
from .models import Difficulty, Puzzle
from .serializers import DifficultySerializer, PuzzleSerializer
from rest_framework import routers, serializers, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
# Create your views here.
# ViewSets define the view behavior.
class DiffViewSet(viewsets.ModelViewSet):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer

class PuzzViewSet(viewsets.ModelViewSet):
    queryset = Puzzle.objects.all()
    serializer_class = PuzzleSerializer
    authenticationClasses = (TokenAuthentication,)
    permissionClasses = (IsAuthenticated,)
