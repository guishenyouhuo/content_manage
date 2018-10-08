from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_message, name='show_message'),
    path('unvisit_message', views.unvisit_message, name='unvisit_message'),
    path('message_task/<int:day>', views.message_task, name='message_task'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('to_manage', views.to_manage, name='to_manage'),
    path('add', views.add_message, name='add_message'),
    path('edit/<int:message_id>', views.edit_message, name='edit_message'),
]
