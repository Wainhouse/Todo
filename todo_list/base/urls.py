from django.urls import path
from .views import TaskList, TaskDetail, taskCreate

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', taskCreate.as_view(), name='task-create'),
]
