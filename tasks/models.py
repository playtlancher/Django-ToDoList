from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, default="Scheduled")

    def __str__(self):
        return self.name
