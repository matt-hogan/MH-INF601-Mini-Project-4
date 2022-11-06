from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50, null=False, help_text="Required")
    description = models.CharField(max_length=200)
    done = models.BooleanField(default=False)