from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import Profile
class UserRegisterationForm(UserCreationForm):
    email = forms.EmailField()
    def __init__(self, *args, **kwargs):
        super( UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username','email','first_name','last_name','password1','password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email',]
              
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        