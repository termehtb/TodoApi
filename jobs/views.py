import kwargs as kwargs
import self as self
from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.datetime_safe import datetime
from rest_framework import generics
from rest_framework.decorators import api_view, action
from rest_framework.generics import RetrieveAPIView, get_object_or_404, UpdateAPIView
from rest_framework.response import Response

from jobs.models import Todojob
from jobs.serializers import TodoSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated

from jobs import permissions

from jobs.permissions import IsNotBanned, IsAdmin, IsOwnerOrAdmin
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from user.models import User

from user.serializers import UserSerializer

from userprofile.models import UserProfile

from jobs.utils import Red

"""
Below Function going to display all the tasks store in the data base.
"""



class TaskListView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, permissions.IsOwnerOrAdmin)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        tasks = Todojob.objects.filter(author=request.user)
        serializer = TodoSerializer(tasks, many=True)

        return Response(serializer.data)





class CreateTaskView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def post(self,request):
        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(author=request.user)
        return Response(serializer.data)


class UpdateTaskView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,permissions.IsOwnerOrAdmin)
    authentication_class = JSONWebTokenAuthentication
    queryset = Todojob.objects.all()
    serializer_class = TodoSerializer
    def post(self, request, pk):
        task = Todojob.objects.get(pk=pk)
        serializer = TodoSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)




class DeleteTask(RetrieveAPIView):
    permission_classes = (IsAuthenticated,permissions.IsOwnerOrAdmin)
    authentication_class = JSONWebTokenAuthentication
    queryset = Todojob.objects.all()
    serializer_class = TodoSerializer

    def post(self,request,  pk):
        task = Todojob.objects.get(pk=pk)
        task.delete()
        return Response("Taks deleted successfully.")


