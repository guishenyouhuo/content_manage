from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# 用户模型扩展
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_num = models.CharField(max_length=20, unique=True, verbose_name='用户编号')
    # 1：启用 ；0：停用
    user_status = models.IntegerField(default=1, verbose_name='用户状态')

    def __str__(self):
        return self.user.username


def get_user_num(self):
    if UserProfile.objects.filter(user=self).exists():
        profile = UserProfile.objects.get(user=self)
        return profile.user_num
    else:
        return ''


def get_user_status(self):
    if UserProfile.objects.filter(user=self).exists():
        profile = UserProfile.objects.get(user=self)
        return profile.user_status
    else:
        return ''


User.user_num = get_user_num
User.user_status = get_user_status


# 留言资源模型
class CustMessage(models.Model):
    # 留言客户姓名(可以为空)
    cust_name = models.CharField(null=True, blank=True, max_length=30, default=None)
    # 客户手机号（不可重复）
    cust_mobile = models.CharField(max_length=30, unique=True)
    # 客户地址
    cust_address = models.CharField(null=True, blank=True, max_length=50, default=None)
    # 客户留言信息
    message = models.TextField(null=True, blank=True, default=None)
    # 跟进客服
    follow_user = models.ForeignKey(UserProfile, to_field='user_num', related_name='follow_user',
                                    on_delete=models.CASCADE)
    # 上一跟进客服
    last_follow_user = models.ForeignKey(UserProfile, to_field='user_num', related_name='last_follow_user',
                                         on_delete=models.DO_NOTHING, null=True, blank=True, default=None)
    # 访问记录
    visit_record = models.TextField(null=True, blank=True, default=None)
    # 下次回访日期
    next_visit_date = models.DateField(null=True, blank=True, default=None)
    # 留言类型(0:删除, 1:正常, 2:意向)
    type = models.IntegerField()
    # 来源标记
    source_tag = models.CharField(max_length=50, null=True, blank=True, default=None)
    # 创建时间
    created_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    updated_time = models.DateTimeField(auto_now=True)

    def get_cust_name(self):
        return '暂无姓名' if self.cust_name is None else self.cust_name

    def get_cust_address(self):
        return '暂无地址' if self.cust_address is None else self.cust_address

    def get_message(self):
        return '暂无留言' if self.message is None else self.message

    def get_source_tag(self):
        return '暂无来源' if self.source_tag is None else self.source_tag

    def get_visit_date(self):
        return '暂无下次回访' if self.next_visit_date is None else self.next_visit_date

    def get_visit_record(self):
        return '暂无回访记录' if self.visit_record is None else self.visit_record

    class Meta:
        ordering = ['-created_time']
