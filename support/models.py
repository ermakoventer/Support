from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    class StatusMessage(models.TextChoices):
        FROZEN = 'Frozen'
        RESOLVED = 'Resolved'
        UNRESOLVED = 'Unresolved'

    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.CharField(default=StatusMessage.FROZEN, choices=StatusMessage.choices, max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_support = models.TextField(blank=True)

    def __str__(self):
        return self.title
