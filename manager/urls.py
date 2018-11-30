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
    path('show_by_user', views.show_by_user, name='show_by_user'),
    path('user_message/<int:user_pk>', views.show_message_by_user, name='show_message_by_user'),
    path('all_complete', views.show_complete, name='all_complete'),
    path('user_complete/<int:user_pk>', views.show_complete_by_user, name='user_complete'),
    path('complete_change', views.complete_change, name='complete_change'),
    path('dispatch_message', views.dispatch_message, name='dispatch_message'),
    path('manager_search', views.search_message, name='manager_search'),
    path('auto_message', views.auto_message, name='auto_message'),
    path('import_message', views.import_message, name='import_message'),
    path('add_template', views.add_template, name='add_template'),
    path('add_tag', views.add_tag, name='add_tag'),

]
