from django.shortcuts import render
from .models import Difficulty, Puzzle
from .serializers import DifficultySerializer, PuzzleSerializer, PuzzlePlaygroundSerializer
from rest_framework import routers, serializers, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from django.contrib.auth.models import User
from django.db.models.aggregates import Max

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
    serializer_class = PuzzlePlaygroundSerializer

    def get_queryset(self):
        name = self.kwargs.get('puzzleSlug')

        if (name == 'me'):
            name = self.request.user.username
        else:
            pass

        puzzle = Puzzle.objects.get(puzzle_slug=name)

        try:
            user = puzzle.solvers.get(username=self.request.user.username)
            puzzle.hasDone = True
        except User.DoesNotExist:
            pass
        
        return [puzzle]
    
    authenticationClasses = (TokenAuthentication,)
    permissionClasses = (IsAuthenticated,)




