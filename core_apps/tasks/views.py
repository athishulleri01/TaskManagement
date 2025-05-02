from django.shortcuts import render, redirect
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer, TaskStatusUpdateSerializer
from django.contrib.auth.decorators import login_required
from core_apps.users.models import User

class UserTaskListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)


class TaskStatusUpdateAPIView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskStatusUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)

    def perform_update(self, serializer):
        serializer.save()


class TaskReportAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        if not request.user.is_superuser and not request.user.is_staff:
            return Response({'error': 'Access denied'}, status=status.HTTP_403_FORBIDDEN)

        if task.status != 'completed':
            return Response({'error': 'Task not completed'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'completion_report': task.completion_report,
            'worked_hours': task.worked_hours
        })




@login_required
def create_task_view(request):
    if request.method == 'POST' and request.user.role in ['admin', 'superadmin']:
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            assigned_to_id=request.POST['assigned_to'],  
            due_date=request.POST['due_date'],
            status='pending'
        )

        return redirect('task_list')
    
    users = User.objects.filter(role='user')
    return render(request, 'adminside/tasks/task_page.html', {'users': users})

@login_required
def task_list_view(request):
    if request.user.role == 'user':
        tasks = Task.objects.filter(assigned_to=request.user)
    else:
        tasks = Task.objects.all()
        users = User.objects.filter(role="user")
    return render(request, 'adminside/tasks/list_tasks.html', {'tasks': tasks, 'users' :users})