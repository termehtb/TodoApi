import logging

import kwargs as kwargs
import self as self
from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.datetime_safe import datetime
from rest_framework import generics, status
from rest_framework.decorators import api_view, action
from rest_framework.generics import RetrieveAPIView, get_object_or_404, UpdateAPIView
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.response import Response

from jobs.models import Todojob
from jobs.serializers import TodoSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated

from jobs import permissions

from jobs.permissions import IsNotBanned, IsAdmin, IsOwnerOrAdmin
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


logger = logging.getLogger('django')


class TaskListView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, permissions.IsOwnerOrAdmin)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        tasks = Todojob.objects.filter(author=request.user)
        serializer = TodoSerializer(tasks, many=True)
        return Response(serializer.data)


class TaskView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, permissions.IsOwnerOrAdmin)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request, pk):
        task = Todojob.objects.get(pk=pk)
        if task.author == request.user:
            serializer = TodoSerializer(task)
            return Response(serializer.data)
        else:
            status_code = status.HTTP_403_FORBIDEN
            return Response("This task is not yours", status=status_code)


class CreateTaskView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def post(self, request):
        serializer = TodoSerializer( data=request.data)
        if serializer.is_valid():
            status_code = status.HTTP_201_CREATED
            text = serializer.validated_data['text']
            logger.critical(request.user.email + ' created new task: ' + text)
            serializer.save(author=request.user)
            return Response(serializer.data, status=status_code)
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response('data is not valid', status=status_code)


class UpdateTaskView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, IsOwnerOrAdmin)
    serializer_class = TodoSerializer
    authentication_class = JSONWebTokenAuthentication

    def post(self, request, pk):
        task = Todojob.objects.get(pk=pk)
        serializer = TodoSerializer(instance=task, data=request.data)
        first_text = task.text
        if serializer.is_valid():
            if task.author == request.user or request.user.is_superuser:
                text = serializer.validated_data['text']
                logger.critical(request.user.email + ' updated task: ' + first_text + ' to ' + text)
                serializer.save(author=task.author)
                serializer.save()
            else:
                status_code = status.HTTP_403_FORBIDEN
                return Response("dont have the permission to update this task.",  status=status_code)

        return Response(serializer.data)


class DeleteTask(RetrieveAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated, permissions.IsOwnerOrAdmin)
    authentication_class = JSONWebTokenAuthentication

    def post(self, request,  pk):
        task = Todojob.objects.get(pk=pk)
        text = task.text
        if task.author == request.user or request.user.is_superuser:
            task.delete()
            logger.critical(request.user.email + ' deleted ' + text)
        else:
            status_code = status.HTTP_403_FORBIDEN
            return Response("you cannot delete this task", status=status_code)

        status_code = status.HTTP_204_NO_CONTENT
        return Response("Task deleted successfully.", status=status_code)



