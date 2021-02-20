from django.shortcuts import render, redirect
from .tasks import spam_message
from .forms import AuthUserForm, ProfileForm, RegisterUserForm, TrenerForm, ClientForm, SportProductsForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.views.generic import ListView
from django.contrib.auth import authenticate, login
from .models import Profile, Trener, Client, SportProducts
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.conf import settings
# redis
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT

from django.contrib import messages

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

''' Main views '''
# Home Page
class HomePageView(View):
    def get(self, request):
        # spam_message('alexryzhak238@gmail.com')
        return render(request, 'main/index.html')

# About us Page
class AboutUsView(View):
    def get(self, request):
        return render(request, 'main/about-us.html')

class GalleryProducts(View):
    def get(self, request):
        if cache.get("product"):
            sport_product = cache.get("product")
        else:
            sport_product = SportProducts.objects.all()
            cache.set("product", sport_product)
        return render(request, 'main/gallery_product.html', {'sport_product': sport_product})
''''''


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
def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user and user.is_active:
                form.add_error(None, 'This username is already exits')
                return render(request, 'auth/register.html', {'form': form})
            else:
                user = form.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('fillprofile')
        else:
            return render(request, 'auth/register.html', {'form': form})
    else:
        return render(request, 'auth/register.html', {'form': RegisterUserForm()})

@login_required()
def FillProfile(request):
    if request.GET.get("profile-form") == 'trener':
        if request.method == 'POST':
            trener = Trener(profile=request.user.profile)

            if request.method == 'POST':
                form = TrenerForm(request.POST,request.FILES ,instance=trener)
                print(form)
                if form.is_valid():
                    f = request.user.profile
                    f.is_trener = True
                    f.save()
                    form.save()
                    return redirect('profile')
            else:
                form = TrenerForm(instance=profile)
        return render(request, 'auth/fill_trener_profile.html')

    if request.GET.get("profile-form") == 'pupils':
        if request.method == 'POST':
            client = Client(profile=request.user.profile)

            if request.method == 'POST':
                form = ClientForm(request.POST,request.FILES ,instance=client)
                print(form)
                if form.is_valid():
                    f = request.user.profile
                    f.is_client = True
                    f.save()
                    form.save()
                    return redirect('profile')
            else:
                form = ClientForm(instance=client)
        return render(request, 'auth/fill_pupils_profile.html')
    else:
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
                    return redirect('profile')
                else:
                    form.add_error(None, 'Form is not valid, check please email address and poster')
                    return render(request, 'auth/fillprofile.html', {'form': form})
            else:
                form = ProfileForm(instance=profile)
        return render(request, 'auth/fillprofile.html')

def UpdateProfileView(request):
    if request.method == 'POST':
        try:
            profile = request.user.profile
        except UserProfile.DoesNotExist:
            profile = Profile(user=request.user)

        if request.method == 'POST':
            form = ProfileForm(request.POST,request.FILES ,instance=profile)
            if form.is_valid():
                form.save()
                return redirect('profile')
            else:
                form.add_error(None, 'Form is not valid, check please email address and poster')
                return render(request, 'auth/update_profile.html', {'form': form})
        else:
            form = ProfileForm(instance=profile)
    else:
        return  render(request, 'auth/update_profile.html')


class Profile(View):
    def get(self, request):
        return render(request, 'auth/profile.html')
''''''


''' Sport Products '''
def sport_product_add(request):
    if request.method == "POST":
        form = SportProductsForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('profile')
        else:
            messages.error(request, 'Please, fix this errors:')
            return render(request, 'sport_prod\sport_add.html', {'form':form})
    else:
        form = SportProductsForm()
        return render(request, 'sport_prod\sport_add.html', {'form':form})

#
# ''' Blog '''
# class BlogView(ListView):
#
