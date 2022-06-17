from dataclasses import fields
from statistics import mode
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}), max_length=50, required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields=['username','email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # fields = "__all__"
        exclude = ['user']


class UpdateZoneForm(forms.ModelForm):
    model = UserProfile
    fields = ['zone']






    #  exclude = ['user', 'post_date']