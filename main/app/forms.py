from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile, Trener, Client, SportProducts

# Captcha
from captcha.fields import CaptchaField

''' Authorization and Registration Forms '''
class AuthUserForm(AuthenticationForm, forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password')

class RegisterUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password')
	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('face', 'intro', 'email', 'age', 'last_name', 'first_name')

class TrenerForm(forms.ModelForm):
	class Meta:
		model = Trener
		fields = ('staj', 'salary', 'time_work')

class ClientForm(forms.ModelForm):
	class Meta:
		model = Client
		fields = ('weight', 'height',)
''''''

''' Sport Products '''
class SportProductsForm(forms.ModelForm):
	captcha = CaptchaField()

	class Meta:
		model = SportProducts
		fields = ("title", "price", "poster","intro")
