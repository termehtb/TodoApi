from rest_framework import serializers


class RemoveUserSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
