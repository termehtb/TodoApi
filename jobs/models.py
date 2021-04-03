from django.db import models

# Create your models here.
from user.models import User


class Todojob(models.Model):
    text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True , null=True)
    image = models.ImageField(default=' static/default.png')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
