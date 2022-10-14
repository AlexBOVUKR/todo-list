import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class Tag(models.Model):
    name = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    content = models.CharField(max_length=63, unique=True)
    detail = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["deadline"]

    def __str__(self):
        return f"{self.created_at}: {self.content} "

    @property
    def timedelta(self):
        now = datetime.datetime.now()
        if self.deadline:
            if now > self.deadline:
                time_left = self.deadline - now
                time_left = str(time_left)
                result = time_left.split(".")
                return result
        return ""
