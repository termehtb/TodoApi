import logging

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView, get_object_or_404, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from user.serializers import UserRegistrationSerializer

from user.serializers import UserLoginSerializer

from user.models import User

from jobs import permissions

from user.serializers import UserSerializer


logger = logging.getLogger('django')


class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success': 'True',
            'status code': status_code,
            'message': 'User registered  successfully',
        }
        logger.critical('user ' + email + ' registered successfully')
        return Response(response, status=status_code)

class UserLoginView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token': serializer.data['token'],
            }
        status_code = status.HTTP_200_OK
        logger.critical('user ' + email + ' logged in  successfully')

        return Response(response, status=status_code)


class DeleteUser(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def post(self, request):
        ins = request.user
        email = ins.email
        ins.delete()
        status_code = status.HTTP_204_NO_CONTENT
        logger.critical('user ' + email + 'deleted account')
        return Response("user deleted successfully.", status=status_code)


class Deactive(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def post(self, request):
        user = request.user
        user.is_active = False
        user.save()
        logger.critical('user ' + user.email + 'deactivated account')
        return Response("user deactivated")



