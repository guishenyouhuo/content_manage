from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User
from django.db import transaction
from django.http import JsonResponse
from .models import AutoMessage, MsgTemplate, TagMapping
from message_core.models import UserProfile
from message_core.views import get_message_common_data, forward_superuser, build_message
from message_core.models import CustMessage
from message_core.forms import MessageModelForm as MessageForm
from .forms import ManagerLoginForm, UserForm, ProfileForm, MsgTemplateForm, TagMappingForm


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
    user_list = User.objects.filter(is_active=True, is_superuser=False, userprofile__user_status=1)
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
            auto_config = AutoMessage()
            follow_user_id = request.POST['follow_user_id']
            if follow_user_id == 'auto':
                auto_config = AutoMessage.objects.all()[0]
                user_list = User.objects.filter(is_active=True, is_superuser=False, userprofile__user_status=1)
                index = 0
                while index < user_list.count():
                    if user_list[index].pk == auto_config.cur_user.user_id:
                        break
                    index += 1
                index += 1
                # 默认取第一个(包含当前是最后一个或者没有当前用户)
                user_id = user_list[0].pk
                # 如果还在列表范围内，取index位置用户
                if index < user_list.count():
                    user_id = user_list[index].pk
            else:
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
            # 如果是自动分配，需要更新当前用户
            if follow_user_id == 'auto':
                auto_config.cur_user = user_profile
                auto_config.save()
            return redirect(reverse('show_all'), args=[])
    else:
        message_form = MessageForm()
        user_list = User.objects.filter(is_active=True, is_superuser=False, userprofile__user_status=1)
        context['message_form'] = message_form
        context['user_list'] = user_list
    return render(request, 'manager/dispatch_message.html', context)


def search_message(request):
    context = {}
    if request.method == 'POST':
        search_text = request.POST['search_text']
        message_list = CustMessage.objects.filter(cust_mobile=search_text)
        if not message_list:
            message_list = CustMessage.objects.filter(cust_name=search_text)
        context = get_message_common_data(message_list, request)
        context['message_title'] = '留言搜索结果'
        context['no_message_tip'] = '未搜索到留言'
        return render(request, 'manager/message.html', context)
    return render(request, 'manager/search_message.html', context)


def auto_message(request):
    context = {}
    auto_config = None
    if AutoMessage.objects.exists():
        auto_config = AutoMessage.objects.all()[0]
        context['auto_config'] = auto_config
    user_list = User.objects.filter(is_active=True, is_superuser=False, userprofile__user_status=1)
    context['user_list'] = user_list
    if request.method == 'POST':
        sel_user_id = int(request.POST['cur_user_id'])
        sel_user = UserProfile.objects.get(user_id=sel_user_id)
        if auto_config is None:
            auto_config = AutoMessage()
        auto_config.cur_user = sel_user
        auto_config.save()
        context['auto_config'] = auto_config
    return render(request, 'manager/auto_message.html', context)


def import_message(request):
    context = {}
    user_list = User.objects.filter(is_active=True, is_superuser=False, userprofile__user_status=1)
    tag_list = TagMapping.objects.all()
    context['user_list'] = user_list
    context['source_tag_list'] = tag_list
    return render(request, 'manager/import_message.html', context)


def add_template(request):
    context = {}
    if request.method == 'POST':
        template_form = MsgTemplateForm(request.POST)
        if template_form.is_valid():
            template = MsgTemplate()
            template.template_key = template_form.cleaned_data['template_key']
            has_first_line = request.POST.get('has_first_line')
            if has_first_line is None:
                template.has_firstline = False
            template.col_mobilephone = template_form.cleaned_data['col_mobilephone']
            template.col_username = template_form.cleaned_data['col_username']
            template.col_address = template_form.cleaned_data['col_address']
            template.col_message = template_form.cleaned_data['col_message']
            template.save()
            return redirect(reverse('add_tag'), args=[])
    else:
        template_form = MsgTemplateForm()
    context['template_form'] = template_form
    return render(request, 'manager/add_template.html', context)


def add_tag(request):
    context = {}
    if request.method == 'POST':
        tag_form = TagMappingForm(request.POST)
        if tag_form.is_valid():
            tag_map = TagMapping()
            tag_map.tag_name = tag_form.cleaned_data['tag_name']
            ref_template_id = request.POST.get('msg_template_key')
            tag_template = MsgTemplate.objects.get(pk=ref_template_id)
            tag_map.ref_template = tag_template
            tag_map.save()
            return redirect(reverse('import_message'), args=[])
    else:
        tag_form = TagMappingForm()
    template_list = MsgTemplate.objects.all()
    context['template_list'] = template_list
    context['tag_form'] = tag_form
    return render(request, 'manager/add_tag.html', context)
