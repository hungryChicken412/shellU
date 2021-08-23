from django.db.models import fields
from rest_framework import serializers, viewsets
from .models import Difficulty, Puzzle



# Serializers define the API representation.
class DifficultySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Difficulty
        fields = ['puzzle_category', 'category_summary']

class PuzzleSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Puzzle
        fields = ['title', 'puzzle_category', 'puzzle_slug', 'xps']

class PuzzlePlaygroundSerializer(serializers.HyperlinkedModelSerializer):
    hasDone = False
    class Meta:
        model = Puzzle
        fields = ['title', 'puzzle_category', 'puzzle_slug', 'content', 'puzzleDesiredOutput','functionName', 'puzzleSolution', 'hint', 'starterCode', 'testCases', 'xps', 'hasDone']


