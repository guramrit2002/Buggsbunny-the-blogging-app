# import form class from django
from django import forms
from .models import *

class PostCreateForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = "__all__"