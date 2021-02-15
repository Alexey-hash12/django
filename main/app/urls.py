from django.urls import path

from . import views

urlpatterns = [
	path('', views.HomePageView.as_view(), name='home'),
	path('about-us/', views.AboutUsView.as_view(), name='about'),

	path('login/', views.MyProjectLoginView.as_view(), name='login_page'),
	path('register/', views.RegisterUserView.as_view(), name='register_page'),
	path('logout', views.MyProjectLogoutView.as_view(), name='logout'),

	path('fill_profile/', views.FillProfile, name='fillprofile'),
	path('profile/', views.Profile.as_view(), name='profile'),

]
