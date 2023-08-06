from django.urls import path
from todo.views import todo

urlpatterns = [
    path('todos', todo.todo_list, name='todo-list'),
    path('todos/<int:pk>', todo.todo_detail, name='todo-detail'),
]
