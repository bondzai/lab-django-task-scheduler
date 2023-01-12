from rest_framework import viewsets, status
from apis.models import Task
from apis.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('pk')
    serializer_class = TaskSerializer
