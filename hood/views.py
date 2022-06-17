from django.shortcuts import render, HttpResponse

def home(request):

    return render(request, 'app/home.html')