from django.shortcuts import redirect, get_object_or_404, render
from .forms import *
from .models import UserProfile
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import View
from hood.models import *


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




# update profile
def profile(request):
   
    
    return render(request, 'members/profile.html') 


def getStarted(request):
    hoods = hood.objects.all()

    return render(request, 'django_registration/registration_complete.html', {'hoods':hoods})


# view account
class AccountView(LoginRequiredMixin,View):
    def get(self, request, pk, *args, **kwargs):
     
     


        return render(request, 'members/dashboard.html')

      
# select hood
class HoodView(LoginRequiredMixin,View):
    def get(self, request, pk,  *args, **kwargs):
       
       
        
        
        
        return render(request, 'members/hood.html') 
            
        