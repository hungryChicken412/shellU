from rest_framework import serializers, viewsets
from .models import Difficulty

# Serializers define the API representation.
class DifficultySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Difficulty
        fields = ['puzzle_category', 'category_summary']
