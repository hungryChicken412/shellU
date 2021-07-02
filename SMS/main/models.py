from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

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
	published = models.DateTimeField("date published", default=datetime.now())
	puzzle_slug = models.CharField(max_length=200, default=1)
	puzzle_category = models.ForeignKey(Difficulty, default=1, verbose_name="Difficulty", on_delete=models.CASCADE)
	answer = models.CharField(max_length=200, default=0)


	
	def __str__(self):
		return self.title



class PuzzleSolution(models.Model):
	puzzle = models.OneToOneField(Puzzle, on_delete=models.CASCADE)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add = True)
	content = models.TextField(null=True)

	def __str__(self):
		return f"{self.user.username}--{self.puzzle.title}"

