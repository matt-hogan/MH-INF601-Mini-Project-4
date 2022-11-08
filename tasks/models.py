from django.conf import settings
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50, null=False, help_text="Required")
    description = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)