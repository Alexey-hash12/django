from django.db import models
from django.contrib.auth.models import User

class UserBlog(models.Model):
	''' User Blog Content '''
	title = models.CharField(max_length=150)
	auth_user = models.ForeignKey(User, on_delete=models.CASCADE)
	poster = models.ImageField(upload_to='images/', null=True)
	intro = models.TextField()
	date = models.DateTimeField(auto_now=True)
	slug = models.SlugField(null=True)

	def __str__(self):
		return self.title