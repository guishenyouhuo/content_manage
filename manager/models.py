from django.db import models
from message_core.models import UserProfile


# Create your models here.

class AutoMessage(models.Model):
    # 当前分配
    cur_user = models.ForeignKey(UserProfile, to_field='user_num', related_name='ref_auto_msg',
                                 on_delete=models.CASCADE)


class MsgTemplate(models.Model):
    template_key = models.CharField(max_length=30, unique=True)
    has_firstline = models.BooleanField(default=True)
    col_username = models.CharField(max_length=2, null=True, blank=True, default=None)
    col_mobilephone = models.CharField(max_length=2, default=None)
    col_address = models.CharField(max_length=2, null=True, blank=True, default=None)
    col_message = models.CharField(max_length=2, null=True, blank=True, default=None)

    def __str__(self):
        return self.template_key


class TagMapping(models.Model):
    tag_name = models.CharField(max_length=30, unique=True)
    ref_template = models.ForeignKey(MsgTemplate, to_field='template_key', related_name='ref_tag',
                                     on_delete=models.CASCADE)
