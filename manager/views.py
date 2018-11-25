from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User
from django.db import transaction
from django.http import JsonResponse
from message_core.models import UserProfile
from message_core.views import get_message_common_data, forward_superuser, build_message
from message_core.models import CustMessage
from message_core.forms import MessageModelForm as MessageForm, SearchForm
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
            return redirect(reverse('user_list'), args=[])
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    context['user_form'] = user_form
    context['profile_form'] = profile_form
    return render(request, 'manager/add_user.html', context)


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


def change_user(request):
    user_id = request.GET.get('user_id')
    user_status = request.GET.get('user_status')
    user_profile = UserProfile.objects.get(user_id=user_id)
    if user_status == '1':
        user_profile.user_status = 0
    else:
        user_profile.user_status = 1
    user_profile.save()
    data = {'status': 'SUCCESS'}
    return JsonResponse(data)


def delete_user(request):
    user_id = request.GET.get('user_id')
    user = User.objects.get(pk=user_id)
    user.delete()
    data = {'status': 'SUCCESS'}
    return JsonResponse(data)


def show_message(request):
    user = request.user
    if not user.is_authenticated or not user.is_superuser:
        return forward_superuser(request)
    message_list = CustMessage.objects.exclude(message_status=0)
    context = get_message_common_data(message_list, request)
    context['message_title'] = '查看全部资源'
    context['no_message_tip'] = '暂无资源'
    return render(request, 'manager/message.html', context)


def show_message_by_user(request, user_pk):
    user = request.user
    if not user.is_authenticated or not user.is_superuser:
        return forward_superuser(request)
    source_user = UserProfile.objects.get(user_id=user_pk)
    message_list = CustMessage.objects.filter(follow_user=source_user).exclude(message_status=0)
    context = get_message_common_data(message_list, request)
    context['message_title'] = '查看' + source_user.user.username + '全部资源'
    context['no_message_tip'] = source_user.user.username + '暂无资源'
    return render(request, 'manager/message.html', context)


def show_complete(request):
    user = request.user
    if not user.is_authenticated or not user.is_superuser:
        return forward_superuser(request)
    message_list = CustMessage.objects.filter(type=3)
    context = get_message_common_data(message_list, request)
    context['message_title'] = '查看全部已完成留言'
    context['no_message_tip'] = '暂无已完成留言'
    return render(request, 'manager/message.html', context)


def show_complete_by_user(request, user_pk):
    user = request.user
    if not user.is_authenticated or not user.is_superuser:
        return forward_superuser(request)
    source_user = UserProfile.objects.get(user_id=user_pk)
    message_list = CustMessage.objects.filter(follow_user=source_user, type=3).exclude(message_status=0)
    context = get_message_common_data(message_list, request)
    context['message_title'] = '查看' + source_user.user.username + '已完成留言'
    context['no_message_tip'] = source_user.user.username + '暂无已完成留言'
    return render(request, 'manager/message.html', context)


# 逻辑删除或者恢复
def change_status(request):
    message_id = request.GET.get('message_id')
    message_status = request.GET.get('message_status')
    message = CustMessage.objects.get(pk=message_id)
    if message_status == '0':
        message.message_status = 1
    else:
        message.message_status = 0
    message.save()
    data = {'status': 'SUCCESS'}
    return JsonResponse(data)


def del_message(request):
    message_id = request.GET.get('message_id')
    message = CustMessage.objects.get(pk=message_id)
    message.delete()
    data = {'status': 'SUCCESS'}
    return JsonResponse(data)


def show_trush(request):
    user = request.user
    if not user.is_authenticated or not user.is_superuser:
        return forward_superuser(request)
    message_list = CustMessage.objects.filter(message_status=0)
    context = get_message_common_data(message_list, request)
    context['message_title'] = '查看回收站资源'
    context['no_message_tip'] = '回收站暂无资源'
    return render(request, 'manager/message.html', context)


def show_by_user(request):
    user_list = User.objects.filter(is_active=True, is_superuser=False)
    context = {'user_list': user_list}
    return render(request, 'manager/message_by_user.html', context)


def complete_change(request):
    object_id = request.GET.get('object_id')
    is_completed = request.GET.get('is_completed')
    message = CustMessage.objects.get(pk=object_id)
    cur_type = message.type
    if is_completed != 'true':
        message.type = 3
    else:
        message.type = message.last_type
    if message.type != cur_type:
        message.last_type = cur_type
    message.save()
    data = {'status': 'SUCCESS'}
    return JsonResponse(data)


def dispatch_message(request):
    context = {}
    if request.method == 'POST':
        message_form = MessageForm(request.POST, user=request.user)
        if message_form.is_valid():
            user_id = int(request.POST['follow_user_id'])
            user_profile = UserProfile.objects.get(user_id=user_id)
            cust_message = CustMessage()
            build_message(cust_message, message_form)
            # 添加默认为正常留言
            cust_message.type = 1
            # 添加才需设置手机号
            cust_message.cust_mobile = message_form.cleaned_data['cust_mobile']
            cust_message.follow_user = user_profile
            cust_message.save()
            return redirect(reverse('show_all'), args=[])
    else:
        message_form = MessageForm()
        user_list = User.objects.filter(is_active=True, is_superuser=False)
        context['message_form'] = message_form
        context['user_list'] = user_list
    return render(request, 'manager/dispatch_message.html', context)


def search_message(request):
    context = {}
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            search_text = search_form.cleaned_data['search_text']
            message_list = CustMessage.objects.filter(cust_mobile=search_text)
            if not message_list:
                message_list = CustMessage.objects.filter(cust_name=search_text)
            context = get_message_common_data(message_list, request)
            context['message_title'] = '留言搜索结果'
            context['no_message_tip'] = '未搜索到留言'
            return render(request, 'manager/message.html', context)
    search_form = SearchForm()
    context['search_form'] = search_form
    return render(request, 'manager/search_message.html', context)