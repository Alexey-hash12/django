from django.db import models
from django.contrib.auth.models import User


class User_Gl(models.Model):
	name = models.CharField(max_length=300)
	sername = models.CharField(max_length=300)
	othername = models.CharField(max_length=300)
	age = models.IntegerField()
	adress = models.CharField(max_length=300)
	poster = models.ImageField(upload_to = 'poster/')
class Trener(models.Model):
	poster = ForeignKey(poster,on_delete =SET_NULL)
	staj = IntegerField()
	salary = IntegerField()
	time_work = models.TimeField()
	name = ForeignKey(User_Gl,on_delete = CASCADE)
	sername = ForeignKey(User_Gl,on_delete = CASCADE)
	othername = ForeignKey(User_Gl,on_delete = CASCADE)
	age = ForeignKey(User_Gl,on_delete = CASCADE)
	adress = ForeignKey(User_Gl,on_delete = CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	def __str__(self):
		return f'{self.name} {self.sername}'
class User(models.Model):
	poster = ForeignKey(poster,on_delete = SET_NULL)
	name = ForeignKey(User_Gl,on_delete = CASCADE)
	sername = ForeignKey(User_Gl,on_delete = CASCADE)
	othername = ForeignKey(User_Gl,on_delete = CASCADE)
	age = ForeignKey(User_Gl,on_delete = CASCADE)
	adress = ForeignKey(User_Gl,on_delete = CASCADE)
	weight = IntegerField()
	height = IntegerField()
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	def __str__(self):
		return f'{self.name} {self.sername}'