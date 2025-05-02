from django.urls import path
from .views import UserTaskListAPIView, TaskStatusUpdateAPIView, TaskReportAPIView

urlpatterns = [
    path('tasks/', UserTaskListAPIView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskStatusUpdateAPIView.as_view(), name='task-update'),
    path('tasks/<int:pk>/report/', TaskReportAPIView.as_view(), name='task-report'),
]
