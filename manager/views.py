from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User
from django.db import transaction
from django.http import JsonResponse
from message_core.models import UserProfile
from .forms import ManagerLoginForm, UserForm, ProfileForm


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


@transaction.atomic
def add_user(request):
    context = {}
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = User.objects.create()
            user.username = user_form.cleaned_data['username']
            user.set_password(user_form.cleaned_data['password'])
            user_profile = UserProfile()
            user_profile.user_num = profile_form.cleaned_data['user_num']
            user_profile.user = user
            user.save()
            user_profile.save()
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    context['user_form'] = user_form
    context['profile_form'] = profile_form
    return render(request, 'manager/add_user.html', context)


def modify_user_pwd(request):
    if request.method == 'POST':
        pass
    else:
        user_id = request.GET.get('user_pk', 0)
        cur_user = User.objects.get(pk=user_id)
        if cur_user is None:
            pass


def show_user_list(request):
    user_list = User.objects.filter(is_active=True, is_superuser=False)
    context = {'user_list': user_list}
    return render(request, 'manager/user_list.html', context)


def modify_user_pwd(request):
    user_id = request.POST['modify_user_id']
    user_pwd = request.POST['user_pwd_new']
    user = User.objects.get(pk=user_id)
    user.set_password(user_pwd)
    user.save()
    data = {'status': 'SUCCESS'}
    return JsonResponse(data)
