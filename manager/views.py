from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from jobs import permissions
from jobs.models import Todojob
from jobs.serializers import TodoSerializer
from user.serializers import UserSerializer
from userprofile.models import UserProfile

from user.serializers import UserRegistrationSerializer

from user.models import User


class UserView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, permissions.IsAdmin)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        users = UserProfile.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)



class AllTaskListView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, permissions.IsAdmin)
    authentication_class = JSONWebTokenAuthentication

    def get(self,request ):
        tasks = Todojob.objects.all()
        serializer = TodoSerializer(tasks, many=True)
        return Response(serializer.data)

class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (IsAuthenticated, permissions.IsAdmin)
    authentication_class = JSONWebTokenAuthentication

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success': 'True',
            'status code': status_code,
            'message': 'User registered  successfully',
        }

        return Response(response, status=status_code)



