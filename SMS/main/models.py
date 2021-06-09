from django.db import models
from datetime import datetime

# Create your models here.




class CourseCategory(models.Model):
	course_category = models.CharField(max_length=200)
	category_summary = models.CharField(max_length=200)
	category_slug = models.CharField(max_length=200, default=1)

	class Meta:
		verbose_name_plural = "Categories"
	def __str__(self):
		return self.course_category



class CourseSeries(models.Model):
	course_series = models.CharField(max_length=200)
	course_category = models.ForeignKey(CourseCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
	course_summary = models.CharField(max_length=200)


	class Meta:
		verbose_name_plural = "Series"
	def __str__(self):
		return self.course_series



class Course(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	published = models.DateTimeField("date published", default=datetime.now())

	course_series = models.ForeignKey(CourseSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
	course_slug = models.CharField(max_length=200, default=1)


	def __str__(self):
		return self.title




                



