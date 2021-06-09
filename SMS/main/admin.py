from django.contrib import admin
from .models import Course, CourseSeries, CourseCategory
from tinymce.widgets import TinyMCE
from django.db import models


# Register your models here.

class CourseAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
	}


admin.site.register(CourseSeries)
admin.site.register(CourseCategory)

admin.site.register(Course, CourseAdmin)
