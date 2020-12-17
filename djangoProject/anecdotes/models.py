from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone


class Anecdote(models.Model):
    date = models.DateField(timezone.now())
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField()
    whoLikedIt = models.CharField(max_length=500)

    def __str__(self):
        return self.text[0:15] + '...'
