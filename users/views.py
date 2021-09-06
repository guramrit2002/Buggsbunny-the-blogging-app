from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import UserRegisterationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from blogs.models import Post

def register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            print('TRUE')
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,'you have account has been created !!you are now able to log in ')
            return redirect('Blog-login')
        else:
            print('FALSE')
    else:
        form = UserRegisterationForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,instance=request.user.profile)
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'your account has been updated ')
            return redirect('Blog-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'users/profile.html',context)