from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
	first_name = models.CharField(max_length=50, null=True, blank=True)
	last_name = models.CharField(max_length=50, null=True, blank=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	face = models.ImageField(upload_to='user_faces/', null=True)
	intro = models.TextField(null=True)
	email = models.EmailField(null=True, blank=True)
	age = models.IntegerField(default=18, null=True, blank=True)
	is_trener = models.BooleanField(null=True, default=False)
	is_client = models.BooleanField(null=True, default=False)

	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

class Trener(models.Model):
	staj = models.CharField(max_length=10)
	salary = models.IntegerField()
	time_work = models.IntegerField()
	profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.staj} {self.salary}'

class Client(models.Model):
	profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
	weight = models.IntegerField()
	height = models.IntegerField()

	def __str__(self):
		return f'{self.weight} {self.height}'
#
# @receiver(post_save, sender=Profile)
# def create_user_profile_trener(sender, instance, created, **kwargs):
# 	if created:
# 		Trener.objects.create(user=instance)
#
#
# @receiver(post_save, sender=Profile)
# def save_user_profile_trener(sender, instance, **kwargs):
# 	instance.trener.save()
