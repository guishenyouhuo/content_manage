import xlrd
import re
from datetime import datetime
from xlrd import xldate_as_tuple
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
from .forms import ManagerLoginForm, UserForm, ProfileForm, MsgTemplateForm, TagMappingForm, ImportForm


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
            user_profile.clear_password = user_form.cleaned_data['password']
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


@transaction.atomic
def modify_user_pwd(request):
    user_id = request.POST['modify_user_id']
    user_pwd = request.POST['user_pwd_new']
    user = User.objects.get(pk=user_id)
    user_profile = UserProfile.objects.get(user=user)
    user.set_password(user_pwd)
    user_profile.clear_password = user_pwd
    user.save()
    user_profile.save()
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
    message_list = CustMessage.objects.filter(type=3).exclude(message_status=0)
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


def dispatch_message(request):
    context = {}
    user_list = UserProfile.objects.filter(user__is_active=True, user__is_superuser=False, user_status=1)
    if request.method == 'POST':
        message_form = MessageForm(request.POST, user=request.user)
        if message_form.is_valid():
            auto_config = AutoMessage()
            follow_user_id = request.POST['follow_user_id']
            if follow_user_id == 'auto':
                auto_config = AutoMessage.objects.all()[0]
                index = 0
                while index < user_list.count() and user_list[index].pk != auto_config.cur_user.pk:
                    index += 1
                index += 1
                # 默认取第一个(包含当前是最后一个或者没有当前用户), 如果还在列表范围内，取index位置用户
                user_index = index if index < user_list.count() else 0
                user_profile = user_list[user_index]
            else:
                user_profile = [user for user in user_list if user.pk == int(request.POST['follow_user_id'])][0]
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
    user_list = UserProfile.objects.filter(user__is_active=True, user__is_superuser=False, user_status=1)
    context['user_list'] = user_list
    if request.method == 'POST':
        sel_user_id = int(request.POST['cur_user_id'])
        sel_user = [user for user in user_list if user.pk == sel_user_id]
        if auto_config is None:
            auto_config = AutoMessage()
        auto_config.cur_user = sel_user[0]
        auto_config.save()
        context['auto_config'] = auto_config
    return render(request, 'manager/auto_message.html', context)


@transaction.atomic
def import_message(request):
    context = {}
    user_list = UserProfile.objects.filter(user__is_active=True, user__is_superuser=False, user_status=1)
    if request.method == 'POST':
        import_form = ImportForm(request.POST, request.FILES)
        if import_form.is_valid():
            excel_file = request.FILES['excel_file']
            sel_source = import_form.cleaned_data['sel_source']
            dispatch_user = import_form.cleaned_data['dispatch_user']
            tag_template = MsgTemplate.objects.get(ref_tag__tag_name=sel_source)
            # 开始解析上传的excel表格
            wb = xlrd.open_workbook(filename=None, file_contents=excel_file.read())
            table = wb.sheets()[0]
            # 分配数据
            first_row = 1
            if not tag_template.has_firstline:
                first_row = 2
            # 用户列表大小
            user_count = user_list.count()
            # 确定用户列表偏移量
            user_shift = 0
            # 批量保存信息列表
            batch_message_list = []
            auto_config = AutoMessage.objects.all()[0]
            last_dispatch_user = auto_config.cur_user
            while user_shift < user_count:
                if user_list[user_shift].pk == auto_config.cur_user.pk:
                    break
                user_shift += 1
            # 有效计数（中间或有跳过数据）
            cur_index = first_row
            # 失败列表
            fail_list = []
            # 构建用户字典
            user_dict = {user.pk: user for user in user_list}
            for i in range(first_row, table.nrows):
                cust_message = CustMessage()
                # 根据配置的映射字段找到excel中具体列的值
                if tag_template.col_mobilephone is not None and tag_template.col_mobilephone.isalpha():
                    mobilephone_idx = ord(tag_template.col_mobilephone.upper()) - ord('A')
                    mobilephone_type = table.cell_type(i, mobilephone_idx)
                    # 字符串类型需要做处理
                    if mobilephone_type == 1:
                        mobilephone = table.cell_value(i, mobilephone_idx)
                        # 去掉非数字字符
                        mobilephone = re.sub("\D", "", mobilephone)
                        # 转整形（主要用于去掉首位0）
                        mobilephone = int(mobilephone) if len(mobilephone) > 0 else 0
                    else:
                        mobilephone = get_cell_value(mobilephone_type, table.cell_value(i, mobilephone_idx))
                    # 不满足手机号格式
                    if not re.search('^1[0-9]{10}$', str(mobilephone)):
                        fail_tuple = (str(table.cell_value(i, mobilephone_idx)), "格式不合法！")
                        fail_list.append(fail_tuple)
                        continue
                    # 检查是否存在
                    if CustMessage.objects.filter(cust_mobile=str(mobilephone)).exists():
                        fail_tuple = (str(mobilephone), "重复号码！")
                        fail_list.append(fail_tuple)
                        continue
                    cust_message.cust_mobile = str(mobilephone)
                if tag_template.col_username is not None and tag_template.col_username.isalpha():
                    cust_name_idx = ord(tag_template.col_username.upper()) - ord('A')
                    cust_name_type = table.cell_type(i, cust_name_idx)
                    cust_message.cust_name = get_cell_value(cust_name_type, table.cell_value(i, cust_name_idx))
                if tag_template.col_address is not None and tag_template.col_address.isalpha():
                    cust_address_idx = ord(tag_template.col_address.upper()) - ord('A')
                    address_type = table.cell_type(i, cust_address_idx)
                    cust_message.cust_address = get_cell_value(address_type, table.cell_value(i, cust_address_idx))
                if tag_template.col_message is not None and tag_template.col_message.isalpha():
                    cust_message_idx = ord(tag_template.col_message.upper()) - ord('A')
                    message_type = table.cell_type(i, cust_message_idx)
                    cust_message.message = get_cell_value(message_type, table.cell_value(i, cust_message_idx))

                cust_message.source_tag = sel_source
                # 分配人设置
                if dispatch_user == 'auto':
                    # 自动分配的情况下，用户索引为当前留言索引加上用户偏移量，模上用户列表长度
                    user_index = (cur_index + user_shift) % user_count
                    follow_user = user_list[user_index]
                else:
                    follow_user = user_dict[int(dispatch_user)]
                # 记录当前处理分配的用户
                last_dispatch_user = follow_user
                cust_message.follow_user = follow_user
                batch_message_list.append(cust_message)
                # 满1000保存一次数据库
                if len(batch_message_list) >= 1000:
                    CustMessage.objects.bulk_create(batch_message_list)
                    batch_message_list.clear()
                cur_index += 1
            # 保存最后存留的一部分数据
            if len(batch_message_list) > 0:
                CustMessage.objects.bulk_create(batch_message_list)
                batch_message_list.clear()
            # 自动分配的情况 还需要更新自动分配配置表
            if dispatch_user == 'auto':
                auto_config.cur_user = last_dispatch_user
                auto_config.save()
            if len(fail_list) > 0:
                context['fail_list'] = fail_list
                return render(request, 'manager/import_fail.html', context)
            return redirect(reverse('show_all'), args=[])
    else:
        import_form = ImportForm()
    tag_list = TagMapping.objects.all()
    context['source_tag_list'] = tag_list
    context['user_list'] = user_list
    context['import_form'] = import_form
    return render(request, 'manager/import_message.html', context)


def get_cell_value(cell_type, cell_value):
    # 如果是整形
    if cell_type == 2 and cell_value % 1 == 0:
        cell_value = int(cell_value)
    elif cell_type == 3:
        # 转成datetime对象
        date = datetime(*xldate_as_tuple(cell_value, 0))
        cell_value = date.strftime('%Y/%d/%m %H:%M:%S')
    elif cell_type == 4:
        cell_value = True if cell_value == 1 else False
    return cell_value


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
