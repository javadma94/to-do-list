from django.db import models
from django.utils import timezone
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.title
