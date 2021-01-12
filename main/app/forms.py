from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import UserBlog

class LoginForm(AuthenticationForm, forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password')

class RegisterUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password')

	def save(self, commit=True):			
		user = super().save(commit=False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user	

class UserBlogForm(forms.ModelForm):
	class Meta:
		model = UserBlog
		fields = ('title', 'poster', 'intro')		