import kwargs as kwargs
import self as self
from django.shortcuts import render

# Create your views here.
from django.utils.datetime_safe import datetime
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from jobs.models import Todojob
from jobs.serializers import TodoSerializer


from jobs import permissions

from jobs.permissions import IsNotBanned, IsAdmin, IsOwnerOrAdmin

from user.models import User

from user.serializers import UserSerializer

from userprofile.models import UserProfile

"""
Below Function going to display all the tasks store in the data base.
"""
@api_view(['GET'])
def taskList(request):
    tasks = Todojob.objects.filter(author=request.user)
    serializer = TodoSerializer(tasks, many=True)
    permission_classes = [
        permissions.IsOwnerOrAdminOrReadOnly, IsOwnerOrAdmin]

    return Response(serializer.data)

"""
This Function going to display Detailed view of one perticuler task with the help of pk.
"""
@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Todojob.objects.get(id=pk)
    serializer = TodoSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def userlist(request):
    users = UserProfile.objects.all()
    serializer = UserSerializer(users, many=True)
    permission_classes = [
        permissions.IsAdmin]

    return Response(serializer.data)

@api_view(['GET'])
def alltaskList(request):
    tasks = Todojob.objects.all()
    serializer = TodoSerializer(tasks, many=True)
    permission_classes = [
        permissions.IsAdmin]

    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TodoSerializer(data=request.data)
    permission_classes = (permissions.IsNotBanned)
    if serializer.is_valid():
        serializer.save(author=request.user)
    return Response(serializer.data)



@api_view(['POST'])
def taskUpdate(request, pk):
    task = Todojob.objects.get(id=pk)
    permission_classes = (permissions.IsOwnerOrAdmin)
    serializer = TodoSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    permission_classes = (permissions.IsOwnerOrAdmin)
    task = Todojob.objects.get(id=pk)
    task.delete()
    return Response("Taks deleted successfully.")
