from audioop import add
from dis import dis
from multiprocessing.dummy import active_children
from django.shortcuts import redirect, get_object_or_404, render
from .forms import *
from .models import UserProfile
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import View
from django.views.generic import DeleteView, ListView, UpdateView,DetailView, CreateView

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



class addHood(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        joinedHood = hood.objects.get(pk=pk)
        if request.user.profile.zone == None:
            request.user.profile.zone = joinedHood
            request.user.profile.save()
        return redirect('dashboard')

class exitHood(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        request.user.profile.zone = None
        request.user.profile.save()
        return redirect('joinhood')       


def hoodHome(request):
    joinedHood = request.user.profile.zone
    schls = school.objects.filter(zone=joinedHood.id).all() #  Fetch all Schools in the joined zone
    hosps = hospital.objects.filter(zone=joinedHood.id).all() #  Fetch all Hospitals in the joined zone
    stations = policeStation.objects.filter(zone=joinedHood.id).all() # Fetch all police stations in the joined zone
    bizs = business.objects.filter(zone=joinedHood.id).all() # Fetch all businesses in the joined zone
    posts = Post.objects.filter(zone=joinedHood.id).all() #  Fetch all posts in the joined zone
    if joinedHood == None:
        return redirect('joinHood')
    else:
        displayedHood = hood.objects.get(id=joinedHood.id)
        
        return render(request, 'members/hood.html', {'hood':displayedHood, 'posts':posts,'hosps': hosps,'stations':stations, 'bizs':bizs,'schls':schls})


class addPost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'post']
    template_name = 'members/addPost.html'
    def form_valid(self, form):
        form.instance.author=self.request.user
        form.instance.zone = self.request.user.profile.zone
        return super().form_valid(form)


class addBizz(LoginRequiredMixin, CreateView):
    model = business
    fields = ['bizName','email','contact']
    template_name = 'members/addPost.html'
    def form_valid(self, form):
        form.instance.owner=self.request.user
        form.instance.zone = self.request.user.profile.zone
        return super().form_valid(form)


class addSchl(LoginRequiredMixin, CreateView):
    model = school
    fields = ['schlName','teachersNum','studentsNum','email','contact']
    template_name = 'members/addSchl.html'
    def form_valid(self, form):
        form.instance.owner=self.request.user
        form.instance.zone = self.request.user.profile.zone
        return super().form_valid(form)

class addHosp(LoginRequiredMixin, CreateView):
    model = hospital
    fields = ['hName','doctorsNum','nursesNum','email','contact']
    template_name = 'members/addHosp.html'
    def form_valid(self, form):
        form.instance.owner=self.request.user
        form.instance.zone = self.request.user.profile.zone
        return super().form_valid(form)


class addStation(LoginRequiredMixin, CreateView):
    model = policeStation
    fields = ['stationName','officers','email','contact']
    template_name = 'members/addStation.html'
    def form_valid(self, form):
        form.instance.owner=self.request.user
        form.instance.zone = self.request.user.profile.zone
        return super().form_valid(form)



# view account

      

            
        