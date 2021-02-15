from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	age = models.IntegerField()
	adress = models.CharField(max_length=300)
	poster = models.ImageField(upload_to = 'poster/')
	email = models.EmailField()
	name = models.CharField(max_length=20)
	surname = models.CharField(max_length=20)

	def __str__(self):
		return "Profile"

class Trener(models.Model):
	staj = models.IntegerField()
	salary = models.IntegerField()
	time_work = models.TimeField()
	profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	def __str__(self):
		return f'{self.name} {self.sername}'


class Client(models.Model):
	profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
	weight = models.IntegerField()
	height = models.IntegerField()
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	def __str__(self):
		return f'{self.name} {self.sername}'
