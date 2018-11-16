from django.urls import path
from . import views

urlpatterns = [
    path('', views.to_manage, name='to_manage'),
    path('index', views.manager, name='manager'),

]
