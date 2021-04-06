from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from user.serializers import UserRegistrationSerializer

from user.serializers import UserLoginSerializer

from user.models import User

from jobs import permissions


class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

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

class UserLoginView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token': serializer.data['token'],
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)

class DeleteUser(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    def post(self, request):
        ins = request.user
        ins.delete()
        return Response("user deleted successfully.")



class Deactive(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def __delete__(self, request):
        user = request.user
        user.is_active = False
        user.save()
        return Response("user deactivated")


class DeleteUserbyAdmin(RetrieveAPIView):
    permission_classes = (IsAuthenticated, permissions.IsAdmin)
    authentication_class = JSONWebTokenAuthentication

    def __delete__(self, request, pk):
        ins = User.objects.get(id=pk)
        ins.delete()
        return Response("user deleted successfully.")

