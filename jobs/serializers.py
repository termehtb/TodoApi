from rest_framework import serializers

from jobs.models import Todojob


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todojob
        fields = ['id', 'text', 'image']

        def get_photo_url(self, car):
            request = self.context.get('request')
            photo_url = Todojob.image.url
            return request.build_absolute_uri(photo_url)
