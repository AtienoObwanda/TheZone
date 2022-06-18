from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from members.views import AccountView, addHood, exitHood


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='members/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('join-hood/', views.getStarted, name='joinhood'),
    path('dashboard/hood/<int:pk>/joined', addHood.as_view(), name='activeHood'),
    # path('dashboard/joined-hood/<int:pk>/', views.joinHood, name='activeHood'),
    path('dashboard/',views.hoodHome, name='dashboard'),
    path('dashboard/hood/<int:pk>/exit', exitHood.as_view(), name='exitHood'),


]
