from django.shortcuts import render
from .models import Difficulty, Puzzle
from .serializers import DifficultySerializer, PuzzleSerializer, PuzzlePlaygroundSerializer
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

class PuzzlePlaygrounViewSet(viewsets.ModelViewSet):
    queryset = Puzzle.objects.all()
    serializer_class = PuzzlePlaygroundSerializer

    def get_queryset(self):
        name = self.kwargs.get('puzzleSlug')

        if (name == 'me'):
            name = self.request.user.username
        else:
            pass

        puzzle = Puzzle.objects.filter(puzzle_slug=name)
        return puzzle
    
    authenticationClasses = (TokenAuthentication,)
    permissionClasses = (IsAuthenticated,)





