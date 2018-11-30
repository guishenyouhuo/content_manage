from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from message_core.models import UserProfile
from .models import MsgTemplate, TagMapping


class ManagerLoginForm(forms.Form):
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
        if not user.is_superuser:
            raise forms.ValidationError('非管理员用户无法登录')
        self.cleaned_data['user'] = user
        return self.cleaned_data


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user_num']
        labels = {
            'user_num': '用户编号',
        }
        widgets = {
            'user_num': forms.TextInput(
                attrs={'class': 'form-control txt_input txt_input2', 'placeholder': '请输入用户编号'}
            ),
        }
        error_messages = {
            'user_num': {
                'required': '编号不能为空',
            }
        }

    def clean_user_num(self):
        user_num = self.cleaned_data['user_num']
        if user_num is None:
            raise forms.ValidationError('未填写用户编号')
        if self.instance.pk is None and UserProfile.objects.filter(user_num=user_num).exists():
            raise forms.ValidationError('该用户编号已存在')
        return user_num


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': '用户姓名',
            'password': '密码',
        }
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control txt_input txt_input2', 'placeholder': '请输入用户姓名'}
            ),
            'password': forms.PasswordInput(
                attrs={'class': 'form-control txt_input', 'placeholder': '请输入密码'}
            ),
        }
        error_messages = {
            'username': {
                'required': '姓名不能为空',
            },
            'password': {
                'required': '密码不能为空',
            }
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        if username is None:
            raise forms.ValidationError('未填写用户姓名')
        if self.instance.pk is None and User.objects.filter(username=username).exists():
            raise forms.ValidationError('该用户已存在')
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if password is None:
            raise forms.ValidationError('未填写用户密码')
        return password


class MsgTemplateForm(forms.ModelForm):
    class Meta:
        model = MsgTemplate
        fields = ['template_key', 'col_username', 'col_mobilephone', 'col_address', 'col_message']
        labels = {
            'template_key': 'Excel模板名称',
            'col_username': '客户姓名所在列',
            'col_mobilephone': '客户电话所在列',
            'col_address': '客户地址所在列',
            'col_message': '客户留言所在列',
        }

        error_messages = {
            'template_key': {
                'required': '模板名称不能为空',
            },
            'col_mobilephone': {
                'required': '客户电话列不能为空',
            }
        }

    def clean_template_key(self):
        template_key = self.cleaned_data['template_key']
        if template_key is None:
            raise forms.ValidationError('未填写Excel模板名称')
        if self.instance.pk is None and MsgTemplate.objects.filter(template_key=template_key).exists():
            raise forms.ValidationError('该模板名称已存在')
        return template_key

    def clean_col_mobilephone(self):
        col_mobliephone = self.cleaned_data['col_mobilephone']
        if col_mobliephone is None:
            raise forms.ValidationError('未填写客户电话所在列')
        return col_mobliephone


class TagMappingForm(forms.ModelForm):
    class Meta:
        model = TagMapping
        fields = ['tag_name']
        labels = {
            'tag_name': '来源名称',
        }

        error_messages = {
            'tag_name': {
                'required': '来源名称不能为空',
            }
        }

    def clean_tag_name(self):
        tag_name = self.cleaned_data['tag_name']
        if tag_name is None:
            raise forms.ValidationError('未填来源名称')
        if self.instance.pk is None and TagMapping.objects.filter(tag_name=tag_name).exists():
            raise forms.ValidationError('该来源已存在')
        return tag_name

