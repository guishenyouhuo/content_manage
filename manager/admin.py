from django.contrib import admin
from .models import AutoMessage, MsgTemplate, TagMapping


# Register your models here.


@admin.register(AutoMessage)
class AutoMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'cur_user')


@admin.register(MsgTemplate)
class MsgTemplateAdmin(admin.ModelAdmin):
    list_display = ('template_key', 'has_firstline', 'col_username', 'col_mobilephone', 'col_address', 'col_message')


@admin.register(TagMapping)
class TagMappingAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'ref_template')
