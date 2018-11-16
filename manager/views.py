from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth
from .forms import ManagerLoginForm


# Create your views here.


def manager(request):
    user = request.user
    if not user.is_authenticated or not user.is_superuser:
        return redirect(reverse('to_manage'), args=[])
    return render(request, 'manager/manager.html', {})


def to_manage(request):
    if request.method == 'POST':
        login_form = ManagerLoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(reverse('manager'), args=[])
    else:
        login_form = ManagerLoginForm()
    context = {'login_form': login_form}
    return render(request, 'manager/login.html', context)
