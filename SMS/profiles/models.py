from django.db import models
from django.contrib.auth.models import User
from .utils import get_random_code
from django.template.defaultfilters import slugify

# Create your models here.


class Profile(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	email = models.EmailField(max_length=200)
	avatar = models.ImageField(default='chicken.jpg', upload_to='avatars/')

	updated = models.DateTimeField(auto_now = True)
	created = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return f"{self.user.username}--{self.created}"





