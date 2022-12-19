from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from .import forms
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('inventoryApp:index')
    else:
        form = CreateUserForm()
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)
def userprofile(request):
    return render(request, 'user/profile.html')

def userprofile_update(request):
    if request.method == 'POST':
        u_form =forms.UserUpdateForm(request.POST, instance=request.user)
        p_form =forms.ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('UserApp:userprofile')
    else:
        u_form =forms.UserUpdateForm(instance=request.user)
        p_form =forms.ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'user/profile_update.html', context)

