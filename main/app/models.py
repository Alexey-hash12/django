# from django.db import models
# from django.contrib.auth.models import User
#
#
# class User_Gl(models.Model):
# 	name = models.CharField(max_length=300)
# 	sername = models.CharField(max_length=300)
# 	othername = models.CharField(max_length=300)
# 	age = models.IntegerField()
# 	adress = models.CharField(max_length=300)
# 	poster = models.ImageField(upload_to = 'poster/')
#
# class Trener(models.Model):
# 	staj = models.IntegerField()
# 	salary = models.IntegerField()
# 	time_work = models.TimeField()
# 	profile = models.OneToOneField(User_Gl)
# 	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
# 	def __str__(self):
# 		return f'{self.name} {self.sername}'
#
# class User(models.Model):
# 	poster = models.ForeignKey(User_Gl,on_delete = models.SET_NULL)
# 	name = models.ForeignKey(User_Gl,on_delete = models.CASCADE)
# 	sername = models.ForeignKey(User_Gl,on_delete = models.CASCADE)
# 	othername = models.ForeignKey(User_Gl,on_delete = models.CASCADE)
# 	age = models.ForeignKey(User_Gl,on_delete = models.CASCADE)
# 	adress = models.ForeignKey(User_Gl,on_delete = models.CASCADE)
# 	weight = models.IntegerField()
# 	height = models.IntegerField()
# 	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
# 	def __str__(self):
# 		return f'{self.name} {self.sername}'
