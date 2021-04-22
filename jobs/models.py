from django.db import models

# Create your models here.
from user.models import User
from versatileimagefield.fields import VersatileImageField, PPOIField


# class Image(models.Model):
#     name = models.CharField(max_length=255)
#     image = VersatileImageField(
#         'Image',
#         upload_to='images/',
#         ppoi_field='image_ppoi'
#     )
#     image_ppoi = PPOIField()
#
#     def __str__(self):
#         return self.name


class Todojob(models.Model):
    text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(default='/static/icon.png')
    author = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='Todojobs')

    def __str__(self):
        return self.text

