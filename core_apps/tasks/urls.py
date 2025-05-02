from django.urls import path
from .views import UserTaskListAPIView, TaskStatusUpdateAPIView, TaskReportAPIView
from . import views
urlpatterns = [
    path('tasks/', UserTaskListAPIView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskStatusUpdateAPIView.as_view(), name='task-update'),
    path('tasks/<int:pk>/report/', TaskReportAPIView.as_view(), name='task-report'),
    path('tasks/create/', views.create_task_view, name='create_task'),
    path('all_tasks/', views.task_list_view, name='task_list'),
]
