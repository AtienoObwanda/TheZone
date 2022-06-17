from django.shortcuts import render

def register(request):
    return render(request, 'members/register.html') 

def profile(request):
    return render(request, 'members/profile.html') 

