from django.urls import path

from . import views

urlpatterns = [
	# standart
	path('', views.HomePageView.as_view(), name='home'),
	path('about-us/', views.AboutUsView.as_view(), name='about'),
	path('gallery_product/', views.GalleryProducts.as_view(), name='gallery_product'),

	# auth
	path('login/', views.MyProjectLoginView.as_view(), name='login_page'),
	path('register/', views.RegisterUserView.as_view(), name='register_page'),
	path('logout', views.MyProjectLogoutView.as_view(), name='logout'),

	# profile
	path('fill_profile/', views.FillProfile, name='fillprofile'),
	path('profile/', views.Profile.as_view(), name='profile'),
	path('update_profile/', views.UpdateProfileView, name='update_profile'),

	#sport products
	path('sport_product_add/', views.sport_product_add, name='sport_product_add')
]
