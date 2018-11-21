from django.urls import path
from . import views

urlpatterns = [
    path('', views.to_manage, name='to_manage'),
    path('index', views.manager, name='manager'),
    path('add_user', views.add_user, name='add_user'),
    path('user_list', views.show_user_list, name='user_list'),
    path('modify_user_pwd', views.modify_user_pwd, name='modify_user_pwd'),

]
