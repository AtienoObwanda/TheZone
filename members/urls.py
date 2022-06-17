from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from members.views import AccountView, HoodView


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='members/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('dashboard/<int:pk>/', AccountView.as_view(), name='dashboard'),
    path('hood/<int:pk>/', HoodView.as_view, name='hood'),


]
