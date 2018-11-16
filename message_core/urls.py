from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_message, name='show_message'),
    path('unvisit_message', views.unvisit_message, name='unvisit_message'),
    path('message_task/<int:day>', views.message_task, name='message_task'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('add', views.add_message, name='add_message'),
    path('edit/<int:message_id>', views.edit_message, name='edit_message'),
    path('intent_change', views.intent_change, name='intent_change'),
    path('intent_message', views.intent_message, name='intent_message'),
    path('finished_message', views.finished_message, name='finished_message'),
    path('get_user_list', views.get_user_list, name='get_user_list'),
    path('move_message', views.move_message, name='move_message'),
    path('search_message', views.search_message, name='search_message'),
]
