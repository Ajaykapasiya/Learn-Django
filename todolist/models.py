from django.db import models

class Task(models.Model):
    task = models.CharField(max_length=100)
    is_completed =models.BooleanField()