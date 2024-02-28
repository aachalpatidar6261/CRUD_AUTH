from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('',views.register,name='register'),
    path('login',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),

    path('todo_index',views.todo_index,name='todo_index'),
    ]
