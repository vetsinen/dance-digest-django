from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()


    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Coach(models.Model):
    name = models.CharField(max_length=30)