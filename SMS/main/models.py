from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

import sys
sys.path.append('..')
from profiles.models import Profile


# Create your models here.




class Difficulty(models.Model):
	puzzle_category = models.CharField(max_length=200)
	category_summary = models.CharField(max_length=200)
	category_slug = models.CharField(max_length=200, default=1)

	class Meta:
		verbose_name_plural = "Categories"
	def __str__(self):
		return self.puzzle_category




class Puzzle(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	puzzleDesiredOutput = models.TextField(max_length=500, default='')
	published = models.DateTimeField("date published", default=datetime.now())

	puzzle_slug = models.CharField(max_length=200, default=1)
	puzzle_category = models.ForeignKey(Difficulty, default=1, verbose_name="Difficulty", on_delete=models.CASCADE)
	
	functionName = models.CharField(max_length=200, default=0)
	puzzleSolution = models.TextField(max_length=500, default='')
	solvers = models.ManyToManyField(User, related_name="Solves")
	
	hint = models.TextField(max_length=200, default='')
	starterCode = models.TextField(max_length=200, default='')
	testCases = models.TextField(max_length=300, default='')
	xps = models.IntegerField(default=0)

	hasDone = models.BooleanField(default=0)


	
	def __str__(self):
		return self.title
