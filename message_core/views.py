import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth
from django.core.paginator import Paginator
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from .models import CustMessage, UserProfile
from .forms import LoginForm, MessageModelForm as MessageForm, ChangePasswordForm
from manager.forms import ManagerLoginForm


# Create your views here.

def index(request):
    user = request.user
    # 用户未登陆或者是管理员（管理员只能进入管理页面）
    if not user.is_authenticated:
        logout(request)
        return redirect(reverse('login'), args=[])
    if user.is_superuser:
        return redirect(reverse('manager'), args=[])
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
    login_form = ManagerLoginForm()
    context = {'login_form': login_form}
    return render(request, 'manager/login.html', context)


def get_message_common_data(message_list, request):
    paginator = Paginator(message_list, settings.EACH_PAGE_MESSAGE_NUMBERS)
    # 获取url页面参数（GET请求）
    page_num = request.GET.get('page', 1)
    page_of_messages = paginator.get_page(page_num)
    # 获取当前页
    current_page_num = page_of_messages.number
    # 获取当前页码前后各两页页码
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))

    #  加上省略页码
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')

    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {'page_of_messages': page_of_messages,
               'message_list': page_of_messages.object_list,
               'page_range': page_range}
    return context


# 显示全部留言
def show_message(request):
    user = request.user
    if user.is_superuser:
        return forward_superuser(request)
    message_list = CustMessage.objects.filter(follow_user=user.userprofile).exclude(message_status=0)
    context = get_message_common_data(message_list, request)
    context['message_title'] = '我的全部资源'
    context['no_message_tip'] = '暂无留言内容'
    return render(request, 'message/message.html', context)


# 未回访留言
def unvisit_message(request):
    user = request.user
    if user.is_superuser:
        forward_superuser(request)
    message_list = CustMessage.objects.filter(follow_user=user.userprofile, next_visit_date__isnull=True,
                                              visit_record__isnull=True).exclude(message_status=0)
    context = get_message_common_data(message_list, request)
    context['message_title'] = '我的未回访留言'
    context['no_message_tip'] = '暂无未回访留言'
    return render(request, 'message/message.html', context)


# 已完成留言(type=3)
def finished_message(request):
    user = request.user
    if user.is_superuser:
        forward_superuser(request)
    message_list = CustMessage.objects.filter(follow_user=user.userprofile, type=3).exclude(message_status=0)
    context = get_message_common_data(message_list, request)
    context['message_title'] = '我的已完成留言'
    context['no_message_tip'] = '暂无已完成留言'
    return render(request, 'message/message.html', context)


# 意向组留言(type=2)
def intent_message(request):
    user = request.user
    if user.is_superuser:
        forward_superuser(request)
    message_list = CustMessage.objects.filter(follow_user=user.userprofile, type=2).exclude(message_status=0)
    context = get_message_common_data(message_list, request)
    context['message_title'] = '我的意向组'
    context['no_message_tip'] = '暂无意向留言'
    return render(request, 'message/message.html', context)


# 我的任务
def message_task(request, day):
    # day表示哪一天的任务 0:今天; 1:明天; 2:后天; 3:历史
    user = request.user
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
        message_list = CustMessage.objects.filter(follow_user=user.userprofile, next_visit_date=task_date).exclude(
            message_status=0).exclude(type=3)
    else:
        task_name = '历史'
        message_list = CustMessage.objects.filter(follow_user=user.userprofile, next_visit_date__lt=task_date).exclude(
            message_status=0).exclude(type=3)
    context = get_message_common_data(message_list, request)
    context['message_title'] = '我的' + task_name + '任务'
    context['no_message_tip'] = '暂无' + task_name + '任务'
    return render(request, 'message/message.html', context)


def build_message(cust_message, message_form):
    cust_message.cust_name = message_form.cleaned_data['cust_name']
    cust_message.cust_address = message_form.cleaned_data['cust_address']
    cust_message.message = message_form.cleaned_data['message']
    cust_message.visit_record = message_form.cleaned_data['visit_record']
    cust_message.next_visit_date = message_form.cleaned_data['next_visit_date']
    cust_message.source_tag = message_form.cleaned_data['source_tag']


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
        return render(request, 'message/message.html', context)
    return render(request, 'message/search_message.html', context)


def add_message(request):
    context = {}
    user = request.user
    if request.method == 'POST':
        message_form = MessageForm(request.POST, user=user)
        if message_form.is_valid():
            cust_message = CustMessage()
            build_message(cust_message, message_form)
            # 添加默认为正常留言
            cust_message.type = 1
            # 添加才需设置手机号
            cust_message.cust_mobile = message_form.cleaned_data['cust_mobile']
            if not user.is_superuser:
                cust_message.follow_user = user.userprofile
            else:
                logout(request)
            cust_message.save()
            return redirect(reverse('show_message'), args=[])
    else:
        message_form = MessageForm()
        message_form.fields['next_visit_date'].widget.attrs['class'] = 'div-hide'
    context['message_form'] = message_form
    return render(request, 'message/add_message.html', context)


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
                logout(request)
            cust_message.save()
            return redirect(request.GET.get('from', reverse('show_message')), args=[])
    else:
        message_form = MessageForm(instance=CustMessage.objects.get(pk=message_id))
        message_form.fields['cust_mobile'].widget.attrs['readonly'] = True
    context['message_form'] = message_form
    return render(request, 'message/edit_message.html', context)


def intent_change(request):
    object_id = request.GET.get('object_id')
    is_intented = request.GET.get('is_intented')
    message = CustMessage.objects.get(pk=object_id)
    if is_intented != 'true':
        message.type = 2
    else:
        message.type = 1
    message.save()
    data = {'status': 'SUCCESS'}
    return JsonResponse(data)


def get_user_list(request):
    users = User.objects.filter(is_active=True, is_superuser=False, userprofile__user_status=1)
    user_list = []
    for user in users:
        user_list.append(model_to_dict(user))
    data = {'user_list': user_list, 'status': 'SUCCESS'}
    return JsonResponse(data)


def move_message(request):
    message_id = request.GET.get('message_id')
    user_id = request.GET.get('user_id')
    message = CustMessage.objects.get(pk=message_id)
    last_user = message.follow_user
    cur_user = UserProfile.objects.get(user_id=user_id)
    message.follow_user = cur_user
    message.last_follow_user = last_user
    message.save()
    data = {'status': 'SUCCESS'}
    return JsonResponse(data)


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


def edit_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST, user=request.user)
        if form.is_valid():
            user = request.user
            new_password = form.cleaned_data['new_password']
            user.set_password(new_password)
            user.save()
            auth.logout(request)
            return redirect(reverse('login'), args=[])
    else:
        form = ChangePasswordForm()
    context = {'edit_password_form': form}
    return render(request, 'message/edit_password.html', context)


def logout(request):
    auth.logout(request)
    return redirect(reverse('index'), args=[])
