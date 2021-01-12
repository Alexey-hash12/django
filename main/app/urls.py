from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about-us/', views.about, name='about-us'),
    path('contact/', views.contact, name='contact'),

    path('blog_article_list/<slug:slug>/', views.BlogListView.as_view(), name='blog_article_list'),
    path('blog-article/', views.blogaddlist, name='add'),
    path('blog_article_list/add', views.BlogAddView, name='add_view'),

    path('login/', views.LoginUserView.as_view(), name='login'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('logout', views.LogoutView.as_view(), name='logout'),	
]
