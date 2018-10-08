import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth
from .models import CustMessage
from .forms import LoginForm, MessageModelForm as MessageForm


# Create your views here.

def index(request):
    user = request.user
    # 用户未登陆或者是管理员（管理员只能进入管理页面）
    if not user.is_authenticated or user.is_superuser:
        return redirect(reverse('login'), args=[])
    return render(request, 'index.html', {})


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(reverse('index'), args=[])
    else:
        login_form = LoginForm()
    context = {'login_form': login_form}
    return render(request, 'login.html', context)


# 超级用户跳转到超级用户管理页面
def forward_superuser(request):
    login_form = LoginForm()
    context = {'login_form': login_form}
    return render(request, 'login.html', context)


# def

def show_message(request):
    user = request.user
    context = {}
    if user.is_superuser:
        return forward_superuser(request)
    message_list = CustMessage.objects.filter(follow_user=user.userprofile, type=1)
    context['message_list'] = message_list
    context['message_title'] = '我的全部资源'
    context['no_message_tip'] = '暂无留言内容'
    return render(request, 'message.html', context)


def unvisit_message(request):
    user = request.user
    context = {}
    if user.is_superuser:
        forward_superuser(request)
    message_list = CustMessage.objects.filter(follow_user=user.userprofile, type=1, next_visit_date__isnull=True)
    context['message_list'] = message_list
    context['message_title'] = '我的未回访留言'
    context['no_message_tip'] = '暂无未回访留言'
    return render(request, 'message.html', context)


def message_task(request, day):
    # day表示哪一天的任务 0:今天; 1:明天; 2:后天; 3:历史
    user = request.user
    context = {}
    if user.is_superuser:
        forward_superuser(request)
    if day < 0:
        day = 0
    if day > 3:
        day = 3
    task_date = datetime.datetime.now()
    if day < 3:
        if day == 0:
            task_name = '今日'
        elif day == 1:
            task_name = '明日'
        else:
            task_name = '后天'
        delta = datetime.timedelta(days=day)
        task_date = task_date + delta
        message_list = CustMessage.objects.filter(follow_user=user.userprofile, type=1, next_visit_date=task_date)
    else:
        task_name = '历史'
        message_list = CustMessage.objects.filter(follow_user=user.userprofile, type=1, next_visit_date__lt=task_date)
    context['message_list'] = message_list
    context['message_title'] = '我的' + task_name + '任务'
    context['no_message_tip'] = '暂无' + task_name + '任务'
    return render(request, 'message.html', context)


def build_message(cust_message, message_form):
    cust_message.cust_name = message_form.cleaned_data['cust_name']
    cust_message.cust_mobile = message_form.cleaned_data['cust_mobile']
    cust_message.cust_address = message_form.cleaned_data['cust_address']
    cust_message.message = message_form.cleaned_data['message']
    cust_message.visit_record = message_form.cleaned_data['visit_record']
    cust_message.next_visit_date = message_form.cleaned_data['next_visit_date']
    cust_message.type = 1
    # cust_message.source_tag = message_form.cleaned_data['s']


def add_message(request):
    context = {}
    user = request.user
    if request.method == 'POST':
        message_form = MessageForm(request.POST, user=user)
        if message_form.is_valid():
            cust_message = CustMessage()
            build_message(cust_message, message_form)
            if not user.is_superuser:
                cust_message.follow_user = user.userprofile
            else:
                pass
            cust_message.save()
            return redirect(reverse('show_message'), args=[])
    else:
        message_form = MessageForm()
    context['message_form'] = message_form
    return render(request, 'add_message.html', context)


def edit_message(request, message_id):
    context = {}
    user = request.user
    if request.method == 'POST':
        message_form = MessageForm(request.POST, user=user)
        message_form.instance.pk = message_id
        if message_form.is_valid():
            cust_message = CustMessage.objects.get(pk=message_id)
            build_message(cust_message, message_form)
            if not user.is_superuser:
                cust_message.follow_user = user.userprofile
            else:
                pass
            cust_message.save()
            return redirect(reverse('show_message'), args=[])
    else:
        message_form = MessageForm(instance=CustMessage.objects.get(pk=message_id))
        message_form.fields['cust_mobile'].widget.attrs['readonly'] = True
    context['message_form'] = message_form
    return render(request, 'edit_message.html', context)


def to_manage(request):
    return render(request, 'manger_login.html')


def logout(request):
    auth.logout(request)
    return redirect(reverse('index'), args=[])
