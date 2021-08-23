from django.contrib import admin
from .models import Puzzle, Difficulty
from tinymce.widgets import TinyMCE
from django.db import models


# Register your models here.
"""
class CourseAdmin(admin.ModelAdmin):
	formfield_overrides = {
		'content': {'widget': TinyMCE()}
	}

"""

admin.site.register(Difficulty)
admin.site.register(Puzzle) #CourseAdmin
