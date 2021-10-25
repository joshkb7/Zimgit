from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home'),
    path('details/', views.details, name='details'),
    path('creators/', views.creators, name='creators'),
    path('use_cases/', views.use_cases, name='use_cases'),
    path('libraries/', views.ProductListView.as_view(), name='libraries'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
]