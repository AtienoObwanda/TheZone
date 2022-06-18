from multiprocessing.dummy import active_children
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
            return redirect('joinhood')
    else:
        form = UserRegistrationForm()
    return render(request, 'members/register.html', {'form': form}) 

def getStarted(request):
    hoods = hood.objects.all()

    return render(request, 'django_registration/registration_complete.html', {'hoods':hoods})


# def joinHood(request, pk):
#     joinedHood = hood.objects.get(pk=pk)
#     if request.user.profile.zone == None:
#         request.user.profile.zone = joinedHood
#         request.user.profile.save()
#         return redirect('home')
#     else:
#         return redirect('joinhood')


class addHood(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        joinedHood = hood.objects.get(pk=pk)
        if request.user.profile.zone == None:
            request.user.profile.zone = joinedHood
            request.user.profile.save()
        return redirect('dashboard')
        


def hoodHome(request):
    current_hood = request.user.profile.zone
    if current_hood == None:
        return redirect('joinHood')
    else:
        showing = hood.objects.get(id=current_hood.id)
        return render(request, 'members/hood.html', {'hood':showing})






# update profile
def profile(request):
   
    
    return render(request, 'members/profile.html') 

# view account
class AccountView(LoginRequiredMixin,View):
    def get(self, request, pk, *args, **kwargs):
     
     


        return render(request, 'members/dashboard.html')

      

            
        