from django.contrib.auth.models import User
from django.db import models

status_message = (
    ('Frozen', 'Frozen'),
    ('Resolved', 'Resolved'),
    ('Unresolved', 'Unresolved'),
)


class Message(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.CharField(default="Frozen", choices=status_message, max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_support = models.TextField(blank=True)

    def __str__(self):
        return self.title

