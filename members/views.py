from django.shortcuts import redirect, get_object_or_404, render
from .forms import *

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
    return render(request, 'members/register.html') 

def profile(request):
    
    return render(request, 'members/profile.html') 

