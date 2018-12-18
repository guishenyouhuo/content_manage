import os
import django

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "content_manage.settings")
# django.setup()
#
# import xlrd
# from manager.models import UserProfile
# from django.contrib.auth.models import User
#
# if __name__ == '__main__':
#     user_excel = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\gs_user.xls")
#     table = user_excel.sheets()[0]
#     for i in range(1, table.nrows):
#         # print(table.cell_value(i, 1) + ', ' + table.cell_value(i, 2) + ', '
#         #       + table.cell_value(i, 3) + ', ' + table.cell_value(i, 4))
#         user_name = table.cell_value(i, 1)
#         user_num = table.cell_value(i, 2)
#         user_password = table.cell_value(i, 3)
#         user_status = table.cell_value(i, 4)
#         user = User.objects.create()
#         user.username = user_name
#         user.set_password(user_password)
#         user_profile = UserProfile()
#         user_profile.user_num = user_num
#         user_profile.user = user
#         user_profile.user_status = int(user_status)
#         user.save()
#         user_profile.save()
#         print(user_name + '保存成功！')
