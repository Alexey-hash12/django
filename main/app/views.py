from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import LoginForm, RegisterUserForm, UserBlogForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import UserBlog
from django.views.generic.list import ListView
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(ListView):
	model = UserBlog
	paginate_by = 10
	def get_context_data(self, **kwargs):
		kwargs['blog_article'] = UserBlog.objects.all()
		context = super().get_context_data(**kwargs)
		return context

def about(request):
	return render(request, 'about.html')

def blogaddlist(request):
	context = {}
	context['form'] = UserBlogForm
	return render(request, 'blogview.html', context)


def contact(request):
	return render(request, 'contact.html')


class BlogListView(View):
	def get(self, request, slug):
		blog_article_list = UserBlog.objects.filter(title=slug)
		return render(request, 'blog_article_list.html', {'blog_article_list': blog_article_list})


class LoginUserView(LoginView):
	template_name = 'login.html'
	form_class = LoginForm
	success_url = reverse_lazy('home')	

	def get_success_url(self):
		return self.success_url


class RegisterUserView(CreateView):
	model = User	
	template_name = 'register.html'
	form_class = RegisterUserForm
	success_url = reverse_lazy('home')

	def form_valid(self, form):
		form_valid = super().form_valid(form)
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		email = form.cleaned_data['email']
		aut_user = authenticate(username=username, password=password, email=email)
		login(self.request, aut_user)
		return form_valid


class LogoutView(LogoutView):
	next_page = reverse_lazy('home')		

def BlogAddView(request):
	if request.method == 'POST':
		form = UserBlogForm(request.POST, request.FILES)
		if form.is_valid():
			f = form.save(commit=False)
			f.auth_user = request.user
			f.save()
			return redirect('/')
# class BlogListAddView(LoginRequiredMixin, CreateView):
# 	model = UserBlog
# 	form_class = UserBlogForm
# 	template_name = 'blog_list_add_view.html'
# 	login_url = 'login/'
# 	success_url = reverse_lazy('home')

# 	def form_valid(self, form):
# 		self.objects = form.save(commit=False)
# 		self.objects.auth_user = self.request.user
# 		self.objects.save()
# 		return super().form_valid(form)
