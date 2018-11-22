from django.urls import path
from . import views

urlpatterns = [
    path('', views.to_manage, name='to_manage'),
    path('index', views.manager, name='manager'),
    path('add_user', views.add_user, name='add_user'),
    path('user_list', views.show_user_list, name='user_list'),
    path('modify_user_pwd', views.modify_user_pwd, name='modify_user_pwd'),
    path('change_user', views.change_user, name='change_user'),
    path('delete_user', views.delete_user, name='delete_user'),
    path('show_all', views.show_message, name='show_all'),
    path('change_status', views.change_status, name='change_status'),
    path('del_message', views.del_message, name='del_message'),
    path('show_trush', views.show_trush, name='show_trush'),

]
