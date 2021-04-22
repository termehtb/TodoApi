from rest_framework import serializers

from jobs.models import Todojob
from versatileimagefield.serializers import VersatileImageFieldSerializer



class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model =Todojob
        fields = ['id', 'text',  'completed', 'image']

        # def get_photo_url(self, Todojob, request):
        #     context = {'request': request}
        #     request = self.context.get('request')
        #     photo_url = Todojob.image.url
        #     return request.build_absolute_uri(photo_url)
#
#
# class ImageSerializer(serializers.ModelSerializer):
#     image = VersatileImageFieldSerializer(
#         sizes='product_headshot'
#
#     )
#
#     class Meta:
#         model = Image
#         fields = ['pk', 'name', 'image']
