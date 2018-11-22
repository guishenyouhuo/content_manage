from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustMessage, UserProfile


# Register your models here.


@admin.register(CustMessage)
class CustMessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'message', 'cust_name', 'cust_mobile', 'cust_address', 'follow_user', 'last_follow_user',
                    'visit_record', 'next_visit_date', 'type', 'source_tag', 'created_time', 'updated_time')


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'user_num', 'user_status', 'email', 'is_staff', 'is_active', 'is_superuser')

    def user_num(self, obj):
        return obj.userprofile.user_num

    user_num.short_description = '编号'

    def user_status(self, obj):
        return obj.userprofile.user_status

    user_status.short_description = '状态'


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_num')
