from rest_framework import serializers

from jobs.models import Todojob


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todojob
        fields = ['id', 'text', 'image']
