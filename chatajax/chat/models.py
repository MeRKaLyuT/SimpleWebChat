from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType, ContentTypeManager
from django.contrib.contenttypes.fields import GenericForeignKey
from datetime import datetime
from django.urls import reverse


class Room(models.Model):
    title = models.CharField(max_length=60)
    object_id = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='Автор', blank=True, null=True, on_delete=models.CASCADE)
    message = models.CharField(max_length=255, blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('message', args=[str(self.id)])
