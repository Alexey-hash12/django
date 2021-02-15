from django.shortcuts import render, redirect
from .tasks import spam_message
from .forms import AuthUserForm, ProfileForm, RegisterUserForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from .models import Profile
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View

def index(request):
    # spam_message('alexryzhak238@gmail.com')
    return render(request, 'main/index.html')


''' Auth Views '''
# Login
class MyProjectLoginView(LoginView):
	template_name = 'auth/login.html'
	form_class = AuthUserForm
	success_url = reverse_lazy('home')

	def get_success_url(self):
		return self.success_url

#logout
class MyProjectLogoutView(LogoutView):
	next_page = reverse_lazy('home')

#Registration
class RegisterUserView(CreateView):
    model = User
    template_name = 'auth/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('fillprofile')
    success_msg = 'Пользователь создан'

    def form_invalid(self, form):
	    """If the form is invalid, render the invalid form."""
	    return redirect('valid_error')

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid


@login_required()
def FillProfile(request):
    if request.method == 'POST':
        try:
            profile = request.user.profile
        except UserProfile.DoesNotExist:
            profile = Profile(user=request.user)

        if request.method == 'POST':
            form = ProfileForm(request.POST,request.FILES ,instance=profile)
            print(form)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = ProfileForm(instance=profile)
    return render(request, 'auth/fillprofile.html')

class Profile(View):
    def get(self, request):
        return render(request, 'auth/profile.html')
''''''
