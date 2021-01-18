from django.db import models


class TodoModel(models.Model):
    objects = models.Manager()
    content = models.CharField(max_length=255)
