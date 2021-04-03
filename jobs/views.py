import self as self
from django.shortcuts import render

# Create your views here.
from django.utils.datetime_safe import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response

from jobs.models import Todojob
from jobs.serializers import TodoSerializer



"""
Below Function going to display all the tasks store in the data base.
"""
@api_view(['GET'])
def taskList(request):
    tasks = Todojob.objects.all()
    serializer = TodoSerializer(tasks, many=True)
    return Response(serializer.data)

"""
This Function going to display Detailed view of one perticuler task with the help of pk.
"""
@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Todojob.objects.get(id=pk)
    serializer = TodoSerializer(tasks, many=False)
    return Response(serializer.data)



@api_view(['POST'])
def taskCreate(request):
    serializer = TodoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(author=self.request.user, date=datetime.date.today()
)
    return Response(serializer.data)



@api_view(['POST'])
def taskUpdate(request, pk):
    task = Todojob.objects.get(id = pk)
    serializer = TodoSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Todojob.objects.get(id = pk)
    task.delete()
    return Response("Taks deleted successfully.")
