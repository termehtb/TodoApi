from django.db import models

# Create your models here.
from user.models import User


class Todojob(models.Model):
    text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    date = models.DateTimeField()
    image = models.ImageField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

