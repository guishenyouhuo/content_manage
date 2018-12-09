import re
from django import forms
from django.contrib import auth
from ckeditor.widgets import CKEditorWidget
from .models import CustMessage


class LoginForm(forms.Form):
    username = forms.CharField(
        label='用户名',
        widget=forms.TextInput(
            attrs={'class': 'form-control txt_input txt_input2', 'placeholder': '请输入用户名'}
        )
    )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control txt_input', 'placeholder': '请输入密码'}
        )
    )

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = auth.authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('用户名或密码不正确')
        self.cleaned_data['user'] = user
        return self.cleaned_data


class MessageModelForm(forms.ModelForm):
    class Meta:
        model = CustMessage
        fields = ['cust_name', 'cust_mobile', 'cust_address', 'message', 'visit_record', 'source_tag',
                  'next_visit_date']
        labels = {
            'cust_name': '客户姓名',
            'cust_mobile': '客户电话',
            'cust_address': '客户地址',
            'message': '客户留言',
            'visit_record': '回访记录',
            'source_tag': '留言来源',
            'next_visit_date': '下次回访日期',
        }
        widgets = {
            'cust_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '请输入客户姓名'}
            ),
            'cust_mobile': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '请输入客户电话'}
            ),
            'cust_address': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '请输入客户地址'}
            ),
            'message': forms.Textarea(attrs={'cols': 70, 'rows': 5}),
            'visit_record': CKEditorWidget(config_name='message_ckeditor'),
            'source_tag': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '请输入留言来源'}
            ),
            'next_visit_date': forms.DateInput(attrs={'id': 'datepicker'}),
        }
        error_messages = {
            'cust_mobile': {
                'required': '手机号不能为空',
                'invalid': '手机号格式错误',
            }
        }

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(MessageModelForm, self).__init__(*args, **kwargs)

    def clean(self):
        # 判断用户是否登录
        if self.user.is_authenticated:
            self.cleaned_data['user'] = self.user
        else:
            raise forms.ValidationError('用户尚未登录')
        return self.cleaned_data

    def clean_cust_mobile(self):
        cust_mobile = self.cleaned_data['cust_mobile']
        if cust_mobile is None:
            raise forms.ValidationError('未填写手机号')
        cust_mobile = cust_mobile.strip()
        if not re.search('^1[0-9]{10}$', cust_mobile):
            raise forms.ValidationError('手机号格式不正确')
        if self.instance.pk is None and CustMessage.objects.filter(cust_mobile=cust_mobile).exists():
            raise forms.ValidationError('该手机号已存在')
        return cust_mobile

    def clean_visit_record(self):
        visit_record = self.cleaned_data['visit_record']
        if len(visit_record.strip()) == 0:
            visit_record = None
        return visit_record


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(
        label='原密码',
        min_length=6,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': '请输入原密码'}
        )
    )
    new_password = forms.CharField(
        label='新密码',
        min_length=6,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': '请输入新密码'}
        )
    )
    new_password_again = forms.CharField(
        label='再次输入新密码',
        min_length=6,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': '请再次输入新密码'}
        )
    )

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    def clean(self):
        # 验证两次新密码是否一致
        new_password = self.cleaned_data.get('new_password', '')
        new_password_again = self.cleaned_data.get('new_password_again', '')
        if new_password != new_password_again or new_password == '':
            raise forms.ValidationError('两次输入的密码不一致')

    def clean_old_password(self):
        # 验证旧的密码是否正确
        old_password = self.cleaned_data.get('old_password', '')
        if not self.user.check_password(old_password):
            raise forms.ValidationError('原密码错误')
        return old_password
