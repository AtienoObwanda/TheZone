from django.shortcuts import redirect, get_object_or_404, render
from .forms import *
from .models import UserProfile
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import View


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            form.save()
            # send_welcome_email(username,email)
            # HttpResponseRedirect('login')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'members/register.html', {'form': form}) 





def profile(request):
    
    return render(request, 'members/profile.html') 

class AccountView(LoginRequiredMixin,View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        zone = profile.zone.all()
        if zone is None:
            return render(request, 'members/dashboard.html', {'profile': profile, 'zone': zone, 'profile' : profile})

            
        else: redirect('profile')

class HoodView(LoginRequiredMixin,View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        zone = profile.zone.all()
        if zone:
            return render('dashboard')
        else: return render(request, 'members/profile.html', {'user':user})