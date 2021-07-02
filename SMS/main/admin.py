from django.contrib import admin
from .models import Puzzle, Difficulty, PuzzleSolution
from tinymce.widgets import TinyMCE
from django.db import models


# Register your models here.

class CourseAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
	}



admin.site.register(Difficulty)
admin.site.register(PuzzleSolution)
admin.site.register(Puzzle, CourseAdmin)
