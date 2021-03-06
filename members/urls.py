from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views
from members.views import addBizz, addHood, addHosp, addNewHood, addPost, addSchl, addStation, exitHood


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='members/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('join-hood/', views.getStarted, name='joinhood'),
    path('dashboard/hood/<int:pk>/joined', addHood.as_view(), name='activeHood'),
    path('dashboard/',views.hoodHome, name='dashboard'),
    path('dashboard/hood/<int:pk>/exit', exitHood.as_view(), name='exitHood'),
    path('add-post/', addPost.as_view(), name='addPost'),
    path('add-business/', addBizz.as_view(), name='addBizz'),
    path('add-school/', addSchl.as_view(), name='addSchl'),
    path('add-hospital/', addHosp.as_view(), name='addHosp'),
    path('add-station/', addStation.as_view(), name='addStation'),
    path('add-hood/', addNewHood.as_view(), name='addHood'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)